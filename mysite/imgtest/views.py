from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from imgtest.forms import ImageForm
from imgtest.models import PostImage
# handle_upload_file?


def upload(request):
	form = ImageForm(request.POST, request.FILES)

	if request.method == 'POST':
		if form.is_valid():
			image = form.save(commit=False)
			image.save()
			src = get_object_or_404(PostImage, pk=image.pk).photo.url
			return render(request, "imgtest/upload.html", {'src': src})
	else:
		form = ImageForm()

	return render(request, "imgtest/upload.html", {'form': form})


