from django.shortcuts import render
import requests
import bs4
import urllib
import urllib3
import random
import tkinter
from PIL import ImageTk,Image
from django.templatetags.static import static
import threading
import os.path

X=1
Y=0
Water=False

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

def appJoke(request):
	x=random.randint(1,3)
	if x==1:
		return render(request,'html/baobab.html',{})
	elif x==2:
		return render(request,'html/mikiprune.html',{})
	elif x==3:
		return render(request,'html/frog.html',{})
	



def appSanrio (request):
	data=["hellokitty","mymelody","kikilala","cinnamon","pompompurin","gudetama","kuromi","keroppi","tuxedosam","badtzmaru"]
	
	link = 'https://www.sanrio.co.jp/character/'+random.choice(data)+'/'
	
	res = requests.get(link)
	
	soup = bs4.BeautifulSoup(res.text, "html5lib")

	title = soup.find_all("div",class_="profile")[0].getText()
	character = title.split()
	return render(request, 'html/sanrio.html', {'title':character[1],'bun':character[3], 'link':link })


def appMAZE(request):
	t=threading.Thread(target=mainMaze,daemon=True)
	t.start()
	return render(request,'html/maze.html',{})
	
def mainMaze():
	root=tkinter.Tk()
	root.title("maze:葉っぱにお水を")
	root.minsize(840,454)
	root.option_add("*font",["メイリオ",14])
	
	canvas=tkinter.Canvas(width=620,height=434)
	canvas.place(x=10,y=10)
	canvas.create_rectangle(0,0,620,434,fill="gray",tag="drawfield")
	
	
	def draw():
		for y in range(0,7):
			for x in range(0,10):
				p=map_data[y][x]
				canvas.create_image(x*62+31,y*62+31,image=images[p])
		canvas.create_image(X*62+31,Y*62+31,image=images[4],tag="chara")
	
	def end():
		canvas.delete("all")
		canvas.create_rectangle(0,0,620,434,fill="black")
		canvas.create_text(300,200,text="ククノチは今日も葉っぱに”水”をあげた\nこの葉っぱがミキプルーンになるのはまた別のお話...",
		fill="white",font=("MS ゴシック",15))
		Bup["state"]="disabled"
		Bdown["state"]="disabled"
		Bleft["state"]="disabled"
		Bright["state"]="disabled"
	
	def cheak(x,y):
		global X,Y,Water
		if x>=0 and x<10 and y>=0 and y<7:
			if map_data[y][x]==1:
				return
			elif map_data[y][x]==2:
				if Water==True:
					end()
				else:
					return
			elif map_data[y][x]==3:
				Water=True
				map_data[y][x]=0
				canvas.delete("all")
				draw()
			
			X=x
			Y=y
			canvas.coords("chara",X*62+31,Y*62+31)
	
	
	def click_Bup():
		cheak(X,Y-1)
	
	def click_Bdown():
		cheak(X,Y+1)
		
	def click_Bleft():
		cheak(X-1,Y)
		
	def click_Bright():
		cheak(X+1,Y)
	
	
	
	Bup=tkinter.Button(text="↑")
	Bup.place(x=720,y=150)
	Bup["command"]=click_Bup
	Bdown=tkinter.Button(text="↓")
	Bdown.place(x=720,y=210)
	Bdown["command"]=click_Bdown
	Bleft=tkinter.Button(text="←")
	Bleft.place(x=660,y=180)
	Bleft["command"]=click_Bleft
	Bright=tkinter.Button(text="→")
	Bright.place(x=780,y=180)
	Bright["command"]=click_Bright
	
	BASE=os.path.dirname(os.path.abspath(__file__))
	data0=os.path.join(BASE,"static/img/way0.png")
	data1=os.path.join(BASE,"static/img/rock1.png")
	data2=os.path.join(BASE,"static/img/goal2.png")
	data3=os.path.join(BASE,"static/img/key3.png")
	data4=os.path.join(BASE,"static/img/kukunoti4.png")
	
	#url0=static("img/way0.png")
	#url1=static("img/rock1.png")
	#url2=static("img/goal2.png")
	#url3=static("img/key3.png")
	#url4=static("img/kukunoti4.png")
	
	images=[tkinter.PhotoImage(file=data0),
			tkinter.PhotoImage(file=data1),
			tkinter.PhotoImage(file=data2),
			tkinter.PhotoImage(file=data3),
			tkinter.PhotoImage(file=data4)]
		
	
	map_data=[[1,0,1,1,1,1,1,1,1,1],
			[1,0,0,0,0,1,0,1,3,1],
			[1,0,1,1,0,1,0,1,0,1],
			[1,0,1,2,0,0,0,1,0,1],
			[1,0,1,1,1,1,1,1,0,1],
			[1,0,0,0,0,0,0,0,0,1],
			[1,1,1,1,1,1,1,1,1,1]
			]
	
	draw()
	root.mainloop()
	