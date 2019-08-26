import scrapy

class BookSpider(scrapy.Spider):
	name = "bookspider"
	start_urls = ['https://books.toscrape.com']

	def parse(self,response):
		for book in response.css("article.product_pod"):
			yield {
				'price': book.css(".price_color::text").extract_first(),
				'title': book.css("h3 > a::attr(title)").extract_first()
				}

			next = response.css(".next > a::attr(href)").extract_first()
			if next:
				yield response.follow(next, self.parse)