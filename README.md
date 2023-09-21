# whatsap_msg_auto
To use the pywhatkit library in Python to send WhatsApp messages and create a read.md file to document the process, you can follow these steps:

Install pywhatkit:
First, make sure you have pywhatkit installed. You can install it using pip:

Copy code
pip install pywhatkit
Replace "1234567890" with the recipient's phone number (including the country code but without the '+').
Modify the message variable to contain the text you want to send.
You can adjust the send_time to specify when you want to send the message. In this example, it's set to send the message 1 minute from the current time.
Run the Script:
Run the script using your Python interpreter. Ensure that WhatsApp Web is open and authenticated in the browser before running the script.

Scheduled Execution (Optional):
If you want to schedule the script to run at specific times, you can use tools like cron on Unix-based systems or Task Scheduler on Windows.

Please note that this script utilizes pywhatkit to automate WhatsApp messages and sends them at a scheduled time. It also logs the messages sent in the read.md file. Be sure to follow WhatsApp's terms of service and policies when automating messages.
