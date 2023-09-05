# from django import forms
# from django.forms import widgets
# from .models import ContactMessage

# class ContactForm(forms.ModelForm):
#     service = forms.ChoiceField(choices=[
#         ("", "Select service"),
#         ("1", "One"),
#         ("2", "Two"),
#         ("3", "Three"),
#     ], widget=forms.Select(attrs={"class": "single-input-field"}))

#     class Meta:
#         model = ContactMessage
#         exclude = ("timestamp",)
#         widgets = {
#             "full_name": widgets.TextInput(attrs={"class": "single-input-field", "placeholder": "Your Name"}),
#             "email": widgets.EmailInput(attrs={"class": "single-input-field", "placeholder": "Email address"}),
#             "phone_number": widgets.NumberInput(attrs={"class": "single-input-field", "placeholder": "Phone number"}),
#             "message": widgets.TextInput(attrs={"class": "single-input-field","placeholder": "Message"}),
#         }


from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     number = forms.CharField(max_length=20)
#     optionC = forms.ChoiceField(choices=[('1', 'One'), ('2', 'Two'), ('3', 'Three')])
#     message = forms.CharField(widget=forms.Textarea)


from django import forms
from .models import ServiceMessage
from .models import Comment

class ContactForm(forms.ModelForm):
    class Meta:
        model = ServiceMessage
        fields = ['name', 'email', 'number', 'optionC', 'message']




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'email', 'comment']

# class EmailSubscriptionForm(forms.ModelForm):
#     class Meta:
#         model = EmailSubscription
#         fields = ['email']