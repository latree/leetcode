# Template

## requirements

    1. functional requirements
    
    2. non-functional requirements
        highly available
        latency requriement
        high scallability
        consitency
        highly reliable

        decide if system is a read heavy system

    3. Capacity estimation
        a. traffic estimation
        b. storage estimation
        c. bandwith estimation
        d. memory estimation
    
    4. System APIs
        remmeber: api_dev_key always needed for some general APIs

## Standard solution for each component and their pros and cons

    1. Load balancer
        a. Round robin
            pros: 
                distribute evenly and simply LB solution
                Another benefit of this approach is that if a server is dead, LB will take it out of the rotation and stop sending any traffic to it
            cons: 
                Round robin does not consider server load
            improvement: have periodically server load checks on LB then decide if request can be sent to server
        
    2. Data partition in data store
        a. Range based partition
            pros: straight forward
            cons: distribution can be un-balanced
        b. Hash-based partition
            pros: make sure data partitioned evenly
            cons: Adding nodes can be mess when all partitions overload because it needs to do rehash and partitioning, which can be solved using Consistent Hashing.

        c. Consistent Hashing
            pros: 
                resolve issue with simple based hashing for adding or removing nodes
            cons:
                this scheme can result in non-uniform data and load distribution, since when a node is removed, the next node becomes responsible for all of the keys stored on the outgoing node
                solution for this cons: add virtual node. 

## mocking interview notes

1. Discuss with interviewer for the functional and non-functional requriements
2. non-functional requirement
    availability
    scalability
    consistency
    latency
    reliability
3. estimate and calculation the storage, traffic
4. Design a data schema and API this part may spend small time on this. Maybe 3 mins
5. Design the architecture. 
6. Talk about design bottleneck and how to improve it. easy way is scaling up
7. The mock interview does not focus too much on data sharding. 

## data partioning methods

1. vertical based partitioning
    always has pros and cons, the reason is different based on the use case
    scale issue, if there is some special case happend, e.g. some influencer is popular
    table joing can be an issue
2. range-based partitioning
    always have in-balanced partitioning
    if range based on alphabet, a's data is large, b's data is small
3. hash-based partitioning
    may leads to overload partition if the hash_map is not enough. There is high cost on rehashing
    consistant hashing solve the problem. 
