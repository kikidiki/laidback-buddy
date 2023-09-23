import imaplib
import email

imap_server = "imap.gmail.com"
SMTP_PORT = 993

email_address = "cdicolc21@gmail.com"
file_path = "D:\\PycharmProjects\\dsa.txt"

with open(file_path, 'r') as file:
    password = file.read().strip()

imap = imaplib.IMAP4_SSL(imap_server)
imap.login(email_address, password)

imap.select("Inbox")

_, msgnums = imap.search(None, "ALL")

# Get the 10 most recent emails
msgnums = msgnums[0].split()[-10:]

for msgnum in msgnums:
    _, data = imap.fetch(msgnum, "(RFC822)")
    message = email.message_from_bytes(data[0][1])

    #print(f"Message Number: {msgnum}")
    print(f"From: {message.get('From')}")
    #print(f"To: {message.get('To')}")
    #print(f"BCC: {message.get('BCC')}")
    print(f"Date: {message.get('Date')}")
    print(f"Subject: {message.get('Subject')}")

    print("Content:")

    for part in message.walk():
        if part.get_content_type() == "text/plain":
            content = part.get_payload(decode=True)
            if part.get_content_charset():
                content = content.decode(part.get_content_charset())
            else:
                content = content.decode("utf-8", "ignore")
            print(content)
