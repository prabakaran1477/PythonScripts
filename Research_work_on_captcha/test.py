#!/usr/bin/env python

import time
import pycurl
import cStringIO
from captchaapi import captchaAPI

apikey = "86JWPWP9";

eu = captchaAPI()

#
# Guthaben
#
print "Guthaben: " + eu.guthaben(apikey)

#
# Neues Captcha holen
#
CaptchaID = eu.usercaptchanew(apikey);
print "Neues Captcha: "+CaptchaID;#INT oder NO CAPTCHA

#
# Neues Captcha anzeigen
#
Bild = eu.usercaptchashow(apikey,CaptchaID);#Binary

if(CaptchaID != 'NO CAPTCHA' and Bild):
	fileObj = open("testbild.png","w")
	fileObj.write(Bild)
	fileObj.close()

	#
	# Captcha antwort senden
	#
	antwort = '2C888V';
	eu.usercaptchacorrect(apikey,CaptchaID,antwort);#String
else:
	print "Kein neues Captcha";

#
# Captcha einreichen
#
NewCaptchaID = eu.usercaptchaupload(apikey,'sample.png');#INT
print "NewCaptchaID: "+NewCaptchaID;

#
# Captcha daten holen
#
wait = 10;
time.sleep(wait)
for i in range(wait, 100, 1): 
	ergebnis = eu.usercaptchacorrectdata(apikey,NewCaptchaID);#String
	print "Ergebnis: "+ergebnis;

	if(ergebnis != ""):
		if(ergebnis == '2C888V'):
			#
			# Captcha richtig
			#
			eu.usercaptchacorrectback(apikey,NewCaptchaID,"1");#String = OK
		else:
			#
			# Captcha falsch
			#
			eu.usercaptchacorrectback(apikey,NewCaptchaID,"2");#String = OK
		break

	time.sleep(3)
