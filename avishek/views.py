import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer,ContactSerailizer
from django.core.mail import send_mail
from django_q.tasks import async_task, schedule
from django_q.models import Schedule
from django.db.models import Q
from datetime import datetime, timedelta


@api_view(['GET'])
def get_all_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def contact_view(request):

    name=request.data['name']
    subject=request.data['subject']
    email=request.data['email']
    message=request.data['message']

    schedule('django.core.mail.send_mail',
            f'{subject} from {name}({email})',
            message,
            "Avishek Das",
            [os.environ.get('RECEIVER_EMAIL')],
            schedule_type=Schedule.ONCE,
            next_run=datetime.utcnow() + timedelta(minutes=1))
        
    return Response({'status':True,'message':f'Thank you {name} for contacting me! I will be back to you later.'},status=status.HTTP_201_CREATED)