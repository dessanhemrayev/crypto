from __future__ import unicode_literals
import codecs
alfawit="АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ_".lower()
key='Ю_ЦЗВ_'.lower()

kl=[]
for i in range(len(key)):
    for x in range(len(alfawit)):
        if key[i]==alfawit[x]:
            kl.append(x)

def fun(str1):
    
    i=0
    x=0
    lk=[]
    for i in range(len(str1)):
        for x in range(len(alfawit)):
            if str1[i]==alfawit[x]:
                lk.append(x)   
    return lk

def fun1(f,k):
    wer=''
    for w in f:
        for z in k:
            for s in range(32):
                if (s+z)%32==w:
                    wer+=alfawit[s]
                    break
    return wer

try:
    with codecs.open('slowa.txt', encoding='utf-8') as fin:
        line1 = next(fin)
        data=line1.split(' ')
        for line in data:
            print(fun1(kl,fun(line)))
except IOError:
    print("An IOError has occurred!")
