from django import forms

from album.models import Album_form

class AlbumModelForm(forms.ModelForm):
    class Meta:
        model = Album_form
        fields = '__all__'
        widgets = {
            'album_release_date':forms.DateTimeInput(attrs={'type':'datetime-local'})
        }
    def clean(self):
        cleaned_data = super().clean()
        
        
        print(cleaned_data)
        if  'album_rating' in cleaned_data:
            rating = cleaned_data['album_rating']
            print(rating)
            if rating is not None and rating > 5:
                raise forms.ValidationError('Must be 1 to 5 rating exits ')

