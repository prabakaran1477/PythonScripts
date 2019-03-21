print('Script Initiated')
file_name = 'D:/python_RnD/nlp_whatsapp/media.txt'
input_file = 'D:/python_RnD/nlp_whatsapp/input_file.txt'
word_count_filename = 'D:/python_RnD/nlp_whatsapp/word_count.csv'

'''
file_name = 'D:/python_RnD/nlp_whatsapp/my_school_group.txt'
input_file = 'D:/python_RnD/nlp_whatsapp/temp/input_file.txt'
word_count_filename = 'D:/python_RnD/nlp_whatsapp/temp/word_count.csv'
'''

print('Modules Loading...')
regex_3split = r'(\d+\/\d+\/\d+\,\s*\d+\:\d+\s*[\w]+)\s*\-\s*([\w\W]*?)\:([\w\W]*?)$'
import re
import pandas as pd
import numpy as np
from collections import Counter
print('Reading Input...')
f = open(file_name,'r', encoding="utf8").readlines()
list_data = []
for i in f:
    strings = re.findall(regex_3split, str(i),re.IGNORECASE)
    if strings:
        value = strings[0]
        templist = [value[0],value[1],value[2]]
        list_data.append(templist)
    # val = raw_input()
    # if val == 'break':
    #     break

print('Game with Pandas...')
'''converting multi dimensional list into pandas dataframe'''
MsgTable = pd.DataFrame.from_records(list_data,columns=['DateTime', 'Sender', 'Message'])
MsgTable.to_csv(input_file, index=False, header=False)

'''converting message frame into list'''
MsgList = MsgTable['Message'].tolist()
WordList = ' '.join(MsgList).lower().split()

'''Converting messing list into dataframe dict'''
df = pd.DataFrame.from_dict(dict(Counter(WordList)), orient='index').reset_index()
print(df)
input('mark1')
df.columns =['Word','Count']
print(df)
input('mark1')
'''Removing unwanted character'''
# df['Word'].replace(regex=True,inplace=True,to_replace=r'\d|\W|\?|http*',value=r'')
DropWords = ['','a','and','u','to','for','with','of','in','omitted','image','the','is']
df['Word'].replace(DropWords, np.nan, inplace=True)
df.dropna(subset=['Word'], inplace=True)

'''Sorting and saving the file'''
df.sort_values(by=['Count'],axis=0, ascending=False, inplace=True)
df.to_csv(word_count_filename, index=False, header=False)

Datetime_list = MsgTable['DateTime'].tolist()
df1 = pd.DataFrame.from_dict(dict(Counter(Datetime_list)), orient='index').reset_index()
df1.columns =['Time','Count']
df1['Time'].replace(regex=True,inplace=True,to_replace=r'\,\s*\d+\:\d+\s*[\w]+\s*',value=r'')
df1.dropna(subset=['Time'], inplace=True)
df1["Time"] = pd.to_datetime(df1["Time"])
df1.sort_values(by=['Count'],axis=0, ascending=False, inplace=True)
df1.to_csv('D:/python_RnD/nlp_whatsapp/Timing.csv', index=False, header=False)



'''
.replace(regex=True,inplace=True,to_replace=r'\d+\/\d+\/\d+',value=r'  * ')
df["DateTime"] = pd.to_datetime(df["DateTime"])
'''


MsgResponse = MsgTable['Sender']
labels = MsgTable['Sender'].unique()
print(labels)
response = pd.DataFrame(0,index=labels,columns=labels)
i =0
while (len(MsgResponse)==-1):
        if MsgResponse.iloc[i] != MsgResponse.iloc[i+1]:
            response.loc[MsgResponse.iloc[i+1],MsgResponse.iloc[i]] += 1
        i+=1
response.to_csv('D:/python_RnD/nlp_whatsapp/Response.csv', index=True, header=True)




