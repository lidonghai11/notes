# notes
A simple note-taking system based on the full-text search engine elasticsearch, which assists in recording knowledge and skills in daily, work and study, and quickly searches for the required records


##docker镜像，直接运行镜像并运行，按照步骤启动各个组件
docker pull  lidonghai11/private:notes_03
1、运行nginx:
/export/servers/app/nginx/sbin/nginx
2、运行uwsgi:
source  /export/servers/app/notes/bin/activate
uwsgi --ini /etc/uwsgi.ini &

3、运行elasticsearch7.15，需要切换到elasticsearch用户启动:用户密码（elastic/Fukaili9259#）
启动命令:ES_PATH_CONF=/export/servers/app/elasticsearch-7.15.2/config/  ./bin/elasticsearch  -d -p /export/servers/data/es7.15/pid
4、运行mysqld:用户密码(root/lidonghai11)
systemctl start mysqld 

5、宿主机和容器端口映射可以通过pen命令:HelloWorld目录下有安装包，可rpm强行安装
yum localinstall pen-0.25.1-1.el6.x86_64.rpm
pen  0.0.0.0:9200 172.17.0.2:9200  #将宿主机9200端口映射到容器的9200,其他服务端口自行映射


##git clone下来的程序里边HelloWorld目录就是项目目录
git  clone git@github.com:lidonghai11/notes.git
ln -s notes/kuibunotes/HelloWorld/  /export/servers/app/notes/HelloWorld/  #链接下，方便测试
