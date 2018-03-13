from twocaptchaapi import TwoCaptchaApi
import os
import base64
import requests
import re
import time
s=requests.session()
API_key="9e8138d9ba14dc"
# API_key="62973dd01dd7"
api = TwoCaptchaApi(API_key)

def base64_text_captcha(base64_url):
	try:
		current_working_dir=os.getcwd()
		base64_image=current_working_dir+"\\"+"sample.png"
		captcha_image = base64.b64decode(base64_url)
		with open(base64_image,"wb") as F:
			F.write(captcha_image)
		raw_input("ch")
		result=text_captcha(base64_image)
		os.remove(base64_image)
		return result
	except Exception as e:
		error="Error on captcha solving:"+str(e)
		return error
def text_captcha(image):
	try:	
		with open(image, 'rb') as captcha_file:
			captcha = api.solve(captcha_file)
		result=captcha.await_result()
		return result
	except Exception as e:
		error="Error on captcha solving:"+str(e)
		return "Error Occured"
def re_captcha(page_url,header):
	try:
		page_url_obj=s.get(page_url)
		page_url_content=page_url_obj.content
		# site_key=re.findall(r"<div\s*class=[\"\']g\s*\-\s*recaptcha[\"\']\s*data\s*\-\s*sitekey=[\"\']([^<]*?)[\"\']",page_url_content,re.I)[0]
		site_key=re.findall(r"data\s*\-\s*sitekey=[\"\']([^<]*?)[\"\']",page_url_content,re.I)[0]
		page_url_1=page_url+str("&here=no")
		captcha_url="http://2captcha.com/in.php?key="+str(API_key)+"&method=userrecaptcha&googlekey="+str(site_key)+"&pageurl="+str(page_url_1)
		captcha_url_obj=s.get(captcha_url)
		captcha_url_content=captcha_url_obj.content
		
		get_id=captcha_url_content.split('|')[1]
		
		time.sleep(20)
		f=1
		while f==1:
			response_captcha_url="http://2captcha.com/res.php?key="+str(API_key)+"&action=get&id="+str(get_id)
			response_captcha_obj=requests.get(response_captcha_url)
			response_captcha_content=response_captcha_obj.content
			with open("response_captcha_content.html","w") as F:
				F.write(response_captcha_content)
			if "CAPCHA_NOT_READY" not in response_captcha_content:
				f=2
			else:	
				time.sleep(10)
				continue
		captcha=response_captcha_content.split('|')[1]
		post_con="g-recaptcha-response="+str(captcha)+"&update="
		page_response_obj=s.post(page_url,data=post_con,headers=header)
		page_response_content=page_response_obj.content
		return page_response_content
	except Exception as e:
		error="Error on Recaptcha solving:"+str(e)
		return error
	

			
		
		
		
		

		
	