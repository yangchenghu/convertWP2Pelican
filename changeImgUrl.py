#coding=utf-8

import re

# 这里修改成自己的空间地址
strbucketurl = 'http://bucket.qiniudn.com/'

# 打开RSS文件读取内容
file = open('wordpress.2014.xml', 'r')
content = file.read()
file.close()

# 用正则从RSS中提取所有图片链接地址
p = re.compile('(http:.*?\.(jpg|png))')
urls = p.findall(content)

print urls

iCount = 0

# 替换所有url
for arrlist in urls:
    url = arrlist[0]
    newname = url[url.rfind('/')+1:]
    newurl = strbucketurl + newname
    print url
    print newurl
    print '------------'
    iCount = iCount + 1
    content = content.replace(url, newurl)

print 'change url count:%d' % iCount

outputfile = open('new2013.xml', 'w')
outputfile.write(content)
outputfile.close()
