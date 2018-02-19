"""
This is the Backend entry point. Its role is to:

    * start the DataReceiver() to receive and store in Database the HTTP POST messages from SigFox callback.
"""
from data_receiver.data_receiver import DataReceiver

#sigfox IP -  185.110.97.11


if __name__ == '__main__':

    # Start DataReceiver
    receiver = DataReceiver()
    receiver.run()
