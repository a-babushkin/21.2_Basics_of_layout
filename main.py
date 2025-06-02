from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8088


class MyServer(BaseHTTPRequestHandler):
    """Класс, отвечающий за обработку входящих запросов"""

    def do_GET(self):
        """Метод для обработки входящих GET-запросов"""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        with open("html_files/contacts.html", "r", encoding="utf-8") as file:
            data = file.read()
        self.wfile.write(bytes(data, "utf-8"))

    def do_POST(self):
        """Метод для обработки POST-запросов"""
        content_length = int(self.headers.get('Content-Length', 0))

        if content_length > 0:
            post_data = self.rfile.read(content_length).decode('utf-8')

            print(f'Ответ сервера:\n{post_data}')

        self.send_response(200)
        self.end_headers()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
