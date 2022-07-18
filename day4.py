# https://ssr1.scrape.center/ 爬取网址
import json
import multiprocessing
import requests
import logging
import re
from urllib.parse import urljoin
from os import makedirs
from os.path import exists

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s : %(message)s')

BASE_URL = 'https://ssr1.scrape.center'
TOTAL_PACE = 10
RESULT_DIR = 'results'
exists(RESULT_DIR) or makedirs(RESULT_DIR)


def save_data(data):
    name = data.get('name')
    data_path = f'{RESULT_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


def scrapy_page(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code %s while scraping %s', response.status_code, url)

    except requests.RequestException:
        logging.error('error occurred while scraping %s', url, exc_info=True)


def scrapy_index(page):
    index_url = f'{BASE_URL}/page/{page}'
    return scrapy_page(index_url)


def scrapy_detail(url):
    return scrapy_page(url)


def parse_index(html):
    pattern = re.compile('<a.*?href="(.*?)".*?class="name"')
    items = re.findall(pattern, html)
    if not items:
        return []
    for item in items:
        detail_url = urljoin(BASE_URL, item)
        logging.info('get detail url %s', detail_url)
        yield detail_url


def parse_detail(html):
    cover_pattern = re.compile('<div.*?class="item.*?">.*?<img.*?src="(.*?)".*?class="cover"', re.S)
    name_pattern = re.compile('<h2.*?>(.*?)</h2>')
    categories_pattern = re.compile('<button.*?category.*?>.*?<span>(.*?)</span>.*?</button>', re.S)
    published_at_pattern = re.compile('(\d{4}-\d{2}-\d{2})\s?上映')
    drama_pattern = re.compile('<div.*?drama.*?>.*?<p.*?>(.*?)</p>', re.S)
    score_pattern = re.compile('<p.*?score.*?>(.*?)</p>', re.S)
    cover = re.search(cover_pattern, html).group(1).strip() if re.search(cover_pattern, html) else None
    name = re.search(name_pattern, html).group(1).strip() if re.search(name_pattern, html) else None
    categories = re.findall(categories_pattern, html) if re.findall(categories_pattern, html) else []
    published = re.search(published_at_pattern, html).group(1) if re.search(published_at_pattern, html) else None
    drama = re.search(drama_pattern, html).group(1).strip() if re.search(drama_pattern, html) else None
    score = float(re.search(score_pattern, html).group(1).strip()) if re.search(score_pattern, html) else None
    return {
        # 封面
        'cover': cover,
        # 名称
        'name': name,
        # 类别
        'categories': categories,
        # 上映时间
        'published': published,
        'drama': drama,
        'score': score
    }


# def main():
#     for page in range(1, TOTAL_PACE + 1):
#         index_html = scrapy_index(page)
#         detail_urls = parse_index(index_html)
#         # logging.info('detail urls %s', list(detail_urls))
#         for detail_url in detail_urls:
#             detail_html = scrapy_detail(detail_url)
#             data = parse_detail(detail_html)
#             logging.info('detail data %s', data)
#             logging.info('saving data to json file')
#             save_data(data)
#             logging.info('data saved successfully')

# 多进程抓取
def main(page):
    index_html = scrapy_index(page)
    detail_urls = parse_index(index_html)
    for detail_url in detail_urls:
        detail_html = scrapy_detail(detail_url)
        data = parse_detail(detail_html)
        logging.info('detail data %s', data)
        logging.info('saving data to json file')
        save_data(data)
        logging.info('data saved successfully')


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pages = range(1, TOTAL_PACE + 1)
    pool.map(main, pages)
    pool.close()
    pool.join()
