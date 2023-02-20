from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver

# This is signal will run at login sucess 
@receiver(user_logged_in,sender=User)
def login_success(sender,request, user, **kwargs):
    print("Sender :",sender)
    print("Request :",request)
    print("User :",user)
    print(f"Key Word Argument :{kwargs}")
    print("All detail ".center(50,"-"))
    print("First Name :", user.first_name)
    print("Last name :", user.last_name)
    print("Email Address :", user.email)
    print("Last login :", user.last_login)
    print("Date of Joined :", user.dat_joined)
# user_logged_in.connect(login_success, sender=User)


# # This is signal will run at loogdout sucess 
# @receiver(user_logged_out,sender=User)
def logout_success(sender,request, user, **kwargs):
    print("Sender :",sender)
    print("Request :",request)
    print("User :",user)
    print(f"Key Word Argument :{kwargs}")
    print("All detail ".center(50,"-"))
    print("First Name :", user.first_name)
    print("Last name :", user.last_name)
    print("Email Address :", user.email)
    print("Last login :", user.last_login)
    print("Date of Joined :", user.dat_joined)

user_logged_out.connect(logout_success, sender=User)


# this signal will run at login failed 
# @receiver(user_login_failed,sender=User)

def login_fail(sender, request,credntials, **kwargs):
    print("Sender :",sender)
    print("Request :",request)
    print(f"Key Word Argument :{kwargs}")
    print("All detail ".center(50,"-"))
    # print("Credentials :",credntials)
    for i in credntials.item():
        print(i)
user_login_failed.connect(login_fail)