import os
import socketserver

class ForkingEchoRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # Echo the back to the client
        data = self.request.recv(1024)
        print(f"Receive {data}")
        cur_pid = os.getpid()
        response = 'data received by the server: %s' % ( data.decode())
        self.request.send(response.encode())
        return

# use ThreadingMixIn rather than ForkingMixIn b/c of Windows
#class ForkingEchoServer(socketserver.ForkingMixIn, socketserver.TCPServer):
class ForkingEchoServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == '__main__':
    import socket
    import threading

    address = ('localhost', 3000) # let the kernel give us a port
    server = ForkingEchoServer(address, ForkingEchoRequestHandler)
    ip, port = server.server_address # find out what port we were given

    print(f"Server listen at {ip}:{port}")

    t = threading.Thread(target=server.serve_forever)
    #t.setDaemon(True) # don't hang on exit
    t.start()
    print('Server loop running in process:', os.getpid())

    # Connect to the server
    ##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ##s.connect((ip, port))

    # Send the data
    ##message = 'Hello, world'
    ##print 'Sending : "%s"' % message
    ##len_sent = s.send(message)

    # Receive a response
    ##response = s.recv(1024)
    ##print 'Received: "%s"' % response

    # Clean up
    #s.close()
    #server.socket.close()
