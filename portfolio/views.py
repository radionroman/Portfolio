from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Project, Screenshots
from django.shortcuts import get_object_or_404

def index(request):
    projects_list = Project.objects.order_by("name")[:5]
    screenshots_list = Screenshots.objects.order_by("id")[:]
    template = loader.get_template("portfolio/index.html")
    context = {
        "projects_list": projects_list,
        "screenshots_list": screenshots_list,
    }
    return HttpResponse(template.render(context, request))

def details(request, project_name):
    project_object = get_object_or_404(Project, name=project_name)
    template = loader.get_template("portfolio/project_details.html")
    context = {
        "project_name": project_name,
        "project_object": project_object,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
