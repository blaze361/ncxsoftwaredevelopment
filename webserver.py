import time
import http
from http.server import HTTPServer, BaseHTTPRequestHandler


hostName = "localhost"
serverPort = 9851
class myServer(BaseHTTPRequestHandler):  
  def do_GET(self): #the do_GET method is inherited from BaseHTTPRequestHandler 
    self.send_response(200)    
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write(bytes("<html><head><title>https://testserver.com</title></head>", "utf-8"))
    self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
    self.wfile.write(bytes("<body>", "utf-8"))
    self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
    self.wfile.write(bytes("</body></html>", "utf-8"))
    self.send_respose(400)

if __name__ == "__main__":        
  webServer = HTTPServer((hostName, serverPort), myServer)
  print("Server started http://%s:%s" % (hostName, serverPort))  #Server starts
try:
          webServer.serve_forever()
except KeyboardInterrupt:
  pass
webServer.server_close()  #Executes when you hit a keyboard interrupt, closing the server
print("Server stopped.")
