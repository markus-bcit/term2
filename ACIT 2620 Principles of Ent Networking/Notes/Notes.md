#### PowerShell CMD
```PS C:\Users\Markus> ssh admin@10.20.30.253
ssh: connect to host 10.20.30.253 port 22: Connection refused
PS C:\Users\Markus> ssh admin@10.20.30.100
The authenticity of host '10.20.30.100 (10.20.30.100)' can't be established.
ECDSA key fingerprint is SHA256:/IazpuOgtUOjwhmUBxnuCyE0MdRkImxfuFczPkdlCKw.
Are you sure you want to continue connecting (yes/no/[fingerprint])? Y
Please type 'yes', 'no' or the fingerprint: yes
Warning: Permanently added '10.20.30.100' (ECDSA) to the list of known hosts.
admin@10.20.30.100's password:
Last login: Fri Jan 13 14:27:24 2023
[admin@base ~]$ ssh r1
ssh: Could not resolve hostname r1: Name or service not known
[admin@base ~]$ exit
logout
Connection to 10.20.30.100 closed.
PS C:\Users\Markus> ssh r1
ssh: connect to host r1 port 22: Connection timed out
PS C:\Users\Markus> ssh r2
ssh: Could not resolve hostname r2: No such host is known.
PS C:\Users\Markus> ssh r2
ssh: Could not resolve hostname r2: No such host is known.
PS C:\Users\Markus> cd .\.ssh\
PS C:\Users\Markus\.ssh> ssh r2
ssh: Could not resolve hostname r2: No such host is known.
PS C:\Users\Markus\.ssh> cd ..
PS C:\Users\Markus> ssh r2
The authenticity of host '10.20.30.200 (10.20.30.200)' can't be established.
ECDSA key fingerprint is SHA256:/IazpuOgtUOjwhmUBxnuCyE0MdRkImxfuFczPkdlCKw.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.20.30.200' (ECDSA) to the list of known hosts.
Last login: Fri Jan 13 14:27:42 2023
[admin@r2 ~]$ exit
logout
Connection to 10.20.30.200 closed.
PS C:\Users\Markus> ssh r1
Last login: Fri Jan 13 14:29:40 2023 from 10.20.30.253
[admin@r1 ~]$ exit
logout
Connection to 10.20.30.100 closed.
PS C:\Users\Markus>
```

# OSI Model


1. Application || Files
---
2. Presentation || 
--- 
3. Session ||
--- 
4. Transport || NAT Router. Firewall
--- 
5. Network || Router (ip), NAT Router, WIFI
--- 
6. Datalink || NIC, Switch, Bridge, WIFI
--- 
7. Physical || NIC, hub

`P.D.N.T.S.P.A
`people dont need transgender sucking penis amen``

## Network Devices 
- Network Interface Controller/Card (NIC) 
	- ![[Pasted image 20230113151324.png]]
- Hub
	- ![[Pasted image 20230113151529.png]]
- Bridge
	- ![[Pasted image 20230113151605.png]]
- Switch
	- 
	- ![[Pasted image 20230113151220.png]]
- Router - Connects networks
	- ![[Pasted image 20230113152001.png]]
- NAT Router 
	- ![[Pasted image 20230113153105.png]]
- Firewall
- Wireless Access Point (WAP)

## Topologies

- Mesh | all devices are connected together
	- fast connections, hard to scale, 
	- ![[Pasted image 20230113154837.png]]
- Bus | all devices are connected to a single wire
	- cheap, 
	- ![[Pasted image 20230113155707.png]]
- Star | all devices stem from a center point
	- switch 
	- ![[Pasted image 20230113155757.png]]
- Ring | O
	- impossible for more than one device to use at a time

