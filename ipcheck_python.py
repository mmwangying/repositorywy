# -*- coding: utf-8 -*-
ip_time = {}
dic_ip = {}
dic_exception = {}
line_list = []
logfile = file('D:\\winnie\\repositorywy\\log.txt','r')
for log_line in logfile.readlines():
    line_list = log_line.split(' ')
    dic_ip.update({line_list[0]:line_list[3][1:18]})
    n = 0
    ip = line_list[0]+line_list[3][1:18]
    if dic_exception.has_key(line_list[0]+line_list[3][1:18]):
        n = dic_exception[ip]
    n = n + 1
    #print ip,n
    ip_time = {ip:n}
    dic_exception.update(ip_time)
print "独立ip有：".decode('utf-8'),dic_ip
print "独立ip共： ".decode('utf-8'),len(dic_ip.keys())
print "异常ip有：".decode('utf-8')
for ip in dic_exception.keys():
    if dic_exception[ip] < 30:
        dic_exception.pop(ip)
print dic_exception