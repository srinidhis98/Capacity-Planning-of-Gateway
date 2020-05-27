## Capacity-Planning-of-Gateway

#### File Description:

  - combine_data.py -- combines 2 csv files, filters the data based on User prompted value, displays a basic graph with relation between time and another entity(NAT/ Flow_count)
  - summary.py -- prepares summary for the Overall CPU util at 80/85%, removes NaN values and Unnamed(Index) columns.
  - traffic_gen.sh -- sends iperf, ping and traffic from various clients to Gateway given the IP by the User.
  - param_collect.sh -- runs on the Gateway, while the traffic is sent from various clients, collects the Velocloud Parameters, CPU info, Memory Info and Network Bandwidth
  - data_cleaning.sh -- runs on the local machine, takes out only the needed data from the files copied from the Gateway
  
