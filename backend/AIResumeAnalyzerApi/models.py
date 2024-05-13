from django.db import models
from django.contrib.auth.models import User

class ResumeUpload(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Uploaded by {self.user.username} at {self.uploaded_at}"

class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload = models.ForeignKey(ResumeUpload, on_delete=models.CASCADE)
    # Additional fields
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    experience = models.PositiveIntegerField(default=0)
    skills = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    score = models.FloatField(default=0)
    
    def __str__(self):
        return f"Resume for {self.name} uploaded by {self.user.username}"

class AnalysisResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    result_text = models.TextField(blank=True, null=True)
    score = models.FloatField(default=0)

    def __str__(self):
        return f"Analysis result for {self.resume.name} by {self.user.username} created at {self.created_at}"
