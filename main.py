from http.server import HTTPServer, CGIHTTPRequestHandler
# импорт библиотек

server_data = ('localhost', 8080)
# параметры для сервера

server = HTTPServer(server_data, CGIHTTPRequestHandler)

server.serve_forever()
