#!/usr/bin/python

# Imports!

# Needed for sleep
import time

# Needed for nmap/shell commands
import nmap

#############################################################################
# Define functions here

## This is the start menu function, prints the original selections 
def startmenu():
    print "Please select from the following list: "
    print "1) General Security Audit"
    print "2) Generate Security Report"
    print "3) Attack specific vector"

    selection = raw_input("Selection:")

    return selection

## This is the function for the "General Security Audit" 
def gsa(ipaddr):
    print "Loading audit module, please wait."
    time.sleep(2)
    print "Running scan to identify external attack vectors"


## Nmap Function
def nmapd(ipaddr):
   nm = nmap.PortScanner()
   host = ipaddr
   nm.scan(host)
   print ('------------------------')
   print ('Host: %s' % host)
   print ('State: %s' % nm[host].state())

   for proto in nm[host].all_protocols():
        print('-----------')
        print ('Protocol: %s' % proto)

        lport = nm[host][proto].keys()
        lport.sort()
        for port in lport:
            print ('port:  %s\tstate : Open' % (port ))




############################################################################


selection = startmenu()

print "Please enter the external ip for the client"
ipaddr = raw_input("Address: ")


if selection == "1" :

    nmapd(ipaddr)

else :
    print blah

