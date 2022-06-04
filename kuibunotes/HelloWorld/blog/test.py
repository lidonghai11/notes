
myFile='bbb'
MUSICNAME='aaa'
newmusic=""",{
        mp3:'/static/music-js/demo/mix/""" + myFile + """',
        oga:'/static/music-js/demo/mix/11.ogg',
        title:'"""+ MUSICNAME +"""',
        artist:'NOBODY',
        rating:5,
        buy:'',
        price:'0',
        duration:'',
        cover:'/static/music-js/demo/mix/2.jpg'
    }"""

print(newmusic)
