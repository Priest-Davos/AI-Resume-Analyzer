from rest_framework import serializers
from .models import ResumeUpload, Resume, AnalysisResult

class ResumeUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResumeUpload
        fields = ['id', 'user', 'file', 'uploaded_at']

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ['id', 'user', 'upload', 'name', 'email', 'phone_number', 'experience', 'skills', 'education', 'summary', 'score']

class AnalysisResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnalysisResult
        fields = ['id', 'user', 'resume', 'created_at', 'result_text', 'score']