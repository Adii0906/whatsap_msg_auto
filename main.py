import pywhatkit

print("WhatsApp Message Automation")
number = input("Enter the number to send the message to (include the country code, e.g., +919876543210): ")
message = input("Enter the message you want to send: ")
hour = int(input("Enter the hour (24-hour format): "))
minute = int(input("Enter the minute: "))

pywhatkit.sendwhatmsg(number, message, hour, minute)

