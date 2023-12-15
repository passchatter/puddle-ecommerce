from django import forms
from .models import Items

INPUT_CLASES = 'w-full py-4 px-6 rounded-xl border'

class NewItemsForms(forms.ModelForm):
   class Meta:
    model = Items
    fields = ('category', 'nama', 'description', 'price', 'image',)
  
    widgets = {
      'category' : forms.Select(attrs={
         'class' : INPUT_CLASES
      }),
      'nama': forms.TextInput(attrs={
         'class' : INPUT_CLASES,
         'placeholder' : 'input name items'
      }),

      'description': forms.Textarea(attrs={
         'class' : INPUT_CLASES,
         'placeholder' : 'input description items'
      }),
      'price' : forms.TextInput(attrs={
         'class' : INPUT_CLASES,
         'placeholder' : 'input price'
      }),
      'image': forms.FileInput(attrs={
         'class': INPUT_CLASES
      })
    }