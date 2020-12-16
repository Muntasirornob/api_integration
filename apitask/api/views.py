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

def submit_form(request):
	form=SubmitForm()
	cgpa=3.44
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

		#cgpa=info.float_cgpa()
		created=info.update_time_created()
		updated=info.update_time_updated()
		payload = {'tsync_id':info.tsync_id,'name':info.name,'email':info.email,'phone':info.phone,'full_address':info.full_address,'name_of_university':info.name_of_university,'graduation_year':info.graduation_year,'cgpa':cgpa,'experience_in_months':info.experience_in_months,'current_work_place_name':info.current_work_place_name,'applying_in':info.applying_in,'expected_salary':info.expected_salary,'field_buzz_reference':info.field_buzz_reference,'github_project_url':info.github_project_url,'cv_file':info.cv_file,'on_spot_update_time':updated,'on_spot_creation_time':created}
		print(payload)

		
		#if url_id:
			#request.session['url']
		print(json.dumps(payload))
		url = 'https://recruitment.fisdev.com/api/v1/recruiting-entities/'
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
        print(cv_id)
        file=Pdf.objects.last()
        files=file.pdf
        files_url=files.url
        print(files_url)   
        payload={}
        files1={'file':open(f'media/{files}','rb')}
        #files1=[('file',(f'{files}',open({files},'rb'),'application/pdf'))]
        #files1=[('file',(f'{files}',open(f'C:\Users\win 10\Desktop\apiproject\apitask\media\uploads\{files_url}','rb'),'application/pdf'))]
        url = f'https://recruitment.fisdev.com/api/file-object/{cv_id}/'
        print(url)
        headers={'Authorization': 'token be8796b9f6ca425c05a9a91aa4d29ef493d0553d'}
        response = requests.request("PUT", url, headers=headers, data=payload, files=files1)
        print(response.json())
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
			#https://recruitment.fisdev.com/api/file-object/{FILE_TOKEN_ID}/
			#https://recruitment.fisdev.com/api/file-object/{FILE_TOKEN_ID}/
#with open ("sample.pdf", "rb") as f:
   #pdf = pdf2.PdfFileReader(f)
#files1=[
  #('file',(f'{files}',open(f'{files_url}','rb'),'application/pdf'))
#]