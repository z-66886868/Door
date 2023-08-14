import utils
from Mode_Enum import Mode
from WgWebapi import WgWebapi

# 使用示例
if __name__ == '__main__':
    webapi = WgWebapi.get_instance()

    webapi.setUrl(url="http://192.168.31.188:61080/")

    # 远程开门
    # utils.openDoor(webapi, 1)

    # 查询控制器状态
    # utils.checkState(webapi)

    # 校验时间
    # utils.checkTime(webapi)

    # 提取记录
    # utils.getRecord(webapi)

    # 恢复已提取记录
    # utils.recoverRecord(webapi)

    # 提取记录_时间范围
    # utils.getRecordWithTime(webapi, "2023-08-12 00:00:00", "2023-08-15 00:00:00")

    # 设置门参数
    # utils.setDoorParam(webapi, 1, Mode.online, 10)

    # 读取门参数
    # utils.getDoorParam(webapi)

    # 上传全部权限
    # utils.uploadPrivs(webapi)

    # 权限总数读取
    # utils.getPrivsTotal(webapi)

    # 单个权限添加修改
    # utils.updatePrivs(webapi, 1230005)

    # 权限删除
    # utils.deletePrivs(webapi, 1230001)

    # 权限查询
    # utils.queryPrivs(webapi, 1230001)

    # 上传全部有用时段测试10个
    # utils.uploadFrameTime(webapi)

    # 提取权限
    utils.getTimeFrame(webapi)