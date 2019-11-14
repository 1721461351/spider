import requests
import json
import re
import urllib3



class doubanspider:

    def __init__(self):
        self.temp_url = "https://movie.douban.com/j/new_search_subjects?sort=S&range=0,10&tags=&start={}&genres=恐怖"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}

    def parse_url(self, url):
        reponse = requests.get(url=url, headers=self.headers, verify=False)
        return reponse.content.decode()
        print(url)

    def get_content_list(self, json_str):
        dict_ret = json.loads(json_str)
        data = dict_ret["data"]
        return data

    def save_content(self, data):
        with open("douban.txt", "a",encoding="utf-8") as f:
            for content in data:
                # todo
                f.write(json.dumps(content, ensure_ascii=False))
                f.write("\n")
            print("保存成功")

    def run(self):
        urllib3.disable_warnings()
        num = 0
        while True:
            url = self.temp_url.format(num)
            print(url)
            # 1.解析url
            json_str = self.parse_url(url)
            # print(html_str)
            # 2.提取数据
            data = self.get_content_list(json_str)
            # print(data)
            # 3.保存
            self.save_content(data)

            if len(data) < 20:
                break

            num += 20


if __name__ == '__main__':
    doubanspider = doubanspider()
    doubanspider.run()
