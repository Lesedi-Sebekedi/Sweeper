# Sweeper
script to check the reachability of multiple IP addresses


# IP Scanner with Hostname and Port Detection

## Overview
This program is a network scanning utility designed to:
1. **Ping IP addresses** to check their reachability.
2. Retrieve the **hostname** of each reachable IP.
3. Perform a **port scan** on reachable IPs to identify open ports.
4. Provide detailed output for each scanned IP.

The script is customizable, efficient, and supports multithreading for faster execution, making it suitable for scanning large IP ranges across multiple subnets.

---

## Features

1. **Ping Detection**:
   - Sends ICMP echo requests to determine if an IP address is active or inactive.
   - Extracts response times from the ping command for active IPs.

2. **Hostname Resolution**:
   - Uses reverse DNS lookup to retrieve hostnames for active IP addresses.
   - Displays "No hostname found" if no reverse DNS entry exists.

3. **Port Scanning**:
   - Scans specified port ranges for open ports on active IP addresses.
   - Defaults to scanning ports 20-1024 but can be adjusted as needed.

4. **Multithreading**:
   - Uses `ThreadPoolExecutor` to scan multiple IP addresses concurrently, significantly improving performance for large networks.

5. **Dynamic Range Configuration**:
   - Allows users to define the third and fourth octet ranges for scanning specific IP subsets.
   - Supports easy customization of port ranges.

6. **Cross-Platform Support**:
   - Compatible with Windows, Linux, and macOS. (Ping arguments may require adjustment for non-Windows systems.)

---

## Usage Instructions

### Prerequisites
- Python 3.7 or higher.
- Basic knowledge of network structure and subnets.
- Permissions to run ping and port scan operations on the target network.

### Installation
1. Clone or download the repository.
2. Install Python if not already installed.
3. Ensure you have the necessary permissions to run network scans on your system and network.

### Execution
1. Open the script file (`Sweeper.py`).
2. Modify the following ranges as needed:
   - `third_octet_range`: Defines the third octet range of the IPs to scan (e.g., `range(0, 2)` for `10.145.0.0` to `10.145.1.255`).
   - `fourth_octet_range`: Defines the fourth octet range of the IPs to scan (e.g., `range(200, 255)` for `10.145.x.200` to `10.145.x.254`).
   - `port_range`: Defines the ports to scan (e.g., `range(20, 1025)` for ports 20 to 1024).

3. Run the script:
   ```bash
   python Sweeper.py
   ```
4. View the output in the terminal for detailed information about each scanned IP.

---

## Output Example
For each scanned IP, the program displays:
- **IP Address**: The scanned IP.
- **Activity Status**: Active or inactive.
- **Hostname**: Reverse DNS entry for active IPs.
- **Response Time**: Ping response time in milliseconds.
- **Open Ports**: A list of open ports detected on active IPs.

Example Output:
```
10.145.0.200 is active | Hostname: example-host.local | Response Time: 12 ms | Open Ports: [22, 80, 443]
10.145.0.201 is inactive
10.145.1.200 is active | Hostname: No hostname found | Response Time: 8 ms | Open Ports: [22, 8080]
```

---

## Customization

### Adjusting IP Ranges
Modify these variables to change the scan range:
- `third_octet_range`: Range for the third octet.
- `fourth_octet_range`: Range for the fourth octet.

Example:
```python
third_octet_range = range(0, 3)  # Scans 10.145.0.x to 10.145.2.x
fourth_octet_range = range(100, 201)  # Scans .100 to .200
```

### Adjusting Port Ranges
Modify the `port_range` variable to scan different port ranges.
Example:
```python
port_range = range(1, 65536)  # Scan all 65535 ports
```

---

## Notes

1. **Performance Considerations**:
   - Scanning large ranges or full port lists can be time-consuming. Use smaller subsets if possible.
   - Adjust `max_workers` in `ThreadPoolExecutor` to control concurrency (default is 50 threads).

2. **Error Handling**:
   - The script gracefully handles errors and logs any issues (e.g., inaccessible IPs or ports).

3. **Cross-Platform Compatibility**:
   - For Linux/macOS, adjust the `ping` command arguments from `-n` and `-w` to `-c` and `-W` respectively.

4. **Permissions**:
   - Administrator/root privileges may be required for certain operations, especially port scanning.

---

## License
This script is open-source and free to use. Contributions are welcome!

