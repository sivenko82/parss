from .models import Artik
from  django.forms import ModelForm,TextInput,DateTimeInput,Textarea

class ArtikFrom(ModelForm):
    class Meta:
        model=Artik
        fields=['title','anons','full','date']
        widgets={
            'title': TextInput(attrs={
                'class':"from-control",
                'placeholder':'название статьи'
            }),
            'anons': TextInput(attrs={
                'class': "from-control",
                'placeholder': 'Анонс статьи'
            }),
            'date':DateTimeInput (attrs={
                'class': "from-control",

            }),
            'full': Textarea(attrs={
                'class': "from-control",
                'placeholder': 'ТЕкс татьи'
            })
        }