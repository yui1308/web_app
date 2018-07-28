from django.shortcuts import render
import requests
import bs4
import urllib
import urllib3
import random

# Create your views here.
def appmain(request):
	#data = {'sl':'en','tl':'it','text':'word'} 
	#q=urllib.parse.urlencode(data)
	#res=urllib3.PoolManager().request('https://translate.google.com/?hl=ja#en/ja/welcome','?',fields=q)
	#res=requests.get('https://translate.google.com/?hl=ja#en/ja/welcome'+'?',q)
	#soup=bs4.BeautifulSoup(res.text,"html5lib")
	#welcome=soup.select("#result_box")[0].getText()
	welcome="ようこそ"
	return render(request,'html/main.html',{'value':welcome})
	
def appBB(request):
	return render(request,'html/BEMYBABY.html',{})

def appSanrio (request):
	data=["hellokitty","mymelody","kikilala","cinnamon","pompompurin","gudetama","kuromi","keroppi","tuxedosam","badtzmaru"]
	
	link = 'https://www.sanrio.co.jp/character/'+random.choice(data)+'/'
	
	res = requests.get(link)
	
	soup = bs4.BeautifulSoup(res.text, "html5lib")

	title = soup.find_all("div",class_="profile")[0].getText()
	character = title.split()
	return render(request, 'html/sanrio.html', {'title':character[1],'bun':character[3], 'link':link })
