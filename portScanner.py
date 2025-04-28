#!/usr/bin/env python3

import socket

def scan_ports(ip, start_port, end_port):
	open_ports = []
	print(f"\nScanning {ip} from port {start_port} to {end_port}... \n")
	
	for port in range(start_port, end_port + 1):
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.settimeout(0.5) #Timeout in seconds
			result = sock.connect_ex((ip, port))
			if result == 0:
				open_ports.append(port)
			sock.close()
		except socket.error:
			print(f"Could not connect to port {port}")
	return open_ports

def get_valid_ip():
	while True:
		ip = input("Enter the IP address to scan: ").strip()
		try:
			socket.inet_aton(ip) #chec if IP is valid
			return ip
		except socket.error:
			print("Invalid IP address. Please try again")

def get_valid_port(prompt):
	while True:
		try: 
			port = int(input(prompt))
			if 0<=port<=65535:
				return port
			else:
				print("Port must be between 0 65535.")
		except ValueError:
			print("Please enter a valid integer.")

#Main program
if __name__ == "__main__":
	target_ip = get_valid_ip()
	start_port =  get_valid_port("Enter the starting port number: ")
	end_port = get_valid_port("Enter the ending port number: ")

	if start_port > end_port:
		print("Starting port cannot be  greater than ending por.")
	else:
		open_ports = scan_ports(target_ip, start_port, end_port)

		if open_ports:
			print("\nOpen ports found:")
			for port in open_ports:
				print(f"Port {port} is open")
			else:
				print("\nNo open ports found in the given range.")

