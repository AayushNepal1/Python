def show_message(text_message, sent_message):
    while text_message:
        active_msg = text_message.pop()
        print(f"Sending Message: {active_msg}\n.....")
        sent_message.append(active_msg)




def send_message(sent_message):
    print("\nThe sent message are:")
    for sender in sent_message:
        print(sender)


text_message = [
    'Hello, World from python.',
    'I love to code in a python.',
    'Python have many frameworks.',
]

sent_message = []

show_message(text_message=text_message, sent_message=sent_message)

send_message(sent_message=sent_message)
send_message(sent_message=sent_message[:])
