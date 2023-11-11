import http.server
import socketserver

from functools import cached_property
from urllib.parse import parse_qsl, urlparse
from http.cookies import SimpleCookie

# HOST = "172.16.1.108"
# PORT = 9999     # 5432


class Controller(http.server.SimpleHTTPRequestHandler):

    @cached_property
    def url(self):
        return urlparse(self.path)

    @cached_property
    def query_data(self):
        return dict(parse_qsl(self.url.query))

    @cached_property
    def post_data(self):
        content_length = int(self.headers.get("Content-Length", 0))
        return self.rfile.read(content_length)

    @cached_property
    def form_data(self):
        return dict(parse_qsl(self.post_data.decode("utf-8")))

    @cached_property
    def cookies(self):
        return SimpleCookie(self.headers.get("Cookie"))
    """
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"Serving From Python http.server module.")
        print('EpicEvents server program is now running: You can open your page at \'localhost:9999\' port:9999')
    """
    def create_collaborator(self):
        pass

    def delete_collaborators(self):
        pass

    def create_customer(self):
        pass

    def delete_customer(self):
        pass

    def create_contract(self):
        pass

    def delete_contract(self):
        pass
