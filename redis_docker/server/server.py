import http.server
import socketserver

# Переменная нужна для обработки запросов клиента к серверу.

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", 1234), handler) as httpd:

    # Благодаря этой команде сервер будет выполняться постоянно, ожидая запросов от клиента.

   httpd.serve_forever()