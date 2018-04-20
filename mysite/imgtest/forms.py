from django import forms
from .models import PostImage


class ImageForm(forms.ModelForm):
	class Meta:
		model = PostImage
		fields = ('title', 'photo')

	def __init__(self, *args, **kwargs):
		super(ImageForm, self).__init__(*args, **kwargs)
		self.fields['photo'].required = False

