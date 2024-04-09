import time
import http
from http.server import HTTPServer, BaseHTTPRequestHandler


hostName = "10.1.165.2"
serverPort = 9851
class myServer(BaseHTTPRequestHandler):  
  def do_GET(self): #the do_GET method is inherited from BaseHTTPRequestHandler 
    self.send_response(200, message="OK")    
    self.send_header("Content-type", "application/json")
    self.end_headers()
  def do_POST(self):
    self.send_response(200, message="OK")
    self.send_header("Content-type", "application/json")
    self.end_headers()
    message = int(self.headers.get("Content-Length"))
    post_body = self.rfile.read(message)
    print(post_body)

if __name__ == "__main__":        
  webServer = HTTPServer((hostName, serverPort), myServer)
  print("Server started http://%s:%s" % (hostName, serverPort))  #Server starts
try:
  webServer.serve_forever()
except KeyboardInterrupt:
  pass
webServer.server_close()  #Executes when you hit a keyboard interrupt, closing the server
print("Server stopped.")
