import os
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer,ContactSerailizer
from django.core.mail import send_mail


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

    send_mail(
        f'{subject} from {name}({email})',
        message,
        "Avishek Das <os.environ.get('EMAIL_USER')>",
        [os.environ.get('RECEIVER_EMAIL')]
    )

    return Response({'message':f'Thank you {name} for contacting me! I will be back to you later.'},status=status.HTTP_201_CREATED)