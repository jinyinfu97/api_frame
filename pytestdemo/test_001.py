import requests


def get_token():
	url = "https://api.weixin.qq.com/cgi-bin/token"
	data = {
		"grant_type": "client_credential",
		"appid": "wxac9525af0278fe45",
		"secret": "f12e101c5b159d22c60b8a39cf5bf673"
	}

	res = requests.request('get', url=url, params=data)
	access_token = {"access_token":res.json()['access_token']}
	expires_in = {"expires_in":res.json()['expires_in']}
	data = [access_token,expires_in]
	# print(res.json()['access_token'])
	return data


print(get_token())
print(type(get_token()))
