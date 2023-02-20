from django import forms 


# class Register(forms.Form):
#     user_name=forms.CharField(initial='Shoeb Ansari')
#     email=forms.EmailField(initial="Shoeb@gamil.com",
#     label="User Email Address ",
#     )
#     age=forms.IntegerField(initial=00)
#     password1=forms.CharField(required=True,
#     error_messages={'required':'password is must!!'},
#     widget=forms.PasswordInput,
#     label='Password',
#     )
#     password2=forms.CharField(required=True,
#     widget=forms.PasswordInput,
#     label="Confirm Password",
#     help_text='User Password Comes Hear..')

    # father_name=forms.CharField(error_messages={'required':"Father Name is ,must...  "})

    # mother_name=forms.CharField(
    #     widget=forms.TextInput(attrs={'class':'mymothername','id':'mymother2'})
    # )

    # salary=forms.CharField(widget=forms.NumberInput(attrs={'class':'salary'}))

    # email_address=forms.CharField(widget=forms.EmailInput())
    # web_address=forms.CharField(widget=forms.URLInput())

    # adhar_no=forms.CharField(initial=4837463,widget=forms.HiddenInput)

    # dob=forms.CharField(widget=forms.DateTimeInput)

    # biodata=forms.CharField(widget=forms.Textarea(attrs={'row':20,'cols':40,'class':'biodata'}))

    # color=forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'colos'},check_test=None))

    # place=forms.ChoiceField(choices=[("","--select--"),('I',"India"),('A',"AMrica"),("J",'japan')])

    # country=forms.NullBooleanField()


class Register(forms.Form):
    user_name=forms.CharField(required=True,error_messages={'required':'User name is must'})
    email=forms.EmailField(required=True,error_messages={'requirde':'Email is required'})
    age=forms.IntegerField(required=False)
    password1=forms.CharField(required=False,min_length=5,max_length=10,strip=False)
    password2=forms.CharField(required=False,min_length=5,max_length=10)


    # cleening and validating specifide field 
    # def Cleen_user_name(self):
    #     valname=self.cleened_data.get("user_name")
    #     if len(valname)<5:
    #         raise forms.ValidationError("Enter user name length greater then or equal to 5 ")
    #     return valname

    # def Cleen_Password1(self):
    #     pass1=self.cleened_data.get("Password1")
    #     if len(pass1)<5:
    #         raise forms.ValidationError("Enter password length greater then or equal to 8 ")
    #     return pass1    
        
    # def Cleen_Password2(self):
    #     pass2=self.cleened_data.get("Password2")
    #     if len(pass2)<5:
    #         raise forms.ValidationError("Enter password conform length greater then or equal to 8 ")
    #     return pass2


    # cleening and validating at onese
    def cleen(self):
        super(Register,self).cleen()
        username=self.cleaned_data.get("user_name")
        pass1=self.cleaned_data.get("password1")
        pass2=self.cleaned_data.get("password2")
        if len(user)

