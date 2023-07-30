from spider import BirdLifeMagazineSpider

def main():
    # Run the spider
    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess()
    process.crawl(BirdLifeMagazineSpider)
    process.start()


if __name__ == "__main__":
    main()