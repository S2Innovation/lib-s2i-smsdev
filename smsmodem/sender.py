"""Provide an SMS sender interface."""

# Imports
import PyTango

# Send SMS function
def send_sms(numbers, message, host='192.168.127.254', extended=False, priority=2,
             port=2040, username='admin', password='admin'):
    """Send a message to the given numbers using a given host name.

    Args:
        numbers (iterator): phone number
        message (str or unicode): body of the message
        host (str): Not Implemented
        extended (bool): Not Implemented
        priority (int): Not Implemented
        port (int): Not Implemented
        username (str): Not Implemented
        password (str): Not Implemented

        The limits in characters for the different encoding are:
            - ASCII: 160 characters
        """
    sender = SmsSender(host, port, username, password)
    return sender.send_sms(numbers, message, extended, priority)


# SMS sender class
class SmsSender(object):
    """Provide methods to send SMS via a given server.

    Args:
        host (str): host name of the server
        port (int): port for tcp communcation
        username (str): user name for authentification
        password (str): password for authentification
    """

    def __init__(self, host='192.168.127.254', port=2040, username='admin', password='admin'):
        """Initialize with hostname, port and login of the server.

        Args:
            host (str): host name of the server
            port (int): port for tcp communcation
            username (str): user name for authentification
            password (str): password for authentification
        """

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

