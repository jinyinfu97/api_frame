import requests
def rrrr():
    url = 'https://dataapineice.1234567.com.cn/form/page/postRequest'
    data = {"url":"http://10.205.202.145/zktfavor/formapi/search","params":{"filter":{"pageIndex":1,"pageSize":100,"sortFiled":"","Order":""},"ID":"1631879597243","data":{"MrgName":'',"PassportID":'',"MrgSelfTagType":''},"dataType":{}}}
    res = requests.request('post',url=url,json =data)
    print(res.text)
    need = []
    for n in res.json()['Data']:
        a= n['_id']
        need.append(int(a))
    print(need)

list0=[1727094670125804,7435376187333510,1860114714251838,1133285275805138,6447094368484528,1008285942891186,5464346291892546,5029246050827902,3293065075183750,8860111237800606,7499111293882370,7125111294186242,5585111294815984,6269111298791428,6737111327535980,7262111360093988,7319111396571552,9557111401732474,7394111445373052]
list1=[1727094670125804, 7435376187333510, 1860114714251838, 1133285275805138, 6447094368484528, 1008285942891186, 5464346291892546, 5029246050827902, 3293065075183750, 1004655253181366, 5143094574046442, 1002655252258730, 3503094035001102, 2941305774261750, 8534336262272632]

for n in list1:
    if n in list0:
        list0.remove(n)
# print(list0)
v = "天青色等烟雨而我在等你"
test1 = "天青色等烟雨"
test2 = "炊烟袅袅升起"
v_list=list(v)
a_list = list(test1)
b_list = list(test2)


for n in v_list:
    if n in a_list:
        if a_list.index(n)==v_list.index(n):
            v_list[a_list.index(n)]=test2[a_list.index(n)]
        else:
            v_list[v_list.index(n)]=test2[a_list.index(n)]
print(v_list)



url = 'http://61.152.230.33/home/GetCfhList2'

headers = {"Cookie": "ASP.NET_SessionId=wfmsg3cgghgwfxbtxhyszl3b"}
res = requests.request('post',url=url,headers=headers)
print(res.text)
need = []
for n in res.json():
    a= n['CFHID']
    need.append(a)
print(need)