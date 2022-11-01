

class Email:
    
    is_send = False

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def send(self):
        self.is_send = True

    def get_info(self):
        return f'{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}'

class MailBox:

    def __init__(self):
        self.emails = []

    def add_email(self, email):
        self.emails.append(email)

    def send_emails(self, indices):
        for index in indices:
            self.emails[index].send()

    def print_mailbox(self):
        for email in self.emails:
            print(email.get_info())

mailbox = MailBox()

while True:
    command = input()
    if command == 'Stop':
        break

    sender, receiver, content = command.split()
    email = Email(sender, receiver, content)
    mailbox.add_email(email)

send_indices = [int(x) for x in input().split(', ')]
mailbox.send_emails(send_indices)
mailbox.print_mailbox()

# Path: email.py
