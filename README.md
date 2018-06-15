panic-smslib
=============
***

Provide an interface for SMSGateway device server for MOXA. Implemeted for SOLARIS.

Usage
-----

```python
from smslib import SMSThred,

sender = SMSThread(["+48.....", ], "message")
sender.start()
```

Installation
------------

Run:

    $ python setup.py install

