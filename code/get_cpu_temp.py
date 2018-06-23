#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2018/6/23 7:46 PM
__author__ = 'wjy'

import datetime


def get_cpu_temp():
    with open("/sys/class/thermal/thermal_zone0/temp") as f:
        return float(f.read()) / 1000
    return 0  # 若读取失败，则返回0


def write_time_and_temp():
    with open('/home/pi/Documents/cpu_temp.txt', 'a+') as f:
        now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(now_time + '\t' + str(get_cpu_temp()) + '\n')


if __name__ == '__main__':
    write_time_and_temp()  # 将当前时间和温度写入到文件中
    # 后续通过定时任务，每10分钟执行一次程序

"""
`crontab -l` 查看当前用户的计划任务
`crontab -e` 编辑计划任务，对应编辑`/var/spool/cron/crontabs/`路径下文件名为当前用户的计划任务表
`sudo service cron restart` 重启cron服务
`/30 * * * *    /usr/bin/python3 /home/pi/projects/get_cpu_temp.py`
"""