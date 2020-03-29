from gpiozero import PingServer, StatusZero
from gpiozero.tools import negated
from signal import pause

sz = StatusZero('router', 'google', 'NAS')

router = PingServer('192.168.178.1')
google = PingServer('8.8.8.8')
NAS = PingServer('192.168.178.64')

sz.router.green.source = router.values
sz.router.green.source_delay = 60
sz.router.red.source = negated(sz.router.green.values)

sz.google.green.source = google.values
sz.google.green.source_delay = 60
sz.google.red.source = negated(sz.google.green.values)

sz.NAS.green.source = NAS.values
sz.NAS.green.source_delay = 60
sz.NAS.red.source = negated(sz.NAS.green.values)

pause()
