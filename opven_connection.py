import os
import sys
import signal
import random
import glob
import time
from multiprocessing import Process



PATH = '/etc/openvpn/ovpn_tcp/'
VPN_LIST = glob.glob(PATH + 'us*')

class Vpn_connection:
    def __init__(self, exit_time):
        self.VPN_PROFILE = random.choice(VPN_LIST)
        self._time = exit_time 
        self.run()

    def connection(self):
        os.system(f'sudo openvpn --config {self.VPN_PROFILE} --auth-user-pass /home/davek/.openvpn/profile')

    def exition(self):
        time.sleep(self._time)
        os.system('sudo killall openvpn')

    def run(self):
        p1 = Process(target=self.connection)
        p2 = Process(target=self.exition)

        p1.start()
        p2.start()

        p1.join()
        p2.join()


vpn_h = Vpn_connection(exit_time=10)
last_profile = vpn_h.VPN_PROFILE
_ , filename = os.path.split(last_profile)
print(len(VPN_LIST))
