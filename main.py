
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import pyperclip

df1 = pd.read_excel('Rtr.xlsx')

name=df1['name']
namelist=[]
for i in name:
    namelist.append(i)
time=df1['time']
timelist=[]
for j in time:
    timelist.append(j)
ph=df1['phone']
phonelist=[]
for j in ph:
    phonelist.append(j)

flag=1
i=0
while(flag!=0):
    inp=input()
    if(inp=='c'):
        print(namelist[i])
    elif(inp=='n'):
        i+=1
        jrname = namelist[i]
        jrtime = timelist[i]
        print(jrname)
    elif(inp=='p'):
        i=0 if i==0 else i-1
        jrname = namelist[i]
        jrtime = timelist[i]
        print(jrname)
    elif(inp=='f'):
        flag=0
    elif(inp=='1'):
        pyperclip.copy('wa.me/+91'+str(phonelist[i]))
    elif(inp=='m'):
        pyperclip.copy('Greetings, '+namelist[i]+'!\n\nThe time to move on from *"can I"* to *"I can"* is here!✨\n\n*The Rotaract Club of SRM Easwari Engineering College* is pleased that you have taken a step towards becoming a part of this team as a Junior Office-Bearer 🤗. We are glad to bring to your knowledge that the audition is set to take place online.📢\n\n*It is little keys that open up big doors*. This is your opportunity to show us what you have got to become an office-bearer in the Rotaract Club of SRM Easwari Engineering College ❤️.\n\nDate:🗓  19th June.\nTime: 🕠' + timelist[i]+'PM')
    
