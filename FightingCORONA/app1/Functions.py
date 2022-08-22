import smtplib
import ssl
import random


def mail(receiver_email, message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "fightingcorona2021@gmail.com"  # Enter your address
    password = "pxfvucsampcosost"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

# define a function to get tips
def getTip():
    tips = [
        "Wash milk bags the moment we take it & wash your hands while you are at it.",
        "Consider cancelling newspapers",
        "Keep a separate tray for couriers. Courier person can place the envelope/pkg in the tray and courier may be left untouched for at least 24 hours.",
        "Instruct maids not to touch main door. On entering the home, she has to immediatly wash hands thoroughly, before touching other things . After that, wipe the calling-bell switch with a cleaning fluid :)",
        "Avoid getting swiggy, amazon etc as far as possible.",
        "Wash all fruits and vegitables once we bring them home"
        "Remote, phone and keyboards are the most highly contaminated elements in our house. Clean them at least once a day using cleaning fluid.",
        "Wash hands frequently when in house or in office. Once every hour at least.",
        "Avoid public transport as far as possible. Even Ola and Uber may be used when absolutely unavoidable.",
        "Avoid gyms, swimming pool and other exercise areas, where surface contact or air - borne contamination is inevitable",
        "Cancel tuitions, dance/music classes, etc.",
        "When you return home from office, shopping, etc. discard your clothes and wash your hands and feet thoroughly.",
        "Most importantly do not touch hands anywhere on face. Inform children and parents.",
        "Ask senior citizens to stop going for the routine walking exercise."
    ]
    return (tips[random.randint(0, len(tips) - 1)])
