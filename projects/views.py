from django.http import JsonResponse
from .models import Project

def project_list(request):
    projects = Project.objects.all()
    data = []
    for project in projects:
        data.append({
            "id": project.id,
            "name": project.name,
            "description": project.description,
            "status": project.status,
            "created_at": project.created_at.isoformat(),
            "owner_id": project.owner_id,
            "owner_name": project.owner.username,
        })
    return JsonResponse(data, safe=False)

def project_detail(request, project_id):
    try:
        project = Project.objects.values(
            "id", "name", "description", "status", "created_at"
        ).get(id=project_id)
    except Project.DoesNotExist:
        return JsonResponse({"detail": "Not found"}, status=404)
    return JsonResponse(project)

def project_detail(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return JsonResponse({"detail": "Not found"}, status=404)
    data = {
        "id": project.id,
        "name": project.name,
        "description": project.description,
        "status": project.status,
        "created_at": project.created_at.isoformat(),
        "owner_id": project.owner_id,
        "owner_name": project.owner.username,
    }
    return JsonResponse(data)

def health(request):
    return JsonResponse({"status": "ok"})
