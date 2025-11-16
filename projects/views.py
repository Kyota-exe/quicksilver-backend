from django.http import JsonResponse
from .models import Project

def project_list(request):
    projects = Project.objects.all().values("id", "name", "status", "created_at")
    return JsonResponse(list(projects), safe=False)

def project_detail(request, project_id):
    try:
        project = Project.objects.values(
            "id", "name", "description", "status", "created_at"
        ).get(id=project_id)
    except Project.DoesNotExist:
        return JsonResponse({"detail": "Not found"}, status=404)
    return JsonResponse(project)
