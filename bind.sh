#!/bin/bash

# For bind to HC-05
# Just a reminder for myself in case I change BT module
# Here is how to discover MAC Address:
# bluetoothctl
# power on
# scan on

/usr/bin/rfcomm bind 0 98:D3:31:F5:79:86 1
