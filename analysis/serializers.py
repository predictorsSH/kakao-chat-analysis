from rest_framework import serializers
from .models import Basic_stats, Advanced_analyis


class BasicStatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basic_stats
        fields = ('f_id', 'user_count', 'active_time', 'user_words_count')

class FileIDSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basic_stats
        fields = ('f_id',)


class UserCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basic_stats
        fields = ('user_count',)

class ActiveTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basic_stats
        fields = ('active_time',)


class AdvancedAnalysisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advanced_analyis
        fields = ('test',)

