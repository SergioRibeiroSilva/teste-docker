import os
import socket
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = int(os.environ.get("PORT", "8000"))
MESSAGE = os.environ.get("MESSAGE", "Olá do container Docker!")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"""<!doctype html>
<html lang="pt-BR">
<head><meta charset="utf-8"><title>Docker demo</title></head>
<body style="font-family: sans-serif; padding: 2rem;">
  <h1>{MESSAGE}</h1>
  <p><b>Hostname do container:</b> {socket.gethostname()}</p>
  <p><b>Hora do servidor:</b> {datetime.now():%d/%m/%Y %H:%M:%S}</p>
  <p><b>Caminho pedido:</b> {self.path}</p>
  <p>Sérgio</p> 
</body>
</html>
""".encode("utf-8")
        print(f"GET {self.path} recebido", flush=True)
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print(f"Servidor rodando na porta {PORT}", flush=True)
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
