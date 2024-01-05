import paho.mqtt.client as mqtt



# Define callback functions
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker")
    else:
        print("Connection failed with code", rc)

def on_message(client, userdata, message):
    # Handle incoming MQTT messages here
    print("Received message on topic", message.topic, "with payload", message.payload)

# Clean up when the Django app exits
def on_exit(client):
    client.loop_stop()
    client.disconnect()
