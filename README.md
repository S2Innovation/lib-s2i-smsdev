python-smsmodem
===============
***

Provide an interface for SMSGateway device server MOXA.

Usage
-----

```python
from smsmodem import SmsSender,

sender = SmsSender("192.168.2.1")
sender.send_sms("0123456789", "Hello world!")
```

Installation
------------

Run:

    $ python setup.py install

