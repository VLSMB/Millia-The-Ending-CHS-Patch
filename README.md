# Millia-The-Ending-CHS-Patch
基于Steam上的Millia -The Ending- 汉化补丁

汉化补丁使用方法：
（此界面的信息可在补丁程序的“帮助”选项中查看）
运行本汉化补丁最低操作系统要求为Microsoft Windows 7 x32且仅限Windows，本汉化补丁为控制台界面，需要输入指定字符并按回车，按照程序的提示即可。
本汉化补丁需要放在游戏程序本体的目录中运行，如果你不知道游戏目录，本汉化补丁可以在游戏运行时搜索目录，但最好自行找到目录（在Win7x64位中如果有*32程序正在运行会无法找到）。

本游戏最终解释权归Millia Soft所有，本补丁由超巨星汉化组发布，仅供学习交流。禁止任何组织任何个人用于任何商业用途，任何商业用途与本汉化组没有任何关系，本汉化组不承担任何因商业问题而带来的麻烦。
本汉化补丁程序由Python编写，源码仅供学习交流，同样不得用于商业用途（包括附带的游戏相关文档）。

游戏地址：
Steam：https://store.steampowered.com/app/428060/Millia_The_ending/
KickStarter：https://www.kickstarter.com/projects/1803299001/millia-the-ending-visual-novel

以下是本补丁程序所用到的Python模块：
自带模块：os,sys,zipfile,shutil,random,platform,datetime,re
需自行安装的模块：requests,psutil

本补丁脚本的简单说明：
DownloadOnline.py —— 联机下载所需要的文件，资源在http://vlsmb.ys168.com
GetGamePath.py —— 尝试获取游戏路径
NetJudge.py —— 判断网络状态
PatchInstall.py —— 安装补丁
PatchUnstall.py —— 卸载补丁
ZipError.py —— 检验压缩包是否损坏
