#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    import pycurl
except:
    print "Please install python curl library!"
    exit(1)
import cStringIO

API_URL = "http://www.9kw.eu/index.cgi";

class captchaAPI():
	def __init__(self, apikey = None):
		self.apikey = apikey

	def usercaptchaupload(self, apikey, filename):
		buf = cStringIO.StringIO()

		c = pycurl.Curl()
		c.setopt(c.URL, API_URL);
        	c.setopt(c.POST, 1)
	        c.setopt(c.VERBOSE, 0)
	        c.setopt(c.HTTPPOST, [
			('file-upload-01', (c.FORM_FILE, filename)),
			('apikey', apikey),
			('source', 'pythonapi'),
			('action', 'usercaptchaupload')
		])
		c.setopt(c.WRITEFUNCTION, buf.write)
		c.perform()

		back = buf.getvalue()
		buf.close()
		return back

	def usercaptchacorrect(self, apikey, id, antwort):
		buf = cStringIO.StringIO()

		c = pycurl.Curl()
		c.setopt(c.URL, API_URL + "?action=usercaptchacorrect&source=pythonapi&apikey=" + apikey + "&id=" + id + "&antwort=" + antwort);
		c.setopt(c.WRITEFUNCTION, buf.write)
		c.perform()

		back = buf.getvalue()
		buf.close()
		return back

	def usercaptchacorrectdata(self, apikey, id):
		buf = cStringIO.StringIO()

		c = pycurl.Curl()
		c.setopt(c.URL, API_URL + "?action=usercaptchacorrectdata&source=pythonapi&apikey=" + apikey + "&id=" + id);
		c.setopt(c.WRITEFUNCTION, buf.write)
		c.perform()

		back = buf.getvalue()
		buf.close()
		return back

	def usercaptchacorrectback(self, apikey, id, correct):
		buf = cStringIO.StringIO()

		c = pycurl.Curl()
		c.setopt(c.URL, API_URL + "?action=usercaptchacorrectback&source=pythonapi&apikey=" + apikey + "&id=" + id + "&correct=" + correct);
		c.setopt(c.WRITEFUNCTION, buf.write)
		c.perform()

		back = buf.getvalue()
		buf.close()
		return back

	def usercaptchashow(self, apikey, id):
		buf = cStringIO.StringIO()

		c = pycurl.Curl()
		c.setopt(c.URL, API_URL + "?action=usercaptchashow&source=pythonapi&apikey=" + apikey + "&id=" + id);
		c.setopt(c.WRITEFUNCTION, buf.write)
		c.perform()

		back = buf.getvalue()
		buf.close()
		return back

	def usercaptchanew(self, apikey):
		buf = cStringIO.StringIO()

		c = pycurl.Curl()
		c.setopt(c.URL, API_URL + "?action=usercaptchanew&source=pythonapi&apikey=" + apikey);
		c.setopt(c.WRITEFUNCTION, buf.write)
		c.perform()

		back = buf.getvalue()
		buf.close()
		return back

	def guthaben(self, apikey):
		buf = cStringIO.StringIO()

		c = pycurl.Curl()
		c.setopt(c.URL, API_URL + "?action=usercaptchaguthaben&source=pythonapi&apikey=" + apikey);
		c.setopt(c.WRITEFUNCTION, buf.write)
		c.perform()

		back = buf.getvalue()
		buf.close()
		return back

def main():
    pass

    if __name__ == "__main__":
        main()