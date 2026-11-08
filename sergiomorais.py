import os
from http.server import BaseHTTPRequestHandler, HTTPServer

PAGE = """<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="utf-8">
    <title>CloudNova — Portal Corporativo</title>
</head>
<body>
    <h1>CloudNova</h1>
    <h2>Portal Corporativo — Sérgio Morais</h2>
    <p>A aplicação está em execução num contentor.</p>
    <p>Integrações com identidade, dados e ficheiros em preparação.</p>
</body>
</html>"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            body = b'{"status":"ok"}'
            content_type = "application/json"
        elif self.path == "/":
            body = PAGE.encode("utf-8")
            content_type = "text/html; charset=utf-8"
        else:
            self.send_error(404)
            return

        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()
