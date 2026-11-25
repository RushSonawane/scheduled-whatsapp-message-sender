
# STEP 1: Import required libraries
from twilio.rest import Client
from datetime import datetime
import time
import os


# Store credentials as environment variables.
# STEP 2: Twilio credentials

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

if not account_sid or not auth_token:
    raise ValueError("Twilio credentials are missing!")

client = Client(account_sid, auth_token)

# STEP 3: WhatsApp sender number
# Use your Twilio-approved WhatsApp sender.
TWILIO_WHATSAPP_NUMBER = "whatsapp:+91 8766463117"


# STEP 4: Design send message function
def send_whatsapp_message(recipient, message_body):

    try:
        message = client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            body=message_body,
            to=f"whatsapp:{recipient}"
        )

        print("Message sent successfully!")
        print(f"Message SID: {message.sid}")

    except Exception as e:
        print("An error occurred:", e)


# STEP 5: User input
name = input("Enter recipient name: ")

recipient_number = input(
    "Enter recipient WhatsApp number with country code: "
)

message_body = input(
    f"Enter message you want to send to {name}: "
)


# STEP 6: Parse date and time
date_str = input(
    "Enter date (YYYY-MM-DD): "
)

time_str = input(
    "Enter time (HH:MM, 24-hour format): "
)

try:
    scheduled_datetime = datetime.strptime(
        f"{date_str} {time_str}",
        "%Y-%m-%d %H:%M"
    )

except ValueError:
    print("Invalid date or time format.")
    raise SystemExit


# STEP 7: Calculate delay
current_datetime = datetime.now()

time_difference = scheduled_datetime - current_datetime

delay_seconds = time_difference.total_seconds()


# STEP 8: Validate scheduled time
if delay_seconds <= 0:

    print("The specified time is in the past!")
    print("Please schedule a future time.")

else:

    print(
        f"Message scheduled for {name} "
        f"at {scheduled_datetime}"
    )

    print("Waiting for scheduled time...")

    # STEP 9: Wait until scheduled time
    time.sleep(delay_seconds)

    # STEP 10: Send WhatsApp message
    send_whatsapp_message(
        recipient_number,
        message_body
    )
