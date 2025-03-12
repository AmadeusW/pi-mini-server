# Setup
Install prerequisites
`pip install flask`
`sudo python3 shutdown_server.py`
Update `pi-mini-server.service` with actual location to the script
`cp pi-mini-server.service /etc/systemd/system/pi-mini-server.service`
`sudo systemctl enable pi-mini-server`