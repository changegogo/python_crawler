import urllib.request
import urllib.parse
import json

base_url = 'https://sp0.baidu.com/5a1Fazu8AA54nxGko9WTAnF6hhy/su'
while True:
    wd = input('请输入要查询的词语:')
    query_params = {}
    query_params['json'] = 1
    query_params['cb'] = 'callback'
    query_params['wd'] = wd
    params = urllib.parse.urlencode(query_params)

    url = base_url+"?"+params

    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36'

    req = urllib.request.Request(url, None, head)
    res = urllib.request.urlopen(req)

    html = res.read()

    html = html.split(b'(')[-1].split(b')')[0]
    obj = json.loads(html.decode('gbk'))
    # master
    print(obj['s'])
    is_continue = input('是否继续查询(y/n):')
    if is_continue == 'n':
        break
