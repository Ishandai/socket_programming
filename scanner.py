
import sys
import socket
from datetime import datetimegit 

#define our target host

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax: python scanner.py <ip>")
    sys.exit()

#add a pretty banner
print("-" * 50)
print("Scanning Target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(1, 65535): #scan all ports
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) #timeout for the connection
        result = s.connect_ex((target, port)) #returns an error indicator
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Could not connect to server.")
    sys.exit()