import os
if os.name == 'nt':
    print "Disabling Wiimote; you're using windows!"
else:
    import cwiid

class Wiimote():
    def __init__(self):
        print 'Put Wiimote in discoverable mode now (press 1+2)...'
        self.w = cwiid.Wiimote()
        self.rpt_mode = 0
        self.rpt_mode ^= cwiid.RPT_ACC
        self.rpt_mode ^= cwiid.RPT_BTN
        self.w.rpt_mode = self.rpt_mode
        self.w.led = 1
        self.lastbutton = 0
