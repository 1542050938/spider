# 导入依赖的库
import requests
import json
from multiprocessing import Pool
import pymongo

# "authority": "user.qzone.qq.com",
#     "method": "GET",
#     "path": "/proxy/domain/r.qzone.qq.com/cgi-bin/right_frame.cgi?uin=1542050938&param=3_1542050938_0%7C14_1542050938"
#             "%7C8_8_1542050938_0_1_0_0_1%7C10%7C11%7C12%7C13_0%7C17%7C20%7C9_0_8_1%7C18&g_tk=671795532&qzonetoken"
#             "=35f9d11c047eddf0b01c36f1bbb07dbfcd956e4a43b0f03a43c9b6753c41a09efe0a55c5821684d13c19&g_tk=671795532",
#     "scheme": "https",
#     "accept": "*/*",
#     "accept-encoding": "gzip, deflate, br",
#     "accept-language": "zh-CN,zh;q=0.9",
#     "cookie": "pgv_pvid=802035090; pac_uid=0_5de9348968740; pgv_pvi=5281920000; ptisp=cnc; RK=HyywAzdsP/; "
#               "ptcz=b44593d60caa906cbd9ea1bee767dabb1e379083676e2338be0b38588e24bdf5; zzpaneluin=; zzpanelkey=; "
#               "pgv_si=s3435499520; _qpsvr_localtk=0.9464570238004855; Loading=Yes; qz_screen=1280x720; "
#               "1542050938_todaycount=0; 1542050938_totalcount=6586; QZ_FE_WEBP_SUPPORT=1; __Q_w_s_hat_seed=1; "
#               "rv2=80EAD28073D542FF9CAE6263310372699ADEB9598EA192B74C; "
#               "property20=6986DBC468EC6640AD4086F057777EC7CF447CD5997E6B0B4923BDC05D70EF569D997B9B2C9AFE6F; "
#               "__Q_w_s__QZN_TodoMsgCnt=1; pgv_info=ssid=s6234914274&pgvReferrer=; cpu_performance_v8=3; "
#               "uin=o1542050938; skey=@qx1QZDp8m; p_uin=o1542050938; "
#               "pt4_token=sA0-XRm-ntCMUfChWbiPZZZ24KkWNjtYxK2PIZdK*hQ_; "
#               "p_skey=pmE*imaiQVPJu*7BZoGtwa7st-BnMfsCMj9eYHLFNY4_",
#     "referer: https": "//user.qzone.qq.com/1542050938",
#     "sec-fetch-mode": "cors",
#
# 浏览器的头
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 "
                  "Safari/537.36 "
}
ownQQ = '1542050938'
g_tk = '1013878675'
url = 'https://user.qzone.qq.com/proxy/domain/r.qzone.qq.com/cgi-bin/right_frame.cgi?uin=1542050938&param' \
      '=3_1542050938_0%7C14_1542050938%7C8_8_1542050938_0_1_0_0_1%7C10%7C11%7C12%7C13_0%7C17%7C20%7C9_0_8_1%7C18&g_tk' \
      '=671795532&qzonetoken=35f9d11c047eddf0b01c36f1bbb07dbfcd956e4a43b0f03a43c9b6753c41a09efe0a55c5821684d13c19' \
      '&g_tk=671795532 '
# 本地数据库
client = pymongo.MongoClient('localhost', 27017)
# 数据库名 Qzone2
mydb = client['Qzone2']

# 好友列表
QQs = mydb[ownQQ + 'QQs']
# 存取说说信息
qzone = mydb[ownQQ + 'qzone']


# 第一步 爬取好友列表
def getFriends(url):
    html = requests.get(url, headers=headers)
    # 因为返回的数据格式不符合json，需要处理一下
    # 91可能会有所变化 如果格式不对 自己打印查看然后改进一下
    # 测试json格式是否正确的网站：http://www.bejson.com/
    response = '[' + html.text[10:][:-90] + '}}}]'
    print(response)
    # 解析json数据
    json_Data = json.loads(response)[0]['data']['module_3']['data']
    for da in json_Data['items']:

        qq = da['uin']
        try:
            # name = json_Data['data'][qq]['realname']
            name = da['name']
            info = {
                'qq': qq,
                'realname': name
            }
        except:
            info = {
                'qq': qq,
                'realname': ''
            }
        QQs.insert_one(info)


# 第二步 爬取信息
def getInfos(qq):
    # 没有权限的跳过
    try:
        url = 'https://user.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin=' + qq + '&pos=0&num=20&g_tk=' + g_tk
        html = requests.get(url, headers=headers)
        # 格式处理
        response = '[' + html.text[10:][:-2] + ']'
        json_Data = json.loads(response, encoding='utf-8')[0]
        total = json_Data['total']
        for pos in range(0, int(total), 20):
            url = 'https://user.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin=' + qq + '&pos=' + str(
                pos) + '&num=20&g_tk=' + g_tk
            html = requests.get(url, headers=headers)
            # 格式处理
            response = '[' + html.text[10:][:-2] + ']'
            json_Data = json.loads(response, encoding='utf-8')[0]
            msglist = json_Data['msglist']
            if msglist != None:
                for msg in msglist:
                    # 评论数量
                    cmtnum = msg['cmtnum']
                    # 说说内容
                    Scontent = msg['content']
                    # 发表时间
                    timeShuo = msg['createTime']
                    comments = []
                    if cmtnum:
                        # 评论人员列表
                        commentlist = msg['commentlist']
                        for comment in commentlist:
                            # 评论人qq
                            qq_comment = comment['uin']
                            # nickname
                            # name = comment['name']
                            # 评论时间
                            createTime = comment['createTime']
                            createTime2 = comment['createTime2']
                            # 内容
                            # content = comment['content']
                            comments.append('{ "qq_comment":"' + str(
                                qq_comment) + '","createTime":"' + createTime + '","createTime2":"' + createTime2 + '"}')
                    tid = msg['tid']
                    # 构造说说url
                    Surl = 'http://user.qzone.qq.com/' + qq + '/mood/' + tid + '.1'
                    Like = get_likes(Surl)
                    data = {
                        'qq': qq,
                        'content': Scontent,
                        'createTime': timeShuo,
                        'cmtnum': cmtnum,
                        'comment': comments,
                        'like_number': Like['like_number'],
                        'like_info': Like['like_info']
                    }
                    qzone.insert_one(data)
    except:
        print('error')
        pass


# 获取点赞信息
def get_likes(url):
    # 根据传入的说说地址 构造获取点赞信息的url
    url = 'https://user.qzone.qq.com/proxy/domain/users.qzone.qq.com/cgi-bin/likes/get_like_list_app?uin=' + ownQQ + '&unikey=' + \
          url + '&begin_uin=0&query_count=60&if_first_page=1&g_tk=' + g_tk
    html = requests.get(url, headers=headers)
    # 网页编码转换为unicode
    html.encoding = 'unicode'
    # 格式处理
    response = '[' + html.text[10:][:-3] + ']'
    json_Data = json.loads(response)[0]['data']
    total_number = json_Data['total_number']
    likes = []
    if total_number:
        like_uin_info = json_Data['like_uin_info']
        for info in like_uin_info:
            addr = info['addr']
            constellation = info['constellation']
            fuin = info['fuin']
            gender = info['gender']
            if_qq_friend = info['if_qq_friend']
            if_special_care = info['if_special_care']
            is_special_vip = info['is_special_vip']
            # nick = info['nick']
            likes.append('{ "addr":"' + addr + '","constellation":"' + constellation + '","fuin":"' + str(
                fuin) + '","gender":"' + gender +
                         '","if_qq_friend":"' + str(if_qq_friend) + '","if_special_care":"' + str(
                if_special_care) + '","is_special_vip":"' + str(is_special_vip) + '"}')
            likes.append('{ "fuin":"' + str(fuin) + '"}')
    data = {
        'like_number': total_number,
        'like_info': likes
    }
    return data


if __name__ == '__main__':
    # 每次使用，更新headers中的cookie或者全部更新headers 和 g_tk
    # 换号时更新headers ownQQ 和g_tk
    getFriends(url)
    QQ = [item['qq'] for item in QQs.find()]
    pool = Pool(processes=4)
    pool.map(getInfos, QQ)
