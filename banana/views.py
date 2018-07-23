from django.shortcuts import render
from django.utils import timezone
from .models import Post
import requests   # Web からデータを取ってくる時に使う
import bs4        # スクレイピング
import random

# Create your views here.
def appmain (request):
	data=["hellokitty","mymelody","kikilala","cinnamon","pompompurin","gudetama","kuromi","keroppi","tuxedosam","badtzmaru"]
	
	link = 'https://www.sanrio.co.jp/character/'+random.choice(data)+'/'
	
	res = requests.get(link)
	
	# 「おまかせ表示」に現われたページをスクレイピング
	soup = bs4.BeautifulSoup(res.text, "html5lib")

	# この Wiki エントリのタイトルの文字列を変数 title に代入
	title = soup.find_all("div",class_="profile")[0].getText()
	character = title.split()
	return render(request, 'sanrio.html', {'title':character[1],'bun':character[3], 'link':link })