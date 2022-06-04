# chat_simple
chat by css ,js

客服聊天框（单对话框）  --> https://github.com/tenbamboo/chat_simple

客服聊天框（多选对话框）--> https://github.com/tenbamboo/chat_multiple


使用第三方插件列表:

1.umeditor -->https://github.com/fex-team/umeditor

2.mCustomScrollbar  -->https://github.com/astula/mCustomScrollbar


API:

方法说明:


	addSendMessage(message) - 添加一条发送信息($.chat("addSendMessage","test"))

	addReceiveMessage(message) - 添加一条接收信息($.chat("addReceiveMessage","test"))

	openChat() - 打开聊天窗口($.chat("openChat"))

	closeChat() - 关闭聊天窗口($.chat("closeChat"))

	addTimestamp() -添加时间戳($.chat("addTimestamp") or $.chat("addTimestamp","12:20");)



参数说明:

	 {String} title - 标题
	  
	 {String} recipientImg - 接受者头像
	 
	 {String} senderImg - 发送者头像
	 
	 {String} width - 宽度(最小300)
	 
	  {String} height - 高度(最小400)
	  
	  {function} beforeSend - 发送之前触发事件
	  
	  {function} afterSend - 发送之后触发事件
	  
	  {Json} loadHistory - 加载更多组件
	  
	  {Blooean} loadHistory.enable - 加载更多是否可用
	  
	  {String} loadHistory.url - jquery.ajax方法同
	  
	  {String} loadHistory.type - jquery.ajax方法同
	  
	  {Json} loadHistory.data - jquery.ajax方法同
	  
	  {function} loadHistory.success - jquery.ajax方法同
	 
	  {function} loadHistory.error - jquery.ajax方法同
	
	
参数结构:
	 
	 var defaults = {
	 
		title:"车主提问",
		
		recipientImg:"./images/face1.jpg",
		
		senderImg:"./images/face2.jpg",
		
		width:600,
		
		height:500,
		
		beforeSend:undefined,
		
		afterSend:undefined,
		
		loadHistory:{
		
			enable:false,
			
			url:"",
			
			type:"GET",
			
			data:{},
			
			success:undefined,
			
			error:undefined,
			
		}
	};




