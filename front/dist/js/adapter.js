var html=document.getElementsByTagName("html")[0];var width=window.innerWidth;if(width>1080){width=1080}else{if(width<320){width=320}}var fontSize=100/1080*width;html.style.fontSize=fontSize+"px";window.onresize=function(){var b=document.getElementsByTagName("html")[0];var c=window.innerWidth;if(c>1080){c=1080}else{if(c<320){c=320}}var a=100/1080*c;b.style.fontSize=a+"px"};