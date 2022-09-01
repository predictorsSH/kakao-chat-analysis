from django.shortcuts import render, redirect
from . import models
from . import forms



def fileUpload(request):
    if request.method == "POST":
        # Fetching the form data
        # title = request.POST["title"]
        attached = request.FILES["attached"]

        # Saving the information in the database
        fileupload = models.FileUpload(
            # title=title,
            attached=attached
        )
        fileupload.save()

        return redirect('fileupload')

    else :
        fileuploadForm = forms.FileUploadForm
        context = {
            'fileuploadForm' : fileuploadForm
        }

    return render(request, "fileupload.html", context)