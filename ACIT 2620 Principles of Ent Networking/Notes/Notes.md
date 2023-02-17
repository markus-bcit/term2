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
---
^^^QUIZ 1^^^
---
# Ethernet and LAN

- ## Subdivided Data Link Layer
	- ![[Pasted image 20230120143607.png]]
- ## Data Link Layer Sublayers
	- Logical Link Control (LLC)
		- Used to facilitate multiple upper layer (i.e. network )  protocols  
		- Provides common interface to upper layers  
		- Supplies multiplexing and flow control services  
		- Provides error checking
- ## Media Access Control (MAC)  
	- Media Access Control (MAC) is a protocol used in networking to control access to a shared medium, such as a wired or wireless network.
	- MAC is responsible for managing the communication between devices on a network, ensuring that data is transmitted and received correctly.
	- Each device on a network has a unique MAC address assigned to it.
	- MAC protocol uses these MAC addresses to control access to the network and to identify devices.
- ## Frames: Outermost PDU
	- -   A frame is the outermost Protocol Data Unit (PDU) in networking.
	-   It contains the data being transmitted, as well as control information such as error detection and correction codes, source and destination addresses, and other headers and trailers.
	-   The frame is responsible for providing the physical link between devices on a network and for ensuring that data is transmitted reliably and correctly.
	-   The frame format can vary depending on the type of network and protocol being used, but generally includes fields for source and destination addresses, control information, and the payload (the actual data being transmitted).
		- Structured package for moving data  
		- Includes raw data (or payload) along with sender’s and receiver’s:  
			- Network addresses  
			- Error-checking and control information
	- ![[Pasted image 20230120144803.png]]
- ## Ethernet II Frames
	-  Ethernet II frames are the standard frame format used in Ethernet networks.
	-   They include fields for source and destination MAC addresses, a type field, and a payload (data being transmitted).
	-   The Ethernet II frame also includes a cyclic redundancy check (CRC) field, which is used to detect errors in the transmission of the frame.
	-   The minimum size of an Ethernet II frame is 64 bytes and the maximum is 1518 bytes, including the header and the payload but not including the preamble and SFD.
	-   Ethernet II frames are usually used for Internet Protocol (IP) and Address Resolution Protocol (ARP) packets, but can also be used for other types of packet as well.
	- A
		- Preamble  
			- Marks beginning of entire frame  
		- Start of Frame Delimiter (SFD)  
			- Indicates beginning of addressing frame  
		- Destination Address  
			- Contains destination node address  
		- Source Address  
			- Contains address of originating node  
		- Length (LEN)  
			- Indicates length of packet  
		- Data  
			- Contains data, or segmented part of data, transmitted from originating node  
		- Pad  
			- Used to increase size of the frame to its minimum size requirement of 46 bytes  
		- Frame Check Sequence (FCS)  
			- Provides an algorithm to determine whether data were correctly received  
				- Most commonly used algorithm is Cyclic Redundancy Check (CRC)
				- 
- ## Ethernet Addressing
	- ![[Pasted image 20230120145318.png]]
	- MAC address: Media Access Control (MAC) sub-layer  
	- 48 Bits  
	- Number uniquely defining a network node  
	- Generally rendered as Hex: 00:1e:33:ba:87:c1  
	- first three bytes  
		- Either Manufacturer hard coded  
		- Or Reserved Addresses (common ones)  
			- Broadcast Address : FF:FF:FF:FF:FF:FF  
			- **Spanning Tree Multicast:  01:80:C2:00:00:00  **
			- IANA reserves all address starting  with 00:00:5E see Ethernet Numbers (this includes IPv4 multicast - and inserts the low 23 Bits of the multicast  IPv4 Address into the Ethernet Address)  
			- 33:33:XX is reserved for IPv6 Multicast  
		- Doesn't contain any data regarding network location – just an ID
- ## Switches and Bridges: Making a bigger LAN
	- ![[Pasted image 20230120145455.png]]
	- -   A switch is a networking device that connects multiple devices together on a network.
	-   It uses MAC addresses to forward data packets only to the intended device, increasing network performance by reducing network congestion and collisions.
	-   A bridge is a networking device that connects multiple network segments together, allowing devices on different segments to communicate with each other.
	-   Bridges use MAC addresses to forward data packets only to the intended segment, increasing network performance by reducing the size of collision domains.
	-   Both switches and bridges use a process called store-and-forward switching, where the device receives a frame, examines its MAC address, and then forwards it to the correct output port.
		- Forward/Filter Decisions 
		- Filtering database  
			- Collection of data created and used by a bridge / switch that correlates the MAC addresses of connected workstations with their locations  
		• Also known as a **forwarding table**
- ## Forwarding Table Creation
	- -   A forwarding table is a data structure used by networking devices, such as switches and routers, to determine where to forward incoming packets.
	-   The table is created by the device learning the location of devices on the network by examining the source MAC address of packets received.
	-   The device adds the source MAC address and the corresponding input port to the forwarding table.
	-   When a packet is received, the device looks up the destination MAC address in the forwarding table and forwards the packet to the corresponding output port.
	-   If the destination MAC address is not found in the forwarding table, the packet is typically broadcast to all ports.
	-   Some devices may use additional information like IP address to create the forwarding table.
	-   The process of creating and updating the forwarding table is called learning.
		- Transparent bridging  
			- Method used on many Ethernet networks  
			- Builds up table port / destination in the course of operation  
		- Spanning tree algorithm  
			- Necessitated by multiple paths links between networks  
			- Routine that can detect circular traffic patterns and modify the way multiple bridges work together, in order to avoid such patterns  
			- Explicit exchange of bridging information
- ## Broadcast Loop Problem
	- ![[Pasted image 20230120145605.png]]
- ## Spanning Tree Protocol
	- ![[Pasted image 20230120150327.png]]
- ## VLANs
	- -   VLAN (Virtual Local Area Network) is a way to segment a physical network into multiple logical networks.
	-   Each VLAN is a separate broadcast domain, meaning that devices on one VLAN cannot communicate directly with devices on another VLAN, unless a router is used to connect them.
	-   VLANs are configured by creating a **VLAN ID** and assigning devices to it, allowing the network administrator to group devices together based on their function, department or security requirements.
	-   VLANs can be implemented using software or hardware, such as VLAN-enabled switches, that can create and maintain VLANs.
	-   VLANs provide increased security and flexibility by isolating network traffic and allowing the network administrator to create multiple smaller broadcast domains within a larger network.
	- ![[Pasted image 20230120150446.png]]
- ## VLAN “Port” Types
	- Access:  have dedicated VLAN assignment at the switch  
	- Trunk:  Carry the VLAN tag as part of the ethernet frame
- ## 802.1Q: Virtual LAN Frames
	- ![[Pasted image 20230120151416.png]]
	- 802.1Q adds a 4-byte tag header:  
		- 2-byte tag protocol identifier (TPID) :  
			- a fixed value of 0x8100 that indicates the frame carries tag  information.  
		- 2-byte tag control information (TCI) :  
			- Three-bit user priority (used to prioritize traffic  
			- Drop Eligible Indicator (DEI) (in congestion is frame “dropable”
			- Twelve-bit VLAN identifier (VID)-Uniquely identifies the VLAN to  which the frame belongs
- ## Accessing the link: Ethernet Channel Access Methods
	- Contention  
		- CSMA/CD  
		- CSMA/CA  
	- Buffered: i.e. switched Ethernet  
	- Polling: i.e. devices asked by host  
	- Token Passing
- ## CSMA-CD Ethernet
	- ![[Pasted image 20230120151902.png]]
- ## Some Definitions
	- On an Ethernet network, an individual network segment is known as a **collision domain ** 
		- Portion of network in which collisions will occur if two nodes transmit data at same time  
	- Data propagation delay  
		- Length of time data take to travel from one point on the  segment to another point 
- ## CSMA CA: Wireless Ethernet
	- ![[Pasted image 20230120152033.png]]
# Day 4


| MODE | VM to Host | Host to VM | VM to VM | VM to External | External to VM | 
| --- | --- | --- | --- | --- | --- | 
| Host Only | Yes | Yes | Yes | No | No | 
| Internal | No | No | Yes | No | No | 
| Bridge | Yes | Yes | Yes | Yes | Yes | 
| NAT | Yes | Port Forward | No | Yes | Port forward | 
| NAT Network | Yes | Port Forward | Yes | Yes | Port Forward |
| Not attached | No | No | No | No | No |

## TCP/IP Suite

- Internet Protocol (IP)  
- Routing Protocols (Used in routing table generation)  
- Dynamic Host Configuration Protocol (DHCP)  
- Transport Control Protocol (TCP)  
- User Datagram Protocol (UDP)
- Internet Control Message Protocol (ICMP)  
- Address Resolution Protocol (ARP)

## Related TCP/IP Suite Protocols

- User Datagram Protocol (UDP)  
	- Connectionless transport service  
- Internet Control Message Protocol (ICMP)  
	- Notifies sender of an error in transmission process and that packets were not delivered  
- Address Resolution Protocol (ARP)  
	- Obtains MAC address of host or node  
	- Creates local database mapping MAC address to host’s IP address

## ARP  
- ARP table  
- Database that lists the associated MAC and IP addresses  
	- Contains two types of entries:  
		- Dynamic ARP table entries  
		- Static ARP table entries  
- ARP utility provides a way of obtaining information from and manipulating a device’s ARP table

## Reverse Address Resolution Protocol (RARP)  
- Allows the client to send a broadcast message with the MAC address of a device and receive the device’s IP address in reply
	- ![[Pasted image 20230215193358.png]]

## Packet Internet Groper (PING)  
- Troubleshooting utility that can verify TCP/IP is installed, bound to the NIC, configured correctly, and communicating with the network  
- An echo request is a signal sent out to another computer  
- An echo reply is the other computer’s response signal  
- Process of sending this signal back and forth is known as pinging

## Data Link Layer  
- Generally Ethernet  
- Handles the movement of data between nodes on the same link  E.g. Ethernet 
- Present on every network device  
- Data Link Specific Devices  bridge, hub, switch

## Network Layer  
- Goal: move packets for source to destination  
- Path Determination  
- the calculation of the route taken by packets  routing 
	- Forwarding  
		- The movement of a packet from one network to the next appropriate network

## The Internet Network layer  
Host, router network layer functions:
	![[Pasted image 20230215193706.png]]

## Internet Protocol (IP)  
- Provides information about how and where data should be delivered  
- Subprotocol that enables TCP/IP to **internetwork** 
	- To internetwork is to traverse more than one LAN segment and more than one type of network through a router  
	- In an internetwork, the individual networks that are joined together are called subnetworks 
- IP is an unreliable, connectionless protocol, which means it does not guarantee delivery of data  
- Allows protocol to service a request without requesting verified session and without guaranteeing delivery of data, making it simpler and faster
- 
## IP Addressing: introduction  
IP address: 32-bit identifier for host, router interface  
- interface: connection between host, router and physical link  
- router’s typically have multiple interfaces  
- host may have multiple interfaces  
- IP addresses associated with interface, not host, router
	- ![[Pasted image 20230215194057.png]]
- IP address: 
	- network part (high order bits)  
	- host part (low order bits)  
- What’s a network ?  ( from IP perspective)  
	- device interfaces with same network part of IP address  
	- can physically reach each other without intervening router
	- ![[Pasted image 20230215194239.png]]
## IP Addressing  
- How to find the  networks?  
- Detach each interface from router, host  
- create “islands of isolated networks
- ![[Pasted image 20230215194335.png]]
## IP Addresses
![[Pasted image 20230215194359.png]]

## IP addressing: CIDR  
- Class based addressing:  
	- inefficient use of address space, address space exhaustion  
	- e.g., class B net allocated enough addresses for 65K hosts, even if only 2K hosts in that network  
- CIDR: Classless Inter Domain Routing  
- network portion of address of arbitrary length  
- address format: a.b.c.d/x, where x is # bits in network portion of address  
- Also written as address + subnet mask
	- ![[Pasted image 20230215194501.png]]
## CIDR Revisited: Subnet Mask  
- Usually written in dotted decimal notation
- ![[Pasted image 20230215194521.png]]

## Special IP Addresses
- ![[Pasted image 20230215194542.png]]
## Broadcast IP Addresses  
- Limited Broadcast 
	- 255.255.255.255  
	- Transmitted only on local segment  not routed  
- Network Broadcast Address  
	- Network Address + All host bits set to one  
		- Network Address = 192.168.1.x  
		- Network Broadcast Address = 192.168.1.255  
- Multicast Address  
	- Lie within the 224.0.0.0 /4 network  
	- http://www.iana.org/assignments/multicast-addresses

## How IP addresses are assigned:  
- Hosts (host portion):  
- Static  hard-coded by system administrator  
- DHCP: Dynamic Host Configuration Protocol:  
	dynamically get address: “plug-and-play”  
	- host broadcasts “DHCP discover” msg  
	- DHCP server responds with “DHCP offer” msg  
	- host requests IP address: “DHCP request” msg  
	- DHCP server sends address: “DHCP ack” msg

## IPv4 Header
- ![[Pasted image 20230215194724.png]]
## IPv6 Header
- ![[Pasted image 20230215194740.png]]
## Getting a datagram from source to destination
- datagram remains unchanged, as it travels source to destination  
- addr fields of interest here
- ![[Pasted image 20230215194837.png]]
- tarting at A, given IP datagram addressed to B:  
	- look up net. address of B  
	- find B is on same net. as A  
	- link layer will send datagram directly to B inside link-layer frame  
		- B and A are directly connected
- Starting at A, dest. E:  
	- look up network address of E  
	- E on different network  
	- A, E not directly attached  
	- routing table: next hop router to E is 223.1.1.4  
	- link layer sends datagram to router 223.1.1.4 inside link- layer frame  
- datagram arrives at 223.1.1.4
- Arriving at 223.1.4, destined for 223.1.2.2  
	- look up network address of E  
	- E on same network as router’s interface 223.1.2.9  
		- router, E directly attached  
	- link layer sends datagram to 223.1.2.2 inside link-layer frame via interface 223.1.2.9  
	- datagram arrives at 223.1.2.2!!! (hooray!)
- ![[Pasted image 20230215194852.png]]
- 
## Easing Configuration1: Bootstrap Protocol (BOOTP)
- Service that simplifies IP address management
- ![[Pasted image 20230215195251.png]]
## Bootstrap Protocol (BOOTP)  
- Thanks to BOOTP, a client does not have to remember its own IP address  
	- Therefore, network administrators do not have to go to each workstation on a network and manually assign its IP address  
- This situation is ideal for diskless workstations

## Easing Configuration2: Dynamic Host Configuration Protocol  (DHCP)
- Automated means of assigning a unique IP address to every device on a network  
- Reasons for implementing DHCP 
	- Reduce the time and planning spent on IP address management  
	- Reduce the potential for errors in assigning IP addresses  
	- Enable users to move their workstations and printers without having to change their TCP/IP configuration  
	- Make IP addressing transparent for mobile users
## DHCP Leasing Process  
- Agreement between DHCP server and client on how long the client will borrow a DHCP-assigned IP address
- ![[Pasted image 20230215195514.png]]

## Terminating a DHCP Lease  
- A DHCP lease may expire based on the period established for it in the server configuration  
- A DHCP lease may be manually terminated at any time from either the client’s TCP/IP configuration or the server’s DHCP configuration  
- In some instances, a user must terminate a lease 
- Release  
	- The act of terminating a DHCP lease
## IP address space  
- IP address: 32-bit identifier for host, router interface  
- This translates to 4,294,967,296 unique addresses  
- The internet is network of networks, i.e. a collection of multiple IP networks spread across the globe  
- Each IP network is a range of IP addresses – a smaller address space  
- An IP address space is identified by a subnet ID obtained using a subnet mask  
- The size of the address space is determined by the hosts bits
- “The internet does not have a hierarchical topology, rather the interpretation of addresses is hierarchical.” (RFC 950)

## IP addressing: ISPs  
Q: How does an ISP get block of addresses?  
A: **ICANN**: **I**nternet **C**orporation for **A**ssigned **N**ames and **N**umbers  
	- allocates addresses  
	- manages DNS  
	- assigns domain names, resolves disputes

## IP addresses: how to get one?  
Network (network portion):  
- get allocated portion of ISP’s address space:
```
ISP's block 11001000 00010111 00010000 00000000 200.23.16.0/20  
Organization 1 11001000 00010111 00010010 00000000 200.23.18.0/23  
Organization 2 11001000 00010111 00010100 00000000 200.23.20.0/23  
	...                   .....              ....       ....  
Organization 7 11001000 00010111 00011110 00000000 200.23.30.0/23
```

## Subnetting  
- The prefix “sub” implies a relation (i.e. a portion of another larger network)  
- It is the process dividing a larger address range into a contiguous sets of addresses (whose size is a power of 2) to best reflect a network’s logical topology  
- Example:  
	- Subnet 10.1.0.0/16,  
		- 8 more bits are assigned to the network ID, to create 256 subnets with a /24 mask.  
	- Mask allows for 254 host addresses per subnet  
	- Subnets range from:  
		- 10.1.0.0 / 24 to 10.1.255.0 / 24
- ![[Pasted image 20230215200326.png]]

## Subnetting - Why  
- Smaller networks are easier to manage  
- Network topology constraints  
- Reduced network traffic. LANs rely on ARP broadcasting to communicate. Because of this broadcasting nature of LAN, larger networks mean poor performance.  
- Increased security  
- Reduced IP wastage

## Subnet size  
- Each subnet represents a finite address space, a block or range of IP addresses  
- The first address in the range is used to identify the entire subnet  
- The last address in the range is the broadcast address for the subnet  
- If N is the size of subnet S, then the number of usable addresses in S is N – 2  
- Eg. Given IP address 10.0.15.20/24 then:  
		Subnet size: 256  
		Subnet ID: 10.0.15.0/24  
		Broadcast ID: 10.0.15.255/24  
		Usable addresses: 254 (10.0.15.1 – 10.0.15.254)
		
## Smallest possible subnet  
- Since two addresses are reserved for the network ID and broadcast ID, the smallest possible subnet has a size of 4  
- 2 bits are needed to represent a magnitude of 4  
- In subnetting, 2 bits are always reserved for the host  
- /30 is the smallest subnet  
- In reality, the need for such a network rarely occurs

## Subnet prefix  
- The subnet prefix is the portion of the IP address that identifies the subnet, in binary  
- For classful subnets, this maps to a decimal prefix  
- Example:  
	- 10.0.1.0/8 prefix: 10  
	- 192.168.0.1/16 prefix: 192.168  
	- 10.0.15.20/24 prefix: 10.0.15  
- For classless subnets, the binary prefix does not always map to a decimal representation  
- Example: 
	- 10.48.20.200/12 and 10.63.255.10/12 are both part of the same subnet (in this case, the network ID is 10.48.0.0/12 and the broadcast ID is 10.63.255.255/12)
- ![[Pasted image 20230215200613.png]]

## Classless subnetting  
- Traditionally, breaking a larger network into smaller subnets followed a classful strategy, i.e. the split occurred at the byte boundary  
- Example:  
	- Large address space: 10.0.0.0/16  
	- Subnets:  
		- 10.0.0.0/24  
		- 10.0.0.1/24  
		- 10.0.0.2/24  
		- etc  
- The problem with this approach is that it wastes addresses. All subnets have the same size, regardless of actual requirements (Fixed Length Subnet Mask or FLSM)  
- Classless subnetting supports both FLSM and VLSM (Variable Length Subnet Mask) subnetting
- Instead of splitting the network at byte boundary, you estimate the number of host bits to use in subnetting based on desired number of networks and range requirements for each subnet  
- Example:  
	- Large address space: 10.0.1.0/24  
	- Subnets:  
		- 10.0.1.0/25       126 hosts  
		- 10.0.1.128/26      62 hosts  
		- 10.0.1.192/26      62 hosts  
		- etc

# Day 6 
192.168.2.128/25 size: 128
sizes : 32
128/32 = 4 

## Generic process 
1. Determine number of networks
2. determine number of hosts per netwrok 
3. Add 2 to number of hosts per netwrok and round to the neraest power of 2
4. perform a quick check that assigned netwrok range can accomodate all the required addresses/
5. sort the neweroks in order of size (this can be altered but makes process not algorithmic)
6. Start with the largest network:
	1. divide network into equal parts size according to the largest subnet. the number of parts will deternime how many bits to use in subnetting
	2. Example: 1 extra bit to yield 2 subnets, 2 extra bits to yield 4 subnets, 3 extra bits to yield 8 subnets etc 
		- `Extra bit * 2`
	3. assign the blocks to the subnets excleduding already assignment blocks
	4. repeat the process . starting with the bext biggest subnet until all subnets have been assigned 
198.168.5.0/24 => 256

Requirements: subnet1 -> 35 hosts => 37 => 64
						subnet2 -> 50 hosts => 52 => 64
						subnet3 -> 90 hosts => 92 => 128/256
						
Sorting: 128, 64, 64


``` python 
Step 1: 192.168.5.0 - 192.168.5.127 / 25 
		192.168.5.128 - 192.168.5.255 / 25
Step 2: 192.168.5.128 - 192.168.5.191 / 26
		192.168.5.192 - 192.168.5.255 / 26
Sorting:
	128 Sub1: 192.168.5.0 / 25
	64  Sub2: 192.168.5.128 / 26
	64  Sub3: 192.168.5.192 / 26
```

ex2:
```js
172.16.53.0 / 24 -> 256
Requirements: S1: 50 hosts => 52 -> 64  |
			  S2: 25 hosts => 27 -> 32  |
			  S3: 20 hosts => 22 -> 32
			    |
			  S4: 10 hosts => 12 -> 16  |
			  S5: 15 hosts => 17 -> 32  >>>> / 256    
			  S6: 32 hosts => 34 -> 64  |
			  S7: 5 hosts  => 7  -> 8   |

Step 1: 172.16.53.0-63    /
		172.16.53.64-127  / >>  26
		172.16.53.128-192 / >>
		172.16.53.192-255 /

Step 2: 172.16.53.128-159  / 27
		172.16.53.160-191  / 27

Step 3: 172.16.53.192-223  / 27
		172.16.53.224-255  / 27

Step 4: 172.16.53.224-239  / 23
		172.16.53.240-247  / 29

S1: 172.16.53.0 / 26
S2: 172.16.53.64 / 26
S3: 172.16.53.128 / 26
S4: 172.16.53.160 / 26
S5: 172.16.53.192 / 26
S6: 172.16.53.224 / 26
S7: 172.16.53.240 / 29

-   10.0.0.0 to 10.255.255.255
-   172.16.0.0 to 172.31.255.255
-   192.168.0.0 to 192.168.255.255
-   192.168.12.8
-   10.25.6.9
-   172.16.4.7
-   172.25.16.10
```