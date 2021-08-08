from bs4 import BeautifulSoup
import requests,re

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
    else:
        DLlinksA.extend(re.findall(r'<a\shref=".*"\stitle',str(tempsoup),re.I))
Vertemp = DLnames.pop(0)

#进行链接处理
for link in DLlinksA:
    linkA = link.replace(' class="new"','')[9:][:-7]
    DLlinks.append(linkA)
    print(linkA)
#检查版本信息
VersionOn =int(Vertemp[-4:-1])/100
print(VersionOn)
print(DLlinks)
input()
#.replace(" class=\"new\"","")

