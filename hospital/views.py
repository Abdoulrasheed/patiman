from .forms import StudentAddForm
from .models import Student
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def homePage(request):
	return render(request, 'hospital/home.html', {})


@login_required
def addPatient(request):
	if request.method == "POST":
		form = StudentAddForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Successfully added')
			return redirect('add_patient')
		else:
			ctx = {"form": form}
			return render(request, 'hospital/add_patient.html', ctx)
	else:
		return render(request, 'hospital/add_patient.html', {})


def search(request):
	q = request.GET['q']
	print(q)
	ctx = Student.objects.filter(
		Q(idnumber__startswith=q) | 
		Q(firstname__startswith=q) | 
		Q(lastname__startswith=q)
	)
	return render(request, 'hospital/ajax/search_results.html', {"students": ctx})


def get_student_detail(request):
	student_id = request.GET['id']
	student = Student.objects.get(id=student_id)
	return render(request, 'hospital/ajax/student_detail.html', {"student": student})