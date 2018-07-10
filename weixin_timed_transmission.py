# python3
import time
import requests
from wxpy import *
from threading import Timer
import datetime


bot = Bot()

def log(*args, **kwargs):
    print('log', *args, **kwargs)


def get_date():
    """
    更新get_words中的url的时间为当天
    """
    isoTimeFormat = '%Y-%m-%d'
    date = time.strftime(isoTimeFormat,time.localtime())
    log("date", date)
    return date


def get_words():
    """
    获取毒鸡汤，毒汤日历API
    """
    url = 'http://www.dutangapp.cn/u/toxic?date={}'.format(get_date())
    # log(url)
    req = requests.get(url)
    # log(req)
    datas = ''
    for i in range(3):
        data = req.json()['data'][i]['data']
        datas += data + '\n\n'
    log(datas)
    return datas


def send_words():
    try:
        datas = get_words()

        # 朋友的微信名称，不是备注，也不是微信帐号。

        my_friend = bot.friends().search('duckduck')[0]
        my_friend.send(datas)
        my_friend.send(u"————来自爸爸的毒鸡汤")
    except:

        # 自己的微信名称

        my_friend = bot.friends().search('Alpha 前行')[0]
        my_friend.send(u"今天消息发送失败了")


def send_time():
# TODO 第一条发生在启动时，非定时
    send_words()

    now_time = datetime.datetime.now()
    # 获取明天时间
    next_time = now_time + datetime.timedelta(days=+1)
    next_year = next_time.date().year
    next_month = next_time.date().month
    next_day = next_time.date().day
    # 获取明天8点时间
    next_time = datetime.datetime.strptime(str(next_year) + "-" + str(next_month) + "-" + str(next_day) + " 08:00:00",
                                           "%Y-%m-%d %H:%M:%S")
    # # 获取昨天时间
    # last_time = now_time + datetime.timedelta(days=-1)

    # 获取距离明天8点时间，单位为秒
    timer_start_time = (next_time - now_time).total_seconds()

    log(timer_start_time)

    # 定时器,参数为(多少时间后执行，单位为秒，执行的方法)
    timer = Timer(timer_start_time,send_time)
    timer.start()


if __name__ == '__main__':
    send_time()