from django import forms
from django.core import validators

# widgets == field to html input
class contactForm(forms.Form):
    name = forms.CharField(label="User Name", initial='Jhon Doe', help_text='Total length must be 5 characters', required=False, disabled=False, widget=forms.TextInput(attrs= {'id' : 'test_area', 'class' : 'myClass1 myClass2', 'placeholder' : 'Enter your Name.'}))
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'png'], message='File extension must be with .pdf or .png')])
    email = forms.CharField(label="User Email", widget=forms.EmailInput, validators=[validators.EmailValidator(message="Enter a valid email")])
    age = forms.CharField(widget=forms.NumberInput)
    weight = forms.FloatField()
    check = forms.BooleanField(label='Confirm to take Appointment!')
    birthday = forms.CharField(label="Date Of Birth", widget=forms.DateInput(attrs = {'type' : 'date'}))
    appointment = forms.CharField(widget=forms.DateInput(attrs = {'type' : 'datetime-local'}))
    CHOICES = [('15', '15 Minutes'), ('30', '30 Minutes'), ('45', '45 Minutes'), ('60', '60 Minutes')]
    duration = forms.ChoiceField(choices = CHOICES, widget=forms.RadioSelect)
    SESSION = [('M', 'Morning'),('A', 'Afternoon'),('N', 'Night')]
    appointment_time = forms.MultipleChoiceField(choices = SESSION, widget=forms.CheckboxSelectMultiple)

    def clean(self):
        cleaned_data = super().clean()
        name_value = self.cleaned_data['name']
        pass_value = self.cleaned_data['password']
        confirm_pass_value = self.cleaned_data['confirm_password']
        if len(name_value) < 5 :
            raise forms.ValidationError("Enter a name with at least 5 characters")
        if pass_value != confirm_pass_value:
            raise forms.ValidationError("Password doesn't match")

    