from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('my-posted-jobs/', views.my_posted_jobs, name='my_posted_jobs'),

    path('candidate-register/', views.candidate_register, name='candidate_register'),
    path('recruiter-register/', views.recruiter_register, name='recruiter_register'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('jobs/', views.job_list, name='job_list'),
    path('post-job/', views.post_job, name='post_job'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),

    path('my-applications/', views.my_applications, name='my_applications'),

    path('profile/', views.profile, name='profile'),

    path('edit-profile/', views.edit_profile, name='edit_profile'),

    path(
    'job-applicants/<int:job_id>/',
    views.job_applicants,
    name='job_applicants'
        ),
    
    path('edit-job/<int:job_id>/', views.edit_job, name='edit_job'),
    path('delete-job/<int:job_id>/', views.delete_job, name='delete_job'),

    path('save-job/<int:job_id>/', views.save_job, name='save_job'),
    path('saved-jobs/', views.saved_jobs, name='saved_jobs'),

    path(
    'update-application-status/<int:application_id>/',
    views.update_application_status,
    name='update_application_status'
        ),

    path(
    'candidate-profile/<int:user_id>/',
    views.candidate_profile,
    name='candidate_profile'
    ),

    path('my-posted-jobs/', views.my_posted_jobs, name='my_posted_jobs'),

    path(
    'toggle-save-job/<int:job_id>/',
    views.toggle_save_job,
    name='toggle_save_job'
),

    path(
    'export-applicants/<int:job_id>/',
    views.export_applicants_excel,
    name='export_applicants_excel'
),

path(
    'password-reset/',
    auth_views.PasswordResetView.as_view(
        template_name='password_reset.html'
    ),
    name='password_reset'
),

path(
    'password-reset/done/',
    auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'
    ),
    name='password_reset_done'
),

path(
    'reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'
    ),
    name='password_reset_confirm'
),

path(
    'reset/done/',
    auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'
    ),
    name='password_reset_complete'
),
]