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
    def __init__(self):
        self.run()

    def connection(self):
        VPN_PROFILE = random.choice(VPN_LIST)
        os.system(f'sudo openvpn --config {VPN_PROFILE} --auth-user-pass /home/davek/.openvpn/profile')

    def exition(self):
        os.system('sudo killall openvpn')


    def run(self):
        p1 = Process(target=self.connection)
        p2 = Process(target=self.exition)

        p1.start()
        p2.start()

        p1.join()
        p2.join()


a = Vpn_connection()

while True:
    try:
        a.run()
    except:
        continue
