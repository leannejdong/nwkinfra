! Disable DNS lookup:
no ip domain-lookup

! Configure the device name (replace "SwitchName" with the desired name):
hostname SwitchName

! Assign "cisco" as the console and vty passwords and enable login:
line console 0
password cisco
login
exit
line vty 0 15
password cisco
login
exit

! Assign "class" as the encrypted privileged EXEC mode password:
enable secret class

! Configure logging synchronous for the console:
line console 0
logging synchronous
exit

! Shut down all switch ports (replace "x/y" with the actual interface numbers):
interface range FastEthernet 0/1 - 24
shutdown
exit
interface range GigabitEthernet 0/1 - 2
shutdown
exit

! Copy the running configuration to the startup configuration:
copy running-config startup-config
