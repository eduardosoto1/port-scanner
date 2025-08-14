# Port_Scanner
This is a Python-based port scanner allowing you to view open or closed TCP ports on a given host. It is intended for educational purposes and authorized network testing ONLY.

## Features
- Scan a single port or range of ports
- Adjustable timeout for slower or faster scans
- Hostname-to-IP resolution
- output showing open/closed ports

## Install dependencies
```
Python 3.10 or newer
view 'requirements.txt' for any dependencies:
- pyfiglet
```

## How to use
```
py main.py --target [TARGET HOST or IP address] --timeout [OPTIONAL TIMEOUT SECONDS]
```
- Target is used to view the destination you are connecting to.
- Timeout has a default set to 1, use timeout to change it to your preference
- use [-h] for help menu

Heres an Example of scanning ports 20-25
```bash 
python main.py --target networksettings.com --timeout 0.8

Enter port range: 20-25
```
### **5. Legal/Ethical Disclamer**
⚠️ **Disclaimer:**  
This tool is intended for authorized testing and educational purposes only.  
Do not use it to scan systems without explicit permission.  
Unauthorized scanning may be illegal in your jurisdiction.