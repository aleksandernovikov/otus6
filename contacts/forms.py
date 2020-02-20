from django import forms
from .tasks import send_email_task


class ContactForm(forms.Form):
    name = forms.CharField(min_length=3, max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, max_length=1000)

    def send_email(self):
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        message = self.cleaned_data.get('message')
        send_email_task.delay(name, email, message)
