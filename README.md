# Raspberry Pi IoT Monitoring System

**AWS IoT Core | MQTT | AWS Lambda | Python | Discord**

## Project Overview

This project explores an IoT-based monitoring and alert system using MQTT communication and AWS cloud services.

The goal is to collect sensor data, evaluate predefined thresholds, and generate automated notifications when abnormal conditions are detected.

This repository documents both completed AWS IoT experiments and the ongoing Raspberry Pi integration project.

## System Architecture

```text
Sensor Data / MQTT Test Client
              |
              v
        AWS IoT Core
              |
              v
     TemperatureAlertRule
       (Temperature > 30°C)
              |
        +-----+-----+
        |           |
        v           v
  MQTT Republish  AWS Lambda
        |           |
        v           v
  Alert Topic    Discord Webhook
                    |
                    v
              Discord Alert
```

## Technologies Used

- **Raspberry Pi:** Planned hardware platform for sensor integration
- **Python:** Application and Lambda programming
- **MQTT:** Publish/Subscribe messaging protocol
- **AWS IoT Core:** Cloud-based MQTT message broker
- **AWS IoT Rules:** Threshold-based message processing
- **AWS Lambda:** Serverless alert processing
- **Discord Webhook:** Automated notifications
- **TinyDB:** Local data storage component of the ongoing team project
- **Qwen SLM:** Language model component under development in the team project

## Completed AWS IoT Demonstration

The initial cloud-based monitoring demonstration was successfully tested without a physical Raspberry Pi.

1. Published simulated temperature data using the AWS IoT Core MQTT Test Client.
2. Subscribed to MQTT topics to verify message delivery.
3. Created an AWS IoT Rule with a temperature threshold of 30°C.
4. Configured a separate MQTT topic for warning messages.
5. Connected AWS IoT Core to AWS Lambda.
6. Used a Discord Webhook to deliver automated temperature alerts.
7. Verified that a temperature reading of 35°C triggered a Discord notification.

## MQTT Configuration

| Parameter | Value |
|---|---|
| AWS Region | us-east-2 (Ohio) |
| Input topic | `raspi/temperature` |
| Alert topic | `raspi/alerts/temperature` |
| Rule | `TemperatureAlertRule` |
| Lambda function | `IoTDiscordAlert` |
| Temperature threshold | Above 30°C |

## Example Input

```json
{
  "device": "raspberry-pi",
  "sensor": "temperature",
  "value": 35,
  "unit": "C"
}
```

## Expected Discord Notification

```text
AWS IoT TEMPERATURE ALERT

Device: raspberry-pi
Temperature: 35°C
Threshold: 30°C
Status: WARNING
```

## Repository Structure

```text
Raspberrypi-IoT/
├── README.md
└── aws-iot-discord-demo/
    ├── lambda_function.py
    ├── iot_rule.sql
    └── sample_temperature.json
```

## Reproducing the AWS Demonstration

1. Create an AWS IoT Core Rule using `iot_rule.sql`.
2. Configure the rule to republish to `raspi/alerts/temperature`.
3. Create an AWS Lambda function using `lambda_function.py`.
4. Configure the `DISCORD_WEBHOOK_URL` environment variable in Lambda.
5. Grant AWS IoT Core permission to invoke the Lambda function.
6. Add the Lambda action to the IoT Rule.
7. Subscribe to the alert topic in the MQTT Test Client.
8. Publish `sample_temperature.json` to `raspi/temperature`.
9. Verify that a Discord alert is received.

AWS service configuration, IAM permissions, and a valid Discord Webhook are required. Cloud resources may incur charges.

## Current Project Status

**Completed:**
- MQTT Publish/Subscribe testing
- AWS IoT Rule threshold filtering
- MQTT alert topic republishing
- AWS Lambda integration
- Discord notification testing

**Ongoing / Planned:**
- Physical Raspberry Pi sensor integration
- Camera, temperature, and distance sensor data collection
- Local data storage using TinyDB
- Qwen SLM integration
- End-to-end hardware and cloud testing

## Security

Webhook URLs, credentials, private keys, and AWS authentication information are not included in this repository.

## Project Context

University-level Computer Systems Lab and independent AWS IoT learning exercises.

This repository documents hands-on learning, system integration, and ongoing development.
