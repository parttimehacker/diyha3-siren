#!/usr/bin/python3
""" DIYHA Application Configuration Initializer """

# The MIT License (MIT)
#
# Copyright (c) 2019,2020, 2021 parttimehacker@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import argparse
import logging
import logging.config

class ConfigModel:
    """ Command line arguement model which expects an MQTT broker hostname or IP address,
        the location topic for the device and an option mode for the switch.
    """

    def __init__(self,):
        """ Parse the command line arguements """
        logging.config.fileConfig(fname='/usr/local/siren/logging.ini',
                                  disable_existing_loggers=False)
        # Get the logger specified in the file
        self.logger = logging.getLogger(__name__)
        PARSER = argparse.ArgumentParser('siren.py parser')
        PARSER.add_argument('--mq', help='MQTT broker server IP address')
        PARSER.add_argument('--loc', help='Location topic required')
        ARGS = PARSER.parse_args()
        # command line arguement for the MQTT broker hostname or IP
        if ARGS.mq == None:
            self.logger.error("Terminating> --mq not provided")
            exit() # manadatory
        self.broker_ip = ARGS.mq
        # command line arguement for the location topic
        if ARGS.loc == None:
            self.logger.error("Terminating> --loc not provided")
            exit() # mandatory
        self.location = ARGS.loc

    def get_broker(self, ):
        """ MQTT BORKER hostname or IP address."""
        return self.broker_ip

    def get_location(self, ):
        """ MQTT location topic for the device. """
        return self.location
