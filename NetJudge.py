def  NetJudge():
    """判断网络状态"""

    import requests
    from requests.exceptions import ReadTimeout,HTTPError,RequestException
    
    try:
        trynet = requests.get("http://vlsmb.ys168.com",timeout=1)
    except ReadTimeout:
        print("网络超时！请检查网络速度！")
        return False
    except HTTPError:
        print("HTTP协议错误！")
        return False
    except RequestException:
        print("请求网络服务失败！")
        return False
    return True

    if trynet.status_code == 403:
        print("403：访问服务器被拒绝！")
        print("请手动浏览http://vlsmb.ys168.com寻找相关文件并下载。")
        return False
    if trynet.status_code == 404:
        print("404：找不到下载网站！请联系汉化组寻找相关信息！")
        return False

