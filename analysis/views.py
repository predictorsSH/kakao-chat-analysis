from django.shortcuts import render, redirect
from .models import FileUpload, Basic_stats
from . import forms
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BasicStatSerializer
from rest_framework.generics import get_object_or_404
# mnps
from whorwe.mnps.mnps import DataProcess
import json


def fileUploadView(request):

    if request.method == "POST":

        attached = request.FILES["attached"]
        fileupload = FileUpload(
            attached=attached
        )
        fileupload.save()

        # 데이터 전처리
        dp = DataProcess(fileupload.attached.path)
        # user(채팅 참가자)별로 말한 횟수 카운트
        u_count, act_time = dp.basic_analysis()
        #user별 count dictionary 생성
        u_count_data = {}
        for n, c in u_count.items():
            u_count_data[n] = c

        #Basic_stats에 count 입력하고 저장.
        basic_stats = Basic_stats(
            count=json.dumps(u_count_data, ensure_ascii=False),
            active_time=act_time
        )
        basic_stats.save()

        return redirect('fileupload')

    else:

        fileuploadForm = forms.FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm
        }

    return render(request, "analysis/fileupload.html", context)

class BasicStatView(APIView):
    def get(self, request, id):
        basic_stats = get_object_or_404(Basic_stats, id=id)
        serializer = BasicStatSerializer(basic_stats)
        return Response(serializer.data, status=status.HTTP_200_OK)
