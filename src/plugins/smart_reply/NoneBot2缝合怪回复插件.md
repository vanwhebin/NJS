# nonebot2智能(障)回复插件·改

## 功能

基于 2 个词库、2 个聊天 API 和 2 个图片 API 的缝合怪。


### env配置项:

**.env完全不配置不影响插件运行, 但是部分功能会无法使用**

| 配置名 | 类型 | 默认 | 说明 |
| :---: | :---: | :---: | :---: |
| BAN_DATA_PATH | str | "./data/ban_CD" | 存放被屏蔽用户 CD 时间，删掉可提前解除屏蔽 |
| SETU_API | bool | True | 戳一戳图片默认使用的api, True 为 MirlKoi; False 为 Pixiv |
| BAN_CD_TIME | int | 21600 | 当有人骂了 bot 时的屏蔽时间(秒) |
| BOT_NICKNAME | str | 脑积水 | bot 的昵称 |
| BOT_MASTER | str | (๑•小丫头片子•๑) | bot 主人的昵称 |
| xiaoai_apikey | str | None | 小爱同学 apikey, [注册账号后获取](https://api.apibug.com/doc/xiaoai.html) |

### 小爱同学 apiKey 的申请步骤:

    1. 进入网页 https://api.apibug.com/doc/xiaoai.html
    2. 右上角注册登录
    3. 左边接口列表
    4. 找到"小爱同学AI"零元购买
    5. 请求接口中 "&apiKey="后面的值就是你的apiKey, 填在.env内
       

## 开始使用 *★,°*:.☆(￣▽￣)/$:*.°★* 。

**全部指令均需要艾特机器人(私聊不用()**
| 指令 | 说明 |
| :---: | :---: |
| @bot + 任意内容 | 开始聊天 |
| @bot + 查看api | 查看当前使用的api |

**可以响应戳一戳: 20% 概率掉落图片; 25% 概率回复语音; 20% 概率戳回去; 35% 概率回复文字**

| 超管指令 | 说明 |
| :---: | :---: |
| @bot + rm_qq + QQ号 | 提前解除被屏蔽用户 |
| @bot + 切换图片api | 切换图片api |
| @bot + 切换小爱同学模式1/模式2/青云客 | 切换聊天api |
