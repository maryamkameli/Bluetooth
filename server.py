import bluetooth
import uuid
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM) # Create a bluetooth socket using the RFCOMM protocol
server_sock.bind(("MinMar", bluetooth.PORT_ANY))
server_sock.listen(1)
print("socket listening")
port = server_sock.getsockname()[1]
print(port)
uuid_version_1 = uuid.uuid1()
print("UUID of version one is as follows", uuid_version_1)
uuid = str(uuid_version_1) # Your Code Here: Generate a new UUID so you don't interfere with other groups. Use the UUID library imported above
service_name = "MinMar"
# REPLACE - Make sure the same name is used in the client, and that it's not used by other groups

bluetooth.advertise_service(server_sock, service_name, service_id=uuid,
                            service_classes=[uuid, bluetooth.SERIAL_PORT_CLASS],
                            profiles=[bluetooth.SERIAL_PORT_PROFILE],
                            )

#bluetooth.advertise_service(server_sock, service_name, service_id = uuid)
print("Waiting for connection on RFCOMM channel", port)

client_sock, client_info = server_sock.accept()
print("Accepted connection from", client_info)

try:
    while True:
    
    
        # Your Code Here - Implement Two-Way communication. Use the client_sock.send() and client_sock.recv() functions to accomplish this.
        # Taking input and recieving from the socket are both blocking functions in Python, so the client and server must alternate sending messages
        # (unless you want to implement multithreading or multiple sockets)
except OSError:
    pass

print("Disconnected.")

client_sock.close()
server_sock.close()
print("All done.")
