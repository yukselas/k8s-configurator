from cidrize import cidrize



'''

	start: 192.168.66.100
	end: 192.168.66.150
	gateway: 192.168.66.254
	netmask: 255.255.255.0
	nvr1: 192.168.66.148
	nvr2: 192.168.66.149
	nvr3: 192.168.66.150


multusnet=192.168.66.148-192.168.66.150,192.168.66.0/24,192.168.66.254



'''

def genmultusnetstr(nvriprange,iprange,gateway):
    mycidr=str(cidrize(iprange)[0])
    multusnet=nvriprange+','+mycidr+','+gateway
    return multusnet


configstr=genmultusnetstr('192.168.66.148-192.168.66.150','192.168.66.100-192.168.66.150','192.168.66.254')

print('multusnet config:')
print(configstr)