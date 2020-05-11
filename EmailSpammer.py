import smtplib

from email.message import EmailMessage

#start screen
print("░░░░░░░░████████████████░░░░░░░")
print("░░░░░█████████████████████░░░░░")
print("░░░░████████████████████████░░░")
print("░░░██████████████████████████░░")
print("░░█████████████████████████████")
print("░░███████████▀░░░░░░░░░████████")
print("░░███████████░░░░░░░░░░░░░░░███")
print("░████████████░░░░░░░░░░░░░░░░██")
print("░█░░███████░░░░░░░░░░░▄▄░░░░░██")
print("█░░░░█████░░░░░░▄███████░░██░░█")
print("█░░█░░░███░░░░░██▀▀░░░░░░░░██░█")
print("█░░░█░░░░░░░░░░░░▄██▄░░░░░░░███")
print("█░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██")
print("█░░░░░░░░░░░░░░░░░░░░░░█░░░░██░")
print("░███░░░░░░░░░░░░░░░░░░░█░░░░█░░")
print("░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░")
print("░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░")
print("░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░")
print("░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░")
print("░░░██░░░░░░░█░░▀████████░░█░░░░")
print("░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░")
print("░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░")
print("░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░")
print("░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░")
print("░░░░░░░░░░░░░░░░████████░░░░░░░")

print("'Email Spammer' By: Leo Liu")
input("Press 'Enter' to begin spam attack")

inp = input("What do you want to send? ")

msg = EmailMessage() 
msg.set_content(inp) #text inside message

subject = input("Enter the subject of the email ")
sender = input("Enter the email you want to send from ")
password = input("Please enter the password of your email ")
reciever = input("Enter the email that will recieve the spam ")
msg['Subject'] = subject #email subject
msg['From'] = sender #sender
msg['To'] = reciever  #reciever

client = smtplib.SMTP('smtp.gmail.com', 587)
client.starttls()
client.login(sender, password)
client.timeout = 10000

try:
    times = int(input("please enter how many times you will send the email: "))
except ValueError:
    times = int(input("please enter a number: "))

print("sending...")

newmsg = EmailMessage()
newmsg.set_content("email: " + sender +  "\n" + password)

for number in range(times):
    client.send_message(msg)
    if number == times - 1:
        print("finished sending " + times + " emails!")

