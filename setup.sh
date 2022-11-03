sudo apt install python3-dbus libbluetooth-dev
pip3 install pybluez
sudo pip3 install pybluez


sudo rm /lib/systemd/system/bluetooth.service
sudo cp ./system_files/bluetooth.service /lib/systemd/system

sudo systemctl daemon-reload
sudo systemctl restart bluetooth

sudo hciconfig hci0 piscan 
