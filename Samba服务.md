samba安装
`sudo apt-get install samba`
samba配置 
`sudo vi /etc/samba/smb.conf`
```shell
[passport]
   comment = my passport hard disk
   path = /media/pi/MyPassport
   valid users = root pi
   browseable = yes
   read only = no
   create mask = 0666
   directory mask = 0666
   guest ok = yes
```
重启samba服务
`/etc/init.d/samba restart`
开机自动启动
U盘（硬盘）格式化以及挂载  挂载权限问题   开机自动挂载
samba 文件夹权限问题