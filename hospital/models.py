from django.db import models

class Student(models.Model):
	idnumber 	= models.CharField(max_length=15, unique=True)
	firstname 	= models.CharField(max_length=50)
	lastname 	= models.CharField(max_length=50)
	othername 	= models.CharField(max_length=50)
	address 	= models.CharField(max_length=50)
	sickness 	= models.CharField(max_length=50)
	school 		= models.CharField(max_length=50)
	department 	= models.CharField(max_length=50)
	level 		= models.CharField(max_length=5)
	hall 		= models.CharField(max_length=50)
	phone 		= models.CharField(max_length=50)
	dob 		= models.DateTimeField()

	def __str__(self):
		return self.idnumber

	def get_fullname(self):
		return f'{self.firstname} {self.lastname} {self.othername}'