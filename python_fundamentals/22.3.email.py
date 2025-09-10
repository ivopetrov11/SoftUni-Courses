class Email:
    def __init__(self, sender: object, receiver: object, content: object):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        print(f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}")

emails = []
while True:
    command = input()
    if command == "Stop":
        indices = [int(i) for i in input().split(", ")]
        for num in indices:
            emails[num].send()
        for email in emails:
            email.get_info()
        break

    command_list = command.split(" ")
    person1 = command_list[0]
    person2 = command_list[1]
    message = command_list[2]

    email =  Email(person1,person2,message)
    emails.append(email)



