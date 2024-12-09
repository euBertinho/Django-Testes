from django import forms
from .models import Posts

class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['titulo', 'descricao', 'imagem']
    
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo')
        if len(titulo) < 5:
            raise forms.ValidationError("O título deve ter pelo menos 5 caracteres.")
        return titulo
