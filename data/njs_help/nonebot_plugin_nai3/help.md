## 🎉 使用

```
指令: nai3/nai
参数:
    prompt          提示词(支持你喜欢的画风串), 默认: None
    -n/--negative   负面提示词, 默认: nsfw,...
    -r/--resolution 画布形状/分辨率, ["mb", "pc", "sq"] 三选一, 默认: mb
    -s/--scale      提示词相关性, 默认: 5.0
    -sm             sm, 默认: False
    -smdyn          smdyn, 默认: False
    --sampler       采样器, 默认: k_euler
    --schedule      噪声计划表, 默认: native
示例: nai3 1girl, loli, cute -r mb -s 5.0
返回: 
```

![img](https://github.com/zhulinyv/nonebot_plugin_nai3/raw/main/img/1.png)

```
指令: nai3黑名单/黑名单(需要超级用户, 群主或群管理员权限)
参数:
    添加    添加黑名单
    删除    删除黑名单
    用户    指定添加类型
    群聊    指定添加类型
    群号/QQ号/@sb.
示例: nai3黑名单添加用户 @脑积水
返回: 
```

![img](https://github.com/zhulinyv/nonebot_plugin_nai3/raw/main/img/2.png)