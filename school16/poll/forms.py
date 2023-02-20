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

    father_name=forms.CharField(error_messages={'required':"Father Name is ,must...  "})

    mother_name=forms.CharField(
        widget=forms.TextInput(attrs={'class':'mymothername','id':'mymother2'})
    )

    salary=forms.CharField(widget=forms.NumberInput(attrs={'class':'salary'}))

    email_address=forms.CharField(widget=forms.EmailInput())
    web_address=forms.CharField(widget=forms.URLInput())

    adhar_no=forms.CharField(initial=4837463,widget=forms.HiddenInput)

    dob=forms.CharField(widget=forms.DateTimeInput)

    biodata=forms.CharField(widget=forms.Textarea(attrs={'row':20,'cols':40,'class':'biodata'}))

    color=forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'colos'},check_test=None))

    place=forms.ChoiceField(choices=[("","--select--"),('I',"India"),('A',"AMrica"),("J",'japan')])

    country=forms.NullBooleanField()