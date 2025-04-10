def _(*args, **kwargs):
    return args[0] if args else None

class ApplicationError(Exception):
    code = 200
    message = _("你的请求发生了错误，请稍后再试。")


class InvalidAuthentication(ApplicationError):
    code = 10400
    message = _("无效认证")


class UserLoginFailed(ApplicationError):
    code = 10401
    message = _("用户未登录")


class UserTokenWasExpired(ApplicationError):
    code = 10402
    message = _("用户验证信息有误或已过期，请重新登录")


class UserWasAlreadyDisabled(ApplicationError):
    code = 10403
    message = _("该账户已禁用，请联系管理员")


class UserTokenWasUpdated(ApplicationError):
    code = 10404
    message = _("检测到账号已在其他地方登录，请重新登录")


class UserAuthFailed(ApplicationError):
    code = 10405
    message = _("用户名或密码错误")


class UserExistRegisterFailed(ApplicationError):
    code = 10406
    message = _("该邮箱或手机号已存在")


class CaptchaWasExpired(ApplicationError):
    code = 10407
    message = _("验证码已过期，请重新获取")


class CaptchaVerifyFailed(ApplicationError):
    code = 10408
    message = _("验证码输入有误，请重试")


class UserNewPasswordEqualToOldFailed(ApplicationError):
    code = 10409
    message = _("新密码不能与旧密码相同")


class UserOldPasswordVerifyFailed(ApplicationError):
    code = 10410
    message = _("历史密码输入错误")


class GetUserPhoneNumberFailed(ApplicationError):
    code = 10411
    message = _("获取手机号失败，请稍后重试")


class UserNotRegisterFailed(ApplicationError):
    code = 10412
    message = _("该账号不存在，请确认后重试")


class UserNameAlreadyExists(ApplicationError):
    code = 10413
    message = "该用户名已存在"


class UserWechatAuthFailed(ApplicationError):
    code = 10414
    message = _("微信授权失败，请稍后重试")


class UserEmailHasSentTooManyTimes(ApplicationError):
    code = 10415
    message = _("用户邮箱账号已达当日发送上限，请明日再试!")


class SMSGateWayResponseError(ApplicationError):
    code = 10416
    message = _("短信接口出错，请稍后再试!")


class UserPhoneHasSentTooManyTimes(ApplicationError):
    code = 10417
    message = _("用户手机号已达当日发送上限，请明日再试!")


class PhoneExistBindError(ApplicationError):
    code = 10418
    message = _("该手机号已被绑定，请更换手机号后重试")


class SnMissFailed(ApplicationError):
    code = 11401
    message = _("该设备sn未进行出厂录入，请确认后重试")


class SystemBusyError(ApplicationError):
    code = 11402
    message = _("交换机繁忙，请稍后再试。")


class DeviceBindExistFailed(ApplicationError):
    def __init__(self, phone_number):
        self.message = _(f"该设备已被{phone_number}绑定，请确认后重试")

    code = 11403


class ProjectIdMissFailed(ApplicationError):
    code = 11404
    message = _("项目不存在或已被管理员收回")


class DeviceMissOrOfflineFailed(ApplicationError):
    code = 11405
    message = _("设备不存在或不在线")


class ProjectPermissionFailed(ApplicationError):
    code = 11406
    message = _("分享的项目已到期或无权限")


class DevicePermissionFailed(ApplicationError):
    code = 11407
    message = _("分享的设备已到期或无权限")


class DeviceShareTimeOutFailed(ApplicationError):
    code = 11408
    message = _("分享的设备已到期")


class ProjectMissDeviceFailed(ApplicationError):
    code = 11409
    message = _("该项目暂无绑定设备")


class ProjectMissDeviceSacnFailed(ApplicationError):
    code = 11410
    message = _("该项目暂无上报设备数据，请稍后再试")


class DifferentLANDeviceError(ApplicationError):
    code = 11411
    message = _("该项目存在不同局域网设备，请移除后再试")


class ShareProjectAndDeviceConflictFailed(ApplicationError):
    code = 11412
    message = _("项目id和设备id只能同时传入一个")


class ShareCustomizeTimeMissFailed(ApplicationError):
    code = 11413
    message = _("请传入自定义时间")


class ShareCustomizeTimeLessThanNowTimeFailed(ApplicationError):
    code = 11414
    message = _("自定义时间不能小于当前时间")


class ShareProjectOrDeviceMissFailed(ApplicationError):
    code = 11415
    message = _("项目设备不存在或无权限再次分享，请确认后再试")


class ShareTimeOutOrMissFailed(ApplicationError):
    code = 11416
    message = _("分享已绑定或已过期")


class ShareYourSelfFailed(ApplicationError):
    code = 11417
    message = _("请将分享链接发送给其他用户")


class ShareDeviceExistFailed(ApplicationError):
    code = 11418
    message = _("分享的设备已存在")


class ShareProjectExistFailed(ApplicationError):
    code = 11419
    message = _("分享的项目已存在")


class ShareManagerNotExistOrExpiredError(ApplicationError):
    code = 11420
    message = _("该分享已回收或已过期")


class UserNotExistError(ApplicationError):
    code = 11421
    message = _("该用户不存在")


class ProjectNotExistOrNoPermissionError(ApplicationError):
    code = 11422
    message = _("项目不存在或无权限")


class ProjectExistTransferFailed(ApplicationError):
    code = 11423
    message = _("接收人已存在当前移交项目")


class ShareNotRecoverOrTimeOutFailed(ApplicationError):
    code = 11424
    message = _("该分享未收回或到期，不可删除")


class BindDeviceMissProjectNameOrGPSFailed(ApplicationError):
    code = 11425
    message = _("项目名称或经纬度不能为空")


class FileCannotBeEmptyError(ApplicationError):
    code = 12401
    message = _("文件不能为空")


class DeviceModelExistError(ApplicationError):
    code = 12402
    message = _("该设备型号已存在")


class DeviceModelNotExistError(ApplicationError):
    code = 12403
    message = _("该设备型号不存在")


class DeviceFirmwareNotExistError(ApplicationError):
    code = 12404
    message = _("该固件不存在")


class DeviceModelFirmwareVersionExistError(ApplicationError):
    code = 12405
    message = _("该型号固件版本号已存在，请更换一个新的固件版本号")


class VersionFormatError(ApplicationError):
    code = 12406
    message = _("版本号格式错误")


class VersionTooLowError(ApplicationError):
    code = 12407
    message = _("版本号不能低于已存在的版本")


class UpgradeVersionTooBigError(ApplicationError):
    code = 12408
    message = _("可升级版本号不能大于当前版本")


class BaseFirmwareCannotUnpublished(ApplicationError):
    code = 12409
    message = _("该固件版本为基础固件，不可取消发布")


class FileNotExistError(ApplicationError):
    code = 12410
    message = _("文件不存在，请确认后重试")


class FileNameAlreadyExistsError(ApplicationError):
    code = 12411
    message = _("该文件名已存在，请重新命名")


class ReleaseFirmwareCannotUnpublished(ApplicationError):
    code = 12412
    message = _("已发布的固件，不可取消公开")


class DeviceFirmwareVersionNotExistError(ApplicationError):
    code = 12413
    message = _("可升级版本号不存在，请确认后重试")


class DeviceFirmwareVersionCannotContainSelfError(ApplicationError):
    code = 12414
    message = _("可升级版本号不能包含自身版本")


class DeviceWebCompressedPackageError(ApplicationError):
    code = 12415
    message = _("设备页面压缩包解压发生错误")