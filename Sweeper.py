import subprocess
import socket
import os
from concurrent.futures import ThreadPoolExecutor

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "No hostname found"

def scan_ports(ip, ports):
    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                if s.connect_ex((ip, port)) == 0:
                    open_ports.append(port)
        except Exception:
            pass
    return open_ports

def ping_and_scan(ip, port_range):
    try:
        # Run ping
        result = subprocess.run(
            ["ping", "-n", "1", "-w", "200", ip],  # Adjust for Linux/Mac
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        if result.returncode == 0:
            # Extract response time
            output = result.stdout.decode()
            if "time=" in output:
                response_time = output.split("time=")[-1].split("ms")[0].strip()
            else:
                response_time = "No response time"

            hostname = get_hostname(ip)
            open_ports = scan_ports(ip, port_range)
            print(f"{ip} is active | Hostname: {hostname} | Response Time: {response_time} ms | Open Ports: {open_ports}")
        else:
            print(f"{ip} is inactive")
    except Exception as e:
        print(f"Error checking {ip}: {e}")

# Define range and ports
third_octet_range = range(0, 2)  # Test smaller ranges to avoid long scan times
fourth_octet_range = range(200, 202)
port_range = range(20, 1025)  # Ports to scan

with ThreadPoolExecutor(max_workers=50) as executor:  # Adjust thread count as needed
    for third_octet in third_octet_range:
        for fourth_octet in fourth_octet_range:
            ip = f"10.145.{third_octet}.{fourth_octet}"
            executor.submit(ping_and_scan, ip, port_range)
