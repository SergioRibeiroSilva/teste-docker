import os
import socket
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = int(os.environ.get("PORT", "8000"))
MESSAGE = os.environ.get("MESSAGE", "Bem-vindo ao ambiente Docker!")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        ambiente = "Nuvem (Render)" if os.environ.get("RENDER") else "Docker Desktop (Local)"
        
        body = f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Docker demo</title>
  <style>
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: #f0f4f8;
      color: #1e293b;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }}
    .card {{
      background: #ffffff;
      padding: 2.5rem;
      border-radius: 12px;
      box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
      max-width: 480px;
      width: 90%;
      border-top: 6px solid #0ea5e9;
    }}
    .badge {{
      display: inline-block;
      background: #e0f2fe;
      color: #0369a1;
      padding: 0.25rem 0.75rem;
      border-radius: 999px;
      font-weight: bold;
      font-size: 0.8rem;
      margin-bottom: 0.5rem;
    }}
    h1 {{
      color: #0284c7;
      margin-top: 0.5rem;
      font-size: 1.6rem;
    }}
    p {{
      line-height: 1.5;
      color: #475569;
    }}
    .info-box {{
      background: #f8fafc;
      border: 1px solid #e2e8f0;
      border-radius: 8px;
      padding: 1rem;
      margin-top: 1.5rem;
      font-size: 0.9rem;
    }}
    .info-item {{
      margin-bottom: 0.5rem;
    }}
    .info-item:last-child {{
      margin-bottom: 0;
    }}
    .footer {{
      margin-top: 1.5rem;
      font-size: 0.85rem;
      color: #64748b;
      text-align: right;
    }}
  </style>
</head>
<body>
  <div class="card">
    <span class="badge">{ambiente}</span>
    <h1>🐳 {MESSAGE}</h1>
    <p>O contêiner está ativo e respondendo corretamente.</p>

    <div class="info-box">
      <div class="info-item"><b>Hostname do container:</b> {socket.gethostname()}</div>
      <div class="info-item"><b>Hora do servidor:</b> {datetime.now():%d/%m/%Y %H:%M:%S}</div>
      <div class="info-item"><b>Caminho pedido:</b> {self.path}</div>
    </div>

    <div class="footer">
      Sérgio Ribeiro da Silva Peixoto
    </div>
  </div>
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
