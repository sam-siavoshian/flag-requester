import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
# Email credentials (use your App Password here)
YOUR_EMAIL = "YOUR_EMAIL"
YOUR_PASSWORD = "YOUR_PASSWORD" 

# Your mailing address
YOUR_ADDRESS = "YOUR_ADDRESS"

def create_email(country):
    subject = f"{country} Flag Request for Personal Collection"
    greeting = f"Dear {country} embassy,"
    
    body = f"""{greeting}

My name is NAME, and I’m a X in Y who is deeply interested in world cultures and history. I’ve started collecting small flags from different countries, and I would be honored to include your nation’s flag in my collection.

If possible, I would truly appreciate it if you could send a small flag to my address:
{YOUR_ADDRESS}

Thank you so much for your time and generosity. It would mean a lot to me.

Warm regards,  
NAME
"""
    return subject, body

def send_email(to_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = YOUR_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(YOUR_EMAIL, YOUR_PASSWORD)
        server.send_message(msg)
        server.quit()
        print(f"✅ Sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send to {to_email}: {e}")

def main():
    with open('embassies.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        for row in reader:
            country = row[0]
            emails = row[1:]
            subject, body = create_email(country)
            for email in emails:
                email = email.strip()
                if email:
                    send_email(email, subject, body)
                    time.sleep(3)

if __name__ == "__main__":
    main()
