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
       "None" : serial.PARITY_NONE,
       "Even" : serial.PARITY_EVEN,
       "Odd"  : serial.PARITY_ODD
    }
    if str(getenv('PARITY')) not in parity_dict:
        raise Exception("Invalid parity")
    try:
        #  open the serial port and get the serial port object
        ser = serial.Serial(str(getenv('PORT')) ,int(getenv('BAUD_RATE')), timeout=1,
        bytesize=int(getenv('DATA_BITS')),parity=parity_dict.get(str(getenv('PARITY'))),
        stopbits=float(getenv('STOP_BITS')))

        while True:
            #  read json payload
            ser.reset_input_buffer()
            data = ser.readline().decode("ISO-8859-1")
            dict_json = json.loads(data)
            log.debug(dict_json)
            send_error=send_data(dict_json)
            if send_error:
                log.error(send_error)
            else:
                log.debug("Data sent successfully.")
    except json.JSONDecodeError as err:
        log.error(f"Exception in the module business logic : {err}")
