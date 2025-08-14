# Port scanner used to determine which ports are open on a network. 
#

import argparse
import pyfiglet
import socket
import threading


# Prompts user to import range
def get_ports():
    try:
        port_selection = input("Enter port ranges (EX: 22-23)\n$ ").strip()

        # Enter range of numbers
        if "-" in port_selection:
            start_port, end_port = port_selection.split("-")
            start_port = int(start_port.strip())
            end_port = int(end_port.strip())
        else:
            start_port = int(port_selection)
            end_port = start_port
        
        if not (1 <= start_port <= 65535) or not (1 <= end_port <= 65535):
            raise ValueError("Please enter number in valid TCP/UDP range (1-65535)")

        if start_port > end_port:
            raise ValueError("Start port must be less than or equal to the end port.")
        
        return start_port, end_port
    
    except ValueError as e:
        print(f"Invalid Input: {e}") 
        return 

# Used to create the command line prompt by importing argparse
def parse_cli_arguments():
    # Get input for target hose and timeout connection.
    parser = argparse.ArgumentParser(description="Port Scanner")
    
    # Adds target host and timeout defaults and help menu
    parser.add_argument("--target", "--th", help="Enter IP address you wish to scan.", required=True)
    # If wish to change timeout default, change your preferred setting to number of your choice on default or use command line argument to change it.
    parser.add_argument("--timeout", default=1, help="This is used to set your own timeout. Default is 1s, supports float timeouts.", type=float, required=False)

    # create object for error handling
    args = parser.parse_args()
    return args

def main():

    args = parse_cli_arguments()

    # Prompt user to import port range:
    start_port, end_port = get_ports()
    
    # Resolve target_host to IP address
    try:
        ip_address = socket.gethostbyname(args.target)
        print(f"The IP address of {args.target} is: {ip_address}")
    except socket.gaierror as e:
        print(f"Could not resolve {args.target}: {e}")

    for port in range(start_port, end_port + 1):
    # create new tcp socket
        try:
             # Creating a TCP connection 
            cl_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # set socket timeout to user input or default
            cl_socket.settimeout(args.timeout)
            # try to connect to target and port
            port_connection = cl_socket.connect_ex((ip_address, port))
            # if successful let user know its open
            if port_connection == 0:
                print(f"[+] Port {port} is OPEN")
            else:
                print(f"[-] Port {port} is CLOSED")
            
            # Close socket
            cl_socket.close()

        
        except ConnectionRefusedError:
            print(f"Connection refused. Please ensure server is running.")
        except Exception as e:
            print(f"Error Occured: {e}")

    print("Scan Complete.")

    

if __name__ == "__main__":
    result = pyfiglet.figlet_format("Port Scanner")
    print(result)
    main()
