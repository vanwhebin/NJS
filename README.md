<p align="center" >
  <a href="https://smms.app/image/plcUTsyMaz4QPgo"><img src="https://s2.loli.net/2023/01/21/plcUTsyMaz4QPgo.png" width="256" height="256" alt="NJS"></a>
</p>
<h1 align="center">脑积水 | NJS</h1>
<h4 align="center">✨基于<a href="https://github.com/nonebot/nonebot2" target="_blank">NoneBot2</a>和<a href="https://github.com/Mrs4s/go-cqhttp" target="_blank">go-cqhttp</a>的多功能QQ机器人✨</h4>

<p align="center">
    <a href="https://github.com/zhulinyv/NJS/raw/Bot/LICENSE"><img src="https://img.shields.io/github/license/zhulinyv/NJS" alt="license"></a>
    <img src="https://img.shields.io/badge/Python-3.10+-green" alt="python">
    <img src="https://img.shields.io/badge/nonebot-2.0.0+-yellow" alt="nonebot-2.0.0">
    <img src="https://img.shields.io/badge/go--cqhttp-1.0.0+-red" alt="go--cqhttp">
    <a href="https://pd.qq.com/s/8bkfowg3c"><img src="https://img.shields.io/badge/QQ频道交流-我的中心花园-blue?style=flat-square" alt="QQ guild"></a>
</p>

## 🚑 缓更

本人高三啦，目前没有太多时间继续更新维护，不过其中大部分功能是没有问题的，而且各插件独立，方便替换。

## 💬 前言

脑积水**缝合**了很多功能, 因此**不亚于**[真寻](https://github.com/HibiKier/zhenxun_bot)、[早苗](https://space.bilibili.com/3191529)、[椛椛](https://github.com/FloatTech/ZeroBot-Plugin)等机器人, 但**不同的**是: 其它机器人项目大都有自己写的依赖和生态, 由于个人能力有限, 因此脑积水并没有我自己写的依赖和生态, 但这样也带来了一些好处, 基本上每个插件各自独立, 不需要考虑依赖打架的问题, 方便修改。

可能有人会问, 自己利用 NoneBot 或者其它框架搭建一个不是更好嘛？我会实话告诉你, 你是正确的。**但是**如果插件用多用久了, 你就会发现, 各种指令冲突、优先级冲突, 数据库打架, 依赖打架……

当然, 其它整合项目也不会存在冲突和打架的问题。脑积水内置了部分我自己写的东西, 做了更多个性化处理来提升用户体验。所以，如果你也想安装好多好多好多插件，但有不想自己动手解决这些冲突，那么，脑积水是一个不错的选择。

~~**说白了就是我是小垃姬 >_<, 错的不是我, 是这个世界啊啊啊！~\~**~~

## ✨ 已经实现的功能

<details>

<summary>展开查看: </summary>

发送 "njs帮助" 后得到的内容:

![c402cf601e1b88472e16da8517a36f32](https://github.com/zhulinyv/NJS/assets/66541860/f2de3ecf-c0ff-4bc7-bd01-b0a36c316dda)

</details>

## 🎉 开始部署

⚠️ 你可能需要一点 Python 和有关计算机的知识。

⚠️ 需要两个 QQ 号, 一个自己的, 一个机器人的。

⚠️ 系统要求: Windows8 及以上, Linux(推荐:Ubuntu)~~, Mac(不会真的有人用 Mac 跑 Bot 叭), Android 自己研究一下 (bushi)~~。

|⚠️ 推荐配置要求: |CPU|RAM||⚠️ 最低配置要求: |CPU|RAM|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|推荐配置|2线程+|2GB+||该配置下部分功能可能无法正常使用|1线程|1GB|

⚠️ 如果遇到任何部署、使用或二次开发上的问题或建议, 可以在 QQ频道: [我的中心花园-开发交流](https://pd.qq.com/s/8bkfowg3c) 找到我。

### 0️⃣ Star 本项目

<details>

<summary>详细帮助: </summary>

o(〃＾▽＾〃)o

1、点击仓库右上角的 Star。![image](https://user-images.githubusercontent.com/66541860/231970470-fe1c6368-8c05-4701-8074-2443bd8ad13d.png)

2、变成 Starred 即表示成功。![image](https://user-images.githubusercontent.com/66541860/231970624-618b0e8c-06dc-4099-9aba-4993ab267e4a.png)

ヾ(≧▽≦*)o

</details>

### 1️⃣ 安装 浏览器、解压软件、文本编辑器

此过程比较简单, 不再附图。

1、警告: **不要**使用 Internet Explorer！如果你的电脑配置比较低, 可以选择 [百分浏览器](https://www.centbrowser.cn/) 等占用小的浏览器, 解压软件可以选择 [7-Zip](https://www.7-zip.org/)、[WinRAR](https://www.ghxi.com/winrarlh.html) 等解压软件(如果你选择下载源码而不用 Git), 文本编辑器任意, 系统自带的记事本都可以, 也可以使用比较高级一点的, 比如 [VScode](https://code.visualstudio.com/)、[Sublime](https://www.sublimetext.com/) 等。**如果你的电脑上已经有其它同类软件, 则跳过此步骤！**

### 2️⃣ 安装 Python

#### Windows下的安装

1、来到 [Python](https://www.python.org/downloads/windows/) 官网的下载页面, 下载并安装 [Python](https://www.python.org/downloads/windows/), 下载 `3.10 版本`即可(这里我下载的是 3.10.9(64-bit), 如果你是 32 位操作系统, 就下载 32 位版本), 但**不要**使用 3.11 版本及以上; 实际上 3.8 版本以上就可以, 但部分插件需要, 因此 3.10 最为合适。

![image](https://user-images.githubusercontent.com/66541860/213637200-dca63b69-fd52-42d1-a3cd-f8b24f492186.png)

2、安装时, 注意勾选 `Add python.exe to PATH` 。

![image](https://user-images.githubusercontent.com/66541860/213638736-729c083f-b2ca-41db-affd-31896db5d4cf.png)

3、出现此页面时, 就表示你已经安装成功了, 此时点击 Close 关闭窗口即可(Disable path length limit 解除路径长度限制, 可选)。

![image](https://user-images.githubusercontent.com/66541860/213639081-6ae459c9-6ef6-4dc1-9cb3-8755934dca2b.png)

4、验证你的下载, `Windows + R` 调出运行框, 输入 `powershell` 按下回车。

![image](https://user-images.githubusercontent.com/66541860/213639939-d6489fde-998a-4a82-baed-140cc9123220.png)

5、输入 `python --version`, 可以看到你的 Python 版本, 这里显示的版本应该和刚刚你安装的版本一致, 如果不一致, 则说明你有多个 Python 或者下载时选错了版本。

![image](https://user-images.githubusercontent.com/66541860/213640522-b6e2756c-32b3-423e-8a7d-c800f5e1b5ef.png)

#### Ubuntu 和 Debian 下的安装

如果是 20+ 的版本, 系统会自带 Python3.8 或 3.10 版本, 如果是 3.10 版本可以直接使用。

如果是更低的版本, 请自行安装 3.10 版本。

Ubuntu 可能没有自带pip命令, 需要运行 `apt install python3-pip` 进行安装

Debian 系统和 Ubuntu 系统同理。

#### CentOS 及其它发行版下的安装

建议更换 Ubuntu, 否则请自行编译安装Python3.8-3.10版本, ~~耗子尾汁~~。

CentOS 在后续也可能有更多的问题, 因此强烈不建议使用 CentOS 如果你执意使用, 后续出现的额外问题, 例如 playwright 缺依赖, 请自行搜索解决。

### 3️⃣ 安装 Git

#### Windows 下的安装

1、来到 [Git](https://git-scm.com/download/win) 官网的下载页面, 下载并安装 [Git](https://git-scm.com/download/win) (如果你是 32 位操作系统, 就下载 32 位版本)。

![image](https://user-images.githubusercontent.com/66541860/213641134-811ad3b9-bb91-4aa0-921e-b54f11214168.png)

2、下载完安装程序后运行, 之后出现的选项均选择 Next 即可, 最后安装完成选择 **Finish**。

![image](https://user-images.githubusercontent.com/66541860/213641800-4eac08d6-32e0-46de-8d9d-95516f17e83f.png)

#### Linux 下的安装

Linux发行版可以用其对应的包管理器安装, 比如 Ubuntu 用 `apt install git`, CentOS 用 `yum install git`。

使用 `git --version` 来检查是否安装成功。

### 4️⃣ 安装 ffmpeg

#### Windows下的安装

1、来到 [ffmpeg](https://www.gyan.dev/ffmpeg/builds/#release-builds) 下载页面, 下载最新版本即可。

![image](https://user-images.githubusercontent.com/66541860/213646782-8ed8dfe1-7784-4bae-b5c7-52566396ad6a.png)

2、解压, 进入 .\bin 目录, 并复制路径

![image](https://user-images.githubusercontent.com/66541860/213647847-b8a27508-f547-4d93-bdad-d347479035e0.png)

3、`Windows + R` 调出运行框, 输入 `control` 按下回车打开控制面板, 依次选择: **系统和安全-系统-高级系统设置-环境变量**

4、点击用户变量下方的**编辑**, 然后在新弹出的窗口中点击**新建**, 粘贴刚刚复制的路径, 选择**确定**。

![image](https://user-images.githubusercontent.com/66541860/213648705-2df64a69-635b-4842-85bc-b012074a02d3.png)

5、**重启**计算机。至此, 环境配置全部结束。🚧

#### Linux 下的安装

Ubuntu系统可以直接使用 `apt install ffmpeg` 来安装。

其他发行版请自行搜索安装教程, 记得添加到环境变量中。

使用 `ffmpeg -version` 来检查是否安装成功。

#### 如果不安装, 脑积水则无法发送**语音**和**视频**等信息。

### 5️⃣ 安装 脑积水

1、打开 powershell, 输入 `git clone -b Bot --depth=1 https://ghproxy.com/https://github.com/zhulinyv/NJS` 来克隆本仓库。

上方链接是镜像源地址, 如有需要, 可将 `https://ghproxy.com/` 删除来直接通过 GitHub 克隆本仓库; `-b Bot` 参数为仅克隆 Bot 分支, 如有需要, 可将其删除以 clone 全部分支。

2、仓库较大, 克隆过程较慢, 耐心等待, 大概会有 4GB 大小。

![image](https://user-images.githubusercontent.com/66541860/213651257-3f3bcb25-329f-4d8b-982a-591494e4513b.png)

备注: 若出现克隆失败的情况, 多半是由于仓库太大造成的, 如果遇到可以尝试用 GitHub 源地址克隆或直接下载 Zip 文件或使用如下命令调整 http 的请求最大容量。

`git config --global http.postBuffer 数字`。(数字即为调整后的最大容量)

如果实在是无法克隆或者下载, 这里有一份[度盘链接](https://pan.baidu.com/s/1JmW1EcgqvZ6Tnsf1m5n0rg?pwd=ytpz), 提取码: ytpz ,下载后可以使用 `git pull` 进行更新。

3、关于额外的资源, 大部分插件会在启动时或启动后自动下载资源。如果出现由于网络问题或其它问题导致的下载失败, 可参照具体插件仓库说明手动下载。

### 6️⃣ 安装 字体

**可选**: 安装字体: 部分插件需要用到特定字体, 不安装不影响使用。

**Windows** 将 ./NJS/data/fonts 目录下的字体文件复制到 /Windows/Fonts 即可; 

**Linux** 将 ./NJS/data/fonts 目录下的字体文件复制到 /usr/share/fonts/truetype 然后用 `sudo fc-cache -fv` 更新字体缓存。

备注: 如果出现中文乱码, 此时必需安装中文字体。

### 7️⃣ 安装 Poetry 和依赖

1、输入 `cd NJS` 回车, 来进入脑积水机器人目录。

2、依次输入以下指令:

```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install poetry
poetry install
```

第一行为全局换源(清华源)操作。

第二行安装 poetry 。

第三行用 poetry 创建环境并安装依赖。

备注: 换源不是必须操作, 按需使用, 国内换国内源可加速安装过程。

如果依赖安装过程中出现问题, 尝试使用这条命令安装 `poetry run pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple` 。


### 8️⃣ 配置 脑积水

1、用记事本等文本编辑器打开 NJS 目录下的 **env.prod** 文件, 里面已经填了一些我使用的配置, 如果另有需要, 可以对照具体插件仓库详细配置项说明在 **env.prod** 文件中添加。

2、在 `SUPERUSER=[""]` **引号**中填写你自己的 QQ 号作为超级管理员, 如果你想拥有多个管理员, 则需要用**英文**逗号隔开。

例如: `SUPERUSER=["1234567890", "0987654321"]`, 其它配置项类似。

注意: 脑积水使用了频道补丁, 因此也可以处理频道信息, 但频道的超管 ID 与 QQ 群的不同, 需要额外配置。

⚠️ 这一步骤非常重要

注意: 其它配置文件请根据[《脑积水使用手册》(已过时)](https://zhulinyv.github.io/NJS/)中具体插件仓库详细配置项说明在 **env.prod** 文件中配置。

注意: 大部分插件都可以在[NoneBot商店](https://nonebot.dev/store)中找到, 配置项较多, 只有少部分是必须的, 可以按需配置。

### 9️⃣ 登录 脑积水

⚠️ 由于 TX 风控, 以下登录方法**可能**无法正常使用。

⚠️ **推荐的项目:**
```
LagrangeDev/Lagrange.Core
2891954521/LiteLoaderQQNT-OneBotApi-JS
linyuchen/LiteLoaderQQNT-OneBotApi
whitechi73/OpenShamrock
Mrs4s/go-cqhttp
```

推荐教程: [https://llonebot.github.io/zh-CN/guide/configuration](https://llonebot.github.io/zh-CN/guide/configuration)

### 🔟 使用 脑积水

1、**在群聊或私聊中发送 `njs帮助` 简便获取帮助。**

好多好多好多功能, ~~我自己都还没完全用过~~, 所以你可能需要一段时间来适应。

这是脑积水自己的帮助插件, 如果需要对帮助进行修改, 请参照 `.\NJS\data\njs_help\help.json` 文件进行修改。

2、《脑积水食用手册》: [https://zhulinyv.github.io/NJS](https://zhulinyv.github.io/NJS)

3、仓库wiki: [https://github.com/zhulinyv/NJS/wiki](https://github.com/zhulinyv/NJS/wiki)

4、备用地址: [https://www.cnblogs.com/xytpz/p/NJS.html](https://www.cnblogs.com/xytpz/p/NJS.html)

<hr>

i、默认 WebUI 地址: [http://127.0.0.1:13579/LittlePaimon/login](http://127.0.0.1:13579/LittlePaimon/login)

说明: 可以通过 WebUI 对脑积水进行较为方便的图形化管理。基于 [小派蒙](https://github.com/CMHopeSunshine/LittlePaimon) WebUI 样式修改。

ii、更新: 艾特脑积水说更新即可在线更新, 更新成功后, 艾特脑积水说重启来应用新的内容。

iii、如有配置、部署或使用中的问题或建议, 请通过本仓库 [Issues](https://github.com/zhulinyv/NJS/issues)、QQ频道: [我的中心花园-开发交流](https://pd.qq.com/s/8bkfowg3c) 或 [博客首页](https://zhulinyv.github.io/) 联系方式联系我。

#### 进阶使用

1、其它插件的安装: 

  方法一: 在 NJS 目录执行 `poetry run nb plugin install xxx`。

  方法二: 
  
  ```
  ① 在 NJS 目录执行 poetry run pip install xxx
  
  ② 在 pyproject.toml 文件如下位置添加刚才安装的插件
  ```

  [https://github.com/zhulinyv/NJS/blob/09adc88317a9a31fcec1ed63c662354fc16b7d42/pyproject.toml#L121](https://github.com/zhulinyv/NJS/blob/09adc88317a9a31fcec1ed63c662354fc16b7d42/pyproject.toml#L121)

  方法三: 直接 clone 或下载某个插件仓库, 把带有 _\_init__.py 的目录放到 NJS\src\plugins 目录下。

2、如果你已经安装并配置好脑积水且对 [NoneBot 文档](https://nonebot.dev/docs/)有一定了解并懂得 Python 基础知识, 那么就可以自己编写插件啦！！

## 👥 鸣谢: 

**感谢 [NoneBot](https://github.com/nonebot/nonebot2) 中的诸多贡献者。**

**感谢 [go-cqhttp](https://github.com/Mrs4s/go-cqhttp) 中的诸多贡献者。**

**感谢 [unidbg-fetch-qsign](https://github.com/fuqiuluo/unidbg-fetch-qsign) 中的诸多贡献者。**

<hr>
<img width="300px" src="https://count.getloli.com/get/@zhulinyv?theme=rule34"></img>
