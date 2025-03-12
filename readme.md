# pi-mini-server
Simple way to execute custom commands on your device.
The use case is to take actioin on a rasberry pi from home assistant.

Popular solution is to use `shell_command` integration to `ssh` into the machine and run a shell command. This is generally unsafe and hard to maintain because
- Home assistant is allowed full access to the machine
- The command is controlled by Home Assistant

**pi-mini-server** allows `shell_command` to `curl` into the server, or use `rest_api` to connect.
Either 
- Home assistant is not allowed full access to the machine
- The command is controlled by the server

### Setup
Install prerequisites
```
sudo apt install python3-flask
```
Update `pi-mini-server.service` with actual location to the script, and create service to launch the server on boot
```
sudo cp pi-mini-server.service /etc/systemd/system/pi-mini-server.service
sudo systemctl enable pi-mini-server
```

Or, start the server directly
```
sudo python3 server.py
```