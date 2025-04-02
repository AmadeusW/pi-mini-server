from flask import Flask
import subprocess
import socket

app = Flask(__name__)

@app.route('/shutdown', methods=['GET'])
def shutdown():
    # Execute the shutdown command
    subprocess.Popen(['sudo', '/sbin/shutdown', '-h', 'now'])
    return "Shutting down...", 200

@app.route('/', methods=['GET'])
@app.route('/status', methods=['GET'])
def status():
    # Simply return a 200 status
    return "OK", 200

if __name__ == '__main__':
    # Get the hostname for display purposes
    hostname = socket.gethostname()
    # Run the server on all network interfaces (0.0.0.0) 
    # so it's accessible from other devices on the LAN
    print(f"Starting server. Access via http://{hostname}/status or http://{hostname}/shutdown")
    app.run(host='0.0.0.0', port=80, debug=False)
