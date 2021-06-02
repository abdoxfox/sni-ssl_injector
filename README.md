# sni ssl injector



sni ssl injector in python works in termux 

# Requirements:

1-apt install git python openssh sshpass netcat -y

2-install tun2tap app from playstore
link: https://play.google.com/store/apps/details?id=com.newtoolsworks.tun2tap

# How it works:

Open termux app and install required package above and follow this steps:

1- git clone https://github.com/abdoxfox/ssl_Tls_injector.git

2- cd ssl_Tls_injector

3- python client.py

4- delete content of sshacc.txt and remplace it by an ssh account as the following example:
host:port@username:password 
the ssh account have to be with stunnel port 443

4- open a new tab in termux

6-run the ssh script python ssh.py

After ssh connected the tun2tap apk will launched if your device rooted else launch it manuelly!

When it launch successfully, add this settings

Server ip 127.0.0.1 

Port 1080


enjoy free surfing 😎😎😂😂
