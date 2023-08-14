import utils
from Mode_Enum import Mode
from WgWebapi import WgWebapi

# 使用示例
if __name__ == '__main__':

    webapi = WgWebapi.get_instance()

    webapi.setUrl(url="http://192.168.31.188:61080/")
    # 远程开门
    utils.openDoor(webapi, 2)

    # 查询控制器状态
    utils.checkState(webapi)

    # 校验时间
    utils.checkTime(webapi)

    # 提取记录
    utils.getRecord(webapi)

    # 恢复已提取记录
    utils.recoverRecord(webapi)

    # 提取记录_指定时间范围_当天记录
    utils.getRecordTime(webapi, "2023-08-11 00:00:00", "2023-08-12 12:00:00")

    # 设置门控制参数
    utils.setDoor(webapi, 1, Mode.open, 10)

    # 读取门控制参数
    utils.getStart(webapi)

    # 上传全部权限1万人
    utils.uploadPrivs(webapi)

    # 权限总数读取
    utils.getPrivsTotal(webapi)

    # 单个权限添加修改
    utils.updatePrivs(webapi, 1230001)

    # 权限删除
    utils.deletePrivs(webapi, 1230001)

    # 权限查询
    utils.queryPrivs(webapi, 1230011)

    # 提取权限
    utils.getPrivs(webapi)
