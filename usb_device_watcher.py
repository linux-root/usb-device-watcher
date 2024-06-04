#!/usr/bin/env python
import pyudev

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by(subsystem="usb")


def device_disconnected_handle(device):
    # this is USB DOngle
    # call http
    print(device)


for device in iter(monitor.poll, None):
    if device.action == "remove":
        device_disconnected_handle(device)
        print(
            f"USB device removed. Vendor: {device.attributes.get('idVendor')}, Product: {device.attributes.get('idProduct')}"
        )
