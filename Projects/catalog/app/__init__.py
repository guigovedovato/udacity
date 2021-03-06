#!/usr/bin/env python3
from flask import Flask, flash
from flask import render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from db import DB_CONNECT
from db.model import Base
from db.model.category import Category
from db.model.category_item import CategoryItem
from db.model.user import User
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
import os
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.secret_key = 'super_secret_key'
app.debug = True
csrf = CSRFProtect(app)


CLIENT_SECRETS = os.path.join(os.getcwd(), 'app/config/client_secrets.json')
CLIENT_ID = json.loads(
    open(CLIENT_SECRETS, 'r').read())['web']['client_id']


# Connect to Database and create database session
engine = create_engine(DB_CONNECT)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in range(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets(CLIENT_SECRETS, scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = requests.get(url)
    result = json.loads(h.content)
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print("Token's client ID does not match app's.")
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already\
                                            connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['provider'] = 'google'
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    response = make_response(json.dumps("you are now logged in as %s"
                                        % login_session['username']),
                             200)
    return response


@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(json.dumps(
            'Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s'\
          % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        response = make_response(json.dumps('Successfully disconnected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps(
            'Failed to revoke token for given user.'), 400)
        response.headers['Content-Type'] = 'application/json'
        return response


# Disconnect based on provider
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            del login_session['gplus_id']
            del login_session['access_token']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['user_id']
        del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('showCategories'))
    else:
        flash("You were not logged in")
        return redirect(url_for('showCategories'))


def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
        'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(
        email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except Exception:
        return None


# JSON APIs to view Catalog Information
@app.route('/api/catalog/<string:category_name>')
def category(category_name):
    category = session.query(Category).filter_by(
        name=category_name).one()
    items = session.query(
        CategoryItem).filter_by(category_id=category.id).all()
    return jsonify(categories=[r.serialize for r in items])


@app.route('/api/catalog/<string:category_name>/<string:categoryItem_name>')
def categoryItem(category_name, categoryItem_name):
    category = session.query(Category).filter_by(
        name=category_name).one()
    item = session.query(
        CategoryItem).filter_by(title=categoryItem_name,
                                category_id=category.id).one()
    return jsonify(CategoryItem=item.serialize)


@app.route('/api/catalog')
def catalog():
    categories = session.query(Category).all()
    return jsonify(categories=[r.serialize for r in categories])


# Show all categories
@app.route('/')
@app.route('/catalog')
@csrf.exempt
def showCategories():
    categories = session.query(Category).order_by(
        asc(Category.name))
    return render_template('catalog.html', categories=categories,
                           login_session=login_session)


# Create a new category
@app.route('/catalog/new', methods=['GET', 'POST'])
def newCategory():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newCategory = Category(
            name=request.form['name'], user_id=login_session['user_id'])
        session.add(newCategory)
        flash('New Category %s Successfully Created' % newCategory.name)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        return render_template('newcatalog.html')


# Edit a category
@app.route('/catalog/<string:category_name>/edit', methods=['GET', 'POST'])
def editCategory(category_name):
    if 'username' not in login_session:
        return redirect('/login')
    editedCategory = session.query(
        Category).filter_by(name=category_name).one()
    if editedCategory.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized\
               to edit this Category. Please create your own Category in order\
               to edit.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
            flash('Category Successfully Edited %s' % editedCategory.name)
            return redirect(url_for('showCategory',
                                    category_name=editedCategory.name))
    else:
        return render_template('editcatalog.html', category=editedCategory)


# Delete a category
@app.route('/catalog/<string:category_name>/delete', methods=['GET', 'POST'])
def deleteCategory(category_name):
    if 'username' not in login_session:
        return redirect('/login')
    categoryToDelete = session.query(
        Category).filter_by(name=category_name).one()
    if categoryToDelete.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized\
               to delete this Category. Please create your own Category in\
               order to delete.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        try:
            session.delete(categoryToDelete)
            session.commit()
            flash('%s Successfully Deleted' % categoryToDelete.name)
            return redirect(url_for('showCategories'))
        except Exception:
            session.rollback()
            flash('%s was not Deleted' % categoryToDelete.name)
            return "<script>function myFunction() {alert('\
                   This Category there are Items, delete those items first');\
                   }</script><body onload='myFunction()'>"
    else:
        return render_template('deletecatalog.html',
                               category=categoryToDelete)


# Show a category
@app.route('/catalog/<string:category_name>')
@csrf.exempt
def showCategory(category_name):
    category = session.query(
        Category).filter_by(name=category_name).one()
    items = session.query(CategoryItem).filter_by(
        category_id=category.id).all()
    creator = getUserInfo(category.user_id)
    return render_template('catalogitem.html', items=items,
                           category=category, creator=creator,
                           login_session=login_session)


# Create a new category item
@app.route('/catalog/<string:category_name>/new', methods=['GET', 'POST'])
def newCategoryItem(category_name):
    if 'username' not in login_session:
        return redirect('/login')
    category = session.query(
        Category).filter_by(name=category_name).one()
    if login_session['user_id'] != category.user_id:
        return "<script>function myFunction() {alert('You are not authorized\
               to add menu items to this category. Please create your own\
               category in order to add items.');}</script><body\
               onload='myFunction()''>"
    if request.method == 'POST':
        newItem = CategoryItem(title=request.form['title'],
                               description=request.form['description'],
                               category_id=category.id,
                               user_id=login_session['user_id'])
        session.add(newItem)
        session.commit()
        flash('New Category %s Item Successfully Created' % (newItem.title))
        return redirect(url_for('showCategory', category_name=category_name))
    else:
        return render_template('newcatalogitem.html',
                               category_name=category_name)


# Edit a category item
@app.route('/catalog/<string:category_name>/<string:categoryItem_name>/edit',
           methods=['GET', 'POST'])
def editCategoryItem(category_name, categoryItem_name):
    if 'username' not in login_session:
        return redirect('/login')
    category = session.query(Category).filter_by(
        name=category_name).one()
    editedItem = session.query(
        CategoryItem).filter_by(title=categoryItem_name,
                                category_id=category.id).one()
    if login_session['user_id'] != category.user_id:
        return "<script>function myFunction() {alert('You are not authorized\
               to edit category items to this category. Please create your\
               own category in order to edit items.');}</script><body\
               onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['title']:
            editedItem.title = request.form['title']
        if request.form['description']:
            editedItem.description = request.form['description']
        session.add(editedItem)
        session.commit()
        flash('Category Item Successfully Edited')
        return redirect(url_for('showCategory', category_name=category_name))
    else:
        return render_template('editcatalogitem.html',
                               category_name=category_name,
                               categoryItem_name=editedItem.title,
                               item=editedItem)


# Delete a category item
@app.route('/catalog/<string:category_name>/<string:categoryItem_name>/delete',
           methods=['GET', 'POST'])
def deleteCategoryItem(category_name, categoryItem_name):
    if 'username' not in login_session:
        return redirect('/login')
    category = session.query(Category).filter_by(
        name=category_name).one()
    itemToDelete = session.query(
        CategoryItem).filter_by(title=categoryItem_name,
                                category_id=category.id).one()
    if login_session['user_id'] != category.user_id:
        return "<script>function myFunction() {alert('You are not authorized\
               to delete category items to this category. Please create your\
               own category in order to delete items.');}</script><body\
               onload='myFunction()''>"
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('Category Item Successfully Deleted')
        return redirect(url_for('showCategory', category_name=category_name))
    else:
        return render_template('deletecatalogitem.html', item=itemToDelete,
                               category_name=category_name)
