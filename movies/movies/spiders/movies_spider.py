from pathlib import Path
from typing import Any
import scrapy
from scrapy.http import Response
from movies.items import MoviesItem

class Movies(scrapy.Spider):
    name = "movies"

    def start_requests(self):
        urls = ["https://uhdmovies.fans/"]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        item = MoviesItem()
        for movies in response.css("article"):
            item['movies_image_link'] = movies.css(".entry-image a img").xpath("@src").get ()
            item['movies_name'] = movies.css(".box-inner-p a .sanket::text").get()
            item['movies_link_for_download'] = movies.css(".box-inner-p a::attr(href)").get()
            yield item
        
        next_page = response.css(".next::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)