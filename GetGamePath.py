def GetGamePath():
    """获取游戏运行的路径"""

    import shutil,sys,os
    import psutil

    while True:
        try:
            for AllProcess in psutil.process_iter():
                if AllProcess.name() == "Millia - The ending -.exe":
                    print("本游戏的安装路径为："+AllProcess.cwd())
                    shutil.copy(sys.argv[0],AllProcess.cwd())
                    input("本程序已在指定目录创建副本，之后会打开这个目录，请按回车键退出，并在即将打开的目录中运行本程序...")
                    os.system('start "" "'+AllProcess.cwd()+'"')
                    break
                    break
            else:
                print("找不到游戏进程！请手动去找游戏目录，并将本补丁复制到游戏目录。")
                input("请按回车键退出...")
                break
        except (psutil.AccessDenied,AttributeError,PermissionError):
            print("寻找进程出错！请打开任务管理器，将进程名中带有“*32”的程序关闭！")
            input("请按回车键重新尝试...")
