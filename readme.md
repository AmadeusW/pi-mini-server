# pi-mini-server
Simple server to execute custom commands on the host device.

## Motivation
My use case is to take an action on a Rasberry Pi from a [Home Assistant](https://www.home-assistant.io/) automation, e.g. shutting it down.

Based on forum search, the most popular solution is to use `shell_command` integration to `ssh` from Home Assistant into the Raspberry Pi and run a shell command. I decided against this due to:
- Poor maintenance: The command is defined in Home Assistant as a invocation of ssh, with target command as one of its parameters.
- Low security: Home Assistant host is allowed full remote access to the machine.

**pi-mini-server** is a minimal [Flask](https://flask.palletsprojects.com/en/stable/) server.
- Server executes commands on GET request.
- The commands are defined in Python and can run arbitrary commands using the [`subprocess`](https://docs.python.org/3/library/subprocess.html) API.
- Request may return a response that'd be used further in the automation
- Home Assistant makes request with either `rest_api` or `shell_command` with `curl`

## Device Setup
Install prerequisites
```
sudo apt install python3-flask
```
Update `/full/path/to/` in `pi-mini-server.service` with actual location to the script, and register it to launch on boot
```
sudo cp pi-mini-server.service /etc/systemd/system/pi-mini-server.service
sudo systemctl enable pi-mini-server
```

For development, start the server directly (sudo to support shutting down the device)
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
Note:
- No trailing slash at the end of the URL.
- Update to your IP/hostname and route
- You should be able to use the hostname, however, Home Assistant has a bug that fails the hostname resolution with "Clent error occured when calling resource"

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
