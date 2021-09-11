from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer

#for /projects
class ProjectList(APIView):

    #for GET /projects
    def get(self, request):
        #get all the projects
        projects = Project.objects.all()
        #serialise all the projects
        serializer = ProjectSerializer(projects, many=True)
        # send all the serialized projects back in response body
        return Response(serializer.data)