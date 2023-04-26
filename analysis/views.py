from django.shortcuts import render, redirect
from .models import FileUpload, Basic_stats, Advanced_analyis
from . import forms
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BasicStatSerializer, AdvancedAnalysisSerializer, UserCountSerializer, FileIDSerializer, ActiveTimeSerializer, AllUserWordsSerializer
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
# mnps
from whorwe.mnps.mnps import DataProcess
import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import csv
import io

@method_decorator(csrf_exempt, name="dispatch")
@api_view(('GET', 'POST'))
def fileUploadView(request):

    if request.method == "POST":

        attached = request.FILES['file']
        ## 바로 읽어오는게 더 좋을수도
        # decoded_file = attached.read().decode('utf-8')
        # io_string = io.StringIO(decoded_file)
        #
        # data = list()
        # for line in csv.reader(io_string, delimiter=','):
        #     print(line)

        fileupload = FileUpload(
            attached=attached
        )
        fileupload.save()
        serializer = FileIDSerializer(fileupload)

        #데이터 전처리
        # dp = DataProcess(fileupload.attached.path)
        # # user(채팅 참가자)별로 말한 횟수 카운트
        # u_count, act_time, u_words_count = dp.basic_analysis()
        # #user별 count dictionary 생성
        # u_count_data = {}
        # for n, c in u_count.items():
        #     u_count_data[n] = c
        #
        # #Basic_stats에 count 입력하고 저장.
        # basic_stats = Basic_stats(
        #     user_count=json.dumps(u_count_data, ensure_ascii=False),
        #     active_time=act_time,
        #     user_words_count=json.dumps(u_words_count, ensure_ascii=False)
        # )
        # basic_stats.save()
        #
        # advanced_analysis = Advanced_analyis(
        #     test='테스트 개발'
        # )
        # advanced_analysis.save()

        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        fileuploadForm = forms.FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm
        }
    return render(request, "analysis/fileupload.html", context)


class BasicStatView(APIView):
    def get(self, request, f_id):
        basic_stats = get_object_or_404(Basic_stats, id=f_id)
        serializer = BasicStatSerializer(basic_stats)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, f_id):

        file = FileUpload.objects.get(f_id=f_id)
        dp = DataProcess(file.attached.path)
        # user(채팅 참가자)별로 말한 횟수 카운트
        u_count, act_time, u_words_count = dp.basic_analysis()
        #user별 count dictionary 생성
        u_count_data = {}
        for n, c in u_count.items():
            u_count_data[n] = c

        #Basic_stats에 count 입력하고 저장.
        basic_stats = Basic_stats(
            f_id=file,
            user_count=json.dumps(u_count_data, ensure_ascii=False),
            active_time=json.dumps(act_time,ensure_ascii=False),
            user_words_count=json.dumps(u_words_count, ensure_ascii=False)
        )
        basic_stats.save()

        return Response(status=status.HTTP_201_CREATED)


class AdvancedAnalysisView(APIView):
    def get(self, request, id):
        advanced_analysis = get_object_or_404(Advanced_analyis, id=id)
        serializer = AdvancedAnalysisSerializer(advanced_analysis)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserCountView(APIView):
    def get(self, request, f_id):
        basic_stats = get_object_or_404(Basic_stats, f_id=f_id)
        serializer = UserCountSerializer(basic_stats)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ActiveTimeView(APIView):
    def get(self, request, f_id):
        basic_stats = get_object_or_404(Basic_stats, f_id=f_id)
        serializer = ActiveTimeSerializer(basic_stats)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AllUserWordsView(APIView):
    def get(self, request, f_id):
        basic_stats = get_object_or_404(Basic_stats, f_id=f_id)
        serializer = AllUserWordsSerializer(basic_stats)
        return Response(serializer.data, status=status.HTTP_200_OK)