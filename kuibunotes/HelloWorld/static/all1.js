
		 	//清空输入框
			document.getElementById("input1").onfocus=function(){
				document.getElementById("input1").value='';
			}
		 
		 
		 
			//更换背景
			setInterval("changebg()",5000);//1000为1秒钟
			
			var arr=["印度斋普省贾玛哈尔美丽的日出景象。我想把宫殿与其他两座建筑都纳入画面，这也是为什么我用超广角镜头拍摄这张照片。清晨遊客不多，所以早晨这里都比较宁静。","虎鲸（学名：Orcinus orca）是一种大型齿鲸，身长为8～10米，体重9吨左右，头部略圆，具有不明显的喙；背鳍高而直立，弯曲长达1米；身体黑、白两色","下大雨了","美洲狮（学名：Puma concolor）又称美洲金猫，大小和花豹相仿，但外观上没有花纹且头骨较小。全长近2米，肩高65cm，体重30～110kg，为猫亚科中最大者。","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册","相册"];
		
			
			function changebg()
			{
			
				var num=Math.round(Math.random()*67);			
				
				var bg_name='bg'+num+'.gif';
				
			
				//alert(arr[num]);
				document.getElementById("replace").value =arr[num];
				//document.body.style.backgroundColor="#FFCC80";
				document.body.style.backgroundColor="black";
				document.body.style.backgroundImage="url("+"/static/"+bg_name+")";//当前ip下，工作目录开始
				
			}
			
			
			
			
		
			
			
			
			
			
			
			
			
			
			
			
 
