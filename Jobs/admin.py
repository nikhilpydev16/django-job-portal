
from django.contrib import admin
from .models import CandidateProfile, RecruiterProfile, Job, Application, SavedJob


@admin.register(CandidateProfile)
class CandidateProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'qualification', 'skills')
    search_fields = ('user__username', 'qualification', 'skills')


@admin.register(RecruiterProfile)
class RecruiterProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company_name', 'phone', 'company_location')
    search_fields = ('user__username', 'company_name', 'company_location')


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'salary', 'status', 'recruiter', 'posted_date')
    list_filter = ('status', 'location', 'posted_date')
    search_fields = ('title', 'company', 'location', 'skills_required')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'job', 'status', 'applied_date')
    list_filter = ('status', 'applied_date')
    search_fields = ('candidate__username', 'job__title')


@admin.register(SavedJob)
class SavedJobAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'job', 'saved_date')
    search_fields = ('candidate__username', 'job__title')