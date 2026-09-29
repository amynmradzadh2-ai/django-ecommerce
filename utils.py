from django.core.mail import send_mail
from django.conf import settings


def send_email_code(email, code):
    send_mail(
        subject='کد تأیید ثبت‌نام|Game Shop  ',
        message=f'''
سلام

کد تأیید شما:

{code}

این کد برای تأیید حساب شماست.
        ''',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )