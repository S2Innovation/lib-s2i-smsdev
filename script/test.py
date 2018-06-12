#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Testing script."""

# Imports
import sys, os
sys.path.insert(0, os.getcwd())
from smsmodem import SmsSender


# Script
sender = SmsSender("130.235.94.141")
sender.send_sms("+33781242662", u"Café à la crème!")
