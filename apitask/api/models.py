from django.db import models
from.fields import IntegerRangeField,FloatRangeField
from .formatChecker import ContentTypeRestrictedFileField
import jsonfield
import uuid

# Create your models here.
choices=(
        ('Mobile', 'Mobile'),
        ('Backend', 'Backend'),
    )
class Info(models.Model):
	tsync_id=models.CharField(max_length=55,blank=True)
	name=models.CharField(max_length=256)
	email=models.EmailField(max_length=256)
	phone=models.CharField(max_length=14)
	full_address=models.CharField(max_length=512,blank=True)
	name_of_university=models.CharField(max_length=256)
	graduation_year=IntegerRangeField(min_value=2015, max_value=2020)
	cgpa=FloatRangeField(min_value=2.0, max_value=4.0,blank=True,null=True)
	experience_in_months=IntegerRangeField(min_value=0, max_value=100,blank=True,null=True)
	current_work_place_name=models.CharField(max_length=256,blank=True)
	applying_in=models.CharField(max_length=10,choices=choices)
	expected_salary=IntegerRangeField(min_value=15000, max_value=60000)
	field_buzz_reference=models.CharField(max_length=256,blank=True)
	github_project_url=models.URLField(max_length=512)
	cv_file=jsonfield.JSONField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.name}"

	def update_time(self):
		create=self.created.timestamp()*1000
		created=str(int(create))
		update=self.updated.timestamp()*1000
		updated=str(int(update))
		return created,updated

	def update_time_created(self):
		create=self.created.timestamp()*1000
		created=int(create)
		return created
	def update_time_updated(self):
		update=self.created.timestamp()*1000
		updated=int(update)
		return updated
	#def float_cgpa(self):
		#cgp=self.cgpa
		#cgpa=float(cgp)
		#return cgpa


	def save(self,*args,**kwargs):
		if self.tsync_id=="":
			self.tsync_id=str(uuid.uuid4()).upper()[:12]
		if self.cv_file=={}:
			self.cv_file={'tsync_id':str(uuid.uuid4()).upper()[:12]}
		return super().save(*args,**kwargs)

class Pdf(models.Model):
    pdf = ContentTypeRestrictedFileField(upload_to='uploads/', content_types=['application/pdf' ],max_upload_size=4194304,blank=True, null=True)