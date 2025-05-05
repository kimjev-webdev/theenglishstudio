from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    subject = forms.ChoiceField(choices=[
        ('After School Club', 'After School Club'),
        ('Private Lessons', 'Private Lessons'),
        ('Business English Lessons', 'Business English Lessons'),
        ('General English Lessons', 'General English Lessons'),
        ('IELTS Enquiry', 'IELTS Enquiry'),
        ('Events', 'Events'),
        ('Other', 'Other'),
    ])
    message = forms.CharField(widget=forms.Textarea)
    subscribe = forms.BooleanField(required=False)
