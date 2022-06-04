/**
 * @todo 聊天插件
 * @namespace chat
 * @author haze.liu
 * @since 2015年10月14日 下午2:34:22
 */
(function($) {

	/**
	 * 方法说明<BR>
	 * addSendMessage(message) - 添加一条发送信息($.chat("addSendMessage","test"))
	 * addReceiveMessage(message) - 添加一条接收信息($.chat("addReceiveMessage","test"))
	 * openChat() - 打开聊天窗口($.chat("openChat"))
	 * closeChat() - 关闭聊天窗口($.chat("closeChat"))
	 * addTimestamp() -添加时间戳($.chat("addTimestamp") or $.chat("addTimestamp","12:20");)
	 */
	/**
	 * 参数说明<BR>
	 * {String} title - 标题
	 * {String} recipientImg - 接受者头像
	 * {String} senderImg - 发送者头像
	 * {String} width - 宽度(最小300)
	 * {String} height - 高度(最小400)
	 * {function} beforeSend - 发送之前触发事件
	 * {function} afterSend - 发送之后触发事件
	 * {Json} loadHistory - 加载更多组件
	 * {Blooean} loadHistory.enable - 加载更多是否可用
	 * {String} loadHistory.url - jquery.ajax方法同
	 * {String} loadHistory.type - jquery.ajax方法同
	 * {Json} loadHistory.data - jquery.ajax方法同
	 * {function} loadHistory.success - jquery.ajax方法同
	 * {function} loadHistory.error - jquery.ajax方法同
	 * 
	 */
	var defaults = {
		title:"提问",
		recipientImg:"/static/robot/images/face1.jpg",
		senderImg:"/static/robot/images/face2.jpg",
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
	var methods = null;
	var _methods = null;
	var um=null;
	methods = {
		init : function(options) {
			defaults = $.extend(defaults, options);
			if(defaults.height<400){
				defaults.height=400;
			}
			if(defaults.width<300){
				defaults.width=300;
			}
			_methods.appendHTML();
			_methods.initTool();
			_methods.initDOM();
			_methods.initEvent();
		},
		addSendMessage:function(message){
			_methods.sendMessage(message);
		},
		addReceiveMessage:function(message){
			_methods.receiveMessage(message);
		},
		addTimestamp:function(time){
			_methods.addTimestamp(time);
		},
		openChat:function(){
			_methods.openChat();
		},
		closeChat:function(){
			_methods.closeChat();
		},
	};
	
	_methods = {
		appendHTML:function(ele){
			var html='<div class="chat" style="display: none;">'+
						'<div class="chat-title">'+
							'<a class="hideBtn">隐藏</a>'+
							'<span>'+defaults.title+'</span>'+
						'</div>'+
						'<div class="chat-content">'+
								'<div class="loadMore">点击显示更多</div>'+	
						'</div>'+
						'<div class="chat-editer">'+
							'<script id="chat-editer-container" name="content" type="text/plain" style="width:100%;height:100%;"></script>'+
						    '<a class="sendMessage">发送</a>'+
						'</div>'+
					'</div>'+
					'<div class="showChat">'+
						'<i class="fa fa-comments"></i>'+
					'</div>';
			$('body').append(html);
		},
		initDOM:function(){
			if (defaults.loadHistory.enable) {

			}else{
				$(".chat .chat-content .loadMore").hide();
			}
		},
		initEvent : function() {
			$(".chat .chat-editer .sendMessage").click(function(event) {
				_methods.sendMessage(um.getContent());
			});
			$(".chat .chat-title .hideBtn").click(function(event) {
				_methods.closeChat();
			});
			$(".showChat").click(function(){
				_methods.openChat();
			});
			$(".chat .chat-content .loadMore").click(function(event) {
				if($(this).html()!="加载中...."){
					_methods.loadMore(this);
				}
			});
				
		},
		initTool:function(){
			$(".chat .chat-content").mCustomScrollbar({
				autoHideScrollbar: true,
				theme: "minimal-dark"
			});
		},
		closeChat:function(){
			$(".chat").animate({width: 0,height:0},function(){
					$(".chat").hide();
					$(".showChat").show();
				});
		},
		openChat:function(){
			$(".showChat").hide();
				$(".chat").show();
				$(".chat").animate({ width: defaults.width,height: defaults.height},function(){
					if($(".edui-editor-body").length==0){
						um = UM.getEditor('chat-editer-container');
					}
					$(".chat .chat-content").mCustomScrollbar("scrollTo","bottom");
				});
		},
		loadMore:function(obj){
			$(obj).html("加载中....");

			$.ajax({
				type: defaults.loadHistory.type,
				url: defaults.loadHistory.url,
				data:defaults.loadHistory.data,
				success:function(data) {
					if(data.history.length==0){
						$(obj).hide();
					}else{
						$(obj).html("点击显示更多");
						$.each(data.history,function(i,n){
							var html=""
							if(n.type=="left"){
								html='<div class="chat-item left">'+
											'<img src="'+defaults.recipientImg+'" class="headPic">'+
											'<div class="chat-item-content content-gray">'+
													n.message+
											'</div>	'+
											'<b class="jiao-wai">'+
				                               ' <b class="jiao-nei"></b>'+
				                            '</b>'+
										'</div>';
										$(obj).after(html);


							}else if(n.type="right"){
								html='<div class="chat-item right">'+
											'<img src="'+defaults.senderImg+'" class="headPic">'+
											'<div class="chat-item-content content-orange">'+
													n.message+
											'</div>	'+
											'<b class="jiao-wai">'+
				                               ' <b class="jiao-nei"></b>'+
				                            '</b>'+
										'</div>';
							}else if(n.type="timestamp"){
									html='<div class="timestamp"><span>'+n.message+'</span></div>';
							}
							if(html!=""){
								$(obj).after(html);
							}
							
						});
					}
					
					if (defaults.loadHistory['success']) {
						defaults.loadHistory.success(data);
					}
				},
				error:function(a,b,c){
					if (defaults.loadHistory['error']) {
						defaults.loadHistory.error(data);
					}
					
				}
			});
		},
		addTimestamp:function(time){
			if(time==null){
				var now = new Date();
				time=now.getHours()+":"+now.getMinutes();
			}
			$(".chat .chat-content .mCSB_container").append('<div class="timestamp"><span>'+time+'</span></div>');
			$(".chat .chat-content").mCustomScrollbar("scrollTo","bottom");
		},
		sendMessage:function(message){
			if (defaults['beforeSend']) {
				defaults.beforeSend(message);
			}
			var html='<div class="chat-item right">'+
							'<img src="'+defaults.senderImg+'" class="headPic">'+
							'<div class="chat-item-content content-orange">'+
									message+
							'</div>	'+
							'<b class="jiao-wai">'+
                               ' <b class="jiao-nei"></b>'+
                            '</b>'+
						'</div>';
			$(".chat .chat-content .mCSB_container").append(html);
			$(".chat .chat-content").mCustomScrollbar("scrollTo","bottom");
			um.execCommand('cleardoc');

			if (defaults['afterSend']) {
				defaults.afterSend(message);
			}
		},
		receiveMessage:function(message){
			var html='<div class="chat-item left">'+
							'<img src="'+defaults.recipientImg+'" class="headPic">'+
							'<div class="chat-item-content content-gray">'+
									message+
							'</div>	'+
							'<b class="jiao-wai">'+
                               ' <b class="jiao-nei"></b>'+
                            '</b>'+
						'</div>';
			$(".chat .chat-content .mCSB_container").append(html);
			$(".chat .chat-content").mCustomScrollbar("scrollTo","bottom");
		},

	};
	$.chat = function() {
		var method = arguments[0];
		if (methods[method]) {
			method = methods[method];
			arguments = Array.prototype.slice.call(arguments, 1);
		} else if (typeof (method) == 'object' || !method) {
			method = methods.init;
		} else {
			$.error('Method ' + method + ' does not exist on jQuery.chat');
			return this;
		}
		return method.apply(this, arguments);
	};
})(jQuery);
