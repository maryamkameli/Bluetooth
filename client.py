import sys

import bluetooth

addr = '10.163.209.177'

if len(sys.argv) < 2:
    print("No device specified. Searching all nearby bluetooth devices for "
          "the SampleServer service...")
else:
    addr = sys.argv[1]
    print("Searching for SampleServer on {}...".format(addr))

service_name = "MinMar" # Make sure this matches the server's service name and isn't being used by anyone else.
service_matches = bluetooth.find_service(name=service_name, address=addr)

if len(service_matches) == 0:
    print("Couldn't find the {} service.".format(service_name))
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("Connecting to \"{}\" on {}".format(name, host))

# Create the client socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))

while True:
    
    # Your Code Here - Implement Two-Way communication. Use the sock.send() and sock.recv() functions to accomplish this.
    # Taking input and recieving from the socket are both blocking functions in Python, so the client and server must
    # alternate sending messages (unless you want to implement multithreading or multiple sockets)
    
    # put the socket into listening mode
    sock.listen(port)    
    print ("socket is listening")           
 
# a forever loop until we interrupt it or
# an error occurs

# Establish connection with client.
    c, addr = sock.accept()    
    print ('Got connection from', addr )
 
  # send a thank you message to the client. encoding to send byte type.
    c.send('Thank you for connecting'.encode())
    sock.close()
