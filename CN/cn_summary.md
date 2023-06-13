# Important stuff
## Internet

- Internet connects End Systems/ Hosts by a system of communications links and package switches
- Pakets: data segment and header
- IP (Internet Protoco): Specifies the format for packets sent among routers and end systems
- DSL (digital subscriber line): broadband residential access
- FDM (Frequency-division multiplexing): link dedicates a frequency band on the band to a communication for the duration of connection. The width of this band is called bandwidth.
- TDM (time-division multiplexing): time is divided into frames of fixes size, and each frame is split into a fixed amount of slots. These slots are dedicated to one connection

## Delays
- **nodal processing delay:** 
    - Time used to decode the header, determine which output needs to be used, bit level checking etc.
    - nedligible in comparison to other delays, little room for improvement here
    
- **queuing delay:** 
    - Time that the packet has to wait in the queue until the desired output will be free
    - better load balancing (i.e. via routing), reduce queue size

- **transmission delay:** 
    - Time after the packet gets out of queue until its on the output line; let L be the length of the packet, R the transmission rate from router A to B, then the transmission delay is L/R.
    - increase the link capacity
- **propagation delay:** 
    - Time, the package takes to propagate through the physical medium (e.g. at light speed with radio waves), i.e. it takes on the way from router A to B
    - if possible, use data replication to shorten the client-server distance. Improving routing or physical transmission media also helps

## Layers
|Layers|
|-|
|Aplication|
|Transport|
|Network|
|Link|
|Physical|

- **Application Layer:** Application protocols and layers reside here. The internet includes many protocols here, as HTTP (provides Web document requests and responses), SMTP (for e-mail transfer) and FTP (file transfer from host to host). The DNS is also an application layer protocol. Packet of information at this layer is called message

- **Transport Layer:** Transports application layer messages between application endpoints. In the internet, there’s TCP and UDP. E.g. longer messages are split into shorter segment. Packets in this layer are called segments.

- **Network Layer:** Packets in this layer are called datagrams. The layer is responsible for moving datagrams from host to host. It receives a segment and an address. This layer includes the IP, which defines the
fields in a datagram and how to work on those fields.

- **Link Layer:** The network layer brings a datagram from one node to another, but to move a packet from one specific node to another, it relies on the link layer. It delivers the packet to the next node. E.g. Ethernet or WiFi. Link layer protocols are called frames.

- **Physical layer:** The job of the link layer is to move whole frames from one node to another; however, the job of the physical layer is to move individual bits. Many protocols exist, depending on the physical medium; e.g. Ethernet has different protocols for different cable types.


## DNS servers
### Resource Records (RRs)
- **Type=A:** Name refers to a hostname, Value refers to the corresponding IP address. Hence, this type provides a standard hostname to IP mapping.
- **Type=NS:** Name is a domain (e.g. foo.com) and Value is the hostname of an authoritative DNS server who can how to obtain the IP address of the query.
- **Type=CNAME:** Value is the canonical host name for the alias host name Name.
- **Type=MX:** Value is the canonical name of a mail server
with alias Name.

## Congestion signals
Signals that warn about congestion:
- **Packet loss**: 
    - Advantage: can be detected easily (doesn't require in-network feature support) by using timers. 
    - Disadvantage: only considers binary feedbaack (i.e., packet either arrives at sender or not)
    - Disadvantage: loss can also be caused by other factors (i.e. cosmic radiation in a satellite link), careful parametrization is needed

- **Packet latency**:
    - Advantage: can be detected easily (doesn't require innetwork feature support). 
    - Advantage: relatively quick feedback of a continuous signal
    - Disadvantage: many factors in the network can affect latency, not only congestion, careful parametrization is needed.

- **In-network marking (i.e. ECN- Explicit Congestionn Notifictation)**
    - Indicate congestion through setting a bit in packet
    - Advantage: early signal of congestion
    - Disadvantage: requires support in the network by i.e. the routers/switches

## Reliable transport protocol:
### Undesirable effects when sending packets:
- Packet loss
- Reordering
- Delay
- Duplication
- Corruption

### Goals of reliable tranfer
- Correctness: ensure data is delivered, in order, and untouched
- Fairness: play well with concurrent communications
- Timeliness: minimize time until data is transferred
- Efficiency: optimal use of bandwidth


## Random
- slow start threshold (ssthresh):
    - function of congestion
    - timout, we set sstresh = cwnd/2
    - initially cwnd is infinity
    - slow start until a timeout occurs
    - slow sart until timeout or we reach ssthresh -> we switch to AIMD

- A socket is a software abstraction by which an application process exchanges network messages with the (transport layer in the) operating system
- The ideal congestion window size is the Bandwidth delay product. $$W = bandwidth * delay$$




## Quiz
- **The Maximum Segment Size(MSS) of TCP is equal to:**
MSS = MTU - header(IP) - headeer(TCP)

- UDP sockets type is SOCK_DGRAM while TCP sockets type is SOCK_STREAM
- For a SOCK_STREAM, an operating system stores both local and remote port
- Given a directed graph G(V, E) with |V| and |E| being the numbers of vertices and edges, how many variables do you need for the max-flow LP formulation discussed in class?
- There is no connectio establishment in UDP
- The objective of flow control is not to overwhelm the hosts
- The objective of congestion control is to not ovewhelm the network
- During congestion avoidance in TCP, the successful acknowledgement of a segment results in the sender congestion window growin by one segment per RTT.
- TCP (SOCK_STREAM) is a connection-based protocol. The connection is established and the two parties have a conversation until the connection is terminated by one of the parties or by a network error.
- UDP (SOCK_DGRAM) is a datagram-based protocol. You send one datagram and get one reply and then the connection terminates.
- Given a directed graph G(V,E), with |V| and |E| being the numbers of vertices and edges, how many variables do you need for the max-flow LP formulation discussed in
class?: O(|E|)
- QUIC can handle switching from WiFi to a cellular network without having to reestablsih the connection:
    - uses connection IDs independent of the IP address istead of a 4-tuple like TCP to identify connections.
    - This way packets using the connection ID are still valid, even if the source IP address changes.




