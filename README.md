## Project name: 

diyha-siren

## Description: 
This is a Raspberry Pi project that implements a loud pulsing siren and flashing red LED as part of a larger "do it yourself home automation" system.  The application is written in Pyhton3. The siren and LED are powered by a 12 volt battery. I usually create a systemd service so the application runs at boot.

## Installation: 
Installation is a two step process. Make the bash scripts executabel and then import two pip3 libraries. MQTT is used to subscribe and publish "do it yourself home automation" topics. 

Step 1 - make the install bash scripts executable
```
chmod +x *.sh
```

Step 2 - installation of MQTT and RPI.GPIO libraries
```chmod +x *.sh
./installation-script.sh
```
Step2 - create the diyha-siren systemd service (it uses an argument to create the service
```
./systemd-script.sh diyha-siren
```
## Usage: 
I recommend making a raspbian systemd service so the application starts when rebooted or via user commands. The systemd-script.sh creates a diyha-siren directory in /usr/local directory. The application files are then copied to this new directory. The application will also create a log file in /var/log called diyha-siren.log

Create the diyha-siren systemd service (the script uses a file name argument to create the service)
```
./systemd-script.sh diyha-siren
```

## Contributing: 
Larger projects often have sections on contributing to their project, in which contribution instructions are outlined. Sometimes, this is a separate file. If you have specific contribution preferences, explain them so that other developers know how to best contribute to your work. To learn more about how to help others contribute, check out the guide for setting guidelines for repository contributors.

## Credits: 
Include a section for credits in order to highlight and link to the authors of your project.

## License: 
MIT
