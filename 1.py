import requests
import time

def visit_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("访问成功:")
            print(response.text)
        else:
            print("访问失败:", response.status_code)
    except Exception as e:
        print("发生异常:", e)

if name == "__main__":
    url = "http://www.hkyuancheng.lol:5679/mytv.php?id=P"
    visit_frequency = 300  # 300秒 = 5分钟

    while True:
        visit_website(url)
        time.sleep(visit_frequency)
