import logging

from django.core.mail import send_mail, mail_admins

from otus6.celery import app


@app.task
def send_email_task(name, email, message):
    subject = f'Hello, {name}'
    message = message

    try:
        # https://docs.djangoproject.com/en/3.0/ref/settings/#admins
        # https://docs.djangoproject.com/en/3.0/topics/email/#mail-admins
        mail_admins(
            subject=subject,
            message=message,
            fail_silently=False,
        )
        # https://docs.djangoproject.com/en/3.0/topics/email/#send-mail
        send_mail(
            subject=subject,
            message=message,
            from_email='noreply@otus-university.dev',
            recipient_list=[email],
            fail_silently=False,
        )
    except Exception as e:
        logging.exception(f"Raised exception params: {name}, {email}, {message}")
        logging.exception(e)
