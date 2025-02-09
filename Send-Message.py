import os
import requests
import time
import platform

# Function to clear the terminal
def clear():
    os.system("cls" if platform.system() == "Windows" else "clear")

# Function to prompt for a valid URL
def get_valid_url():
    while True:
        clear()
        url = input("Enter URL Here: ").strip()

        if not url.startswith("https://"):
            print("❌ INVALID LINK! Must start with 'https://'")
            time.sleep(2)
        else:
            return url  # Return the valid URL

# Main loop to handle messaging
while True:
    url = get_valid_url()

    while True:
        clear()
        message = input("What is the message you want to send? (Type 'URL' to change the URL): ").strip()
        clear()

        if message.upper() == "URL":
            break  # Breaks out of the message loop to change URL

        data = {"content": message}
        result = requests.post(url, json=data)

        if result.status_code == 204:
            print("✅ Message was sent successfully!")
        else:
            print(f"❌ Failed to send message. Status: {result.status_code}, Response: {result.text}")

        time.sleep(2)  # Pause before clearing
        clear()
