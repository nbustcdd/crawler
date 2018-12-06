#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-12-01 08:58:04
# @Author  : cdd (792150219@qq.com)
# @Link    : heiheihei
# @Version : $Id$

import urllib.request
import urllib.parse
import re
import os
import time

#如果page=None,那就不拼接
def handle_request(url,page=None):
	if page != None:
	#拼接url
		url = url + str(page) + '.html'

def get_text(a_href):
	#调用函数构建请求对象
	request = handle_request(a_href)
	headers={
		'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
	}
	#生成请求对象
	request = urllib.request.Request(url=url,headers=headers)
	#发送请求，获取响应
	content = urllib.request.urlopen(request).read().decode()
	#解析内容
	pattern = re.compile(r'<div class="neirong">(,*?)</div>',re.S)
	ret = pattern.findall(content)
	text = ret[0]
	#清空所有图片标签
	pat = re.compile(r'<img .*?>')
	text = pat.sub('',text)
	return text
	

def download_lizhi(content):
	#解析内容,写正则
	pattern = re.compile(r'<h3><a href="(/lizhi/qianming/\d+\.html)">(.*?)</a></h3>')
	ret_title = pattern.findall(content)
	#返回的ret是一个列表，列表中的元素都是元组，元组中第一个元素就是正则中的第一个小括号匹配到的内容，依次类推
#	print(ret_title)
	#遍历列表
	for href_title in ret_title:
		#获取内容的链接
		a_href ='http://www,yikexun.cn'+ href_title[0]
		#获取标题
		title = href_title[-1]
		#向a_href发送请求，获取响应内容
		text = get_text(a_href)
		#写入到html文件中
		string = '<h1>%s</h1>%s' %(title,text)
		#当写字符串时，获取内容若是utf8,那么按照下面的写法
		with open ('lizhi.html''a',encoding='utf8') as fp:
			fp.write(string)
		#带b，必须是二进制
		#with open ('lizhi.html','ab') as fp:
			#fp.write(string.edcode('gbk'))





def main():
	url = 'http://www.yikexun.cn/lizhi/qianming/list_50_'
	start_page = int(input('请输入起始页码：'))
	end_page = int(input('请输入结束页码：'))
	for page in range(start_page, end_page + 1):
	#根据url和page生成指定的request
		request = handle_request(url,page)
		headers={
			'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
		}
		#生成请求对象
		request = urllib.request.Request(url=url,headers=headers)
		#发送请求对象，获取响应内容
		content = urllib.request.urlopen(request).read().decode()
		#解析内容，提取所有的图片链接，下载图片
		download_lizhi(content)

if __name__ == '__main__':
	main()
