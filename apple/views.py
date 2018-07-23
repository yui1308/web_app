from django.shortcuts import render
import requests
import bs4
import urllib
import urllib3

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
