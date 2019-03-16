#from django.http import HttpResponse
from django.shortcuts import render
from ipython_genutils import text
import operator

def homepage(request):
    #the below line is to send the reponse as a text
    #return HttpResponse("This is the first page of the website")
    return render(request,'homepage.html')

def counting(request):
    text=request.GET['fulltext']
    #print(text)
    list1=text.split(" ")
    count={}
    for i in list1:
        if i in count.keys():
            count[i]=count[i]+1
        else:
            count[i]=1
    #print(count.items())
    sorteditems=sorted(count.items(),key=operator.itemgetter(1),reverse=True)
    print(sorteditems)
    return render(request,'count.html',{"text":text,"textlen":len(list1),"sorteddict":sorteditems})

def about(request):
    return render(request,'aboutus.html')
