# -*- coding: gb2312 -*-
import re
from lxml import etree
import csv
import requests
import time
import random



class Crawl:

    def __init__(self):
        self.map = lambda x: x[0] if x else ''
        self.index = True

    def spider(self,page):
        url = 'https://api.bilibili.com/x/web-interface/popular'
        headers ={
        "{": "",
        "\"accept\"": "\"*/*\",",
        "\"accept-encoding\"": "\"gzip, deflate, br\",",
        "\"accept-language\"": "\"zh-CN,zh;q=0.9,en;q=0.8\",",
        "\"cache-control\"": "\"no-cache\",",
        "\"cookie\"": "\"_uuid=DFD98368-3AAD-91E5-95ED-DBFB359B34CD87011infoc; buvid4=0F924021-3D34-68DE-185B-37B4FF4EC48487150-022030800-NWGknCP+/qP7u8SbELwNng%3D%3D; b_nut=1646670187; buvid3=7746D47C-3941-4511-DFF8-59DA66FE853687150infoc; i-wanna-go-back=-1; rpdid=|(RlRul|mJJ0J'uYRYY~|kul; buvid_fp_plain=undefined; nostalgia_conf=-1; CURRENT_BLACKGAP=0; LIVE_BUVID=AUTO7116471798569009; DedeUserID=1987765084; DedeUserID__ckMd5=29399803220e4eb5; CURRENT_QUALITY=80; buvid_fp=77fc06826f89328b9d4f898801440136; b_ut=5; blackside_state=0; fingerprint3=898cfb9ab0de17c4bc37a352f4d46d5a; fingerprint=77fc06826f89328b9d4f898801440136; is-2022-channel=1; SESSDATA=ddd7ba95%2C1675963587%2C67edc%2A81; bili_jct=1625ae40a7477794c80cf6f113474bdf; hit-dyn-v2=1; PVID=1; CURRENT_FNVAL=4048; bp_video_offset_1987765084=694841531684618200; b_lsid=78FD105DF_182A4D0EA93; sid=eioxlxom; b_timer=%7B%22ffp%22%3A%7B%22333.1007.fp.risk_7746D47C%22%3A%22182A4D0EDCB%22%2C%22333.934.fp.risk_7746D47C%22%3A%22182A4D17FD0%22%2C%22333.788.fp.risk_7746D47C%22%3A%22182A4F90D7D%22%7D%7D; innersign=0\",",
        "\"origin\"": "\"https://www.bilibili.com\",",
        "\"pragma\"": "\"no-cache\",",
        "\"referer\"": "\"https://www.bilibili.com/\",",
        "\"sec-ch-ua\"": "\"\\\" Not A;Brand\\\";v=\\\"99\\\", \\\"Chromium\\\";v=\\\"100\\\", \\\"Google Chrome\\\";v=\\\"100\\\"\",",
        "\"sec-ch-ua-mobile\"": "\"?0\",",
        "\"sec-ch-ua-platform\"": "\"\\\"Windows\\\"\",",
        "\"sec-fetch-dest\"": "\"empty\",",
        "\"sec-fetch-mode\"": "\"cors\",",
        "\"sec-fetch-site\"": "\"same-site\",",
        "\"user-agent\"": "\"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36\"",
        "}": ""
    }
        params = {
            'ps': '20',
            'pn': page
        }
        res = requests.get(url,headers=headers,params=params)
        data = res.json()
        self.parse(data)



    def parse(self,data):
        list = data.get('data').get('list')
        for i in list:
            url = 'https://www.bilibili.com/video/' + i['bvid']
            try:
                self.connect(url)
            except:
                continue
            time.sleep(random.uniform(0,1))


    def connect(self, url):
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
            "cache-control": "no-cache",
            "cookie": "_uuid=DFD98368-3AAD-91E5-95ED-DBFB359B34CD87011infoc; b_nut=1646670187; buvid4=0F924021-3D34-68DE-185B-37B4FF4EC48487150-022030800-NWGknCP+/qP7u8SbELwNng%3D%3D; buvid3=7746D47C-3941-4511-DFF8-59DA66FE853687150infoc; i-wanna-go-back=-1; rpdid=|(RlRul|mJJ0J'uYRYY~|kul; buvid_fp_plain=undefined; nostalgia_conf=-1; CURRENT_BLACKGAP=0; LIVE_BUVID=AUTO7116471798569009; DedeUserID=1987765084; DedeUserID__ckMd5=29399803220e4eb5; CURRENT_QUALITY=80; buvid_fp=77fc06826f89328b9d4f898801440136; b_ut=5; blackside_state=0; fingerprint3=898cfb9ab0de17c4bc37a352f4d46d5a; fingerprint=77fc06826f89328b9d4f898801440136; is-2022-channel=1; SESSDATA=ddd7ba95%2C1675963587%2C67edc%2A81; bili_jct=1625ae40a7477794c80cf6f113474bdf; hit-dyn-v2=1; CURRENT_FNVAL=4048; bp_video_offset_1987765084=694841531684618200; b_lsid=EAED37910_182A523AA17; innersign=1; theme_style=light; sid=7fe2fbpx; b_timer=%7B%22ffp%22%3A%7B%22333.1007.fp.risk_7746D47C%22%3A%22182A4D0EDCB%22%2C%22333.934.fp.risk_7746D47C%22%3A%22182A53CFAE7%22%2C%22333.788.fp.risk_7746D47C%22%3A%22182A5519375%22%2C%22333.999.fp.risk_7746D47C%22%3A%22182A54C4618%22%2C%22777.5.0.0.fp.risk_7746D47C%22%3A%22182A5521B66%22%7D%7D; PVID=3",
            "pragma": "no-cache",
            "referer": "https://www.bilibili.com/",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        }
        res = requests.get(url, headers=headers)
        str_data = res.text
        html_obj = etree.HTML(str_data)
        author = self.map(html_obj.xpath('//div[@class="name"]/a[1]/@href')).replace('\n', '').strip()
        id = re.findall('//space.bilibili.com/(\d+)',str(author))[0]

        self.parse_detail(id)
        # writer.writerow(data)


    def parse_detail(self,id):
        headers = {
    "accept": "application/json, text/plain, */*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
    "cache-control": "no-cache",
    "origin": "https://space.bilibili.com",
    "pragma": "no-cache",
    "referer": "https://www.bilibili.com/",
    "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"100\", \"Google Chrome\";v=\"100\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
}
        url = f'https://api.bilibili.com/x/space/acc/info?mid={id}&jsonp=jsonp'
        res = requests.get(url,headers=headers)
        data = res.json().get('data')

        dic = dict()
        dic['id'] = id
        # name 昵称
        dic['name']= data.get('name')
        # sign 签名
        dic['sign']= data.get('sign').replace('\n','').replace(' ','')
        # sex 性别
        dic['sex']= data.get('sex')
        # birthday 生日
        dic['birthday']= data.get('birthday')
        # level 等级
        dic['level']= data.get('level')

        url = f'https://api.bilibili.com/x/relation/stat?vmid={id}&jsonp=jsonp'
        res = requests.get(url,headers=headers)
        data_ = res.json().get('data')
        # following 关注数
        dic['following']= data_.get('following')
        # follower 粉丝数
        dic['follower']= data_.get('follower')

        # vipType 会员类型
        dic['viptype']= data.get('vip').get('type')
        # vipStatus 会员状态
        dic['vipstatus']= data.get('vip').get('status')
        # face 用户图片
        dic['face']= data.get('face')




        header = ['id','name','sign','sex','birthday','level','following','follower','viptype','vipstatus','face']
        with open('哔哩哔哩用户信息2.csv', 'a', newline='', encoding='utf-8')as f:
            writer = csv.DictWriter(f, fieldnames=header)
            if self.index:
                writer.writeheader()
                self.index = False
            writer.writerow(dic)
            print(dic)


    def run(self):
            for i in range(1,29):
                self.spider(i)
                time.sleep(random.uniform(1,2))



if __name__ == '__main__':
    Crawl().run()





