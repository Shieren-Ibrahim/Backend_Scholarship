from django.shortcuts import render,redirect
from .models import *
from datetime import datetime,date,timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import time
import requests
from django.core.mail import send_mail
from django.conf import settings
import json
from django.forms.models import model_to_dict
from django.http import JsonResponse,HttpResponse
from django.core.files import File
import base64
from django.core.files.base import ContentFile
import random
import string
# Create your views here.

global arrived_request
id_code={}

# from sendsms import api
# from django.dispatch import receiver
# from phone_auth.signals import verify_phone
# from sms import send_sms
@csrf_exempt
def login(request):
	body_e=request.body.decode('utf-8')
	body=json.loads(body_e)
	passw=body['password']
	email=body['email']
	try:
		u=Student.objects.get(email=email,password=passw)
		ujs=model_to_dict(u)
		scholarships=Scholarship.objects.all().order_by('rating')
		scholarships_list=[]
		for i in scholarships:
			ss=model_to_dict(i)
			x=ss['img'].split('/')
			x=x[-1]
			ss['img']=x
			
			print(i)
			country_name=Country_Scholarship.objects.get(scholarship=i).country.name
			ss['country']=country_name

			university_name=University_Sch.objects.get(scholarship=i).university.name
			ss['university']=university_name
			scholarships_list.append(ss)
		return JsonResponse({'res':'ok','student':ujs,'scholarships':scholarships_list})
	except Exception as e:
		print(e)
		return JsonResponse({'res':'error'})

@csrf_exempt
def forgetten_password(request):
	decoded_body=request.body.decode('utf-8')
	body=json.loads(decoded_body)
	try:
		email=body['email']
		s=Student.objects.get(email=email).password
		# send_mail('Passowrd', Student.objects.get(email=email).password,settings.EMAIL_HOST_USER ,[email])
		return JsonResponse({'res':s})
	except Exception as e:
		print(e)
		return JsonResponse({'res':'error'})

@csrf_exempt
def signup(request):
	decoded_body=request.body.decode('utf-8')
	body=json.loads(decoded_body)
	global arrived_request
	arrived_request=body
	email=body['email']
	try:
		try:
			student=Student.objects.get(email=email)
			return JsonResponse({"st":'no','res':'exists email'})
		except:
			allowed_chars = ''.join((string.ascii_letters, string.digits))
			# code=''.join(random.choice(allowed_chars) for _ in range(4))
			code='1234'
			id_code[email]=code
			# api.send_sms(body='I can haz txt', from_phone='+963981555555', to=['+963994777777'])
			# send_mail('Verification', code,settings.EMAIL_HOST_USER ,[email],fail_silently=False)
			return JsonResponse({'st':'yes','res':'review_your_email'})
	except Exception as e:
		return JsonResponse({'res':'error'})

@csrf_exempt
def confirm(request):
	decoded_body=request.body.decode('utf-8')
	body=json.loads(decoded_body)
	try:
		my_code=body['code']
		email=body['email']
		if my_code!=id_code[email]:
			return JsonResponse({'res':'error_code'},safe=False)
		
		firstName=body['firstName']
		lastName=body['lastName']
		birthdate=body['birthdate']
		img=body['img']
		country=body['country']
		university=body['university']
		phone=body['phone']
		email=body['email']
		password=body['password']
		try:
			student=Student.objects.get(email=email)
			return JsonResponse({'result':'exists email'})
		except:
			user=Student(password=password,email=email,phone=phone,university=university,country=country,img=img,firstName=firstName,lastName=lastName,birthdate=birthdate)
			user.save()
			ujs=model_to_dict(user)
			scholarships=Scholarship.objects.all().order_by('rating')
			scholarships_list=[]
			for i in scholarships:
				ss=model_to_dict(i)
				x=ss['img'].split('/')
				x=x[-1]
				ss['img']=x
				print(i)
				country_name=Country_Scholarship.objects.get(scholarship=ss['id']).country.name
				ss['country']=country_name
				university_name=University_Sch.objects.get(scholarship=ss['id']).university.name
				ss['university']=university_name
				scholarships_list.append(ss)
			return JsonResponse({'res':'ok','student':ujs,'scholarships':scholarships_list})		
	except Exception as e:
		print(e)
		return JsonResponse({'res':'error'})

@csrf_exempt
def get_sholarships(request): 
	decoded_body=request.body.decode('utf-8')
	body=json.loads(decoded_body)
	try:
		scholarships=Scholarship.objects.all().order_by('rating')
		scholarships_list=[]
		for i in scholarships:
			ss=model_to_dict(i)
			x=ss['img'].split('/')
			x=x[-1]
			ss['img']=x
			country_name=Country_Scholarship.objects.get(scholarship=ss['id']).country.name
			ss['country']=country_name

			university_name=University_Sch.objects.get(scholarship=ss['id']).university.name
			ss['university']=university_name
			scholarships_list.append(ss)
		
		return JsonResponse({'res':'ok','scholarships':scholarships_list})
	except Exception as e:
		print(e)
		return JsonResponse({'res':'error'})

@csrf_exempt
def set_rating(request):
	decoded_body=request.body.decode('utf-8')
	body=json.loads(decoded_body)
	try:
		student_id=body['student_id']
		student=Student.objects.get(id=student_id)
		schoolar_id=body['schoolar_id']
		scholarship=Scholarship.objects.get(id=schoolar_id)
		i=body['i']
		rr=-1
		try:
			sr=Std_Rate.objects.get(student=student,scholarship=scholarship)
			Std_Rate.objects.get(id=sr.id).delete()
			rr=sr.rate
			r=Rate.objects.get(scholarship=scholarship)
			Rate.objects.get(id=r.id).delete()
			if rr==1:
				r.one=r.one-1
			elif rr==2:
				r.two=r.two-1
			elif rr==3:
				r.three=r.three-1
			elif rr==4:
				r.four=r.four-1
			else:
				r.five=r.five-1
			sr.rate=i
			
			sr.save()
			if i==1:
				r.one=r.one+1
			elif i==2:
				r.two=r.two+1
			elif i==3:
				r.three=r.three+1
			elif i==4:
				r.four=r.four+1
			else:
				r.five=r.five+1

			r.save()
			a=[]
			a.append(r.one)
			a.append(r.two)
			a.append(r.three)
			a.append(r.four)
			a.append(r.five)
			index=-1
			max_=-1
			k=0
			for j in a:
				k=k+1
				if j >=max_:
					index=k
					max_=j
			if max_>0:
				ss=Scholarship.objects.get(id=schoolar_id)
				country_=Country_Scholarship.objects.get(scholarship=ss['id'])
				univ_=University_Sch.objects.get(scholarship=ss['id'])
				Scholarship.objects.get(id=schoolar_id).delete()
				
				ss.rating=index
				ss.save()
				Country_Scholarship(country=country_.country,scholarship=ss).save()
				University_Sch(university=univ_.university,scholarship=ss).save()
				scholarship=Scholarship.objects.get(id=ss.id)
			scholarship=model_to_dict(scholarship)
			return JsonResponse({'res':'ok','scholarship':scholarship})

		except:
			sr=Std_Rate(student=student,scholarship=scholarship,rate=i)
			sr.save()
			try:
				r=Rate.objects.get(scholarship=scholarship)
				Rate.objects.get(id=r['id']).delete()
				if i==1:
					r.one=r.one+1
				elif i==2:
					r.two=r.two+1
				elif i==3:
					r.three=r.three+1
				elif i==4:
					r.four=r.four+1
				else:
					r.five=r.five+1
				r.save()
				a=[]
				a.append(r.one)
				a.append(r.two)
				a.append(r.three)
				a.append(r.four)
				a.append(r.five)
				index=-1
				max_=-1
				k=0
				for j in a:
					k=k+1
					if j >=max_:
						index=k
						max_=j
				if max_>0:
					ss=Scholarship.objects.get(id=schoolar_id)
					country_=Country_Scholarship.objects.get(scholarship=ss['id'])
					univ_=University_Sch.objects.get(scholarship=ss['id'])
					Scholarship.objects.get(id=schoolar_id).delete()
					ss.rating=index
					ss.save()
					Country_Scholarship(country=country_.country,scholarship=ss).save()
					University_Sch(university=univ_.university,scholarship=ss).save()
					scholarship=Scholarship.objects.get(id=ss.id)
				scholarship=model_to_dict(scholarship)
				return JsonResponse({'res':'ok','scholarship':scholarship})


			except:
				print('oooo4')
				if i==1:
					r=Rate(scholarship=scholarship,one=1,two=0,three=0,four=0,five=0)
				elif i==2:
					r=Rate(scholarship=scholarship,one=0,two=1,three=0,four=0,five=0)
				elif i==3:
					r=Rate(scholarship=scholarship,one=0,two=0,three=1,four=0,five=0)
				elif i==4:
					r=Rate(scholarship=scholarship,one=0,two=0,three=0,four=1,five=0)
				else:
					r=Rate(scholarship=scholarship,one=0,two=0,three=0,four=0,five=1)
				r.save()

				ss=Scholarship.objects.get(id=schoolar_id)
				country_=Country_Scholarship.objects.get(scholarship=ss)
				univ_=University_Sch.objects.get(scholarship=ss)
				Scholarship.objects.get(id=schoolar_id).delete()
				ss.rating=i
				ss.save()
				Country_Scholarship(country=country_.country,scholarship=ss).save()
				University_Sch(university=univ_.university,scholarship=ss).save()
				scholarship=Scholarship.objects.get(id=ss.id)

				scholarship=model_to_dict(scholarship)
				return JsonResponse({'res':'ok','scholarship':scholarship})
		scholarship=model_to_dict(scholarship)
		return JsonResponse({'res':'ok','scholarship':scholarship})
			
	except Exception as e:
		print(e)
		return JsonResponse({'res':'error'})

@csrf_exempt
def get_specialization(request):
	decoded_body=request.body.decode('utf-8')
	body=json.loads(decoded_body)
	try:
		spec=body['spec']
		scholarships=Scholarship.objects.filter(specialization=spec).order_by('rating')
		scholarships_list=[]
		for i in scholarships:
			ss=model_to_dict(i)
			x=ss['img'].split('/')
			x=x[-1]
			ss['img']=x
			country_name=Country_Scholarship.objects.get(scholarship=ss['id']).country.name
			ss['country']=country_name

			university_name=University_Sch.objects.get(scholarship=ss['id']).university.name
			ss['university']=university_name
			
			scholarships_list.append(ss)
		return JsonResponse({'res':'ok','scholarships':scholarships_list})
	except Exception as e:
		print(e)
		return JsonResponse({'res':'error'})
  
@csrf_exempt
def get_stage(request):
	decoded_body=request.body.decode('utf-8')
	body=json.loads(decoded_body)
	try:
		stage=body['stage']
		scholarships=Scholarship.objects.filter(stage=stage).order_by('rating')
		scholarships_list=[]
		for i in scholarships:
			ss=model_to_dict(i)
			x=ss['img'].split('/')
			x=x[-1]
			ss['img']=x
			country_name=Country_Scholarship.objects.get(scholarship=ss['id']).country.name
			ss['country']=country_name

			university_name=University_Sch.objects.get(scholarship=ss['id']).university.name
			ss['university']=university_name
			scholarships_list.append(ss)
		return JsonResponse({'res':'ok','scholarships':scholarships_list})
	except Exception as e:
		print(e)
		return JsonResponse({'res':'error'})

@csrf_exempt
def get_SchlarshipForCountry(request):
	decoded_body=request.body.decode('utf-8')
	body=json.loads(decoded_body)
	try:
		country=body['country']
		scholarships=Country_Scholarship.objects.filter(country=Country.objects.get(name=country))
		scholarships_list=[]
		for i in scholarships:
			ss=model_to_dict(i.scholarship)
			x=ss['img'].split('/')
			x=x[-1]
			ss['img']=x
			country_name=Country_Scholarship.objects.get(scholarship=ss['id']).country.name
			ss['country']=country_name

			university_name=University_Sch.objects.get(scholarship=ss['id']).university.name
			ss['university']=university_name
			scholarships_list.append(ss)
		
		return JsonResponse({'res':'ok','scholarships':scholarships_list})
	except Exception as e:
		print(e)
		return JsonResponse({'res':'error'})

@csrf_exempt
def get_SchlarshipForUniversity(request):
	decoded_body=request.body.decode('utf-8')
	body=json.loads(decoded_body)
	try:
		university=body['university']
		scholarships=University_Sch.objects.filter(university=University.objects.get(name=university))
		scholarships_list=[]
		for i in scholarships:
			ss=model_to_dict(i.scholarship)
			x=ss['img'].split('/')
			x=x[-1]
			ss['img']=x
			country_name=Country_Scholarship.objects.get(scholarship=ss['id']).country.name
			ss['country']=country_name

			university_name=University_Sch.objects.get(scholarship=ss['id']).university.name
			ss['university']=university_name
			scholarships_list.append(ss)
		
		return JsonResponse({'res':'ok','scholarships':scholarships_list})
	except Exception as e:
		print(e)
		return JsonResponse({'res':'error'})

@csrf_exempt
def get_free(request):
	body_e=request.body.decode('utf-8')
	body=json.loads(body_e)
	try:
		scholarships=Scholarship.objects.filter(cost=0).order_by('rating')
		scholarships_list=[]
		for i in scholarships:
			ss=model_to_dict(i)
			x=ss['img'].split('/')
			x=x[-1]
			ss['img']=x
			country_name=Country_Scholarship.objects.get(scholarship=ss['id']).country.name
			ss['country']=country_name

			university_name=University_Sch.objects.get(scholarship=ss['id']).university.name
			ss['university']=university_name
			scholarships_list.append(ss)
		
		return JsonResponse({'res':'ok','scholarships':scholarships_list})
	except Exception as e:
		print(e)
		return JsonResponse({'res':'error'})

@csrf_exempt
def get_university(request):
	body_e=request.body.decode('utf-8')
	body=json.loads(body_e)
	try:
		universities=University.objects.all()
		universities_list=[]
		for i in universities:
			ss=model_to_dict(i)
			x=ss['logo'].split('/')
			x=x[-1]
			ss['logo']=x
			ss['country']=model_to_dict(Country.objects.get(id=ss['country']))
			universities_list.append(ss)
		
		return JsonResponse({'res':'ok','university':universities_list})
	except Exception as e:
		print(e)
		return JsonResponse({'res':'error'})

@csrf_exempt
def submit_request(request):
	body_e=request.body.decode('utf-8')
	body=json.loads(body_e)
	try:
		student_id=body['student_id']
		schoolar_id=body['schoolar_id']
		degree=body['degree']
		# degree_data = ContentFile(base64.b64decode(degree), name='degree.docx')	
		identification=body['identification']
		passport=body['passport']
		money_transaction_num=body['money_transaction_num']
		scholarship=Scholarship.objects.get(id=schoolar_id)
		student=Student.objects.get(id=student_id)
		state=0
		try:
			Order.objects.get(scholarship=scholarship,student=student)
			return JsonResponse({'res':'exists'})
		except:
			o=Order(degree=degree,identification=identification,passport=passport,money_transaction_num=money_transaction_num,scholarship=scholarship,student=student,state=state)
			o.save()
			return JsonResponse({'res':'ok'})
	except Exception as e:
		print(e)
		return JsonResponse({'res':'error'})
  
@csrf_exempt
def get_orderAndNotification(request):
	body_e=request.body.decode('utf-8')
	body=json.loads(body_e)
	try:
		student_id=body['student_id']
		scholarships=Order.objects.filter(student=Student.objects.get(id=student_id))
		scholarships_list=[]
		for i in scholarships:
			a=model_to_dict(i)
			x=a['scholarship']
			a['scholarship']=model_to_dict(Scholarship.objects.get(id=x))
			a['scholarship']['img']=a['scholarship']['img'].split('/')[-1]
			
			country_name=Country_Scholarship.objects.get(scholarship=a['scholarship']['id']).country.name
			a['scholarship']['country']=country_name

			university_name=University_Sch.objects.get(scholarship=a['scholarship']['id']).university.name
			a['scholarship']['university']=university_name

			scholarships_list.append(a)
		return JsonResponse({'res':'ok','orders':scholarships_list})
	except Exception as e:
		print(e)
		return JsonResponse({'res':'error'})

@csrf_exempt
def cancel_order(request):
	decoded_body=request.body.decode('utf-8')
	body=json.loads(decoded_body)
	try:
		student_id=body['student_id']
		schoolar_id=body['schoolar_id']
		student=Student.objects.get(id=student_id)
		schoolar=Scholarship.objects.get(id=schoolar_id)
		Order.objects.get(scholarship=schoolar,student=student).delete()
		return JsonResponse({'res':'ok'})
	except Exception as e:
		print(e)
		return JsonResponse({'res':'error'})
  
@csrf_exempt
def getOrder(request):
	body_e=request.body.decode('utf-8')
	body=json.loads(body_e)
	try:
		student_id=body['student_id']
		scholarships_id=body['schoolar_id']
		o=Order.objects.filter(student=Student.objects.get(id=student_id),scholarship=Scholarship.objects.get(id=scholarships_id)).first()
		o=model_to_dict(o)
		return JsonResponse({'res':'ok','order':o})
	except Exception as e:
		print(e)
		return JsonResponse({'res':'error'})
      
@csrf_exempt
def UpdateOrder(request):
	body_e=request.body.decode('utf-8')
	body=json.loads(body_e)
	try:
		order_id=body['order_id']
		degree=body['degree']
		identification=body['identification']
		passport=body['passport']
		money_transaction_num=body['money_transaction_num']
		o=Order.objects.get(id=order_id)
		Order.objects.get(id=order_id).delete()
		o=Order(id=order_id,degree=degree,identification=identification,passport=passport,
		money_transaction_num=money_transaction_num,scholarship=o.scholarship,student=o.student,state=o.state)
		o.save()
		return JsonResponse({'res':'ok'})
	except Exception as e:
		print(e)
		return JsonResponse({'res':'error'})

@csrf_exempt
def UpdateProfile(request):
	body_e=request.body.decode('utf-8')
	body=json.loads(body_e)
	try:
		student_id=body['student_id']
		firstName=body['firstName']
		lastName=body['lastName']
		password=body['password']
		email=body['email']
		birthdate=body['birthdate']
		country=body['country']
		university=body['university']
		img=body['img']
		phone=body['phone']

		student=Student.objects.get(id=student_id)
		Student.objects.get(id=student_id).delete()
		student=Student(id=student_id,firstName=firstName,lastName=lastName,password=password,
		email=email,birthdate=birthdate,country=country,university=university,img=img,phone=phone)
		student.save()
		student=model_to_dict(student)
		return JsonResponse({'res':'ok','student':student})
	except Exception as e:
		print(e)
		return JsonResponse({'res':'error'})
	
@csrf_exempt
def contact_us(request):
	decoded_body=request.body.decode('utf-8')
	body=json.loads(decoded_body)
	try:
		email=body['email']
		fallName=body['fallName']
		msg=body['msg']
		c=Comment(fallName=fallName,email=email,msg=msg).save()
		# send_mail('Passowrd', Student.objects.get(email=email).password,settings.EMAIL_HOST_USER ,[email])
		return JsonResponse({'res':'ok'})
	except Exception as e:
		print(e)
		return JsonResponse({'res':'error'})

         
           





            

           


      