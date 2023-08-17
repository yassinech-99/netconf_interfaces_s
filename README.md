# netconf_interfaces_s
a script to query an IOS XE Router All Interfaces, Set or Get Interface via XML config files

## Requirements

- Python 3.x
- The `ncclient` library

## Usage
```sh
python -i netconf-interfaces.py -d DEVICE -u USERNAME -p PASSWORD [-i INTERFACE] [-I INTERFACES] [-s SET] [-v]

-d, --device: Device hostname or IP address.
-u, --username: Device username.
-p, --password: Device password.
-i, --interface: Display details of a specific interface based on an XML file.
-I, --interfaces: Display all interfaces.
-s, --set: Set interface based on an XML config file.

