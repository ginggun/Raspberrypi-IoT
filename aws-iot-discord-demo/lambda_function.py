
import json
import os
import urllib.request


def lambda_handler(event, context):
    temperature = float(event["value"])

    if temperature <= 30:
        return {
            "statusCode": 200,
            "body": "Temperature is normal"
        }

    device = event.get("device", "raspberry-pi")

    message = {
        "content": (
            "🚨 AWS IoT TEMPERATURE ALERT\n"
            f"Device: {device}\n"
            f"Temperature: {temperature:g}°C\n"
            "Threshold: 30°C\n"
            "Status: WARNING"
        )
    }

    webhook_url = os.environ["DISCORD_WEBHOOK_URL"]

    request = urllib.request.Request(
        webhook_url,
        data=json.dumps(message).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "User-Agent": "AWS-IoT-Lab/1.0"
        },
        method="POST"
    )

    with urllib.request.urlopen(request, timeout=10) as response:
        return {
            "statusCode": response.status,
            "body": "Discord notification sent"
        }
