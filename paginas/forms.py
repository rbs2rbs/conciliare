from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True,label="Email")
    nome = forms.CharField(required=True, label="Nome")
    subject = forms.CharField(required=True, label="Assunto")
    message = forms.CharField(widget=forms.Textarea, required=True, label="Mensagem")