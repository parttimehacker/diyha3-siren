#/usr/bin/bash
#
# create aliases
echo "setting up systemctl for $1"
sudo mkdir /usr/local/$1
sudo cp $1.py /usr/local/$1
sudo cp ./logging.ini /usr/local/$1
sudo cp ./pkg_classes /usr/local/$1
sudo cp $1.service /lib/systemd/system/$1.service
sudo chmod 644 /lib/systemd/system/$1.service
sudo systemctl daemon-reload
sudo systemctl enable $1.service
echo "setting up aliases for $1"
echo "alias $1.start='sudo systemctl start $1'" >> $HOME/.bash_aliases
echo "alias $1.stop='sudo systemctl stop $1'" >> $HOME/.bash_aliases
echo "alias $1.status='sudo systemctl -l status $1'" >> $HOME/.bash_aliases
echo "alias $1.restart='sudo systemctl restart $1'" >> $HOME/.bash_aliases
