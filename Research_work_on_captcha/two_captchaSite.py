#!/usr/bin/python2

'''
    Project : "CaptchaAnalysis"
    Module Name: Two_captcha.py
    Created Date: 2018-02-07
    Scope: To solve the text based captcha using 2captcha website .

    Version:V1: 2018-02-07
    Details:
'''

'''two captcha module features from github
   #https://github.com/athre0z/twocaptcha-api'''

from twocaptchaapi import TwoCaptchaApi

# API KEY is generated for the member of 2captcha website.
# api = TwoCaptchaApi('c32f3b1')
api = TwoCaptchaApi('03337')

#list of captcha images
list_image = ["captcha.png", "math.JPG"]


try:
    Balance= (api.get_balance())

    '''check balance in 2captcha source'''
    if float(Balance)==0.0:
        result='Empty'
        raise Exception("OperationFailedError: ERROR_ZERO_BALANCE")
    else:
        for image_1 in list_image:
            #sending the image file to source and solving it
            with open(image_1, 'rb') as captcha_file:
                captcha = api.solve(captcha_file)
            try:
                # Showing the Captcha solution
                result = captcha.await_result()
                print "result", result
                print "%s == %s" % (image_1, result)
                captcha.report_bad()
            except Exception as e:
                print "Error", str(e)
    
    
    print "Balance:", (api.get_balance())

except Exception as e:
    print "Error", str(e)
	
	




