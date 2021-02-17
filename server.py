from http.server import BaseHTTPRequestHandler, HTTPServer
import client


def get_repo(headers):
    if 'repo' in headers.keys():
        return headers['repo']
    else:
        return 'master'


class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
        self._set_headers()
        output = client.get_branches(repo=get_repo(self.headers))
        self.wfile.write(output.encode('utf8'))


def run(server_class=HTTPServer, handler_class=Server, port=8008):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    print('Starting httpd on port %d...', port)
    httpd.serve_forever()


if __name__ == "__main__":
    run()
