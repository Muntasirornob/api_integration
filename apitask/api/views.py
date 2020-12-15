import requests
import json
from django.shortcuts import render
from.forms import SubmitForm
from.forms import PdfsubmitForm
from django.contrib import messages
from.models import Info,Pdf
# Create your views here.
def collect_token(request):
	url='https://recruitment.fisdev.com/api/login/'
	payload={'username':'muntasirornob@gmail.com','password':'f1KyVhf87'}
	r=requests.post(url,data=payload).json()

	token_code={
		'token':r['token'],
	}
	if token_code:
		request.session['token']=token_code
		print(token_code.get("token"))
	context={
		'token_code':token_code
	}
	return render(request,'api/apitoken.html',context)

def submitForm(request):
	form=SubmitForm()
	if request.method=='POST':
		form=SubmitForm(request.POST)
		if form.is_valid():
			form.save()
		else:
			print('haha')
		token_code=request.session['token']
		token_id=token_code.get("token")
		print(token_id)
		info=Info.objects.last()
		cgpa=info.float_cgpa()
		created=info.update_time_created()
		updated=info.update_time_updated()
		payload = {'tsync_id':info.tsync_id,'name':info.name,'email':info.email,'phone':info.phone,'full_address':info.full_address,'name_of_university':info.name_of_university,'graduation_year':info.graduation_year,'cgpa':cgpa,'experience_in_months':info.experience_in_months,'current_work_place_name':info.current_work_place_name,'applying_in':info.applying_in,'expected_salary':info.expected_salary,'field_buzz_reference':info.field_buzz_reference,'github_project_url':info.github_project_url,'cv_file':info.cv_file,'on_spot_update_time':updated,'on_spot_creation_time':created}
		print(payload)

		
		#if url_id:
			#request.session['url']
		print(json.dumps(payload))
		url = 'https://recruitment.fisdev.com/api/v0/recruiting-entities/'
		headers={'Authorization': f'token {token_id}'}
		response = requests.post(url, json= payload,headers=headers)
		x=response.json()
		file_id={
			'cv_id':x['cv_file']['id'],
		}
		if file_id:
			request.session['cv_id']=file_id
			print(file_id)
		print (response.json())
	form=SubmitForm()
	context={'form':form}
	return render(request,'api/form.html',context)

def upload_file(request):
    if request.method == 'POST':
        form = PdfsubmitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        file_id=request.session['cv_id']
        cv_id=file_id.get("cv_id")
        file=Pdf.objects.last()
        files=file.pdf 
        print(files)   
        url = 'https://recruitment.fisdev.com/api/v0/recruiting-entities/'
        headers={'Authorization': 'token be8796b9f6ca425c05a9a91aa4d29ef493d0553d'}
        response = requests.post(url,headers=headers,files=files)
    else:
        form =PdfsubmitForm()
    return render(request, 'api/uploadfile.html', {'form': form})

#def cvUpload(request):
	#form=PdfsubmitForm()
	#if request.method=='POST':
		#form=SubmitForm(request.POST)
		#if form.is_valid():
			#form.save()
		#else:
			#print('haha')