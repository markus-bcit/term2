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
- 