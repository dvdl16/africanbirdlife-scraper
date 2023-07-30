import os
import urllib
import scrapy
import re


class BirdLifeMagazineSpider(scrapy.Spider):
    name = 'birdlife_magazine_spider'
    start_urls = ['https://www.birdlife.org.za/african-birdlife-index/']

    def parse(self, response):
        for year_group in response.css('.vc_tta-panel'):
            year = year_group.css('.vc_tta-title-text::text').get().strip()
            year_directory = os.path.join('magazines', year)
            os.makedirs(year_directory, exist_ok=True)

            for magazine_div in year_group.css('.wpb_column.vc_column_container.vc_col-sm-2'):
                magazine_name = magazine_div.css('div.wpb_wrapper strong::text').get().strip()
                magazine_name = re.sub(r'[/:]', '-', magazine_name)  # Replace "/" with "-"
                magazine_directory = os.path.join(year_directory, magazine_name)
                os.makedirs(magazine_directory, exist_ok=True)

                magazine_page_url = magazine_div.css('a::attr(href)').get()
                if magazine_page_url:
                    yield scrapy.Request(magazine_page_url, 
                                         callback=self.parse_magazine_page,
                                         cb_kwargs=dict(year=year, magazine_name=magazine_name, magazine_directory=magazine_directory))

    def parse_magazine_page(self, response, year, magazine_name, magazine_directory):
        for download_link in response.css('.wpdmdl-btn a::attr(data-downloadurl)'):
            download_url = download_link.get()
            filename = download_url.split('/')[-2] + '.pdf'
            filepath = os.path.join(magazine_directory, filename)
            urllib.request.urlretrieve(download_url, filepath)
            yield {
                'year': year,
                'magazine_name': magazine_name,
                'download_url': download_url,
                'filepath': filepath,
            }
