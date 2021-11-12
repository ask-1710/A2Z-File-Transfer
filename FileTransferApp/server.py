import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
import os
from requests import get

PORT = 8010

dfiles = "D:\\"
os.chdir(dfiles)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # creating client socket
s.connect(("8.8.8.8", 1024)) # connect to google server
link = "http://" + s.getsockname()[0] + ":" + str(PORT) # the directory to access local files  http://ipaddr:8010
# client socket address : s.getsockname()[0]

url = pyqrcode.create(link)  
url.svg("qr-dfiles.svg", scale=8) # save the QR code as svg file
webbrowser.open('D:\\SSN\\SEM5\\NW\\FileTransferApp\\renderDfile.html') # render the html file (containing the QR code ) in a webbrowser

Handler = http.server.SimpleHTTPRequestHandler # supports only get and head requests

with socketserver.TCPServer(("", PORT), Handler) as httpd:
		httpd.serve_forever()