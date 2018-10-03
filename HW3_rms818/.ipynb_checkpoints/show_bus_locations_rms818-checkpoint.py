from __future__ import print_function
import sys
import os
import json

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 3:
    print ("Invalid number of arguments. Run as: python get_bus_info_<NETID>.py <MTA_KEY> <BUS_LINE>")
    sys.exit()

MTA_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+MTA_KEY+"&VehicleMonitoringDetailLevel=calls&LineRef="+BUS_LINE

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

busactivity = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

print("Bus Line : "+BUS_LINE)
print("Number of Active Buses : " + str(len(busactivity)))

for i in range(len(busactivity)):
    print("Bus "+str(i)+" is at lattitude "+str(busactivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])+" and longitude "+str(busactivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))