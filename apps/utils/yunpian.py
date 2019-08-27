import requests
import json


class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"
        self.header = {
            "Content-type": "application/x-www-form-urlencoded",
            "Accept": "text/plain"
        }

    def send_sms(self, code, mobile):
        # 需要传递的参数
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【生鲜超市】您的验证码是%s。如非本人操作，请忽略本短信" % code
        }

        response = requests.post(self.single_send_url, parmas)
        re_dict = json.loads(response.text)
        print(re_dict)
        return re_dict


if __name__ == "__main__":
    # 例如：9b11127a9701975c734b8aee81ee3526
    yun_pian = YunPian("72b4820bbeecf8f1fc14de76c6ac7118")
    yun_pian.send_sms("1234", "15234412838")
