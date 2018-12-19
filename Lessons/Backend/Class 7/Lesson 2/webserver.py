#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi


class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.endswith("/hello"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            output = ""
            output += "<html><body>Hello!"
            output += "<form method='POST' \
                enctype='multipart/form-data' \
                action'/hello'><h2>What would you like me to say?</h2>\
                <input name='message' type='text' />\
                <input value='Submit' type='submit' />\
                </form>"
            output += "</body></html>"
            self.wfile.write(bytes(output, "utf8"))
            print(output)
            return

        if self.path.endswith("/hola"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            output = ""
            output += "<html><body> &#161 Hola ! \
                <a href='/hello'>Back to Hello</a>"
            output += "<form method='POST' \
                enctype='multipart/form-data' \
                action'/hello'><h2>What would you like me to say?</h2>\
                <input name='message' type='text' />\
                <input value='Submit' type='submit' />\
                </form>"
            output += "</body></html>"
            self.wfile.write(bytes(output, "utf8"))
            print(output)
            return

        else:
            self.send_error(404, 'File Not Found: %s' % self.path)

    def do_POST(self):
        self.send_response(201)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        ctype, pdict = cgi.parse_header(
            self.headers.get('content-type'))
        pdict['boundary'] = bytes(pdict['boundary'], "utf-8")
        if ctype == "multipart/form-data":
            fields = cgi.parse_multipart(self.rfile, pdict)
            messageContent = fields.get('message')

        output = ""
        output += "<html><body>"
        output += "<h2> Okay, how about this: </h2>"
        output += "<h1> %s </hi>" % messageContent[0]

        output += "<form method='POST' \
            enctype='multipart/form-data' \
            action'/hello'><h2>What would you like me to say?</h2>\
            <input name='message' type='text' />\
            <input value='Submit' type='submit' />\
            </form>"
        output += "</body></html>"
        self.wfile.write(bytes(output, "utf8"))
        print(output)
        return


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
