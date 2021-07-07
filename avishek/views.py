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

    if request.method == 'POST':
        serializer = ContactSerailizer(data=request.data)
        if serializer.is_valid():
            name=request.POST['name']
            subject=request.POST['subject']
            email=request.POST['email']
            message=request.POST['message']
    
            send_mail(
                f'{subject} from {name}({email})',
                message,
                email,
                [os.environ.get('RECEIVER_EMAIL')]
            )
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

