import requests
from bs4 import BeautifulSoup

from items import ArticleItem


class ArticleCrawler:
    link = "https://pubs.acs.org/toc/jacsat/142/3"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    r = requests.get(link, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    article_info_list = soup.find_all("div", class_="issue-item clearfix")
    # 新建字典列表
    articleList = []
    for i in range(len(article_info_list)):
        item_info = ArticleItem()
        # 标题
        article_title = article_info_list[i].find("h5", class_="issue-item_title").a.text.strip()
        item_info.title = article_title

        # 作者
        article_author_list = article_info_list[i].find_all("span", class_="hlFld-ContribAuthor")
        author = []
        for j in range(len(article_author_list)):
            article_author = article_author_list[j].text.strip()
            author.append(article_author)
        item_info.author = author

        # 页码
        pub_year = article_info_list[i].find("span", class_="issue-item_year").text.strip()
        pub_volumn = article_info_list[i].find("span", class_="issue-item_vol-num").text.strip()
        pub_issue = article_info_list[i].find("span", class_="issue-item_issue-num").text.strip()
        pub_range = article_info_list[i].find("span", class_="issue-item_page-range").text.strip()
        page_info = pub_year + ',' + pub_volumn + ',' + pub_issue + ',' + pub_range
        item_info.pageInfo = page_info

        # 图片
        pic_info = article_info_list[i].find("div", class_="issue-item_img")
        if pic_info is not None:
            pic_relative_url = pic_info.find("img").get("data-original")
            pic_url = 'https://pubs.acs.org' + pic_relative_url
            item_info.pic_url = pic_url

        # 链接
        article_url = 'https://pubs.acs.org' + article_info_list[i].find("div", class_="issue-item_footer").find("a",
                                                                                                                 title="PDF").get(
            "href")

        articleList.append(item_info)

    print(articleList)
