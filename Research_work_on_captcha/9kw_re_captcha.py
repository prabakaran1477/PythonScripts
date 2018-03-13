import requests
import re
import time

s=requests.session()
apikey = "86JWPWP"
url="http://www.siteworthtraffic.com/update-report/4stars.pl"
obj=s.get(url)
con=obj.content
with open("sample.html","w") as F:
	F.write(con)
site_key=re.findall(r"<div\s*class=[\"\']g\s*\-\s*recaptcha[\"\']\s*data\s*\-\s*sitekey=[\"\']([^<]*?)[\"\']",con,re.I)[0]
page_url="http://www.siteworthtraffic.com/update-report/4stars.pl&here=no"

captcha_get_id_url="https://www.9kw.eu/index.cgi?apikey="+str(apikey)+"&action=usercaptchaupload&interactive=1&file-upload-01="+str(site_key)+"&oldsource=recaptchav2&pageurl="+str(page_url)
obj=s.get(captcha_get_id_url)
captcha_id=obj.content
with open("sample1.html","w") as F:
	F.write(captcha_id)

# captcha_id=re.findall(r"([\d]+)",captcha_id_content,re.I)[0]
res_get_url="https://www.9kw.eu/index.cgi?apikey="+str(apikey)+"&action=usercaptchacorrectdata&id="+str(captcha_id)
header={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Referer":url}
f=1
while f==1:
	obj=requests.get(res_get_url)
	get_post_content=obj.content
	with open("sample2.html","w") as F:
		F.write(get_post_content)
	
	post_con=re.findall(r"([^<]+)",get_post_content,re.I)
	if post_con:
		res_id=post_con[0]
		print "Your captcha is solved"
		post_con1="g-recaptcha-response="+str(res_id)+"&update="
		print "post_con",post_con1
		header={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Referer":url}
		obj=s.post(url,data=post_con1,headers=header)
		final_content=obj.content
		with open("final_content.html","w") as F:
			F.write(final_content)
		
		f=2
	else:
		print "Not yet solve captcha so script going to sleep"
		time.sleep(10)
		continue

