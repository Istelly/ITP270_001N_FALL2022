import socket
from IPy import IP 
import pyfiglet
import subprocess
import time

subprocess.call('clear', shell=True)

Port_Scanner_Banner = pyfiglet.figlet_format("PORT SCANNER")
print(Port_Scanner_Banner)

time.sleep(1)

ports = []

banners = []

def scan(target):
    converted_ip = convert_ip(target)
    print('\n' + 'Scanning Target : ' + str(target))
    for port in range(21,80):
        scan_port(converted_ip, port)

def convert_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)

#def get_banner(s):
#   return s.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.1)
        sock.connect((ipaddress, port))

        try:
            banner = get_banner(sock)
            print('[+] Port ' + str(port) + ' is Open ' + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('[+] Port ' + str(port) + ' is Open ')
    except:
        pass

    try:
        sock = socket.socket()
        sock.settimeout(0.01)
        sock.connect((ipaddress, port))

        try:
            ports.append(port)
            banner = sock.recv(1024).decode().strip('\n').strip('\r')
            banners.append(banner)
        except:
            banners.append(' ')
        sock.close()
    except:
        pass

if __name__ == "__main__":
    targets = input('[+] Enter Target/s To Scan( for multiple targets usea  comma): ')
    start_port = input('enter the port to start the scan: ')
    end_port = input('enter the port to end the scan: ')
    start_port = start_port
    end_port = end_port

    if ',' in targets:
        for ip_address in targets.split(','):
            scan(ip_address.strip(' '))
    else:
        scan(targets)

with open("vulnerable_banners.txt", 'r') as file:
    count = 0
    for banner in banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('[!!] VULNERABLE BANNER: "' + banner + '" ON PORT: ' + str(ports[count]))
        count += 1