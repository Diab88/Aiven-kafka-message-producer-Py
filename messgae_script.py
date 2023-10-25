import json
from confluent_kafka import SerializingProducer
import uuid
from datetime import datetime
import random

hostname = "Place the Hostnmae here "
port = "Place the port here "

# Function to serialize the data into a JSON string
def json_serializer(msg, s_obj):
    return json.dumps(msg).encode('ascii')

conf = {
    'bootstrap.servers': hostname + ":" + port,
    'client.id': 'myclient',
    'security.protocol': 'SSL',
    'ssl.ca.location': '/ca.pem',
    'ssl.certificate.location': '/service.cert',
    'ssl.key.location': '/service.key',
    'value.serializer': json_serializer,
    'key.serializer': json_serializer
}

producer = SerializingProducer(conf)

# Function to produce mock IoT sensor data
def produce_mock_iot_event():
    # Generating a random UUID for the key
    event_id = str(uuid.uuid4())
    
    # Generating a random temperature between 20 and 30
    temperature = random.uniform(20, 30)
    
    # Getting the current timestamp in ISO 8601 format
    timestamp = datetime.now().isoformat()

    # Randomly choose a location for the sensor
    locations = ["Living Room", "Bedroom", "Kitchen", "Garage"]
    location = random.choice(locations)

    # Creating the key and value for the Kafka message
    key = {
        "id": event_id
    }
    value = {
        "id": event_id,
        "timestamp": timestamp,
        "temperature": round(temperature, 2),
        "location": location
    }

    # Producing the message to the `iot_sensor_data` topic
    producer.produce(
        "iot_sensor_data",
        key=key,
        value=value
    )
    producer.flush()

# Produce a mock IoT event
produce_mock_iot_event()
