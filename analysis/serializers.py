from rest_framework import serializers
from .models import Basic_stats, Advanced_analyis


class BasicStatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basic_stats
        fields = ('user_count', 'active_time', 'user_words_count')


class AdvancedAnalysisSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advanced_analyis
        fields = ('test',)

