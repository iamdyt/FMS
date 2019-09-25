from .models import Department

def getDepartments(request):
    dept = Department.objects.all()
    return {'dept':dept}