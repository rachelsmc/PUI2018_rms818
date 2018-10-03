from __future__ import print_function
import sys
import os
import json

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

if not len(sys.argv) == 4:
    print ("Invalid number of arguments. Run as: python get_bus_info_<NETID>.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv")
    sys.exit()
    
MTA_KEY = sys.argv[1]
BUS_LINE = sys.argv[2]
FILE_NAME = sys.argv[3]

url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+MTA_KEY+"&VehicleMonitoringDetailLevel=calls&LineRef="+BUS_LINE

response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

busactivity = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

stoppointname = ""
stopstatus = ""

fout = open(FILE_NAME, "w")

fout.write("Latitude,Longitude,Stop Name,Stop Status\n")

for i in range(len(busactivity)):
    lat = str(busactivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])
    long = str(busactivity[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
    
    if bool(busactivity[i]['MonitoredVehicleJourney']['OnwardCalls']):
        stoppointname = busactivity[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        stopstatus = busactivity[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
        
        fout.write(lat+","+long+","+stoppointname+","+stopstatus+"\n")
        
    else:
        fout.write(lat+","+long+","+"N/A, N/A\n")