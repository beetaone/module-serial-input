"""
This file implements module's main logic.
Data inputting should happen here.

Edit this file to implement your module.
"""

from logging import getLogger
from api.send_data import send_data
from os import getenv
import serial
import json
log = getLogger("module")


def module_main():
    """
    Implements module's main logic for inputting data.
    Function description should not be modified.
    """

    log.debug("Inputting data...")

    parity_dict = {
        "None": serial.PARITY_NONE,
        "Even": serial.PARITY_EVEN,
        "Odd": serial.PARITY_ODD
    }

    if str(getenv('PARITY')) not in parity_dict:
        raise Exception("Invalid parity")

    #  open the serial port and get the serial port object
    ser = serial.Serial()
    ser.port = str(getenv('PORT'))
    ser.baudrate = int(getenv('BAUD_RATE'))
    ser.timeout = 1
    ser.bytesize = int(getenv('DATA_BITS'))
    ser.parity = parity_dict.get(str(getenv('PARITY')))
    ser.stopbits = float(getenv('STOP_BITS'))

    ser.open()
    log.debug("Opened a serial port at " + str(getenv('PORT')))

    ser.reset_input_buffer()
    log.debug("Input buffer reset")

    while True:
        data = ser.readline()
        log.debug("Got line: " + str(data))

        try:
            dict_json = json.loads(data)
            log.debug("JSON: %s", dict_json)
        except json.JSONDecodeError:
            log.error("could not decode the following line" + str(data))
            continue

        send_error = send_data(dict_json)
        if send_error:
            log.error(send_error)
        else:
            log.debug("Data sent successfully.")
