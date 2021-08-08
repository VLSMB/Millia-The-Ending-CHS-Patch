def DownloadOnline():
    """联机下载汉化补丁"""
    import sys,re
    import requests
    from bs4 import BeautifulSoup
    from NetJudge import NetJudge
    VERSION = "V2.0"
    print("正在检查联机状态，请稍等...")
    NetCondition = NetJudge()
    if NetCondition == False:
        print("请检查网络连接状态，再进行本操作！")
        input("请按回车键退出...")
        sys.exit()
    else:
        print("网络正常，正在获取文件信息，请稍后...（如果下载的文件异常，请检查汉化补丁程序版本，或留意下载时的网络状态）")

    """从vlsmb.ys168.com中爬取下载链接"""
    #获取ys168网盘根目录信息
    headersA = {"Accept":"*/*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"__yjs_duid=1_e53c16f308d9b8131bdc5b429c95189d1627049806932; ASP.NET_SessionId=f3safvppika35va5qrk0tvew","Host":"cb.ys168.com","Referer":"http://cb.ys168.com/f_ht/ajcx/000ht.html?bbh=1139","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"}
    responseA = requests.get("http://cb.ys168.com/f_ht/ajcx/ml.aspx?cz=ml_dq&_dlmc=vlsmb&_dlmm=",headers=headersA)
    soupA = BeautifulSoup(responseA.text,features="lxml")
    #获取二级目录
    headersB = {"Accept":"*/*","Accept-Encoding":"gzip, deflate","Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2","Connection":"keep-alive","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","Cookie":"__yjs_duid=1_e53c16f308d9b8131bdc5b429c95189d1627049806932; ASP.NET_SessionId=3jgr5biwyp4sbyeaoiel55vt","Host":"cb.ys168.com","Referer":"http://cb.ys168.com/f_ht/ajcx/000ht.html?bbh=1139","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"}
    responseB = requests.get("http://cb.ys168.com/f_ht/ajcx/wj.aspx?cz=dq&jsq=0&mlbh=2182217&wjpx=1&_dlmc=vlsmb&_dlmm=",headers=headersB)
    soupB = BeautifulSoup(responseB.text,features="lxml")
    #找到所有所需要的文件（包括文件夹）
    #提取名称，0位游戏相关介绍V1.5.pdf，1位AllCode.zip，2位MTE_PatchCHSV2.0.part3.cjxpak，
    #          3位MTE_PatchCHSV2.0.part2.cjxpak，4位MTE_PatchCHSV2.0.part1.cjxpak
    DLnames=[]
    DLlinksA=[]
    DLlinks=[]
    for tempsoup in soupB.findAll("a"):
        DLnames.append(tempsoup.text.replace(" ","").replace("\n",""))
        if re.findall(r'<a\shref=".*"\stitle',str(tempsoup),re.I)==[]:
            DLlinksA.extend(re.findall(r'<a\sclass="new"\shref=".*"\stitle',str(tempsoup),re.I))
            #刚上传的文件标有class="new"
        else:
            DLlinksA.extend(re.findall(r'<a\shref=".*"\stitle',str(tempsoup),re.I))
    Vertemp = DLnames.pop(0)

    #进行链接处理
    for link in DLlinksA:
        linkA = link.replace(' class="new"','')[9:][:-7]
        DLlinks.append(linkA)
    #检查版本信息
    VersionOn =float(Vertemp[-4:-1])/100
    #DLlinks Dlnames

    #检查版本号
    if VersionOn == float(VERSION[1:]):
        pass
    else:
        print("\n提示：本汉化补丁程序，已有新版本，最新版本是V"+str(VersionOn)+"，\n请手动访问http://vlsmb.ys168.com获取最新补丁程序！\n（本补丁程序仍然可以使用）")
    while True:
        print("""
您想要下载什么？
============================================================
0、下载全部
1、下载补丁运行必要的文件
2、下载游戏相关文档
3、下载补丁程序源代码
4、帮助
5、退出
============================================================
""")
        dlchoice = input("请输入所选择的项目（仅输入数字）：")
        if dlchoice not in ("0","1","2","3","4","5"):
            print("无效输入！")
        elif dlchoice == "4":
            print("""
下载帮助：
============================================================
以上资源的获取均来自永硕网盘http://vlsmb.ys168.com
选择1所获取的三个cjxpak文件，是汉化补丁运行的必要文件，为必须下载项。

选择2的文档包括官方(Millia Soft)在发布本作品的帖子的原文和译文，
以及本汉化组发布本汉化补丁所声明的内容。

选择3是本汉化补丁的源代码，本汉化补丁基于Python所写，
包括组内测试时的V1.0和V1.5版的代码，供大家学习交流用，
同时也能让大家安心的运行本补丁程序。
============================================================
""")
            input("请按回车键继续...")
        else:
            break
    if dlchoice == "5":
        sys.exit()
    if dlchoice == "0":
        abcd = 0
        for allurl in DLlinks:
            print("正在下载"+DLnames[abcd]+"请稍后...")
            allpatch = requests.get(allurl)
            with open(DLnames[abcd], "wb") as patchcode:
                patchcode.write(allpatch.content)
            print("下载完成！")
            abcd=abcd+1
        input("全部下载完成！请按回车键退出...")
        sys.exit()
    if dlchoice == "1":
        abcd = 2
        for allurl in DLlinks[2:5]:
            print("正在下载"+DLnames[abcd]+"请稍后...")
            allpatch = requests.get(allurl)
            with open(DLnames[abcd], "wb") as patchcode:
                patchcode.write(allpatch.content)
            print("下载完成！")
            abcd=abcd+1
        input("全部下载完成！请按回车键退出...")
        sys.exit()
    if dlchoice == "2":
        print("正在下载"+DLnames[0]+"请稍后...")
        allpatch = requests.get(DLlinks[0])
        with open(DLnames[0], "wb") as patchcode:
            patchcode.write(allpatch.content)
        print("下载完成！")
        input("全部下载完成！请按回车键退出...")
        sys.exit()
    if dlchoice == "3":
        print("正在下载"+DLnames[1]+"请稍后...")
        allpatch = requests.get(DLlinks[1])
        with open(DLnames[1], "wb") as patchcode:
            patchcode.write(allpatch.content)
        print("下载完成！")
        input("全部下载完成！请按回车键退出...")
        sys.exit()
                

