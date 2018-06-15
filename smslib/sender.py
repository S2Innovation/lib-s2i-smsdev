"""Provide an SMS sender interface."""

# Imports
import PyTango
from threading import Thread


# SMS sender class
class SMSThread(Thread):
    """Provide methods to send SMS via a given server."""



    def __init__(self, message='', dest='',  username='', password='', source=''):
        """Initialize with hostname, port and login of the server."""
        Thread.__init__(self)
        self.message = message
        self.destinations = dest

    def run(self):
        # just iterate over list of recipients
        for number in self.destinations:
            send_sms(number, self.message)

    def send_sms(self, numbers, message, extended=True, priority=2):
        """Send a given text message to the given numbers.

        Args:
            numbers (iterator): phone number as strings
            message (str or unicode): body of the message
            extended (bool): Not Implemented
            priority (int): Not Implemented

        SendSMS using SMSGateway class device serwer
        """

        db = PyTango.Database()

        class_name = 'SMSGateway'
        try:
            devs = ['/'.join((class_name, name)) for name in db.get_instance_name_list(class_name)]
            list_of_devs = [dev for dev in db.get_device_class_list(devs[0]) if
                        '/' in dev and not dev.startswith('dserver')]

            device = PyTango.DeviceProxy(list_of_devs[0])
            sms_message = ';'.join([numbers, message])
            device.d.sendSMS(sms_message)
        except Exception as e:
            print('PROBLEM to send sms {0}'.format(e))

