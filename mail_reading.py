import imaplib
import email

imap_server = "imap.gmail.com"  # Updated IMAP server address
SMTP_PORT = 993

email_address = "cdicolc21@gmail.com"
# Specify the path to your file
file_path = "D:\\PycharmProjects\\asd.txt"

# Open the file in read mode
with open(file_path, 'r') as file:
    # Read the password
    spassword = file.read().strip()

password = spassword

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

imap.select("Inbox")

_, msgnums = imap.search(None, "ALL")
for msgnum in msgnums[0].split():
    _, data = imap.fetch(msgnum, "(RFC822)")
    message = email.message_from_bytes(data[0][1])

    print(f"Message Number: {msgnum}")
    print(f"From: {message.get('From')}")
    print(f"To: {message.get('To')}")
    print(f"BCC: {message.get('BCC')}")
    print(f"Date: {message.get('Date')}")
    print(f"Subject: {message.get('Subject')}")

    print("Content:")
    for part in message.walk():
        if part.get_content_type() == "text/plain":
            print(part.as_string())