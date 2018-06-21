1.更新node版本
卸载旧版本 `sudo apt-get remove nodejs`
安装新版本nodejs
下载对应的二进制包，解压缩之后，创建软连接即可
`
sudo ln -s /opt/nodejs/node-v8.11.2-linux-armv7l/bin/node /usr/local/bin/node
sudo ln -s /opt/nodejs/node-v8.11.2-linux-armv7l/bin/npm /usr/local/bin/npm
`
