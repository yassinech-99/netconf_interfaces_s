# netconf_interfaces_s
a script to query an IOS XE Router All Interfaces, Set or Get Interface via XML config files

```bash

usage: Fetch Display and Configure InterFaces [-h] -d DEVICE -u USERNAME -p PASSWORD [-i INTERFACE] [-I INTERFACES] [-s SET] 

optional arguments:
  -d Device, --host HOST  enter host eg: -h sandbox-iosxe-latest-1.cisco.com
  -u USERNAME, --username USERNAME
                        enter username
  -p PASSWORD, --password PASSWORD
                        enter password
  -i INTERFACE, --interface INTERFACE
                        Displays the interface based on xml file provided eg: -i interface.xml
  -I INTERFACES, --Interfaces INTERFACES
                        Displays all the interfaces eg: -I interfaces
  -s SET, --set SET     Set Interface based on an xml config file provided eg: -s interface_config.xml
  -v, --verbose         increase verbosity
