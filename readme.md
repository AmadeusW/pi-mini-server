# pi-mini-server
Simple way to execute custom commands on your device.
The use case is to take an action on a rasberry pi from home assistant.

Popular solution is to use `shell_command` integration to `ssh` into the machine and run a shell command. This is generally unsafe and hard to maintain because
- Home assistant is allowed full access to the machine
- The command is defined and maintained by Home Assistant

**pi-mini-server** allows executing commands through either
- `shell_command` to `curl` into the server,
- `rest_api` to connect.

In both cases,
- Home assistant is not allowed full access to the machine
- The command is defined on the server

### Device Setup
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

### Home Assistant setup
Update `configuration.yaml` to add the [`rest_command`](https://www.home-assistant.io/integrations/rest_command)
e.g.
```
rest_command:
  rpi_status:
    url: "http://10.0.0.100/status"
  rpi_shutdown:
    url: "http://10.0.0.100/shutdown"
```
Note no trailing slash at the end of the URL.
You should be able to use the hostname, however, I'm using IP to workaround "Clent error occured when calling resource" that happens with hostname.

#### Home Assistant action (automation or developer tools)
```
action: rest_command.rpi_shutdown
data: {}
```

#### Home Assistant dashboard button
```
name: Shutdown Pi
icon: mdi:power-plug-off
type: button
show_name: true
show_icon: true
tap_action:
  action: perform-action
  perform_action: rest_command.rpi_shutdown
  target: {}
```
