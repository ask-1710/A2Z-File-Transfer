import http.server
import socket
import webbrowser
import pyqrcode
import os
import socketserver as ss

class MyTCPHandler(ss.BaseRequestHandler):

    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())

PORT = 8010

curr_dir = os.path.dirname(__file__)
print(curr_dir)
directory = input("ENTER THE DIRECTORY YOU WANT TO SHARE : ")
if os.path.isdir(directory) :
    os.chdir(directory)
else:
    print('Directory doesnt exist')
    exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # creating client socket
s.connect(("8.8.8.8", 80)) # connect to google server - port 80 for http requests

link = "http://" + s.getsockname()[0] + ":" + str(PORT) # the directory to access local files  http://ipaddr:8010


url = pyqrcode.create(link)  
url.svg("D:/qrcode.svg", scale=8) # save the QR code as svg file
webbrowser.open(curr_dir+'\\renderFiles.html') # render the html file (containing the QR code ) in a webbrowser

Handler = http.server.SimpleHTTPRequestHandler # supports only get and head requests

with ss.TCPServer(("", PORT), Handler) as httpd:
		httpd.serve_forever()


'''''
1. directory valid - chk
2. accpet post req 
3. terminate server 
4. password user authentication
5. 
'''