"""To download the mta .json file, extract data and output it to a .csv file"""
import json
import sys
from sys import argv
import urllib2
import csv

key=sys.argv[1]
busline=sys.argv[2]

url="http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?\
key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s" %(key,busline)
request=urllib2.urlopen(url)
data=json.loads(request.read())
dat = data["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]\
      ["VehicleActivity"]
busnum =len(dat)
buses = xrange (0,busnum)

with open(sys.argv[3], 'wb') as csvFile:
    writer = csv.writer(csvFile)
    header = ['Latitude', 'Longitude','Stop Name', 'Stop Status']
    writer.writerow(header)
    for bus in buses:
        lat=dat[bus]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
        lon=dat[bus]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
        on=dat[bus]["MonitoredVehicleJourney"]["OnwardCalls"]
        if on!={}:
            stopnm=on["OnwardCall"][0]["StopPointName"]
            stopstats=on["OnwardCall"][0]["Extensions"]["Distances"]["PresentableDistance"]
        else:
            stopnm="N/A"
            stopstats="N/A"
        writer.writerow([lat,lon,stopnm,stopstats])
