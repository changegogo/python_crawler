import urllib.request
import os
# 请求url获取网络数据
def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36')
    res = urllib.request.urlopen(req)
    html = res.read()
    return html
# 获取当前页码
def get_current_page(url):  
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']', a)
    return html[a:b]
# 查找到所有的图片链接
def find_imgs(page_url):
    html = url_open(page_url).decode('utf-8')
    img_addrs = []
    a = html.find('img src=')
    while a != -1:
        b = html.find('.gif', a, a+255)
        c = html.find('.jpg', a, a+255)
        if b!=-1 or c!=-1:
            img_addrs.append(html[a+9: abs(c*b)+4])
        else:
            b = a + 9
        a = html.find('img src=', abs(b*c))
    return img_addrs
# 保存图片到文件夹下
def save_imgs(floder, img_addrs):
        for img in img_addrs:
           name = img.split('/')[-1]
           if os.path.exists(name):
               print(img+' 已存在')
               continue
           with open(name, 'wb') as f:
               print(img+' 正在下载...')
               if img.find('http')<0:
                   img = 'http:'+img
               file = url_open(img)
               f.write(file)
               print(name+' 下载成功')

# 下载图片
def download_mm(floder='pic', pages=10):
    if not os.path.exists('ooxx'):
        os.mkdir(floder)
    os.chdir(floder)

    url = 'http://jandan.net/ooxx'

    cur_page = int(get_current_page(url))
    print(cur_page)
    for i in range(pages):
        cur_page -= i
        page_url = url + '/page-' + str(cur_page) + '#comments'
        img_addrs = find_imgs(page_url)
        if i == 9:
            img_addrs.pop()
        save_imgs(floder, img_addrs)

if __name__ == '__main__':
    download_mm('ooxx',100)
