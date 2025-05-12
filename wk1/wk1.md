# Network infrastruture cluster

CCNA theory and practical

## W1

1. networking concepts

2. cli command

 !!Disable DNS lookup
no ip domain-lookup

!!Configure device name as shown in the topology

hostname S1

!!Assign cisco as the console and vty passwords.
!!Configure logging synchronous for the console line.
line con 0
logging synchronous
password cisco
login
exit
!!Configure a message of the day (MOTD) banner to warn users that unauthorized access is prohibited.
banner motd #Unauthorized access is prohibited!#

!!Configure the IP address listed in the Addressing Table for all interfaces.
int s0/0/0
ip address
no shut

!!Set the clock rate for all DCE serial interfaces at 128000.
clock rat 128000
!!Copy the running configuration to the startup configuration.
copy running-config startup-config


!1Check
sh ip int br
sh running-config
 

