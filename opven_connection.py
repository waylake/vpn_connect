import glob

path = './etc/openvpn/ovpn_tcp/'

vpn_list = glob.glob(path + '*.ovpn')
print(vpn_list)
