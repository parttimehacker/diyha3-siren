## Project name: 

### diyha-siren

## Description: 
This is my latest Raspberry Pi project that implements both a loud, pulsing siren and multiple, flashing red LEDs as part of a larger "do it yourself home automation" system.  The application requires **Raspbian OS** and is written in **python3**. The siren and LED device are controlled by a relay and powered by a single 12 volt battery. I usually create a **systemd service** so the application runs at boot.

## Installation: 
Installation is a two step process. First make the bash scripts executable and  import two **pip3 libraries**. MQTT is used to subscribe and publish "do it yourself home automation" topics. The application uses two of the Raspberry Pi pins. The second step is to decide whether to manually or use systemd to run the application.

- Make bash scripts executable
```
chmod +x *.sh
```

- Install MQTT and RPI.GPIO libraries
```chmod +x *.sh
./installation-script.sh
```

## Usage: 
You need to decide whether you want to manually run the application or have it started as part of the boot process. I recommend making a **Raspbian OS systemd service**, so the application starts when rebooted or controled by **systemctl** commands. The **systemd-script.sh** creates a diyha-siren directory in **/usr/local directory**. The application files are then copied to this new directory. The application will also require a log file in **/var/log directory** called diyha-siren.log

The application subscribes to four MQTT topics. Two of the topics, **diy/system/fire** and **diy/system/panic**, control the siren and flashing LED. Another topic. **diy/system/who**, causes the application to publish its status to the MQTT broker. The fourth topic is **diy/system/test** and is used for developement testing.

The application uses two of the Raspberry Pi pins: **GPIO 17** for the siren and flashing LED device and **GPIO 18** for a green LED indicating that the device is running (easily changed).

- Create the diyha-siren systemd service (the script uses a file name argument to create the service)
```
./systemd-script.sh diyha-siren
```

This script also adds four aliases to the **.bash_aliases** in your home directory for convenience.
```
sudo systemctl start diyha-siren
sudo systemctl stop diyha-siren
sudo systemctl restart diyha-siren
sudo systemctl -l status diyha-siren
```

## Contributing: 

Adafruit supplies most of my hardware. http://www.adafruit.com

My "do it yourself home automation" system leverages the work from the Eclipse IOT Paho project. https://www.eclipse.org/paho/

## Credits: 
Developed by parttimehacker.

## License: 
MIT
