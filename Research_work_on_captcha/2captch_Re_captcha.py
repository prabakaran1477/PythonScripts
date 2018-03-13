#!/usr/bin/python2

'''
    Project : "CaptchaAnalysis"
    Module Name: 2captch_Re_captcha.py
    Created Date: 2018-02-07
    Scope: To solve the graphic based captcha using 2captcha website .

    Version:V1: 2018-02-07
    Details:
'''

import requests
import re
import time
s=requests.session()


# RE-Captcha URL
url="http://www.siteworthtraffic.com/update-report/4stars.pl"
header={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0",
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Referer":"http://www.siteworthtraffic.com/report/4stars.pl"}
obj=s.get(url,headers=header)
con=obj.content

# Regex to get that re-captcha code
site_key=re.findall(r"<div\s*class=[\"\']g\s*\-\s*recaptcha[\"\']\s*data\s*\-\s*sitekey=[\"\']([^<]*?)[\"\']",con,re.I)[0]
# url1="http://2captcha.com/in.php?key=62973dd01dd77f4ea9043dffe6d6bc68&method=userrecaptcha&googlekey="+str(site_key)+"&pageurl=http://www.siteworthtraffic.com/update-report/4stars.pl&here=no"
url1="http://2captcha.com/in.php?key=033377c487886faacd5cc999fe0bc693&method=userrecaptcha&googlekey="+str(site_key)+"&pageurl=http://www.siteworthtraffic.com/update-report/4stars.pl&here=no"
obj=s.get(url1)
con=obj.content
print "con:",con
get_id=con.split('|')[1]
time.sleep(30)

#Loop execute twice to get the captcha from source
f=1
while f==1:
	url2="http://2captcha.com/res.php?key=62973dd01dd77f4ea9043dffe6d6bc68&action=get&id="+str(get_id)
	obj=requests.get(url2)
	con=obj.content
	if "CAPCHA_NOT_READY" not in con:
		f=2
	else:	
		time.sleep(10)
		continue

'''Id from 2captcha source is passed to the actual url through post content'''
res_id=con.split('|')[1]
post_con="g-recaptcha-response="+str(res_id)+"&update="
header={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Referer":url}
obj=s.post(url,data=post_con,headers=header)
con=obj.content
with open("sample3.html","w") as F:
	F.write(con)

	
	
	