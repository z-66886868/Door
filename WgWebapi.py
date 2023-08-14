import json
from datetime import datetime

import requests


class WgWebapi:
    """
    单例模式
    """
    instance = None

    def __init__(self):
        self.url = ""
        self.controllerSN = 425035557

    @classmethod
    def get_instance(cls):
        if not cls.instance:
            cls.instance = cls()
        return cls.instance

    def setUrl(self, url):
        self.url = url

    def setControllerSN(self, controllerSN):
        self.controllerSN = controllerSN

    def getUrl(self):
        return self.url

    def getControllerSN(self):
        return self.controllerSN

    def PushToWebWithjson(self, url, cmdBody, timeoutMs=3000):
        retInfo = ""
        timeout = 3000
        if timeoutMs > timeout:
            timeout = timeoutMs
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        try:
            response = requests.post(url, data=cmdBody, headers=headers, timeout=(5, timeout / 1000))
            retInfo = response.text
        except requests.exceptions.RequestException:
            pass
        return retInfo

    # 是否操作成功
    def successIsTrue(self, strResult):
        bRet = False
        try:
            json_data = json.loads(strResult)
            result = json_data.get("result")
            if result:
                success = result.get("success")
                if success:
                    bRet = success
        except json.JSONDecodeError:
            pass
        return bRet

    @staticmethod
    def logInfoWithTime(info, bShowTime=True):
        if bShowTime:
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(now, info)
            filepath = "wglog.log"
            with open(filepath, "a", encoding='utf-8') as file:
                file.write(f"{now} {info}\n")
        else:
            print(info)
            filepath = "wglog.log"
            with open(filepath, "a", encoding='utf-8') as file:
                file.write(f"{info}\n")

    @staticmethod
    def logInfo(info):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(now, info)
        filepath = "wglog.log"
        with open(filepath, "a", encoding='utf-8') as file:
            file.write(f"{now} {info}\n")

    @staticmethod
    def logInfoInJson(info):
        try:
            json_data = json.loads(info)
            log_info = json.dumps(json_data, indent=4, ensure_ascii=False)
            WgWebapi.logInfo(log_info)
        except json.JSONDecodeError:
            pass

    @staticmethod
    def logInfoInJsonWithoutTime(info):
        try:
            json_data = json.loads(info)
            log_info = json.dumps(json_data, indent=4)
            WgWebapi.logInfoWithTime(log_info, False)
        except json.JSONDecodeError:
            pass

