import socket                   # Import socket module

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server listening....')

conn, addr = s.accept()     # Establish connection with client.
print('Got connection from', addr)
filename=input(str("Enter the file name: "))
file=open(filename,'rb')
file_data=file.read(1024)
conn.send(file_data)
print("Data transfered successfully!!") 