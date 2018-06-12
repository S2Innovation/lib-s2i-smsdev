#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Testing script."""

# Imports
import sys, os
sys.path.insert(0, os.getcwd())
from smsmodem import SmsSender, SmsError


# Script
sender = SmsSender("130.235.94.141")
mid, load = sender.send_sms(["+33781242662"], u"Café à la crème!")
status = sender.get_status(mid)
print mid, load, status
try: print sender.get_status(0)
except SmsError as e:
    print repr(e), str(e)
