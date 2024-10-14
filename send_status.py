import psutil
import requests
import time
import socket

# PythonAnywhere URL where data will be sent
url = 'https://byteunit420.pythonanywhere.com/send-status'  # Replace <your-username> with your actual PythonAnywhere username

def get_system_status():
    """Collect system status metrics, including device name."""
    device_name = socket.gethostname()  # Get the device name
    status = {
        'device_name': device_name,  # Add device name to the status
        'cpu_percent': psutil.cpu_percent(interval=1),
        'memory_percent': psutil.virtual_memory().percent,
        'disk_percent': psutil.disk_usage('/').percent,
        'battery_percent': psutil.sensors_battery().percent if psutil.sensors_battery() else 'No battery',
        'battery_plugged': psutil.sensors_battery().power_plugged if psutil.sensors_battery() else False
    }
    return status

while True:
    # Collect system data
    system_status = get_system_status()
    
    # Send data to the server
    try:
        response = requests.post(url, json=system_status)
        print(f"Sent data: {system_status}, Response: {response.status_code}")
    except Exception as e:
        print(f"Failed to send data: {e}")
    
    # Wait for 60 seconds before sending again
    time.sleep(60)
