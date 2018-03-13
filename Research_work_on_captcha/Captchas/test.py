# from captcha_solve import text_captcha
import captcha_solve
import requests
import re



url="https://bsis.bsmou.org/public/?button=Agree"
obj=requests.get(url)
con=obj.content
with open("test.html","w") as F:
	F.write(con)
url="https://bsis.bsmou.org/public/captcha.php"
obj=requests.get(url)
con=obj.content
with open("test.png","wb") as F:
	F.write(con)
print text_captcha("test.png")

#Recaptcha

url="http://www.siteworthtraffic.com/update-report/4stars.pl"
header={"Content-Type":"application/x-www-form-urlencoded","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Referer":url}
t1=captcha_solve.re_captcha(url,header)
with open("final_sample.html","w") as F:
	F.write(t1)


