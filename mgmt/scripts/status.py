#!/usr/bin/env python
from gpiozero import PingServer, StatusZero
from gpiozero.tools import negated
from signal import pause

sz = StatusZero('router', 'google', 'NAS')

statuses = {
    sz.router: PingServer('192.168.178.1'),
    sz.google: PingServer('8.8.8.8'),
    sz.NAS: PingServer('192.168.178.64'),
}

for strip, server in statuses.items():
    strip.green.source = server.values
    strip.green.source_delay = 60
    strip.red.source = negated(strip.green.values)

pause()
