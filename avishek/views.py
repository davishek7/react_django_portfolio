from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Project, Contact
from .serializers import ProjectSerializer


@api_view(['GET'])
def get_all_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def contact_view(request):

    try:
        contact = Contact()
        contact.name = request.data['name']
        contact.subject = request.data['subject']
        contact.email = request.data['email']
        contact.message = request.data['message']
        contact.save()

        return Response({'status': True, 'message': f'Thank you {contact.name} for contacting me! I will be back to you as soon as possible.'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'status': False, 'message': 'Something went wrong! Please try again later.'}, status=status.HTTP_400_BAD_REQUEST)
