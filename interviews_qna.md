# Interviews questions and answers

### Q: What is aws route53 and why it is called "route53" ?

### Answer:

```
AWS route53 is a highly available domain name system(DNS) web service. provided by amazon web services. DNS translates the human-readable domain names to into ip address.

Route: Routing internet traffic to the correct servers based on domain names.

53: TCP/UDP port 53 is used by dns servers to listen and responds to DNS queries.
```

### Q: What is the difference between "ADD" and "COPY" in Dockerfile?

### Answer:
```
Both ADD and COPY in a Dockerfile are used to copy files and directories into the Docker image, but they have some key differences:

COPY:
  - Copies files and directories from the host machine to the docker image
  - Only accepts local file system paths as source.
  Does not automatically extract compressed files. (eg., .tar, .gz, .zip)
  - More explicit and predictable in its behavior

ADD:
  - Copies files from the host machine as well as from the remote urls to the docker image.
  - Extract compressed files automatically.
  - Less explicit and can lead to unexpected behavior if not used carefully.
```

### Q: What is canary deployments in kubernetes and what is AB testing?

### Answer:
```
Canary:
  - Canary deployments involve releasing a new version of your application to a small subset of users before rolling it out to the entire user base.
  - Working: Deploy a new version of the application and route small percentage of the traffic to it like 5% of traffic. Monitor the this newly deployed version closely and then gradually move the traffic to it and when confident route all traffic to it.
  - You can use Kubernetes services, Ingress controllers, or traffic routing tools like Istio to route traffic to different versions of your application.

A/B Testing:
  - A/B testing is method of comparing two versions of feature, page or application to determine which version performs better.
  - It involves randomly splitting traffic between two versions and measuring key metrics.

Summary:
  - Canary deployments can be used for A/B testing.
  However A/B testing focuses more on user behaviour and business metrics, while canary deployments primarily focus on technical stability and performance. 
```

### Q: What is the difference between dns record type A, AAAA and CNAME?

### Answer:
```
A: A records maps the hostname to IPv4 address.

AAAA: AAAA records maps the hostname to IPv6 address

CNAME: CNAME record use to create an alias for another hostname. In simple term, it defines that one domain name is an alias for another. Use CNAME records when you want to create an alias for a hostname, such as pointing www.example.com to example.com
```

### Q: What is cron jobs also explain its time definition format?

### Answer:
```
Cron jobs are automated tasks scheduled to run periodically on a computer system.
They are typically used to perform routine mainteinance, data backup, system checks and other administrative tasks.
Format: five fileds represented by *
  - * * * * *
  - first field - minutes (0-59)
  - second field - hour (0-23)
  - third field - DOM (day of the month - (1-31))
  - fourth field - month (1-12)
  - fifth field - DOW (day of the week - (0-7, 0 or 7 is sunday))

Example:
  - * * * * *: Runs every minute
  - 0 0 * * *: Runs every day at midnight
  - 0 8 * * 1-5: Runs every weekday at 8:00 AM
  - 30 18 * * *: Runs every day at 6:30 PM
  - 0 0 1 * *: Runs on the first day of every month at midnight
  - 0 0 * * 0: Runs every Sunday at midnight

Special Characters:
  - *: Matches all values for that field
  - , (comma): Separates multiple values for a field (e.g., 0,30 * * * * runs at 00:00 and 00:30)
  - - (hyphen): Specifies a range of values (e.g., 1-5 for days of the month)
  - / (slash): Specifies increments (e.g., */5 * * * * runs every 5 minutes)
```


### Q: What is the difference between a soft link and a hard link?

### Answer:

```
- Hard link:
Hard links are created using `ln` command. Hard links are just another name for the same file. Hard links can not be created for directories. Hard links can not cross file systems.

- Soft link:
Soft links are created using `ln -s` command. Soft links are symbolic links to the original file. Soft links can be created for directories. Soft links can cross file systems.
```

### Q: What is the difference between a process and a thread?

### Answer:

```
- Process:
A process is an instance of a program running on a computer. A process has its own memory space, system resources, and state. A process can have multiple threads.

- Thread:
A thread is a part of a process. A thread shares the same memory space and system resources of the process. A process can have multiple threads. Threads in the same process share the same data.
```

### Q: What is the difference between a container and a virtual machine?

### Answer:

```
- Virtual Machine:
Virtual machines run on a hypervisor. Hypervisor is a software that runs on physical hardware and creates virtual machines. Each virtual machine has its own operating system, memory, and resources. Virtual machines are isolated from each other.

- Container:
Containers run on a container engine. Container engine is a software that runs on physical hardware and creates containers. Containers share the same operating system kernel, memory, and resources. Containers are isolated from each other using namespaces and cgroups.
```

### Q: What is the difference between a stack and a queue?

### Answer:

```
- Stack:
Stack is a data structure that follows LIFO (Last In First Out) order. Elements are added to the top of the stack and removed from the top of the stack. Stack operations are push and pop.

- Queue:
Queue is a data structure that follows FIFO (First In First Out) order. Elements are added at the rear of the queue and removed from the front of the queue. Queue operations are enqueue and dequeue.
```

### Q: What is the difference between a mutex and a semaphore?

### Answer:

```
- Mutex:
Mutex is a synchronization primitive that allows only one thread to access a shared resource at a time. Mutex is binary semaphore with value
```

### Q: What is the use of VPC peering ?

### Answer:

```
VPC peering is used to connect two different VPCs in the same or different region. It allows you to route traffic between them using private ip addresses as if they are in the same network.

VPC peering does not involve a VPN connection or internet gateway or NAT gateway. It is a networking connection between two VPCs that enables you to route traffic between them using private ip addresses.
```

### Q: What is the use of NAT Gateway ?

### Answer:

```
NAT Gateway is used to provide internet access to the private subnet instances. It allows instances in the private subnet to connect the internet for software updates, patches, etc.

NAT gateway is managed by AWS. It is high available and scales automatically up to 10Gbps.
```

### Q: What is the use of NAT Instance ?

### Answer:

```
NAT instance is used to provide internet access to the private subnet instances. It allows instances in the private subnet to connect the internet for software updates, patches, etc.

NAT instance is a single EC2 instance that you manage. It is not high available. You have to manage the failover and scaling.
```

### Q: What is the use of security group in AWS ?

### Answer:

```
Security group acts as a virtual firewall that controls the traffic for one or more instances. It allows you to specify the inbound and outbound traffic rules.

Security group is stateful. If you allow the inbound traffic rule, the return traffic is automatically allowed. You do not have to specify the outbound traffic rule.
```

### Q: What is the use of NACL in AWS ?

### Answer:

```
Network Access Control List(NACL) is used to control the traffic at the subnet level. It acts as a firewall for controlling the traffic in and out of one or more subnets.

NACL is stateless. If you allow the inbound traffic rule, you have to specify the outbound traffic rule.
```

### Q: What is the use of Bastion Host ?

### Answer:

```
Bastion Host is used to securely administer the instances in the private subnet. It acts as a secure gateway to access the instances in the private subnet.

Bastion host is an EC2 instance that you manage. It should be in the public subnet. You have to connect to the bastion host and then connect to the private instances.
```

### Q: What is the difference between AWS EBS and AWS S3?

### Answer:

```
EBS: Elastic Block Store is a block storage service used for EC2 instances. It is like a hard disk attached to your EC2 instance. It is used to store the data that requires frequent updates.

S3: Simple Storage Service is an object storage service used to store and retrieve any amount of data from anywhere. It is used to store static files and backups.
```

### Q: What is the difference between on-demand and reserved instances?

### Answer:

```
On-demand instances: Pay as you go. No upfront payment is required. You can start and stop the instances as needed. It is suitable for short term and unpredictable workloads.

Reserved instances: Reserved instances are purchased for 1 or 3 years. It offers a significant discount compared to on-demand instances. It is suitable for long term and predictable workloads.
```

### Q: What is the difference between public and private subnet?

### Answer:

```
Public subnet: A public subnet is a subnet that is associated with a route table that has a route to an internet gateway. It allows the resources in the subnet to access the internet.

Private subnet: A private subnet is a subnet that is not associated with a route table that has a route to an internet gateway. It does not allow the resources in the subnet to access the internet.
```

### Q: What is the difference between AMI and snapshot?

### Answer:

```
AMI: Amazon Machine Image is a template that contains a software configuration (for example, an operating system, an application server, and applications) to launch EC2 instances.

Snapshot: A snapshot is a point-in-time backup of an EBS volume. It is stored in S3. You can use a snapshot to create a new volume or to restore an existing volume.
```

### Q: What is the difference between a security group and a network ACL?

### Answer:

```
Security group: A security group acts as a virtual firewall that controls the traffic for one or more instances. It is associated with instances. It allows or denies traffic based on the rules.

Network ACL: A network ACL is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. It is associated with subnets. It allows or denies traffic based on the rules.
```

### Q: What is the use of NACL in AWS ?

### Answer:

```
Network Access Control List(NACL) is used to control the traffic at the subnet level. It acts as a firewall for controlling the traffic in and out of one or more subnets.

NACL is stateless. If you allow the inbound traffic rule, you have to specify the outbound traffic rule.
```

### Q: What is the difference between AWS EBS and AWS S3?

### Answer:

```
EBS: Elastic Block Store is a block storage service used for EC2 instances. It is like a hard disk attached to your EC2 instance. It is used to store the data that requires frequent updates.

S3: Simple Storage Service is an object storage service used to store and retrieve any amount of data from anywhere. It is used to store static files and backups.
```

### Q: What is the difference between AMI and snapshot?

### Answer:

```
AMI: Amazon Machine Image is a template that contains a software configuration (for example, an operating system, an application server, and applications) to launch EC2 instances.

Snapshot: A snapshot is a point-in-time backup of an EBS volume. It is stored in S3. You can use a snapshot to create a new volume or to restore an existing volume.
```

### Q: What is the difference between a security group and a network ACL?

### Answer:

```
Security group: A security group acts as a virtual firewall that controls the traffic for one or more instances. It is associated with instances. It allows or denies traffic based on the rules.

Network ACL: A network ACL is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. It is associated with subnets. It allows or denies traffic based on the rules.
```

### Q: What is the difference between TCP and UDP?

### Answer:

```
TCP (Transmission Control Protocol) is a connection-oriented protocol that provides reliable, ordered, and error-checked delivery of a stream of bytes between applications running on hosts communicating over an IP network.

UDP (User Datagram Protocol) is a connectionless protocol that provides unreliable, unordered, and error-checked delivery of a stream of bytes between applications running on hosts communicating over an IP network.
```

### Q: What is the difference between stateful and stateless firewalls?

### Answer:

```
A stateful firewall keeps track of the state of active connections and uses this information to determine which network packets to allow through the firewall. It can make decisions based on the context of the traffic, such as whether it is part of an established connection or a new connection attempt.

A stateless firewall, on the other hand, does not keep track of the state of connections and makes decisions based on individual packets. It filters traffic based on predefined rules, such as source and destination IP addresses, ports, and protocols, without considering the context of the traffic.
```

### Q: What is the difference between a proxy server and a reverse proxy server?

### Answer:

```
A proxy server acts as an intermediary between clients and servers, forwarding requests from clients to servers and responses from servers to clients. It can be used to filter or cache requests, hide the client's IP address, or improve performance by distributing requests across multiple servers.

A reverse proxy server, on the other hand, acts as an intermediary between clients and servers, forwarding requests from clients to servers and responses from servers to clients. It can be used to load balance traffic across multiple servers, cache responses, or provide security features such as SSL termination.
```

### Q: What is the difference between a classic load balancer and an application load balancer in AWS ?

### Answer:

```
Classic Load Balancer:
- Works on layer 4 of the OSI model.
- Supports TCP and SSL protocols.
- Can route traffic based on IP address to different EC2 instances.

Application Load Balancer:
- Works on layer 7 of the OSI model.
- Supports HTTP and HTTPS protocols.
- Can route traffic based on URL in the HTTP header to different EC2 instances.
```

### Q: What is the difference between an AMI and an EBS snapshot in AWS ?

### Answer:

```
AMI(Amazon Machine Image):
- AMI is a template for the root volume of an EC2 instance.
- AMI includes the operating system, application server, and applications.
- AMI can be used to launch multiple EC2 instances with the same configuration.

EBS Snapshot:
- EBS snapshot is a backup of an EBS volume.
- EBS snapshot is a point-in-time copy of the EBS volume.
- EBS snapshot can be used to create a new EBS volume or restore an existing EBS volume.
```

### Q: What is the difference between ec2 and lambda ?

### Answer:

```
EC2: Elastic Compute Cloud, It is a virtual server in the cloud. You can configure the server as per your need, like memory, cpu, storage, etc.

Lambda: Lambda is a serverless computing service provided by AWS. You don't need to provision a server, you just need to write the code and lambda will run it for you.
```

### Q: What is the difference between ec2 and lambda ?

### Answer:

```
EC2: Elastic Compute Cloud, It is a virtual server in the cloud. You can configure the server as per your need, like memory, cpu, storage, etc.

Lambda: Lambda is a serverless computing service provided by AWS. You don't need to provision a server, you just need to write the code and lambda will run it for you.
```

### Q: What is the difference between ssm and kms?

### Answer:

```
SSM: Systems manager service. Used to manage EC2 instances and on-premises servers. It helps to automate tasks, maintain software compliance, and configure OS.

KMS: Key management service. Used to create and manage cryptographic keys. It helps to encrypt data and manage permissions to use the keys.
```

### Q: What is the difference between horizontal and vertical scaling?

### Answer:

```
Horizontal Scaling:
1. Horizontal scaling means that you scale by adding more machines into your pool of resources.
2. Horizontal scaling is the ability to connect multiple hardware or software entities so that they work as a single logical unit.
3. Horizontal scaling is the most common way of increasing capacity in the cloud.
4. Example: Adding more EC2 instances to your application.

Vertical Scaling:
1. Vertical scaling means that you scale by adding more power (CPU, RAM, Storage, etc) to an existing machine.
2. Vertical scaling is the ability to increase the capacity of existing hardware or software by adding resources.
3. Vertical scaling is limited by the fact that you can only get as big as the size of the server.
4. Example: Increasing the RAM of a server.
```

