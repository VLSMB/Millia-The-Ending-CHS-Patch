def PatchUnstall():
    """卸载汉化补丁，需要安装过补丁并留住了备份文件"""
    
    import os,shutil,zipfile
    CurrentPath = os.getcwd()
    PatchAllFiles = ["uvn_van.TTF","times.ttf","script.rpyc","script.rpy","screens.rpy","screens.rpyc","options.rpyc","options.rpy","arial.ttf"]
    
    print("正在还原英文原版，请稍后...")
    os.remove(CurrentPath+"\\Millia - The ending -.exe")
    print("删除："+CurrentPath+"\\Millia - The ending -.exe")
    if os.path.exists(CurrentPath+"\\README.html") == True:
        os.remove(CurrentPath+"\\README.html")
        print("删除："+CurrentPath+"\\README.html")
    shutil.rmtree(CurrentPath+"\\renpy")
    print("删除："+CurrentPath+"\\renpy")
    shutil.rmtree(CurrentPath+"\\lib")
    print("删除："+CurrentPath+"\\lib")
    patcheng=zipfile.ZipFile("MTE_PatchENG.cjxpak")
    patcheng.extractall()
    for x in patcheng.namelist():
        print("解压缩："+CurrentPath+"\\"+x)
    print("\n解压缩完成！")
    print("正在修改archive.rpa，请稍后...")
    os.system("rpatool.exe -d game\\archive.rpa arial.ttf options.rpy options.rpyc screens.rpy screens.rpyc script.rpy script.rpyc times.ttf uvn_van.TTF information_chs.jpg")
    os.system("rpatool.exe -a game\\archive.rpa arial.ttf options.rpy options.rpyc screens.rpy screens.rpyc script.rpy script.rpyc times.ttf uvn_van.TTF")
    for tempfn in PatchAllFiles:
        print("成功："+CurrentPath+"\\"+tempfn)
    print("正在清理临时文件，请稍等...")
    #清理所生成的所有临时文件
    for delfn in PatchAllFiles:
        os.remove(CurrentPath+"\\"+delfn)
        print("删除："+CurrentPath+"\\"+delfn)
    os.remove(CurrentPath+"\\rpatool.exe")
    print("删除："+CurrentPath+"\\rpatool.exe")
    input("还原完成！请按回车键退出...")
