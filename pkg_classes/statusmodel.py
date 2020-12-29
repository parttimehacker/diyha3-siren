#!/usr/bin/python3
""" DIYHA MQTT CPU and OS monitor """

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
import subprocess
from threading import Thread
from time import sleep

import psutil
from gpiozero import CPUTemperature

class StatusModel:
    """ Collect CPU and OS metrics. Publish and log the information every 15 minutes. """

    def __init__(self, client):
        ''' Setup MQTT topics and initialize data elements '''
        self.client = client
        logging.config.fileConfig(fname="/usr/local/diyha_siren/logging.ini",
                                  disable_existing_loggers=False)
        # Get the logger specified in the file
        self.logger = logging.getLogger(__name__)
        self.logger.info("Status Model started")
        self.host = socket.gethostname()
        self.cpu_topic = "diy/" + self.host + "/cpu"
        self.celsius_topic = "diy/" + self.host + "/cpucelsius"
        self.disk_topic = "diy/" + self.host + "/disk"
        self.os_version_topic = "diy/" + self.host + "/os"
        self.pi_version_topic = "diy/" + self.host + "/pi"
        self.cpu_accumulator = 0.0
        self.celsius_accumulator = 0.0
        self.disk_free_accumulator = 0.0
        self.iterations = 0.0


    def collect_data(self, ):
        ''' collect one sample of data '''
        self.cpu_accumulator += psutil.cpu_percent( interval=1 )
        cpu = CPUTemperature()
        self.celsius_accumulator += cpu.temperature
        disk = psutil.disk_usage( '/' )
        # Divide from Bytes -> KB -> MB -> GB
        self.disk_free_accumulator += round( disk.free / 1024.0 / 1024.0 / 1024.0, 1 )
        self.iterations += 1.0


    def publish_averages(self, ):
        ''' publish cpu temperature and free disk to MQTT '''
        if self.iterations > 0:
            cpu = self.cpu_accumulator / self.iterations
            celsius = self.celsius_accumulator / self.iterations
            free = self.disk_free_accumulator / self.iterations
            info = "{0:.1f}".format( cpu )
            self.client.publish( self.cpu_topic, str( info ), 0, True )
            self.logger.info("CPU: " + str( info ))
            info = "{0:.1f}".format( celsius )
            self.client.publish( self.celsius_topic, str( info ), 0, True )
            self.logger.info( "Celsius: " + str( info ) )
            info = "{0:.1f}".format( free )
            self.client.publish( self.disk_topic, str( info ), 0, True )
            self.logger.info( "Disk: " + str( info ) )
            self.cpu_accumulator = 0.0
            self.celsius_accumulator = 0.0
            self.disk_free_accumulator = 0.0
            self.iterations = 0.0


    def publish_os_version(self, ):
        ''' get the current os version and make available to observers '''
        cmd = subprocess.Popen( 'cat /etc/os-release', shell=True, stdout=subprocess.PIPE )
        for line in cmd.stdout:
            if b'=' in line:
                key, value = line.split( b'=' )
                if b'VERSION' == key:
                    data, chaff = value.split( b'\n' )
                    strData = str( data, 'utf-8' )
                    osVersion = strData.replace( '"', '' )
                    self.client.publish( self.os_version_topic, osVersion, 0, True )
                    self.logger.info(osVersion)


    def publish_pi_version(self,):
        ''' get the current pi version and make available to observers '''
        cmd = subprocess.Popen( 'cat /proc/device-tree/model', shell=True, stdout=subprocess.PIPE )
        for line in cmd.stdout:
            key, value = line.split( b' Pi ' )
            data, chaff = value.split( b'\x00' )
            piVersion = str( data, 'utf-8' ) + "Raspberry Pi "
            self.client.publish( self.pi_version_topic, piVersion, 0, True )
            self.logger.info(piVersion)


    def start(self):
        """ Start the monitoring thread """
        self.publish_os_version()
        self.publish_pi_version()
        self.inactive = False
        led_thread = Thread(target=self.collect_metrics, args=())
        led_thread.daemon = True
        led_thread.start()


    def collect_metrics(self):
        """ sleep and then collect data, averaging every 15 minutes """
        while True:
            if self.inactive:
                return
            sleep(60)
            self.collect_data()
            if self.iterations >= 15.0:
                self.publish_averages()


    def stop(self,):
        """ Turn power off to the GPIO pin. """
        self.inactive = True
