import sys

from typing import List

from alibabacloud_dysmsapi20170525.client import Client as Dysmsapi20170525Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models


class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client(
        access_key_id: str,
        access_key_secret: str,
    ) -> Dysmsapi20170525Client:
        """
        使用AK&SK初始化账号Client
        @param access_key_id:
        @param access_key_secret:
        @return: Client
        @throws Exception
        """
        config = open_api_models.Config(
            # 您的AccessKey ID,
            access_key_id=access_key_id,
            # 您的AccessKey Secret,
            access_key_secret=access_key_secret
        )
        # 访问的域名
        config.endpoint = 'dysmsapi.aliyuncs.com'
        return Dysmsapi20170525Client(config)

    @staticmethod
    def main(
      phone_numbers,template_param
    ) -> None:
        client = Sample.create_client('LTAI5t8yabAbP2smpq2oCctX', 'PkonqNNqEYlLpWXNKffjnTpT4nwPcf')
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            phone_numbers= phone_numbers,
            sign_name='猿泓科技',
            template_code='SMS_218901487',
            template_param=str(template_param)
        )
        # 复制代码运行请自行打印 API 的返回值
        a = eval(str(client.send_sms(send_sms_request)))
        if a['body']['Message'] == "OK":
            return True


