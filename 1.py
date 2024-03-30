import requests

def visit_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("访问成功：", url)
        else:
            print("访问失败：", url)
    except Exception as e:
        print("访问出错：", e)

if __name__ == "__main__":
    url = "http://www.hkyuancheng.lol:5679/mytv.php?id=J"  # 将此处的链接替换为你想要访问的链接
    visit_url(url)