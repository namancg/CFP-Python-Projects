import datetime
import re

import scrapy

from techcrunch.items import BlogPost


class TechcrunchspiderSpider(scrapy.Spider):
    name = 'techcrunchSpider'
    allowed_domains = ['techcrunch.com']
    start_urls = ['http://techcrunch.com/']

    def parse(self, response):
        """
        In the parse method, we extract the next page number thanks to a regex on the url. Then we compare it to the
        limit_pages argument, and only if it’s below, we enqueue the next page request.
        """
        for post in response.css(".post-block"):
            title = post.css(".post-block__title__link")
            url = title.css("::attr(href)").extract_first()
            yield scrapy.Request(url, callback=self.parse_post)
        if response.css(".load-more"):
            next_page_url = response.css(".load-more::attr(href)").extract_first()
            # urls look like https://techcrunch.com/page/4/
            match = re.match(r".*\/page\/(\d+)\/", next_page_url)
            next_page_number = int(match.groups()[0])
            if next_page_number <= self.limit_pages:
                yield scrapy.Request(next_page_url)

    def __init__(self, limit_pages=None, *args, **kwargs):
        super(TechcrunchspiderSpider, self).__init__(*args, **kwargs)
        if limit_pages is not None:
            self.limit_pages = int(limit_pages)
        else:
            self.limit_pages = 0

    def parse_post(self, response):
        item = BlogPost(
            title=response.css("h1::text").extract_first(),
            author=response.css(".article__byline>a::text").extract_first().strip(),
            published_at=self.extract_post_date(response),
            content=self.extract_content(response),
            url=response.url
        )
        yield (item)

    def extract_post_date(self, response):
        date_text = response.css("meta[name='sailthru.date']::attr(content)").extract_first()
        return datetime.datetime.strptime(date_text, "%Y-%m-%d %H:%M:%S")

    def extract_content(self, response):
        """
        EXTRACTING CONTECT AND JOINING IT SO THAT IT CAN BE READ BY HUMAN
        :param response:
        :return:
        """
        paragraphs_texts = [
            p.css(" ::text").extract()
            for p in response.css(".article-content>p")
        ]
        paragraphs = ["".join(p) for p in paragraphs_texts]
        paragraphs = [re.subn("\n", "", p)[0] for p in paragraphs]
        paragraphs = [p for p in paragraphs if p.strip() != ""]
        return "\n\n".join(paragraphs)
