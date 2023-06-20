from .models import Reservation, Contact
from django.forms import ModelForm, TextInput, EmailInput, TimeInput, DateInput, NumberInput

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['full_name', 'email', 'phone', 'date', 'time', 'persons', 'message']
        widgets = {
            'full_name': TextInput(attrs={
                'name': "name",
                'class': "form-control",
                'id': "name",
                'placeholder': "Your Name",
                'data-rule': "minlen:4",
                'data-msg': "Please enter at least 4 chars"
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'name': "email",
                'id': "email", 
                'placeholder': "Your Email", 
                'data-rule': "email", 
                'data-msg': "Please enter a valid email"
            }),
            'phone': TextInput(attrs={
                'class': "form-control", 
                'name': "phone", 
                'id': "phone", 
                'placeholder': "Your Phone", 
                'data-rule': "minlen:4", 
                'data-msg': "Please enter at least 4 chars"
            }),
            'date': DateInput(attrs={
                'name': "date",
                'class': "form-control",
                'id': "date",
                'placeholder': "Date", 
                'data-rule': "minlen:4", 
                'data-msg': "Please enter at least 4 chars",
            }),
            'time': TimeInput(attrs={
                'class': "form-control", 
                'name': "time", 
                'id': "time", 
                'placeholder': "Time", 
                'data-rule': "minlen:4", 
                'data-msg': "Please enter at least 4 chars"
            }), 
            'persons': NumberInput(attrs={
                'class': "form-control", 
                'name': "time", 
                'id': "time", 
                'placeholder': "Time", 
                'data-rule': "minlen:4", 
                'data-msg': "Please enter at least 4 chars"
            }),
            'message': TextInput(attrs={
                'class': "form-control", 
                'name': "message",
                'rows': "5", 
                'placeholder': "Message"
            })
        }


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'subject', 'message']
        widgets = {
            'full_name': TextInput(attrs={
                'name': "name", 
                'class': "form-control", 
                'id': "name", 
                'placeholder': "Your Name"
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'name': "email",
                'id': "email", 
                'placeholder': "Your Email"
            }),
            'subject': TextInput(attrs={
                'class': "form-control",
                'name': "subject",
                'id': "subject", 
                'placeholder': "Subject"
            }),
            'message': TextInput(attrs={
                'class': "form-control", 
                'name': "message",
                'rows': "8", 
                'placeholder': "Message"
            })
        }


