# Byzantine chain replication (BCR)

This is phase 2 implementation of Byzantine chain replication protocol for the
course project CSE 535.

## PLATFORM USED FOR DEVELOPMENT AND TESTING

This project is being developed and tested on Mac OSX as well as Linux.
Specifications are as follows:

1. Mac OSX operating system (Yosemite - 10.10.5)
   Python Version - 3.6.3
   Python Implementation - CPython
   DistAlgo Version - 1.0.9
   Type of Host - Laptop(without VMs)
   Testing methodology - single host(multiple nodes)

2. Ubuntu 16.0.4 Operating System
   Python Version - 3.5.2
   Python Implementation - CPython
   DistAlgo Version - 1.0.9
   Type of Host - Laptop with VMs (MacBook Pro with Ubuntu installed on Virtual
   Box)


### INSTRUCTIONS TO RUN PROJECT

    1.) Set up configuration node:
        python3 -m da -n someNode configure_nodes/configure_nodes.da config/<Any File in this folder>
        Eg. python3 -m da -n someNode configure_nodes/configure_nodes.da 
                config/single_client_with_change_operation_failure_at_tail.csv

    2.) Setting up Olympus:
        python3 -m da -n OlympusNode -D configure_nodes/configure_nodes.da
        note : "OlympusNode" is the node name and should not be changed
    
    3.) Setting up Clients:
        python3 -m da -n ClientNode0 -D configure_nodes/configure_nodes.da
        note : Based on the number of clients, increase cline node name index
        For Eg. next client will have node name ClientNode1.

    4.) Setting up Replicas
        python3 -m da -n ReplicaNode0 -D configure_nodes/configure_nodes.da
        note : next replica will have node name ReplicaNode1

    Once all nodes have been set up, workload will be executed by client/clients
    as mentioned in config file and logs will be generated in main folder of project
    under /logs by node name appended by .log

### WORKLOAD GENERATION ALGORITHM

      For generating pseudorandom workload for client, we have used random module of python.
      generate_psedorandom(seed, n) is the method for generating list of n psedorandom operations.

      Steps:
      1.) Keep 4 supported operations (put, get, slice and append) in a list
      2.) call randint function of python random module with arguments seed and seed + n.
          This gives any number between seed and (seed + n) with equal probability 1/n.
      3.) Take mod of the number, say k, by 4 to get one of the index for supported operations.
      4.) For put, get and append, value of k can be used by appending it to some key and value
          string.
      5.) In case of slice, we can randint again with expected number of value length which was produced 
          in the previous step.
      6.) Thus slice also has equal probability of success as well as failure in any random call.

### BUGS AND LIMITATIONS
      1.) So far system is able to tolerate 5 clients with 1000 operations each with 5 replicas.
          After this point Transport Exception occurs.
      2.) Now Configure_nodes.da sets up olympus, clients and replicas and olympus doesn't has
          much meaningful work. We faced issues while calling start from run of another distAlgo
          process.
      3.) Operations on strings having quotes is not handled properly and will trim all quotes.
      4.) Fault injection is not working in all the cases.
      

### CONTRIBUTIONS:
    Mridul Ranjan - Worked mostly on Utils and Replicas.
                  - Fault Triggers and Failures was done collectively.
                  - Result proofs validation at client.
                  - Supporting all dictionary operations.

    Rohit Kumar   - Worked on configuration of nodes with hashing.
                  - Worked on setting up messaging between clients and replicas
                  - Worked on timeouts, generating keys and fixing bugs.

### MAIN FILES:
                  configuration_nodes -> /configure_nodes/configure_nodes.da
                  client -> src/client/client.da
                  olympus -> src/olympus/olympus.da
                  replica -> src/replicas/replica.da
                  utils -> /src/utils/command_executor.py
                           /src/utils/logger.py
                          /src/utils/config_parser.py

### CODE SIZE
        

### LANGUAGE FEATURE USAGE
                  list comprehensions ---> 
                  dictionary comprehensions ---> 
                  set comprehensions  ---> 3
                  aggregations ---> 0
                  quantifications ---> 0




