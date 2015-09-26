"""To open the bus json file n play around with it"""
import json
import sys
from sys import argv
import urllib2

key=sys.argv[1]
busline=sys.argv[2]
url="http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?\
key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" %(key,busline)
request=urllib2.urlopen(url)
data=json.loads(request.read())
dat = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]\
      ["VehicleActivity"]
busnum =len(dat)

print "\nBus Line : {0}\n" .format(busline)
print "Number of Active Buses : {}\n".format(busnum)
buses = xrange (0, busnum)
for bus in buses:
    if bus/10==0:
        print "Bus  {0} is at latitude {1} and longitude {2}"\
    .format(bus, dat[bus]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"],\
      dat[bus]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"])
    else:
        print "Bus {0} is at latitude {1} and longitude {2}"\
    .format(bus, dat[bus]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"],\
      dat[bus]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"])
