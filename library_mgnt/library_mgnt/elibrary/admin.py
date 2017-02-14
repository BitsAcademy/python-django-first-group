from django.contrib import admin
from .models import Book, Student, BookRecord

# Register your models here.

class BookAdmin(admin.ModelAdmin):
	list_display = ['name', 'author', 'publication', 'page','published', 'category']
	list_filter = ['author', 'published', 'category']
	search_fields = ['author', 'name']
	list_per_page = 1
	#fields = ['name', 'author', 'publication', 'category']
	exclude = ['page']


class StudentAdmin(admin.ModelAdmin):
	list_display = ['user','faculty', 'batch','contact_no']
	list_filter = ['batch', 'faculty']
	search_fields = ['user', 'contact_no']
	list_editable = ['contact_no']
	list_display_links = ['user', 'faculty', 'batch']

class BookRecordAdmin(admin.ModelAdmin):
	list_display = ['name', 'issued_date', 'return_date', 'returned']
	list_editable =  ['returned']

admin.site.register(Book, BookAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(BookRecord, BookRecordAdmin)