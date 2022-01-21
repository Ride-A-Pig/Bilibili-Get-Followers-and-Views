# Bilibili informations based on bilibili_api
# Install package: pip3 install bilibili-api
from time import sleep, time
from bilibili_api import video, user, sync, Credential
import time
import os


# Your credential to access bilibili. Some functions require cookies for authentication.
uuid = 00000  # uid of your account (int)
sessdata = ''  # SESSDATA from cookies (str)
bili_jct = ''  # bili_jct from cookies (str)
buvid3 = ''  # buvid3 from cookies (str)


def proof(sessdata, bili_jct, buvid3):
    return Credential(sessdata=sessdata,
                      bili_jct=bili_jct,
                      buvid3=buvid3)


def get_user():
    return user.User(uid=uuid, credential=proof(sessdata, bili_jct, buvid3))


def get_total_followers():
    return sync(get_user().get_followers())['total']


def get_total_views():
    base = sync(get_user().get_up_stat())
    return [base['archive']['view'],
            base['article']['view'],
            base['likes']]


while True:
    os.system('clear')
    print(f'Total follower: {get_total_followers()}')
    print(f'Total video views: {get_total_views()[0]}')
    print(f'Total article views: {get_total_views()[1]}')
    print(f'Total likes: {get_total_views()[2]}')
    # Resfresh every minute, if the frequency is too high, you may get banned.
    time.sleep(60)
