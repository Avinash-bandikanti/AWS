from pyats import aetest                                    #needed for aetest script
from pyats.topology import loader
#import logging
#from genie.testbed import load
#from genie.utils.config import Config

testbed = loader.load('yaml/mytestbed.yaml') #load a device using testbed file

class common_setup(aetest.Testcase):

    @aetest.setup
    def setup_section(self):
        device = testbed.devices['Cat8000V']
        device.connect()                     #connect to the device
        device.execute('show vlan\nshow mac address-table\nshow spanning-tree\nshow processes cpu\nshow processes memory')

class Test_Section(aetest.Testcase):

    @aetest.test
    def change_hostname_and_display(self):
        device = testbed.devices['Cat8000V']  # Replace 'device_name' with the actual device name in your testbed
        new_hostname = 'Sainadh'
        device.configure('hostname ' + new_hostname)
        device.execute('show running-config | include hostname')

class common_cleanup(aetest.Testcase):

    @aetest.cleanup
    def cleanup_section(self):
        device = testbed.devices['Cat8000V']
        device.configure("hostname Cat8000V")
        device.disconnect()  # Replace 'device_name' with the actual device name

if __name__ == '__main__':
    aetest.main()
