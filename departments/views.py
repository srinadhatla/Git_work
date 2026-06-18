from django.shortcuts import render, redirect, get_object_or_404
from .models import Department


def department_list(request):
    search = request.GET.get('search')

    if search:
        departments = Department.objects.filter(name__icontains=search)
    else:
        departments = Department.objects.all()

    return render(request, 'departments/list.html',
                  {'departments': departments})


def add_department(request):
    if request.method == "POST":
        Department.objects.create(
            name=request.POST['name'],
            description=request.POST['description']
        )
        return redirect('department_list')

    return render(request, 'departments/add.html')


def update_department(request, id):
    department = get_object_or_404(Department, id=id)

    if request.method == "POST":
        department.name = request.POST['name']
        department.description = request.POST['description']
        department.save()
        return redirect('department_list')

    return render(request, 'departments/update.html',
                  {'department': department})


def delete_department(request, id):
    department = get_object_or_404(Department, id=id)
    department.delete()

    return redirect('department_list')