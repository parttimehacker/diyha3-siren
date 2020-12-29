#!/usr/bin/python3
""" DIYHA MQTT location initializer """

# The MIT License (MIT)
#
# Copyright (c) 2019 parttimehacker@gmail.com
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

import socket
import logging
import logging.config

class WhoController:
    """ Who controller handles  MQTT broker messsages for diy/system/who ON or OFF.
    """

    def __init__(self,):
        """ Create two topics for this application. """
        logging.config.fileConfig(fname='/usr/local/diyha_siren/logging.ini', disable_existing_loggers=False)
        # Get the logger specified in the file
        self.logger = logging.getLogger(__name__)
        host_name = socket.gethostname()
        self.default_who_message = host_name
        self.status_topic = "diy/system/status"
        self.waiting_for_client = True
        self.logger.info('Waiting for client initialization: '+self.default_who_message)

    def set_client(self, client):
        """ The location topic is typically returned by MQTT message methods
            at startup.
        """
        self.logger.info("Client initialized")
        self.client = client
        self.waiting_for_client = False
        self.logger.info("Class ready")

    def set_message(self, message):
        """ Typically used by MQTT subscribe methods. """
        self.default_who_message = message
        self.logger.info("Default message changed")

    def turn_on(self,):
        """  Response to MQTT diy/system/who message. """
        self.logger.info("Received diy/system/who ON, publish> "+self.default_who_message)
        if not self.waiting_for_client:
            self.client.publish(self.status_topic, self.default_who_message, 0, True)
        else:
            self.logger.error("Client not initialized")

    def turn_off(self,):
        """  Response to MQTT diy/system/who message. """
        self.logger.info("Received diy/system/who OFF")