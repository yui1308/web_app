//jQuery.noConflict();

$(function(){
	$('#main').css('display','none');
	$('#load-background').css('display','block');
	$('#load-main').css('display','block');
	$('#welcome').fadeOut(100);
	$('#BB').fadeOut(100);
	$('#Sanrio').fadeOut(100);
	$('#JOKE').fadeOut(100);
	$('#MAZE').fadeOut(100);
});


$(window).load(function(){
	$('#load-main').delay(1000).fadeOut(3000);
	$('#load-background').delay(2000).fadeOut(4000);
	$('#main').css('display','block');
	$('#welcome').delay(4000).fadeIn(3000);
	setTimeout(RandomText,8000,0);
	RAnimation(7);
});


$(function(){
	var element = document.querySelector('#load-main');
	LoadText1(1,element);
});

function LoadText1(s,e){
	$('#Ltext'+s).fadeOut(600);
	$('#Ltext'+s).fadeIn(600);
	var style = window.getComputedStyle(e);
	var value = style.getPropertyValue('display');
	if(value=='none'){
		
	}else if(s>=10){
		setTimeout(LoadText1,1000,1,e);
	}else{
		setTimeout(LoadText1,300,s+1,e);
	}
}

/*function Welcome(){
	var welcome = document.getElementById('welcome');
	welcome.innerHTML='<h1>ようこそ</h1>';
	//$('#welcome').delay(2000).fadeOut(1000);
}*/

function RandomText(count){
	var welcome = document.getElementById('welcome');
	var a=['#','$','%','&','\\','*','?','@'];
	
	count=count+1;
	if(count>20){
		setTimeout(Welcome,50);
	}else{
		welcome.innerHTML='<h1>'+a[Math.floor(Math.random()*8)]+
		a[Math.floor(Math.random()*8)]+
		a[Math.floor(Math.random()*8)]+
		a[Math.floor(Math.random()*8)]+
		a[Math.floor(Math.random()*8)]+'</h1>';
		setTimeout(RandomText,25,count);
	}
}



function RAnimation(count){
	if(count>=0){
		if(count!=0){
			$('#mback'+count).css('background-color','#338899');
		}else{
			$('#main').css('background-color','#338899');
		}
		if(count!=7){
			var s;
			s=count+1;
			$('#mback'+s).css('background-color','#000000');
		}
		count=count-1;
		setTimeout(RAnimation,39,count);
	}else{
		$('#main').css('background-color','#000000');
		setTimeout(RAnimation,2000,7);
	}
}





