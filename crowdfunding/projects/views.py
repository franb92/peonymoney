from django.shortcuts import render

# Create your views here.
from django.http import Http404
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

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class ProjectDetail(APIView):
    def get_object(self, pk):
        return Project.objects.get(pk=pk)
        
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

