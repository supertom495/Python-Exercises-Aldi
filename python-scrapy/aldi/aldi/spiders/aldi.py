import scrapy


class AldiSpider(scrapy.Spider):
    name = 'aldi'

    def start_requests(self):
        urls = [
            'https://www.aldi.com.au/',
        ]
        yield scrapy.Request(url=urls[0], callback=self.parse)

    def parse(self, response):

        # get the navigation bar
        nav = response.css('nav') 

        # get the list
        lis = nav.xpath('//li[contains(@class, "main-nav--item ym-clearfix")]')

        x = 0
        # output results to text.txt
        with open('text.txt', 'w+') as f:
            # get the elements from the list
            for entry in lis:
                text = entry.xpath('.//a[contains(@class, "main-nav--item--link")]/text()')
                # get the each element
                for i in text:
                    if (len(i.get()) > 0):
                        if x != 0:
                            f.write("\t")
                        x+=1
                        f.write(i.get())
                        f.write("\n")
                f.write("\n")
                x = 0
