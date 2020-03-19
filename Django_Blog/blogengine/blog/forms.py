from django import forms
from django.forms import modelform_factory, DecimalField 
from .models import Post,Tag
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):
        class Meta:
            model = Tag
            fields = ['title','slug']
            widgets = {
                'title':forms.TextInput(attrs={'class':'form-control'}),
                'slug':forms.TextInput(attrs={'class':'form-control'}),
            
        }
        def clean_slug(self):
            new_slug = self.cleaned_data['slug'].lower()
            
            if new_slug == 'create':
                raise ValidationError('Slug may not be "Craete"')
            if Tag.objects.filter(slug__iexact=new_slug).count():
                raise ValidationError('Slug should be unique. We have "{}" slug already'.format(new_slug))
            return new_slug
            
  
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-coontrol'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
        }
    def client_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
            
        if new_slug == 'create':
            raise ValidationError('Slug may not be "Craete"')
        return new_slug
        
     