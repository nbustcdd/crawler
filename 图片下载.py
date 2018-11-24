import urllib.request
import urllib.parse
import re
import os
import time


#处理请求对象url
def handle_request(url,page):
	url =url+str(page)+'/'
	# print(url) 

def download_image(content):
	pattern = re.compile(r'<div class="thumb">.*?<img src="(.*?)".*?>.*?</div>',re.S)
	ret = pattern.findall(content)
	print(ret)
	#遍历列表，依次下载图片
	for image in ret:
		#先处理image
		image = 'https:'+ image
		#创建文件夹
		if not os.path.exists('糗事百科'):
			os.mkdir('糗事百科')
			#图片叫什么名字
			filename = image.split('/')[-1]
			filepath = '糗事百科'+'/'+ filename
			print('%s图片正在下载...'%filename)
			#发送请求，下载图片
			urllib.request.urlretrieve(image,filepath)
			print('%s图片下载结束...'%filename)
			time.sleep(1)

		

def main():
	url ='https://www.qiushibaike.com/imgrank/page/'
	start_page = int(input('请输入起始页码：'))
	end_page = int(input('请输入结束页码：'))
	for page in range(start_page, end_page + 1):
		print ('第%s页开始下载...' % page)
		#处理请求对象
		request = handle_request(url,page)
		#生成请求头
		headers={
        	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
        }
    
        #生成请求对象
		request = urllib.request.Request(url=url,headers=headers)
       
		#发送请求对象，获取响应内容
		content = urllib.request.urlopen(request).read().decode()
        #解析内容，提取所有的图片链接，下载图片
		download_image(content)
		print ('第%s页下载完毕...' % page)
		time.sleep(2)



#当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行
if __name__ == '__main__':
	main()