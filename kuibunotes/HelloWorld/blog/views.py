from django.shortcuts import render
from datetime import datetime
from elasticsearch import Elasticsearch
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import time
import json
import urllib.request
# Create your views here.
from django.http import HttpResponse
from django.template import loader
import socket
import os
from pathlib import Path

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import auth
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def hello(request):
    t = loader.get_template('hello.html')
    d = {"name":"lidonghai","age":29,"sex":"mail"} 
    return HttpResponse(t.render(d))
    #return HttpResponse("Hello world in blog! ")

@login_required
def get_search(request):
    d = {"name":"lidonghai","age":29,"sex":"mail"} 
    return render(request,"get_search.html",d)

@login_required
def search_get(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)

@login_required
def post_search(request):
    return render(request,"post_search.html")


@login_required
def search_post(request):
    request.encoding='utf-8'
    if 'q' in request.POST:
        message = 'post你搜索的内容为: ' + request.POST['q']
    else:
        message = 'post你提交了空表单'

    return HttpResponse(message)









@login_required
def es_search(request):
    return render(request,"es_search.html")


@login_required
def es_notes(request):
    request.encoding='utf-8'
    if 'key_words' in request.GET:
        message =  request.GET['key_words']
    else:
        message = '请输入关键词'
    if  message == "":
        message='请输入关键词'
    t = loader.get_template('es_notes.html')
    d = {"key_words":message}
    return HttpResponse(t.render(d))

@login_required
def es_notes_search(request):
    request.encoding='utf-8'

    #获取用户名拼接索引名字
    index_name=request.user.username + 'content'
    if index_name == "admincontent":
       index_name="content"

    if 'key_words' in request.GET:
        message =  request.GET['key_words']
    else:
        message = '请输入关键词'
    es = Elasticsearch(['localhost:9200'], http_auth="elastic:Fukaili9259#")

    if message == "请输入关键词":
        message = '"' + message + '"'
        res = es.search(index=index_name, body={"from":0,"size" : 100,"query": {"match_all": {}}})
    else:
        message = '"' + message + '"'
        res = es.search(index=index_name, body={"from":0,"size" : 10000,"query": {"multi_match": {             "query":  message,             "type":   "most_fields",             "fields": [ "title", "summary","content","example","annotation" ]         }}})

    paginator = Paginator(res['hits']['hits'], 5)
    page = request.GET.get('page')
    message=eval(message)
    try: # 获取某页
        content_list = paginator.page(page)
    except PageNotAnInteger: # 如果 page 参数不为正整数，显示第一页
        content_list = paginator.page(1)
    except EmptyPage: # 如果 page 参数为空页，跳到最后一页
        content_list = paginator.page(paginator.num_pages)

    t = loader.get_template('right.html')
    d = {"key_words":message,"notes":content_list}
    return HttpResponse(t.render(d))

@login_required
def es_handle(request):
    t = loader.get_template('es_handle.html')
    return HttpResponse(t.render())

@login_required
def es_insert(request):
    request.encoding='utf-8'

    #获取用户名拼接索引名字
    index_name=request.user.username + 'content'
    if index_name == "admincontent":
       index_name="content"


    Title =  request.POST['Title']
    Summary =  request.POST['Summary']
    Content =  request.POST['Content']
    Url =  request.POST['Url']
    Example =  request.POST['Example']
    Annotation =  request.POST['Annotation']
    if 'time' in request.POST:
        time =  request.POST['time']
    else:
        time = datetime.now()
    t = loader.get_template('insert.html')

    es = Elasticsearch(['localhost:9200'], http_auth="elastic:Fukaili9259#")
    doc = {
    'title': Title,
    'summary': Summary,
    'content': Content,
    'url': Url,
    'example': Example,
    'annotation': Annotation,
    'score': 0,
    'time': time,
    }
    res = es.index(index=index_name, body=doc)
    d = {'title': Title,'summary': Summary,'content': Content,'url': Url,'example': Example,'annotation': Annotation,'score': 0,'time': time}
    return HttpResponse(t.render(d))





@login_required
def es_delete(request):
    request.encoding='utf-8'
     #获取用户名拼接索引名字
    index_name=request.user.username + 'content'
    if index_name == "admincontent":
       index_name="content"

    Oid =  request.GET['Oid']
    es = Elasticsearch(['localhost:9200'], http_auth="elastic:Fukaili9259#")
    res = es.delete(index=index_name, id=Oid)
    es.indices.refresh(index=index_name)
    if 'key_words' in request.GET:
        message =  request.GET['key_words']
    else:
        message = '请输入关键词'
    es = Elasticsearch(['localhost:9200'], http_auth="elastic:Fukaili9259#")

    if message == "请输入关键词":
        message = '"' + message + '"'
        res = es.search(index=index_name, body={"from":0,"size" : 100,"query": {"match_all": {}}})
    else:
        message = '"' + message + '"'
        res = es.search(index=index_name, body={"from":0,"size" : 10000,"query": {"multi_match": {             "query":  message,             "type":   "most_fields",             "fields": [ "title", "summary","content","example","annotation" ]         }}})

    paginator = Paginator(res['hits']['hits'], 5)
    page = request.GET.get('page')
    message=eval(message)
    try: # 获取某页
        content_list = paginator.page(page)
    except PageNotAnInteger: # 如果 page 参数不为正整数，显示第一页
        content_list = paginator.page(1)
    except EmptyPage: # 如果 page 参数为空页，跳到最后一页
        content_list = paginator.page(paginator.num_pages)

    t = loader.get_template('right.html')
    d = {"key_words":message,"notes":content_list}
    return HttpResponse(t.render(d))

@login_required
def es_update(request):
    request.encoding='utf-8'

    #获取用户名拼接索引名字
    index_name=request.user.username + 'content'
    if index_name == "admincontent":
       index_name="content"


    Title =  request.POST['Title']
    Summary =  request.POST['Summary']
    Content =  request.POST['Content']
    Url =  request.POST['Url']
    Example =  request.POST['Example']
    Annotation =  request.POST['Annotation']
    Oid =  request.POST['Oid']
    IP=socket.gethostbyname(socket.getfqdn(socket.gethostname()))
    if 'time' in request.POST:
        time =  request.POST['time']
    else:
        time = datetime.now()
    t = loader.get_template('update.html')

    es = Elasticsearch(['localhost:9200'], http_auth="elastic:Fukaili9259#")
    doc = {
    'title': Title,
    'summary': Summary,
    'content': Content,
    'url': Url,
    'example': Example,
    'annotation': Annotation,
    'score': 0,
    'time': time,
    }
    res = es.index(index=index_name,id=Oid, body=doc)
    d = {'title': Title,'summary': Summary,'content': Content,'url': Url,'example': Example,'annotation': Annotation,'score': 0,'time': time,'id': Oid,'IP':IP}
    return HttpResponse(t.render(d))

@login_required
def read(request):
    request.encoding='utf-8'

    #获取用户名拼接索引名字
    index_name=request.user.username + 'content'
    if index_name == "admincontent":
       index_name="content"


    if 'display' in request.GET:
        id =  request.GET['display']
        ctype =  request.GET['ctype']
        es = Elasticsearch(['localhost:9200'], http_auth="elastic:Fukaili9259#")
        res = es.get(index=index_name, id=id)
        display=res['_source'][ctype]
    else:
        display =  ""
    t = loader.get_template('read.html')
    d = {"display":display}
    return HttpResponse(t.render(d))



@login_required
def music(request):
    return render(request,"music.html")

@login_required
def uploadFile(request):  
    if request.method == "POST":    # 请求方法为POST时，进行处理 
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None 
    if not myFile:  
        return HttpResponse("no files for upload!")  

    if os.path.splitext(myFile.name)[1].lower()!=".mp3":  
        return HttpResponse("not a music for upload!")  

    my_file = Path(os.path.join("/export/servers/app/notes/HelloWorld/static/music-js/demo/mix/",myFile.name))
    if my_file.is_file():
        return HttpResponse("music exist dont upload again")

    destination = open(os.path.join("/export/servers/app/notes/HelloWorld/static/music-js/demo/mix/",myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作 

    for chunk in myFile.chunks():      # 分块写入文件 
        destination.write(chunk)  
    destination.close()  
    MUSICNAME=os.path.splitext(myFile.name)[0]
    newmusic=""",{
        mp3:'/static/music-js/demo/mix/""" + myFile.name + """',
        oga:'/static/music-js/demo/mix/11.ogg',
        title:'"""+ MUSICNAME +"""',
        artist:'NOBODY',
        rating:5,
        buy:'',
        price:'0',
        duration:'',
        cover:'/static/music-js/demo/mix/2.jpg'
    }
    """

    lines=[]
    f=open("/export/servers/app/notes/HelloWorld/static/music-js/demo/js/myplaylist.js",'r')
    for line in f:
         lines.append(line)
    f.close()
    lines.insert(len(lines)-1,newmusic)
    s=''.join(lines)
    f=open("/export/servers/app/notes/HelloWorld/static/music-js/demo/js/myplaylist.js",'w+')
    f.write(s)
    f.close()
    del lines[:]

    return HttpResponse("upload over wait for review!")  




@login_required
def album(request):
    return render(request,"album.html")

@login_required
def uploadjpg(request):  
    if request.method == "POST":    # 请求方法为POST时，进行处理 
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None 
    if not myFile:  
        return HttpResponse("no files for upload!")  

    if os.path.splitext(myFile.name)[1].lower()!=".jpg":  
        return HttpResponse("not a jpg picture for upload!")  
    COUNT=len(os.listdir("/export/servers/app/notes/HelloWorld/static/album/")) + 1
    NEXTPICNAME='1_('+ str(COUNT) +').jpg'

    destination = open(os.path.join("/export/servers/app/notes/HelloWorld/static/album/",NEXTPICNAME),'wb+')    # 打开特定的文件进行二进制的写操作 

    for chunk in myFile.chunks():      # 分块写入文件 
        destination.write(chunk)  
    destination.close()  

    search_text1 = "请输入0~"+ str((COUNT - 16)) +"数字"
    search_text2 = "num>"+ str((COUNT - 16)) +""
    replace_text1="请输入0~"+ str((COUNT - 15)) +"数字"
    replace_text2="num>"+ str((COUNT - 15)) +""
    with open(r'/export/servers/app/notes/HelloWorld/blog/template/album.html', 'r',encoding='UTF-8') as file:
         data = file.read()
         data = data.replace(search_text1, replace_text1)    
         data = data.replace(search_text2, replace_text2)    
    with open(r'/export/servers/app/notes/HelloWorld/blog/template/album.html', 'w',encoding='UTF-8') as file:
         file.write(data)

    return HttpResponse("upload over wait for review!")  



@login_required
def answer(request):
    request.encoding='utf-8'
    if 'query' in request.GET:
        message =  request.GET['query']
    else:
        message = '请输入关键词'
    es = Elasticsearch(['localhost:9200'], http_auth="elastic:Fukaili9259#")

    if message == "":
        message = '请输入关键词'
        message = '"' + message + '"'
        d={"answer":message};
    else:
        message = '"' + message + '"'
        res = es.search(index="questions_answers", body={   "from": 0,   "size": 3,   "query": {     "nested": {       "path": "q_a",       "query": {         "bool": {           "should": [             {               "match_phrase": {                 "q_a.query": {                   "query":message,                   "boost": 2,                   "slop": 20                 }               }             },             {               "match_phrase": {                 "q_a.answer": {                   "query": message,                   "boost": 1,                   "slop": 20                 }               }             }           ],           "must": [             {               "multi_match": {                   "query": message,                   "type": "cross_fields",                   "fields": [ "q_a.query^2", "q_a.answer" ],                   "minimum_should_match": "30%"                               }             }           ]         }       }     }   },   "_source": [     "q_a"   ] })


        answers='你的问题：' + message + '</br>'
        for i in range(0, len(res['hits']['hits'])):
            answers= answers + str(i+1) +  ': ' + res['hits']['hits'][i]['_source']['q_a'][0]['query'] + '</br>' +  res['hits']['hits'][i]['_source']['q_a'][0]['answer'] + '</br><hr>'

        if len(res['hits']['hits']) ==0:
            answers=answers + '小伙子换换关键词吧，你太各路了'

        d={"answer":answers};

    return HttpResponse(json.dumps(d))



@login_required
def chat(request):
    return render(request,"chat.html")


def login(request):
    request.encoding='utf-8'
    if 'user' in request.POST and 'password' in request.POST:
        username = request.POST['user']
        password = request.POST['password']
        #验证用户
        user = authenticate(username=username, password=password)
        if user is not None:
           # the password verified for the user
           if user.is_active:
              #print("User is valid, active and authenticated")
              auth.login(request, user)
              path = request.GET.get("next") or "/"
              return redirect(path) 
           else:
              #print("The password is valid, but the account has been disabled!")
              return render(request,"login.html")
        else:
           # the authentication system was unable to verify the username and password
           #print("The username and password were incorrect.")
           return render(request,"login.html")

    else:
        return render(request,"login.html")



def register(request):
    request.encoding='utf-8'
    if 'user' in request.POST and 'password' in request.POST:
        username = request.POST['user']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password) 
        
        #创建用户索引
        es = Elasticsearch(['localhost:9200'], http_auth="elastic:Fukaili9259#")
        index_name = username + 'content'  
        
        request_body = {
        "mappings" : {
        "properties" : {
        "annotation" : {
          "type" : "text"
        },
        "content" : {
          "type" : "text"
        },
        "example" : {
          "type" : "text"
        },
        "score" : {
          "type" : "integer"
        },
        "summary" : {
          "type" : "text"
        },
        "time" : {
          "type" : "date"
        },
        "title" : {
          "type" : "text"
        },
        "url" : {
          "type" : "keyword"
        }
        }}}
        # 创建索引
        es.indices.create(index=index_name, body=request_body)
        #插入欢迎使用示例文档
        Content = """出自先秦荀子的《劝学》
	　　君子曰：学不可以已。
	　　青，取之于蓝，而青于蓝；冰，水为之，而寒于水。木直中绳，輮以为轮，其曲中规。虽有槁暴，不复挺者，輮使之然也。故木受绳则直，金就砺则利，君子博学而日参省乎己，则知明而行无过矣。
	　　故不登高山，不知天之高也；不临深溪，不知地之厚也；不闻先王之遗言，不知学问之大也。干、越、夷、貉之子，生而同声，长而异俗，教使之然也。诗曰：“嗟尔君子，无恒安息。靖共尔位，好是正直。神之听之，介尔景福。”神莫大于化道，福莫长于无祸。
	　　吾尝终日而思矣，不如须臾之所学也；吾尝跂而望矣，不如登高之博见也。登高而招，臂非加长也，而见者远；顺风而呼，声非加疾也，而闻者彰。假舆马者，非利足也，而致千里；假舟楫者，非能水也，而绝江河。君子生非异也，善假于物也。(君子生 通：性)"""
        doc = {
        'title': "不积跬步，无以至千里；不积小流，无以成江海",
        'summary': Content,
        'content': Content,
        'url': "https://so.gushiwen.cn/mingju/juv_634cff4805b5.aspx",
        'example': "Example",
        'annotation': "Annotation",
        'score': 0,
        'time': 0,
        }
        es.index(index=index_name, body=doc)




        return render(request,"login.html")
    else:
        return render(request,"register.html")

def check_register(request):
    request.encoding='utf-8'
    username = request.POST['user']
    CHECK = User.objects.filter(username=username).exists()
    if CHECK:
       return HttpResponse("yes")
    else:
       return HttpResponse("no")
