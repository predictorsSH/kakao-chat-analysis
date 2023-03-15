from django.shortcuts import render, redirect
from .models import FileUpload, Basic_stats
from . import forms
from rest_framework.views import APIView
from .serializers import BasicStatSerializer
from rest_framework.response import Response
from rest_framework import status
# mnps
from whorwe.mnps.mnps import DataProcess
import json


def fileUpload(request):

    if request.method == "POST":
        attached = request.FILES["attached"]
        fileupload = FileUpload(
            attached=attached
        )
        fileupload.save()

        # 데이터 전처리
        dp = DataProcess(fileupload.attached.path)
        # user(채팅 참가자)별로 말한 횟수 카운트
        u_count = dp.basic_analysis()

        u_count_data = {}
        for n, c in u_count.items():
            u_count_data[n] = c

        basic_analysis = Basic_stats(
            count=json.dumps(u_count_data)
        )

        basic_analysis.save()

        return redirect('fileupload')

    else:

        fileuploadForm = forms.FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm
        }

    return render(request, "analysis/fileupload.html", context)

class BasicStatView(APIView):
    def get(self, request):
        basic_stats = Basic_stats.objects
        serializer = BasicStatSerializer(basic_stats)
        return Response(serializer.data, status=status.HTTP_200_OK)
