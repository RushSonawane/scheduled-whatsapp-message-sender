# scheduled-whatsapp-message-sender
Python-based WhatsApp message scheduling automation using Twilio API.
# Scheduled WhatsApp Message Sender using Python & Twilio

## 1. Project Overview

The **Scheduled WhatsApp Message Sender** is a Python-based automation project that allows users to schedule WhatsApp messages for a specific future date and time.

The application uses the Twilio WhatsApp API to send messages automatically at the scheduled time. Users can enter the recipient's name, WhatsApp number, message content, and preferred delivery date and time.

This project demonstrates Python automation, API integration, date-time handling, and environment variable management.

## 2. Project Objectives

- Automate WhatsApp message delivery.
- Schedule messages for a specific future date and time.
- Integrate Python with the Twilio WhatsApp API.
- Handle date and time validation.
- Securely manage API credentials using environment variables.

## 3. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Twilio API | WhatsApp message delivery |
| datetime | Date and time processing |
| time | Scheduling and execution delay |
| os | Environment variable management |

## 4. Project Workflow

1. Import the required Python libraries.
2. Retrieve Twilio Account SID and Auth Token from environment variables.
3. Establish a connection with the Twilio API.
4. Accept recipient details from the user.
5. Accept the WhatsApp message content.
6. Collect the scheduled date and time.
7. Validate the date and time format.
8. Calculate the waiting time.
9. Wait until the scheduled time.
10. Send the WhatsApp message through Twilio.

## 5. Key Features

- **WhatsApp Integration:** Uses Twilio API to send WhatsApp messages.
- **Message Scheduling:** Allows users to select a future delivery date and time.
- **User Input:** Accepts recipient details and customized messages.
- **Date-Time Validation:** Checks the entered date and time format.
- **Error Handling:** Handles API errors and missing credentials.
- **Credential Management:** Uses environment variables instead of hardcoding authentication credentials.

## 6. Project Requirements

Install the required Python package:

```bash
pip install twilio
```

Python's `datetime`, `time`, and `os` modules are included in the standard library.

## 7. Environment Configuration

Before running the application, configure your Twilio credentials as environment variables.

Required variables:

- `TWILIO_ACCOUNT_SID`
- `TWILIO_AUTH_TOKEN`

The application retrieves these credentials using Python's `os.getenv()` function.

**Important:** Never upload your Twilio credentials, authentication tokens, or other private information to GitHub.

## 8. How to Run the Project

**Step 1:** Clone the repository.

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**Step 2:** Navigate to the project directory.

```bash
cd your-project-folder
```

**Step 3:** Install dependencies.

```bash
pip install twilio
```

**Step 4:** Configure your Twilio credentials as environment variables.

**Step 5:** Run the Python script.

```bash
python filename.py
```

**Step 6:** Enter the requested information:

- Recipient name
- Recipient WhatsApp number with country code
- Message content
- Scheduled date (YYYY-MM-DD)
- Scheduled time (HH:MM)

The application waits until the scheduled time and then attempts to send the WhatsApp message.

## 9. Important Notes

- A valid Twilio account and WhatsApp-enabled sender are required.
- The recipient must satisfy Twilio's WhatsApp messaging requirements.
- For WhatsApp Sandbox usage, the recipient must join the configured sandbox.
- The script must remain running until the scheduled message is sent.
- The current implementation supports one scheduled message per execution.
- The scheduling uses the computer's local system time.

## 10. Current Limitations

- The application does not support multiple scheduled messages in one execution.
- The scheduling process stops if the program is closed.
- There is no graphical user interface.
- Messages are not stored in a database.
- The application does not currently provide recurring scheduling.

## 11. Future Enhancements

- Develop a web-based scheduling dashboard.
- Support multiple scheduled messages.
- Integrate a database to store scheduled messages.
- Add recurring message scheduling.
- Implement message delivery status tracking.
- Add logging and notification features.

## 12. Skills Demonstrated

- Python Programming
- API Integration
- WhatsApp Automation
- Date and Time Handling
- Exception Handling
- Environment Variable Management
- Workflow Automation

## 13. Conclusion

This project demonstrates how Python and the Twilio API can be integrated to automate WhatsApp message scheduling.

It provides practical experience with third-party API integration, user input handling, time-based execution, and automation workflows.
