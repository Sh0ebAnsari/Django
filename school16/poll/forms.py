from django import forms 


class register(forms.Form):
    username=forms.CharField(initial='Shoeb Ansari')
    email=forms.EmailField(initial="Shoeb@gamil.com",
    label="User Email Address ",
    )
    age=forms.IntegerField(initial=00)
    password1=forms.CharField(required=True,
    error_messages={'required':'password is must!!'},
    widget=forms.PasswordInput,
    label='Password',
    )
    password2=forms.CharField(required=True,
    widget=forms.PasswordInput,
    disabled=True,
    help_text='User Password Comes Hear..')