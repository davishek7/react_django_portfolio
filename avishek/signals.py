import os
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contact
from django_q.tasks import schedule
from django_q.models import Schedule
from datetime import datetime, timedelta


SENDER_EMAIL = "Avishek Das <noreply@avishekdas.herokuapp.com>"


@receiver(post_save, sender=Contact)
def send_mail_to_both(sender, instance, created, **kwargs):

    schedule('django.core.mail.send_mail',
             f'{instance.subject} from {instance.name}({instance.email})',
             instance.message,
             SENDER_EMAIL,
             [os.environ.get('RECEIVER_MAIL')],
             schedule_type=Schedule.ONCE,
             next_run=datetime.utcnow() + timedelta(seconds=10))

    schedule('django.core.mail.send_mail',
             'New mail from Avishek Das',
             f'Thank you {instance.name} for contacting me, I will be back to you as soon as possible.',
             SENDER_EMAIL,
             [instance.email],
             schedule_type=Schedule.ONCE,
             next_run=datetime.utcnow() + timedelta(seconds=10))
