def PatchInstall():
    """汉化补丁的灵魂所在"""

    import os,sys,zipfile,shutil,random
    from ZipError import ZipError
    #局部变量
    VERSION = "V2.0"
    CurrentPath = os.getcwd()
    PatchAllFiles = ["uvn_van.TTF","times.ttf","script.rpyc","script.rpy","screens.rpy","screens.rpyc","options.rpyc","options.rpy","arial.ttf"]
    
    #重新判断汉化补丁是否存在
    if os.path.exists("MTE_PatchCHS"+VERSION+".part1.cjxpak") == True and os.path.exists("MTE_PatchCHS"+VERSION+".part2.cjxpak") == True and os.path.exists("MTE_PatchCHS"+VERSION+".part3.cjxpak") == True:
        pass
    else:
        print("错误！汉化补丁MTE_PatchCHS"+VERSION+".cjxpak(共3个)仍然缺失！请检查网络运行状态，重新下载汉化补丁！")
        sys.exit()
    #判断压缩包是否完整
    ErrorTemp = ZipError()
    if ErrorTemp == False:
        print("汉化补丁MTE_PatchCHS.cjxpak(共3个)已损坏！请删除这些文件，并重新启动本程序获取新的文件！")
        print("请尝试联网下载补丁...")
        DownloadOnline()
        input("请按回车键退出，并手动重启程序...")
        sys.exit()
    print("""
请仔细阅读以下文档，全部同意方可继续安装本汉化补丁：
============================================================
《汉化组声明》
本游戏最终解释权归Millia Soft所有，本补丁由超巨星汉化组发布，仅供学习交流。
禁止任何组织任何个人用于任何商业用途，任何商业用途与本汉化组没有任何关系，
本汉化组不承担任何因商业问题而带来的麻烦。
本汉化补丁程序由Python编写，源码仅供学习交流，
同样不得用于商业用途（包括附带的游戏相关文档）。
——超巨星汉化组 2021.8.4
============================================================
本补丁程序同时用到了开源项目rpatool，这是github链接：
https://github.com/Shizmob/rpatool
============================================================
Millia Soft游戏原作成员：
组长: Ryou
剧本: Ryou
程序: Tabu, Ryou
美术: Itachi Kanade, Gin
OP曲和BGM: Quan
插入曲和ED曲: Stellatram
UI设计: Shifumi
动画: Nmarecorp & Yuwing Media
校对: Hideaki Katou, Kumomura Yunto, Maya, Mana, Tran Tien Do, Minata Hatsune, Aya Miyako
英语版翻译: Noumi Satsuki
============================================================
汉化成员名单：
翻译：VLSMB
测试：chaos loftus、VLSMB
校对：VLSMB
补丁制作：VLSMB
UI修复：VLSMB
============================================================
""")
    while True:
        t=input("是否同意以上全部内容？(Y/N)：")
        if t=="Y" or t=="y":
            break
        elif t=="N" or t=="n":
            input("请按回车键退出...")
            sys.exit()
        else:
            print("无效输入!")
    os.system("C:\\Windows\\System32\\taskkill.exe /im \"Millia - The ending -.exe\" /f")
    #操作：打包英文版文件
    print("即将开始备份原版文件...")
    patcheng = zipfile.ZipFile("MTE_PatchENG.cjxpak","w",zipfile.ZIP_DEFLATED)
    patcheng.write("Millia - The ending -.exe","Millia - The ending -.exe",zipfile.ZIP_DEFLATED)
    print("打包："+CurrentPath+"\\Millia - The ending -.exe")
    patcheng.write("lib","lib",zipfile.ZIP_DEFLATED)
    patcheng.write("renpy","renpy",zipfile.ZIP_DEFLATED)
    if os.path.exists("README.html")==True:
        patcheng.write("README.html","README.html",zipfile.ZIP_DEFLATED)
        print("打包："+CurrentPath+"\\README.html")
    #将原引擎的文件打包成对应的列表
    for filepathA,dirnamesA,filenamesA in os.walk(CurrentPath+"\\renpy"):
        for filenameA in filenamesA:
            dirnameA = os.path.join(filepathA,filenameA)
            dirnamezipA = dirnameA[len(CurrentPath)+1:len(dirnameA)]
            patcheng.write(dirnameA,dirnamezipA,zipfile.ZIP_DEFLATED)
            print("打包："+dirnameA)
    for filepathB,dirnamesB,filenamesB in os.walk(CurrentPath+"\\lib"):
        for filenameB in filenamesB:
            dirnameB = os.path.join(filepathB,filenameB)
            dirnamezipB = dirnameB[len(CurrentPath)+1:len(dirnameB)]
            patcheng.write(dirnameB,dirnamezipB,zipfile.ZIP_DEFLATED)
            print("打包："+dirnameB)
    #删除原版文件
    shutil.rmtree(CurrentPath+"\\renpy")
    print("删除："+CurrentPath+"\\renpy")
    shutil.rmtree(CurrentPath+"\\lib")
    print("删除："+CurrentPath+"\\lib")
    os.remove(CurrentPath+"\\Millia - The ending -.exe")
    print("删除："+CurrentPath+"\\Millia - The ending -.exe")
    if os.path.exists("README.html")==True:
        os.remove(CurrentPath+"\\README.html")
        print("删除："+CurrentPath+"\\README.html")
    print("原版文件备份成功！")
    #解压缩cjxpak(其实就是zip文件啦)
    patchchs1 = zipfile.ZipFile("MTE_PatchCHS"+VERSION+".part1.cjxpak")
    patchchs1.extractall()
    for tempfn in patchchs1.namelist():
        print("解压缩："+CurrentPath+"\\"+tempfn)
    patchchs2 = zipfile.ZipFile("MTE_PatchCHS"+VERSION+".part2.cjxpak")
    patchchs2.extractall()
    for tempfn in patchchs2.namelist():
        print("解压缩："+CurrentPath+"\\"+tempfn)
    patchchs3 = zipfile.ZipFile("MTE_PatchCHS"+VERSION+".part3.cjxpak")
    patchchs3.extractall()
    for tempfn in patchchs3.namelist():
        print("解压缩："+CurrentPath+"\\"+tempfn)
    shutil.move("windows-x86_64","lib\\windows-x86_64")
    shutil.move("windows-i686","lib\\windows-i686")
    print("解压缩完成！")
    #备份archive.rpa中部分文件
    print("正在备份archive.rpa中部分数据...")
    os.system("rpatool.exe -x game\\archive.rpa arial.ttf options.rpy options.rpyc screens.rpy screens.rpyc script.rpy script.rpyc times.ttf uvn_van.TTF -o game")
    for PatchFile in PatchAllFiles:
        patcheng.write(CurrentPath+"\\game\\"+PatchFile,PatchFile,zipfile.ZIP_DEFLATED)
        print("打包："+CurrentPath+"\\game\\"+PatchFile)
    patcheng.write(CurrentPath+"\\rpatool.exe","rpatool.exe",zipfile.ZIP_DEFLATED)
    print("打包："+CurrentPath+"\\rpatool.exe")
    #打入汉化补丁
    print("正在打入汉化补丁...")
    os.system("rpatool.exe -x game\\archive.rpa arial.ttf options.rpy options.rpyc screens.rpy screens.rpyc script.rpy script.rpyc times.ttf uvn_van.TTF -o game")
    os.system("rpatool.exe -d game\\archive.rpa arial.ttf options.rpy options.rpyc screens.rpy screens.rpyc script.rpy script.rpyc times.ttf uvn_van.TTF")
    os.system("rpatool.exe -a game\\archive.rpa arial.ttf options.rpy options.rpyc screens.rpy screens.rpyc script.rpy script.rpyc times.ttf uvn_van.TTF information_chs.jpg")
    for tempfn in PatchAllFiles:
        print("成功："+CurrentPath+"\\"+tempfn)
    print("成功："+CurrentPath+"\\information_chs.jpg")
    #清理临时文件
    print("正在清理临时文件...")
    for delfile in PatchAllFiles:
        os.remove(CurrentPath+"\\"+delfile)
        os.remove(CurrentPath+"\\game\\"+delfile)
    os.remove(CurrentPath+"\\information_chs.jpg")
    os.remove(CurrentPath+"\\rpatool.exe")
    patcheng.close()
    patchchs1.close()
    patchchs2.close()
    patchchs3.close()
    print("汉化补丁植入完成！汉化组祝您游戏愉快！")
    print("\n32位操作系统请运行带“-32”的应用程序，64位操作系统直接运行本体程序。\n")
    input("请按回车键退出...")
    
def EasterEgg():
    easter = random.randint(0,7)
    egg = ["悄悄告诉你一个小秘密：其实*.cjxpak文件就是一个普通的zip压缩，改个扩展名只是害怕小白自作主张解压导致程序出现错误...","无效输入！","无效输入！","其实把，我写这个汉化补丁比汉化本游戏所用的技术都多...","无效输入！","无论是不起眼的小游戏，还是那种爆火的大游戏；无论是加密程度非常深的，还是文本浅显易取的游戏，只要是没有中文，都是值得尝试汉化的。把所有游戏（违法违德的除外）都翻译成中文版，正是当代汉化人的任务所在。","无效输入！","加油！好好工作，好好学习，好好生活！"]
    print(egg[easter])
