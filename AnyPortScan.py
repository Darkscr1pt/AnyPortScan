import socket
import pyfiglet
from datetime import datetime


def aps():
    # Display banner
    banner = pyfiglet.figlet_format("AnyPortScan")
    print(banner)

    # Ask the user for a target server's FQDN or IP address
    target = input("Enter the target server's FQDN or IP address: ")

    # Ask the user for target port numbers
    # port_numbers = input("Enter port numbers (space separated): ")
    # Or specify a static port list
    port_numbers = "80 389 443 636 1433 2195 2196 5494 5495 5497 9200 9300 13131"

    # Split the port numbers into a list
    port_numbers = port_numbers.split()

    # Convert the port numbers to integers
    port_numbers = (int(x) for x in port_numbers)

    # Show timestamp
    print("-" * 53)
    print(f"Scanning Target ports")
    print("Scanning started at: " + str(datetime.now()))
    print("-" * 53)

    # Perform port scanning
    for port in port_numbers:
        # Create a socket (IPv4)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
        # Close the socket
        s.close()


aps()
