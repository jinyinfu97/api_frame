import time

import requests

def login():
    url = "https://tradeapineice.1234567.com.cn/User/home/LoginCheckForMobile"
    data = {
        "AppType":"ttjj",
        "ReqNo":277668554,
        "Version": "6.5.0",
        "appVersion": "6.9.9",
        "Gtoken": "0663E3A80F6C4F2388D5FD331F7887ad",
        "mobileKey": "87C7E8F1-4A80-4045-B0DD-443176FFA5D3",
        "ServerVersion": "6.5.0",
        "CToken": "nckcce6rnjufj6qnqjeneajc1e-hhure.6",
        "utoken": "6afcnd-1df6kafqe-c6c6cdh8urhrdrf0dx46ud0.6",
        "Account" : "18017216062",
        "Password" : "19f05630ee16140fb75110b323bdfc0e"
    }
    res = requests.request('post',url=url,data=data)
    print(res.text)


def attend():
    url = "https://actsl-test.1234567.com.cn/fundtg2/RedPacketRainApi/CommonActive/AttendActive"
    data = {
        "activeId": "A20220118172708",
        "TaskId": "T1_20220118172708",
        "val": "29",
        "version": "6.5.0",
        "appVersion": "6.9.9",
        "gtoken": "0663E3A80F6C4F2388D5FD331F7887ad",
        "mobileKey": "87C7E8F1-4A80-4045-B0DD-443176FFA5D3",
        "serverVersion": "6.5.0",
        "customerNo": "19f5c89e46f94539b40a343df5e38733",
        "ctoken": "nckcce6rnjufj6qnqjeneajc1e-hhure.15",
        "utoken": "6afcnd-1df6kafqe-c6c6cdh8urhrdrf0dx46ud0.15",
        "userId": "19f5c89e46f94539b40a343df5e38733",
        "passportId": "3503094035001102"
    }
    huobi_lis = 0
    card_lis = 0
    jifen_lis = 0
    for _ in range(1, 1001):
        time.sleep(1)
        res = requests.request('post', url=url, data=data)
        # print(res.text)
        try:
            GiftType = res.json()['Data']['GiftType']
            if GiftType == 6:
                huobi_lis += 1
            elif GiftType == 1:
                jifen_lis += 1
            elif GiftType == 2:
                card_lis += 1
            else:
                print('不在三个类型里,相应信息为', res.text)
        except Exception as erro:
            print('错误信息为', erro)
        print(f"第{_}次循环，卡券总数为", card_lis, f"{card_lis/_:.2%}")
        print(f"第{_}次循环，积分总数为", jifen_lis, f"{jifen_lis/_:.2%}")
        print(f"第{_}次循环，货币总数为", huobi_lis, f"{huobi_lis/_:.2%}")

    print("卡券总数为", card_lis, f"{card_lis/1000:.2%}")
    print("积分总数为", jifen_lis, f"{jifen_lis/1000:.2%}")
    print("货币总数为", huobi_lis, f"{huobi_lis/1000:.2%}")


if __name__ == '__main__':
    attend()
