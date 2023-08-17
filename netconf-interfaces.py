from ncclient import manager
from xml.dom.minidom import parseString
import argparse


class Device(object):
    """
    Device Class takes in (Host,Username,Password) paremeters and returns:
    handler: An ncclient Manager instance or None if it fails
    """
    devices = 0
    def __init__(self, Host,Username,Password):
        Device.devices+=1
        self.router={
            'host':Host,
            'username': Username,
            'password': Password,
            }
    def router_parms(self):
        return self.router

        
    def get_manager(self):

        try:
            handler = manager.connect(**self.router, hostkey_verify=False)
            return handler
        except Exception as e:
            print("Error:", e)
            return ""
        
    def __str__(self):
        return self.router['host']
        
        
class InterfacesInfo(Device):
    """
    InterfaceInfo class inherits the router parameters and the nccclient handler from the parrent class Device, it returns:
    interfaces : dict that contains interface informations in the router
    """
    def __init__(self, Host,Username,Password):
        super().__init__(Host,Username,Password)
        self.router = super().router_parms()

        self.filter="""
                        <filter>
                                <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
                                
                        </filter>
                        """
        
    
        

    def get_interfaces(self):
        """
        Get All Interfaces in xml format 
        """
        try:
            handler = super().get_manager()
            if handler:
                interfaces=handler.get(self.filter)
                return parseString(interfaces).toprettyxml()
            else:
                return ""
        except Exception as e:
            print("Error:", e)
            return ""

        
    def get_interface(self,interface_filter):
        """
        Get Single Interface in xml format by passing a filter
        """
        try:
            with open('interface_filter.xml','r') as  interface_filter:
                handler = super().get_manager()
                if handler:
                    interface=handler.get(interface_filter.read())
                    return parseString(interface).toprettyxml()
                else:
                    return ""
        except Exception as e:
            print("Error:", e)
            return ""   
        
    def set_interface(self,interface_configuration):
        """
        Set Interface
        """
        try:
                with open('interface_config.xml','r') as interface_configuration:
                    handler = super().get_manager()
                    if handler:
                        interface=handler.edit_config(target='running', config=interface_configuration.read())
                        return parseString(interface).toprettyxml()
                    else:
                        return ""
        except Exception as e:
            print("Error:", e)
            return "" 




if __name__ == "__main__":
    parser= argparse.ArgumentParser('Fetch Display and Configure InterFaces')
    parser.add_argument('-d','--device',help="enter host eg: -d sandbox-iosxe-latest-1.cisco.com ", required=True)
    parser.add_argument('-u','--username',help="enter username", required=True)
    parser.add_argument('-p','--password',help="enter password", required=True)
    parser.add_argument('-i', '--interface', help="Displays the interface based on xml file provided eg: -i interface.xml ",required=False)
    parser.add_argument('-I','--Interfaces',help='Displays the all the interfaces eg: -I interfaces')
    parser.add_argument('-s', '--set', help="Set Interface based on an xml config file provided eg: -s interface_config.xml", required=False)
    args= parser.parse_args()

    try:
        call = InterfacesInfo(args.device,args.username,args.password)
        
        if args.Interfaces:
            interfaces=call.get_interface()
            for interface_name, interface_data in interfaces.items():
                print(f"Interface: {interface_name}")
                print(f"Description: {interface_data['description']}")
                print(f"Address: {interface_data['address']}")
                print(f"Enabled: {interface_data['enabled']}")
                print("-" * 40)
        if args.interface:
            interface=call.get_interface()
            print(interface)
        if args.set:
            config_result=call.set_interface()
            print(config_result)        
    except Exception as e:
        print('Error', str(e))

       
        
    
    






