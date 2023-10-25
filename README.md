# IoT Sensor Data Kafka Producer

This Python script simulates the production of IoT sensor data events and sends them to a Kafka topic. It generates mock sensor data such as temperature, timestamp, and location, and produces this data to the `iot_sensor_data` topic.

## Prerequisites

- Python 3.x
- `confluent_kafka` Python library:
  ```
  pip install confluent-kafka
  ```

## How to Use

1. Ensure you have the necessary SSL certificates at the specified locations on your machine:

2. If you have your SSL certificates at different locations, update the paths in the script.

3. Run the script:

## Mock IoT Data

The script produces mock IoT data with the following structure:

- **id**: A unique identifier for the event.
- **timestamp**: Current timestamp in ISO 8601 format.
- **temperature**: A randomly generated temperature value between 20°C and 30°C.
- **location**: A randomly chosen location from ["Living Room", "Bedroom", "Kitchen", "Garage"].

The message is produced with the event's `id` as the key and the entire event data as the value.

---

Make sure you adjust the placeholders like `<script_name>` with the appropriate names before publishing.# Aiven-kafka-message-producer-Py
