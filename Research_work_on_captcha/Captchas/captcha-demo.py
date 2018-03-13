from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
from captcha_solve import text_captcha
from selenium.webdriver.chrome.options import Options
import requests
import re
import xlsxwriter


chrome_options = Options()
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("log-level=3")

files_path = [(x, os.path._getfullpathname(r'Images\\'+x)) for x in os.listdir('Images')]
driver = webdriver.Chrome(chrome_options=chrome_options)
print('\n\t\t\t\t{}'.format('Captcha Demo'))
print('\t\t\t\t{}'.format('____________\n'))

print('{0: <20}'.format('Captcha')+'{0: <20}'.format('Api\'s Response')+'{0: <20}'.format('Time Taken')+'{0:<20}'.format('Result'))
print('{0: <20}'.format('-------')+'{0: <20}'.format('---------------')+'{0: <20}'.format('----------')+'{0:<20}'.format('------'))
total_time_taken=list()
accuracy=list()

for file in files_path:
    driver.get(file[1])
    start_time = time.time()
    output = text_captcha(file[1])
    time_taken = time.time()-start_time
    captcha = file[0].split('.')[0]
    if captcha == output:
        result = 'Success - Correct Case'
        accuracy.append(1)
    elif captcha.lower()==output.lower():
        result = 'Success - Lower Case'
        accuracy.append(1)
    else:
        result = 'Failed'
        accuracy.append(0)
    print('{0: <20}'.format(captcha)+'{0: <20}'.format(output)+'{0: <20}'.format(str(int(time_taken))+' sec')+'{0:<20}'.format(result))
    total_time_taken.append(time_taken)
    time.sleep(2)
    # break
driver.close()

print("\n")
print("Avg. captcha solving time  :  {} seconds".format(int(sum(total_time_taken)/len(total_time_taken))))
print("Accuracy %                 :  {} %".format((sum(accuracy)/len(accuracy))*100))


# workbook = xlsxwriter.Workbook('Captcha_report.xlsx')
# worksheet = workbook.add_worksheet(fileName)
# headerFormat = workbook.add_format({'bold': True, 'font_color': '#ffffff', 'bg_color':'#f4b342', 'border' : True, 'font_size':'10.5', 'align': 'center', 'valign': 'vcenter'})
# cellFormat = workbook.add_format({'border':True, 'font_size':'10.5'})
# worksheet.set_column(0, 20, 25)
# worksheet.freeze_panes(1, 0)
# worksheet.hide_gridlines(2)

# Writing headers to excel
# headers=['Actual Captcha Values', 'Api\'s response', 'Time Taken', 'Result']
# for col, item in enumerate(headers):
    # worksheet.write(0, col, item, headerFormat)
# row=1

# Writing headers to excel
# headers=['Actual Captcha Values', 'Api\'s response', 'Time Taken', 'Result']
# for col, item in enumerate(headers):
    # worksheet.write(0, col, item, headerFormat)
# row=1

# Writing data to excel
# for row_data in result_set
    # for col, item in enumerate(row_data):
        # worksheet.write(row, col, item, headerFormat)
    # row+=1


# workbook.close()