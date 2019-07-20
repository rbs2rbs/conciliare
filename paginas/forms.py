from django import forms

# class ContactForm(forms.Form):
#     from_email = forms.EmailField(required=True,label="Email")
#     nome = forms.CharField(required=True, label="Nome")
#     subject = forms.CharField(required=True, label="Assunto")
#     message = forms.CharField(widget=forms.Textarea, required=True, label="Mensagem")

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True,label="Email",
        widget=forms.TextInput(attrs={
            'placeholder': 'Emaill',
            'name' : 'email',
            'type' : 'text',
            'id':'email',
            'data-error':'Please enter your name',
            'class':'form-control'
        }))
    nome = forms.CharField(required=True, label="Nome",
        widget=forms.TextInput(attrs={
            'placeholder': 'Nome',
            'type':'text',
            'class':'form-control',
            'id':'name'
        }))
    # sobrenome = forms.CharField(required=True, label="Sobrenome",
    #     widget=forms.TextInput(attrs={'placeholder': 'Sobrenome'})) 
    subject = forms.CharField(required=True, label="Assunto",
        widget=forms.TextInput(attrs={
            'placeholder': 'Assunto',
            'type':'text',
            'placeholder':'Assunto',
            'id':'msg_subject',
            'class':'form-control',
            'name':'msg_subject',
            'data-error':'Please enter your assunto'
        }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Assunto',
        'rows': '4',
        'placeholder':'Escreva sua mensagem',
        'id':'message',
        'class':'form-control',
        'name':'message',
        'data-error':'Please enter your assunto'
    }), required=True, label="Mensagem")
                