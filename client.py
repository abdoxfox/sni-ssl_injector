#pylint:disable=E0001
import random
import time
import sys

bg=''
G = bg+'\033[32m'
O = bg+'\033[33m'
GR = bg+'\033[37m'
R = bg+'\033[31m'
logo=logo='''
    ++++  ++++   +++     ++++   +        +
    +  +  +   +  +   +   +  +     +    +
    ++++  +++    +   +   +  +       + 
    +  +  +   +  +   +   +  +     +   +
    +  +  ++++   + +     ++++   +       +
    
            #Github : https://github.com/abdoxfox
            
            
    '''
def welcoming(str):
    	color=[bg,R,O,GR]
    	for n in str+ '\n':
    		print(random.choice(color),end='')
    		sys.stdout.write(n)
    		sys.stdout.flush()
    		time.sleep(0.01)
welcoming(logo)
title=O+"""	Injector SSL with SNI Host in Python
	
	    Created by Abdoxfox.
	
"""+GR
print(title)
import socket, threading, select
import os,signal
from curses import ascii
import subprocess

passed = 0
for i in os.listdir('.'):
    if i == 'sni.log':
        if len(open(i,'r').readlines()) > 0:
       	    passed+=1
            break
    else:
        pass

if passed == 1 :
       SNI_HOST = open('sni.log','r').readline().strip('\n')
       #print(SNI_HOST)
else:

    os.system('touch sni.log')

    SNI_HOST = input('Enter SNI host :')
    file=open('sni.log','w')
    file.write(SNI_HOST)
    file.close()
LISTEN_PORT = 8980


def handler():
    print('killing process ...')
    cmd = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
    output, error = cmd.communicate()
    target_process = "python"
    for line in output.splitlines():
        if target_process in str(line):
            pid = int(line.split(None, 1)[0])
            os.system(f'kill pid {pid}')



def conection(c, a):
    try:
         print('<#> Client {} received!'.format(a[-1]))
         request = c.recv(19192).decode()
         
         host = request.split(':')[0].split()[-1]
         port = request.split(':')[-1].split()[0]
         
        
         payload = request.replace('\r\n\r\n','[crlf][crlf]')
         print(f'payload : {payload}')
    
         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         
         s.connect((str(host), int(port)))
         print(f'{G}connected to {host}:{port}{GR}')
         
    	
         import ssl
         ctx = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
         s = ctx.wrap_socket(s, server_hostname=str(SNI_HOST))
    	#print(s)
    	# Direct
         c.send(b"HTTP/1.1 200 ABDOXFOX\nPython_crazy_coder\r\n\r\n")
    
         connected = True
         while connected == True:
        		r, w, x = select.select([c,s], [], [c,s], 3)
        		
        		if x: connected = False; break
        		for i in r:
        			try:
        				# Break if not data.
        				data = i.recv(19192)
        				if not data: connected = False; break
        				if i is s:
        					# Download.
        					c.send(data)
        				else:
        					# Upload.
        					s.send(data)
        			except:
        				connected = False
        				break
         c.close()
         s.close()
      
         print(R+'<#> Client {} Disconnected {}'.format(a[-1],GR))
         
    except Exception as e:
        print(f'{R}ERROR : {e}{GR}')
        
        
        
    
    
    


# Listen

try:
    l = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    l.bind(('', int(LISTEN_PORT)))
    l.listen(0)
    print('Waiting for incoming connection to : 127.0.0.1:{}\n'.format(LISTEN_PORT))
except OSError:
    print(O+'Port used \nRun script again'+GR)
    handler()
    
while True:
	try:
	    c, a = l.accept()
	    thr=threading.Thread(target=conection, args=(c, a))
	    thr.start()
	    
	except KeyboardInterrupt:
	    print('CTRL + C  Pressed')
	    l.close()
	    handler()
	
	    
l.close()