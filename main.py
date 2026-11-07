from http.server import BaseHTTPRequestHandler, HTTPServer

PAGE = """<!doctype html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Hello</title></head>
<body style="font-family:sans-serif;text-align:center;margin-top:20vh">
<h1>Hello from Dardania Labs</h1>
<p>Running on dardanialabs.app</p>
</body></html>"""


class Hello(BaseHTTPRequestHandler):
    def do_GET(self):
        body = PAGE.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


HTTPServer(("0.0.0.0", 8000), Hello).serve_forever()
