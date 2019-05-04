# Linux Server Configuration

## i. O endereço de IP e a porta SSH para que seu servidor possa ser acessado pelo revisor.
* IP: 35.176.185.122
* posta: 2200

## ii. A URL completa que você hospedou em sua aplicação web.
* http://35.176.185.122/catalog

## iii. Um resumo do software que você instalou e as mudanças feitas em configuração.
Foram instalados os seguintes softwares:
* Apache2
* WSGI
* PostgreSql
* Python3
* psycopg2
* SQLAlchemy
* pip
* git

Foram feitas as seguintes configurações:
* sudo para o usuário grader rodar sem password
* alterada a porta ssh de 22 para 2200
* UFW para 2200, 80 e 123
* timezone para UTC
* Postgre para rodar em localhost
* virtual host no Apache para rodar a aplicação em WSGI

## iv. Uma lista de quaisquer recursos de terceiros que você usou para completar esse projeto.
* AWS lightsail