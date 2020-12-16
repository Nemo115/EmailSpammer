import smtplib

from email.message import EmailMessage

selected = ""
selectedPass = ""

bot1 = "smurf31233@gmail.com"
password1 = "thisIsSmurf1234"

bot2 = "thisIsSmurf1234"

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
try:
    sender = input("Select which email you would like to send from: \n1 \n2 ")
    if sender == "1":
        selected = bot1
        selectedPass = password1
    elif sender == "2":
        selected = bot2
        selectedPass = password1
except:
    sender = input("please enter a number: ")
reciever = input("Enter the email that will recieve the spam: ")
msg['Subject'] = subject #email subject
msg['From'] = selected #sender
msg['To'] = reciever  #reciever

client = smtplib.SMTP('smtp.gmail.com', 587)
client.starttls()
client.login(selected, selectedPass)
client.timeout = 10000

try:
    times = int(input("please enter how many times you will send the email: "))
except ValueError:
    times = int(input("please enter a number: "))

print("sending...")

for number in range(times):
    client.send_message(msg)
    if number == (times - 1):
        t = str(times)
        print("finished sending " + t + " emails!")

