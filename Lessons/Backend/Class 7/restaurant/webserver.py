#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
from database_setup import Base, Restaurant, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql://vagrant@localhost/restaurantmenu_db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.endswith("/restaurants"):
            restaurants = session.query(Restaurant).all()

            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            output = ""
            output += "<a href = '/restaurants/new' > \
                Make a New Restaurant Here </a></br></br>"
            output += "<html><body>"
            for restaurant in restaurants:
                output += restaurant.name
                output += "</br>"
                output += "<a href ='/restaurants/%s/edit' >Edit </a> " \
                    % restaurant.id
                output += "</br>"
                output += "<a href ='/restaurants/%s/delete'> Delete </a>" \
                    % restaurant.id
                output += "</br></br></br>"
            output += "</body></html>"
            self.wfile.write(bytes(output, "utf8"))
            return

        if self.path.endswith("/restaurants/new"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            output = ""
            output += "<html><body>"
            output += "<h1>Make a New Restaurant</h1>"
            output += "<form method = 'POST' \
                enctype='multipart/form-data' \
                action = '/restaurants/new'>"
            output += "<input name = 'newRestaurantName' type = 'text' \
                placeholder = 'New Restaurant Name' > "
            output += "<input type='submit' value='Create'>"
            output += "</form></body></html>"
            self.wfile.write(bytes(output, "utf8"))
            return

        if self.path.endswith("/edit"):
            restaurantIDPath = self.path.split("/")[2]
            myRestaurantQuery = session.query(Restaurant).filter_by(
                id=restaurantIDPath).one()
            if myRestaurantQuery:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = "<html><body>"
                output += "<h1>"
                output += myRestaurantQuery.name
                output += "</h1>"
                output += "<form method='POST' \
                    enctype='multipart/form-data' \
                    action = '/restaurants/%s/edit' >" % restaurantIDPath
                output += "<input name = 'newRestaurantName' type='text' \
                    placeholder = '%s' >" % myRestaurantQuery.name
                output += "<input type = 'submit' value = 'Rename'>"
                output += "</form>"
                output += "</body></html>"

                self.wfile.write(bytes(output, "utf8"))
            return

        if self.path.endswith("/delete"):
            restaurantIDPath = self.path.split("/")[2]

            myRestaurantQuery = session.query(Restaurant).filter_by(
                id=restaurantIDPath).one()
            if myRestaurantQuery:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<h1>Are you sure you want to delete %s?" \
                    % myRestaurantQuery.name
                output += "<form method='POST' \
                    enctype = 'multipart/form-data' \
                    action = '/restaurants/%s/delete'>" % restaurantIDPath
                output += "<input type = 'submit' value = 'Delete'>"
                output += "</form>"
                output += "</body></html>"
                self.wfile.write(bytes(output, "utf8"))
            return

        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        if self.path.endswith("/restaurants/new"):
            ctype, pdict = cgi.parse_header(
                self.headers.get('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('newRestaurantName')

                newRestaurant = Restaurant(name=messagecontent[0])
                session.add(newRestaurant)
                session.commit()

                self.send_response(201)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()

        if self.path.endswith("/edit"):
            ctype, pdict = cgi.parse_header(
                self.headers.get('content-type'))
            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('newRestaurantName')
                restaurantIDPath = self.path.split("/")[2]

                myRestaurantQuery = session.query(Restaurant).filter_by(
                    id=restaurantIDPath).one()
                if myRestaurantQuery != []:
                    myRestaurantQuery.name = messagecontent[0]
                    session.add(myRestaurantQuery)
                    session.commit()
                    self.send_response(201)
                    self.send_header('Content-type', 'text/html')
                    self.send_header('Location', '/restaurants')
                    self.end_headers()

        if self.path.endswith("/delete"):
            restaurantIDPath = self.path.split("/")[2]
            myRestaurantQuery = session.query(Restaurant).filter_by(
                id=restaurantIDPath).one()
            if myRestaurantQuery:
                session.delete(myRestaurantQuery)
                session.commit()
                self.send_response(201)
                self.send_header('Content-type', 'text/html')
                self.send_header('Location', '/restaurants')
                self.end_headers()


def main():
    try:
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print("Web Server running on port %s" % port)
        server.serve_forever()
    except KeyboardInterrupt:
        print("^C entered, stopping web server....")
        server.socket.close()


if __name__ == '__main__':
    main()
