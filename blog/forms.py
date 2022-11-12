from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['user_name', 'user_email', 'comment_content']
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
            'user_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'comment_content': forms.Textarea(attrs={'class': 'form-control'}),
        }