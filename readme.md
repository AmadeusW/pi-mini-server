# Setup
Install prerequisites
sudo apt install python3-flask
// Update `pi-mini-server.service` with actual location to the script
sudo cp pi-mini-server.service /etc/systemd/system/pi-mini-server.service
sudo systemctl enable pi-mini-server
sudo python3 server.py