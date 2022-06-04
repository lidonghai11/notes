
	 
		 
			//更换背景
			setInterval("changebg()",300000);//1000为1秒钟
			
		
			
			function changebg()
			{
			
				var num=Math.round(Math.random()*18);			
				
				var bg_name='bg'+num+'.gif';
				
			
				//alert(arr[num]);
				//document.body.style.backgroundColor="#FFCC80";
				document.body.style.backgroundColor="black";
				document.body.style.backgroundImage="url("+"/static/"+bg_name+")";//当前ip下，工作目录开始
				
			}
			
			
			
			
		
			
			
			
			
			
			
			
			
			
			
			
 
