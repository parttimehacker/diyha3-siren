## Project name: 

diyha-siren

## Description: 
Raspberry Pi project that implements a loud pulsing siren and flashing red LED as part of a larger "do it yourself home automation" system.  The systemd service is written in Pyhton3. The siren and LED are powered by a 12 volt battery.

## Table of Contents: 
Optionally, include a table of contents in order to allow other people to quickly navigate especially long or detailed READMEs.

## Installation: 
Installation is a two step process. First import two pip3 libraries. MQTT is used to subscribe and publish "do it yourself home automation" topics. The second step is to create a systemd service so the application starts when rebooted or via user commands.

step 1 - installation
```chmod +x *.sh
./installation-script.sh
```
step2 - create the systemd service
```
./systemd-script.sh diyha-siren
```
## Usage: 
The next section is usage, in which you instruct other people on how to use your project after they’ve installed it. This would also be a good place to include screenshots of your project in action.

## Contributing: 
Larger projects often have sections on contributing to their project, in which contribution instructions are outlined. Sometimes, this is a separate file. If you have specific contribution preferences, explain them so that other developers know how to best contribute to your work. To learn more about how to help others contribute, check out the guide for setting guidelines for repository contributors.

## Credits: 
Include a section for credits in order to highlight and link to the authors of your project.

## License: 
MIT
