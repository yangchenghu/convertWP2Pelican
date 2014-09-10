#coding=utf-8

import re
import codecs
import urllib2

# 打开RSS文件读取内容
file = codecs.open('wordpress.2014.xml', 'r', 'utf-8')
content = file.read()
file.close()

# 用正则从RSS中提取所有图片链接地址
p = re.compile('src="([\w\W]+?)"')
urls = p.findall(content)

# 下载图片文件，并保存到img目录
for url in urls:
    print url
    opener = urllib2.build_opener()
    req = urllib2.Request(url.encode('utf-8'))
    try:
        resp = opener.open(req, timeout = 5).read()
        newname = url[url.rfind('/')+1:]
        print newname 
        outfile = open('./img/' + newname , 'wb')
        outfile.write(resp)
        outfile.close()
    except Exception, e:
        print '%s image download fail' % url
        # raise
    else:
        pass
    finally:
        pass
