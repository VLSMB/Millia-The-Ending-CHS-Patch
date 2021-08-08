# Millia -The Ending- 简体中文补丁V2.0 by 超巨星汉化组VLSMB

#强烈声明：本汉化补丁仅供学习交流，任何人、任何组织均不可以拿本补丁或打好补丁的游戏进行任何以谋取利益的买卖交易！
#请大家自觉保护GalGame资源，如果有人拿此买卖，请大家及时举报！
import os,datetime,platform,sys
import psutil

from DownloadOnline import DownloadOnline
from GetGamePath import GetGamePath
from PatchInstall import PatchInstall,EasterEgg
from PatchUnstall import PatchUnstall

VERSION = "V2.0"
os.system("title Millia -The Ending- 简体中文补丁V2.0")

#收集运行环境信息
mteapp = os.path.exists("Millia - The ending -.exe")
mtechs1 = os.path.exists("MTE_PatchCHS"+VERSION+".part1.cjxpak")
mtechs2 = os.path.exists("MTE_PatchCHS"+VERSION+".part2.cjxpak")
mtechs3 = os.path.exists("MTE_PatchCHS"+VERSION+".part3.cjxpak")
mterpa = os.path.exists(r"game\archive.rpa")
mterenpy = os.path.exists("renpy")
mtelib = os.path.exists("lib")
mtechs = mtechs1 == True and mtechs2 == True and mtechs3 == True

#声明常量
CurrentPath = os.getcwd()
PatchAllFiles = ["uvn_van.TTF","times.ttf","script.rpyc","script.rpy","screens.rpy","screens.rpyc","options.rpyc","options.rpy","arial.ttf"]
mtejudge = [mteapp,mtechs,mterpa,mterenpy,mtelib]
mtestring = ["游戏运行程序Millia - The ending -.exe","汉化补丁MTE_PatchCHS"+VERSION+".cjxpak(共3个)","游戏数据archive.rpa","游戏引擎文件夹renpy","游戏运行库文件夹lib"]
x = 0

#程序头信息
print("Millia -The Ending-游戏汉化补丁"+VERSION+" 超巨星汉化组测试版")
now = datetime.datetime.now()
print("当前时间：",now.strftime("%Y-%m-%d %H:%M:%S"))
print("计算机操作系统信息：",platform.platform(),platform.machine())
print("\n强烈声明：本汉化补丁仅供学习交流，任何人、任何组织均不可以拿本补丁或打好补丁的游戏进行任何以谋取利益的买卖交易！")
print("本补丁是免费资源！若您是购买而来，请及时举报商家！")
print("请大家自觉保护GalGame资源，如果有人拿此买卖，请大家及时举报！")

#判断游戏是否完整
for judge in mtejudge:
    if judge == False:
        print("\n运行错误！缺少" + mtestring[x] + "！请检查游戏文件是否完整")
        if x == 0:
            print(r"（提示：本游戏默认存放在steam文件夹下的“\steamapps\common\Millia -The ending-”里）")
            input("如果游戏正在运行，本程序将会尝试搜索目录，请运行游戏程序，之后按回车键继续...")              
            GetGamePath()
            sys.exit()
        elif x == 1:
            while True:
                tempchoice = input("是否需要联机下载汉化补丁？(Y/N):")
                if tempchoice in ("Y","y"):
                    DownloadOnline()
                    break
                elif tempchoice in ("N","n"):
                    input("请按回车键退出...")
                    sys.exit()
                else:
                    print("无效输入！")
        else:
            input("请按回车键退出...")
            sys.exit()
    x = x + 1

#补丁程序开始的地方
while True:
    print("""
您想要做什么？（请键入指定数字并回车）：
============================================================
0、联机下载所需要的文件
1、安装汉化补丁
2、卸载汉化补丁（需要之前安装过补丁并由补丁程序做过备份）
3、查看帮助
4、退出
============================================================
""")
    option = input("请输入所选择的项目（仅输入数字）：")
    if option == "0":
        DownloadOnline()
        break
    elif option == "1":
        PatchInstall()
        break
    elif option == "2":
        PatchUnstall()
        break
    elif option == "3":
        print("""
============================================================
程序帮助：
============================================================
运行本汉化补丁最低操作系统要求为Microsoft Windows 7 x32且仅限Windows，
本汉化补丁为控制台界面，需要输入指定字符并按回车，按照程序的提示即可。
本汉化补丁需要放在游戏程序本体的目录中运行，如果你不知道游戏目录，
本汉化补丁可以在游戏运行时搜索目录，但最好自行找到目录
（在Win7x64位中如果有*32程序正在运行会无法找到）。
============================================================
以下是本补丁程序所用到的Python模块：
自带模块：os,sys,zipfile,shutil,random,platform,datetime,re
需自行安装的模块：requests,psutil
============================================================
本补丁脚本的简单说明：
DownloadOnline.py —— 联机下载所需要的文件，资源在http://vlsmb.ys168.com
GetGamePath.py —— 尝试获取游戏路径
NetJudge.py —— 判断网络状态
PatchInstall.py —— 安装补丁
PatchUnstall.py —— 卸载补丁
ZipError.py —— 检验压缩包是否损坏
============================================================
""")
        input("请按回车键继续...")
    elif option == "4":
        sys.exit()
    elif option == "VLSMB":
        EasterEgg()
    else:
        print("无效输入！")


