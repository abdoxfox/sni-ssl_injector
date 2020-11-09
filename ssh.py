import subprocess
import socket
import select
import threading
import random
import time
import sys
# colors
bg=''
G = bg+'\033[32m'
O = bg+'\033[33m'
GR = bg+'\033[37m'
R = bg+'\033[31m'

def ssh_client(socks5_port,host,user,password):
		try:
			global soc , payload
			
			
			dynamic_port_forwarding = '-CND {}'.format(socks5_port)
			host = host 
			port = '443'
			
			username = user 
			password = password 
			inject_host= '127.0.0.1'
			inject_port= '8980'
			payload=f'CONNECT {host}:443 HTTP/1.0\r\n\r\n'		
			soc.send(payload.encode())
			res=soc.recv(8192)
			print(res)
			
			response = subprocess.Popen(
                (
                   f'sshpass -p {password} ssh -o "ProxyCommand=nc --proxy {inject_host}:{inject_port} %h %p" {username}@{host} -p {port} -v {dynamic_port_forwarding} ' + '-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null '
                   
                
                ),
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT
            )
			
			for line in response.stdout:
				line = line.decode().lstrip(r'(debug1|Warning):').strip() + '\r'
				#print(line)
				if 'pledge: proc' in line:
					print(G+'CONNECTED SUCCESSFULLY'+GR)
					cmdl=subprocess.Popen('su -c am start --user 0 -n com.newtoolsworks.tun2tap/com.newtoolsworks.vpn2share.MainActivity',shell=True)
					
				elif 'Permission denied' in line:print(R+'Access Denied'+GR)
				elif 'Connection closed' in line:print(R+'Connection closed'+GR)
				elif 'Could not request local forwarding' in line:print(R+'Port used by another programs'+GR)
		except Exception as e:
		    print(R+'{}{}'.format(e,GR))
		except KeyboardInterrupt:
                      sys.exit(0)
f=open('sshacc.txt','r').readline().strip('\n').split('@')
host=f[0].split(':')[0]
user=f[1].split(':')[0]
password=f[1].split(':')[1]

try:    								
    soc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
    soc.connect(('127.0.0.1',8980))
    
    thread=threading.Thread(target=ssh_client,args=('1080',host,user,password))
    thread.start()
except ConnectionRefusedError:            
    print(R+' <!> Run client.py first in a new tab\n\tthen try again'+GR)
      
except KeyboardInterrupt:
		print(R+'ssh stopped'+GR)

			        

    
    
soc.close()