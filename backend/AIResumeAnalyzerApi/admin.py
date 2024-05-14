from django.contrib import admin

from .models import ResumeUpload, Resume, AnalysisResult

# Register your models with the admin site
admin.site.register(ResumeUpload)
admin.site.register(Resume)
admin.site.register(AnalysisResult)
