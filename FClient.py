import socket                   # Import socket module
 
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect((host, port))
print("Connected Successfully")

filename=input(str("Enter the incoming file name: "))
file=open(filename,'wb')
file_data=s.recv(1024)
file.write(file_data)
file.close()
print("File received Successfully!!")