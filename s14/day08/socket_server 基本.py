import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        try:
            while True:
                self.data = self.request.recv(1024).strip()
                print("{} wrote:".format(self.client_address[0]))
                print(self.data)
                if not self.data: # 代表客户端断开了
                    print(self.client_address,"断开了")
                    break
                self.request.send(self.data.upper())
        except ConnectionResetError as e:
            print("客户端异常关闭")



if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    # Create the server, binding to localhost on port 9999
    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()