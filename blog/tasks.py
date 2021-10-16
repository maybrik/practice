from celery import shared_task

from django.core.mail import send_mail

@shared_task
def sending_email(email, feedback_message):
    send_mail(email, feedback_message, ['admin@admin.com'])
