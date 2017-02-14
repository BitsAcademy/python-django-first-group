from django.shortcuts import render

from .models import Book
from .forms import StudentForm
from django.http import HttpResponse
# Create your views here.

def home(request):
	template_name = 'index.html'
	books = Book.objects.all()
	context = {'name':'Santosh', 'books': books}
	return render(request, template_name, context)

def student_rec(request):
	template_name = 'student_rec.html'
	context = {}
	return render(request, template_name, context)


def add_student(request):
	template_name = 'add_student.html'
	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('Thankyou')
	
	form = StudentForm()

	context = {'form': form}

	return render(request, template_name, context)

