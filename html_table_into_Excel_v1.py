import requests
import time
import re
import xlwt
from twocaptchaapi import TwoCaptchaApi
from datetime import datetime
from dateutil.relativedelta import relativedelta



# sheet1.write(0, 0, "Date")



api = TwoCaptchaApi('18c788d0897708ea27a0207871f')
def Capcha_Convert(capcha_image):
    try:
        Balance = (api.get_balance())

        '''check balance in 2captcha source'''
        if float(Balance) == 0.0:
            result = 'Empty'
            raise Exception("OperationFailedError: ERROR_ZERO_BALANCE")
        else:
            with open(capcha_image, 'rb') as captcha_file:
                captcha = api.solve(captcha_file)
            try:
                result = captcha.await_result()
                print "result", result
                print "%s == %s" % (capcha_image, result)
                return result
            except Exception as e:
                print "Error", str(e)

        print "Balance:", (api.get_balance())
    except Exception as e:
        print "Error", str(e)


def re_findall(regex, content):
    data = re.findall(regex, content)
    return data

def clean(data):
    cleandata = re.sub('(<[^>]*?>)',' ',data)
    cleandata = cleandata.strip()
    return cleandata



def main():
    date_after_month = datetime.today() - relativedelta(months=3)

    # print date_after_month
    From_date = date_after_month.strftime('%d.%m.%Y')
    today = datetime.today()
    To_date = today.strftime('%d.%m.%Y')
    # From_date = today.strftime('%d.%m.%Y')
    # print "from ", From_date
    # print "Today :", To_date
    date_time = str(datetime.now().strftime("%d%m%Y_%H%M"))

    d = date_after_month.strftime('%d')
    m = date_after_month.strftime('%m')
    y = date_after_month.strftime('%Y')
    # print d
    # print m
    # print y

    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet("DataNode")
    style_string = "font: bold on;"
    style = xlwt.easyxf(style_string)

    s = requests.session()
    main_url = 'https://bsis.bsmou.org/public/?button=Agree'
    block_re = '<tr\s*class="[even|odd]*?"[\w\W]*?>([\w\W]*?)<\/tr>'
    id_re = 'value\=\"([^>]*?)"\/>'


    table_block_rx = r'(<table[^>]*?>[\w\W]*?<\/table>)'
    row_block_rx = r'(<tr[^>]*?>[\w\W]*?<\/tr>)'


    headers = {'Host': 'bsis.bsmou.org',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:56.0) Gecko/20100101 Firefox/56.0',
               'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.5',
               'Accept-Encoding': 'gzip, deflate, br',
               'Referer': 'https://bsis.bsmou.org/public/?button=Agree',
               'Connection': 'keep-alive'}
    s.headers.update(headers)
    main_url_response = s.get(main_url)
    detention_url = 'https://bsis.bsmou.org/public_det/?action=print&month=' + str(m) + '&year=' + str(y) + '&auth=0&held=0'
    detection_response = s.get(detention_url)
    detection_content = detection_response.content
    with open('detection_file.xls', 'wb') as f:
        f.write(detection_content)
    PHPSESSID = s.cookies.get('PHPSESSID')
    s.headers.update({'Cookie': 'PHPSESSID={}'.format(PHPSESSID)})
    captcha_url = 'https://bsis.bsmou.org/public/captcha.php'
    captcha_url_response = s.get(captcha_url)
    with open('main_page_1.png', 'wb') as f:
        f.write(captcha_url_response.content)
    time.sleep(5)
    captcha_text = raw_input('Enter the Captcha :')
    # captcha_text = Capcha_Convert('main_page_1.png')
    print('Extered txt:',captcha_text)
    time.sleep(5)
    captcha = captcha_text
    login_url = 'https://bsis.bsmou.org/public/?action=login'
    payload = 'captcha={}'.format(captcha)
    s.headers.update({'Content-Type': 'application/x-www-form-urlencoded','Content-Length': '13'})
    login_url_response = s.post(login_url, data=payload)
    # with open('test_v2.html', 'wb') as file:
    #     file.write(login_url_response.content)
    page = 0
    file_name = 'BlueSea_' + str(date_time) + '.xlsx'

    row_ultimate = 0
    row_inx_temp = []
    flag = 0
    while (page < 109):

        payload = "Page=" + str(
            page) + "&imo=&callsign=&name=&compimo=&compname=&From=" + str(From_date) + "&Till=" + str(
            To_date) + "&authority=0&flag=0&class=0&ro=0&type=0&result=0&insptype=-1&sort1=0&sort2=DESC&sort3=0&sort4=DESC"
        table_url = 'https://bsis.bsmou.org/public/?action=getinspections'
        table_blocks_response = s.post(table_url, data=payload)

        with open('table_V1.html', 'wb') as file:
            file.write(table_blocks_response.content)
        table_content = table_blocks_response.content
        blocks = re.findall(block_re, table_content)
        row_main =  0
        row_main =  row_ultimate + row_main

        row_index = 0
        for b,block in enumerate(blocks):
            # print 'block : ',block
            id = re.findall(id_re,block)
            if id:
                id = "UID="+id[0]
            id_url = 'https://bsis.bsmou.org/public/?action=getshipinsp'
            print "id :",b, id
            table_data_responce = s.post(id_url, data=id)

            table_data_cont = table_data_responce.content
            with open('inner_id_table.html','w') as f:
                f.write(table_data_cont)
            # table_data_cont = open('inner_id_table.html').read()  # For Internal Testing

            table_block = re_findall(table_block_rx,table_data_cont)
            col_index = 0

            col_index_header = 0
            col_index_val = 0

            # print 'col_index_header : ',col_index_header
            # print 'col_index_val : ',col_index_val
            TOTAL_TABLES_REQUIRED = 4
            for table_inx, table_data_block in enumerate(table_block):
                # print 'table:', table_inx, table_block
                try:
                    if table_inx <= TOTAL_TABLES_REQUIRED:
                        row_data_block = re_findall(row_block_rx, table_data_block)

                        row_index = row_index + row_main
                        for row_inx, row_data in enumerate(row_data_block):
                            # print 'row:', row_inx, row_data

                            if row_inx == 0:
                                if flag <= TOTAL_TABLES_REQUIRED:
                                    header_value = re_findall('<th[^>]*?>([\w\W]*?)</th>', row_data)  # Fetches header alone
                                    for index1, data in enumerate(header_value):
                                        index1 = index1 + col_index_header
                                        print 'row_index, index1 = Header Block => ', row_index, index1
                                        sheet1.write(row_index, index1, data,style=style)

                                    col_index_header = index1 + 1
                                    flag = flag + 1
                                    index1 = 0
                                    row_index = row_index + 1
                            else:

                                value = re_findall('(?:<td[^>]*?/>|<td\s*[^>]*?>([\w\W]*?)<\/td>)', row_data)
                                for inx, data in enumerate(value):
                                    inx = inx + col_index_val
                                    print 'row_index, inx = Data Block => ', row_index, inx
                                    data = clean(data)
                                    sheet1.write(row_index, inx, data)
                                row_index = row_index + 1


                        col_index_val = inx + 1
                        inx = 0
                        row_inx_temp.append(row_index)
                        row_index = 0
                        # print 'col_index_val == ', col_index_val
                        # print 'row_index     == ',row_index

                except Exception as e:
                    print 'Error:',e
            book.save(file_name)
            row_main = max(row_inx_temp) + 1
            row_inx_temp = []
            row_ultimate = row_main
            raw_input('raw_input')

if __name__ == '__main__':
    main()


