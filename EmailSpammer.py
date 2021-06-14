import smtplib
from email.message import EmailMessage


selected = ""
selectedPass = ""

bot1 = "smurf31233@gmail.com"
password1 = "thisIsSmurf1234"

bot2 = "pinksmurf221@gmail.com"

class bcolors:
    Green = '\033[92m' #GREEN
    Yellow = '\033[93m' #YELLOW
    Red = '\033[91m' #RED
    Magneta = '\u001b[35m'#Magneta
    Cyan = '\u001b[36m' #Cyan
    Blue = '\u001b[34m'

    Cyan_High_Bold = "\033[1;96m"
    Reset = '\033[0m' #RESET COLOR

#start screen

laughingMan = ("""
░░░░░░░░████████████████░░░░░░░
░░░░░█████████████████████░░░░░
░░░░████████████████████████░░░
░░░██████████████████████████░░
░░█████████████████████████████
░░███████████▀░░░░░░░░░████████
░░███████████░░░░░░░░░░░░░░░███
░████████████░░░░░░░░░░░░░░░░██
░█░░███████░░░░░░░░░░░▄▄░░░░░██
█░░░░█████░░░░░░▄███████░░██░░█
█░░█░░░███░░░░░██▀▀░░░░░░░░██░█
█░░░█░░░░░░░░░░░░▄██▄░░░░░░░███
█░░▄█░░░░░░░░░░░░░░░░░░█▀▀█▄░██
█░░░░░░░░░░░░░░░░░░░░░░█░░░░██░
░███░░░░░░░░░░░░░░░░░░░█░░░░█░░
░░█░█░░░░░░░█░░░░░██▀▄░▄██░░░█░
░░█░█░░░░░░█░░░░░░░░░░░░░░░░░█░
░░░██░░░░░░█░░░░▄▄▄▄▄▄░░░░░░█░░
░░░██░░░░░░░█░░█▄▄▄▄░▀▀██░░█░░░
░░░██░░░░░░░█░░▀████████░░█░░░░
░░█░░█░░░░░░░█░░▀▄▄▄▄██░░█░░░░░
░░█░░░█░░░░░░░█░░░░░░░░░█░░░░░░
░█░░░░░█░░░░░░░░░░░░░░░░█░░░░░░
░░░░░░░░█░░░░░░█░░░░░░░░█░░░░░░
░░░░░░░░░░░░░░░░████████░░░░░░░""")

fiveLineOblique = ("""                                                                                              
      ____                                        ___                                                              
    //   / /                                    //   ) )                                                           
   //____     _   __      ___     ( ) //       ((         ___      ___      _   __      _   __      ___      __    
  / ____    // ) )  ) ) //   ) ) / / //          \\     //   ) ) //   ) ) // ) )  ) ) // ) )  ) ) //___) ) //  ) ) 
 //        // / /  / / //   / / / / //             ) ) //___/ / //   / / // / /  / / // / /  / / //       //       
//____/ / // / /  / / ((___( ( / / //       ((___ / / //       ((___( ( // / /  / / // / /  / / ((____   //    
""")

#print(bcolors.Blue+laughingMan + "\n")
print(bcolors.Magneta + fiveLineOblique)
print(bcolors.Magneta+"[Email Spammer] By: Leo Liu")
input(bcolors.Green + "Press"+bcolors.Reset+" Enter" +bcolors.Green+" to begin spam attack" + bcolors.Reset)

inp = input(bcolors.Yellow+"What do you want to send? "+bcolors.Reset)

msg = EmailMessage()
msg.set_content(inp) #text inside message

subject = input(bcolors.Yellow+"Enter the subject of the email " + bcolors.Reset)
try:
    sender = input(bcolors.Yellow+"Select which email you would like to send from: "+bcolors.Cyan+"\n1 \n2 \n" + bcolors.Reset)
    if sender == "1":
        selected = bot1
        selectedPass = password1
    elif sender == "2":
        selected = bot2
        selectedPass = password1
except:
    sender = input(bcolors.Yellow+"please enter a number: " + bcolors.Reset)
reciever = input(bcolors.Yellow+"Enter the email that will recieve the spam: " + bcolors.Reset)
msg['Subject'] = subject #email subject
msg['From'] = selected #sender
msg['To'] = reciever  #reciever

client = smtplib.SMTP('smtp.gmail.com', 587)
client.starttls()
client.login(selected, selectedPass)
client.timeout = 10000

try:
    times = int(input(bcolors.Yellow+"please enter how many times you will send the email: " + bcolors.Reset))
except ValueError:
    times = int(input(bcolors.Yellow+"please enter a number: " + bcolors.Reset))

print(bcolors.Cyan_High_Bold + "sending...")

for number in range(times):
    client.send_message(msg)
    if number == (times - 1):
        t = str(times)
        print(bcolors.Green+"Finished sending " + t + " emails!"+bcolors.Reset)

