from django.shortcuts import render, redirect
from .models import FileUpload, Basic_stats
from . import forms

# mnps
from whorwe.mnps.mnps import DataProcess



def fileUpload(request):
    if request.method == "POST":

        attached = request.FILES["attached"]

        fileupload = FileUpload(
            attached=attached
        )

        fileupload.save()

        dp = DataProcess(fileupload.attached.path)
        u_count = dp.basic_analysis()

        for n, c in u_count.items():
            basic_analysis = Basic_stats(
                name=n,
                count=c
            )

            basic_analysis.save()

        return redirect('fileupload')

    else:

        fileuploadForm = forms.FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm
        }

    return render(request, "analysis/fileupload.html", context)