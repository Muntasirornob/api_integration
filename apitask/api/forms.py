from django.forms import ModelForm
from.models import Info
from.models import Pdf 
class SubmitForm(ModelForm):
	class Meta:
		model=Info 
		fields=('name','email','phone','full_address','name_of_university','graduation_year','cgpa','experience_in_months','current_work_place_name','applying_in','expected_salary','field_buzz_reference','github_project_url')
class PdfsubmitForm(ModelForm):
	class Meta:
		model=Pdf
		fields='__all__'

		