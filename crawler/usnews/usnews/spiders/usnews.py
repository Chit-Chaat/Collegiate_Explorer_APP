import scrapy
import re

USNEWS_URL = 'https://www.usnews.com'

class USNewsSeedSpider(scrapy.Spider):
    name = 'usnewsseeds'
    start_urls = open('usnews_seed.txt' ,'r').read().splitlines()

    def parse(self, response):
        f = open('usnews_seeds.txt', 'a+')
        for url in response.css('div h3 ::attr(href)').extract():
            f.write(USNEWS_URL + url + '\n')
        f.close()

class USNewsRankSpider(scrapy.Spider):
    name = "usnewsrank"
    start_urls = open('usnewsrank_seeds.txt', 'r').read().splitlines()

    def parse(self, response):
        rankings = []
        for el in response.css('ul.BadgeList-wn7t98-1.bDZATU.mt0.pl0.t3.md-t4.lg-t4 li.BadgeList__ListItem-wn7t98-0.dRyVhI'):
            rankings.append(' '.join(el.css('strong::text').extract()))

        yield {
            'school' : re.sub(' +', ' ', ' '.join(response.css('h2.Heading__HeadingStyled-sc-1w5xk2o-0-h2.bmsqcu.Heading-sc-1w5xk2o-1.Wakanda__Title-rzha8s-10.kiCVGj ::text').extract())),
            'usnewsRank' : rankings
        }


class USNewsSpider(scrapy.Spider):
    name = "usnews"
    start_urls = open('usnews_seeds.txt', 'r').read().splitlines()

    def parse(self, response):
        yield {
            'url' : response.url,
            'school' : re.sub(' +', ' ', ' '.join(response.css('h1.Heading__HeadingStyled-sc-1w5xk2o-0.bSrbmR.Heading-sc-1w5xk2o-1.Wakanda__Title-rzha8s-10.kiCVGj ::text').extract())),
            'overview' : response.css('div.Raw-slyvem-0.util__RawContent-sc-1kd04gx-2.dkHTIy p::text').get(),
            'acceptRate' : response.css('p.Paragraph-sc-1iyax29-0.Section__DataCell-ply21t-2.hKEGVs ::text').extract()[2],
            'website' : response.css('a.Anchor-byh49a-0.Summary__WebsiteAnchor-jca3qn-0.jiYyth.optly-school-website ::attr(href)').get(),
            'address': re.sub(' +', ' ', ' '.join(response.css("p.Paragraph-sc-1iyax29-0.fOjiwz.Hide-kg09cx-0.eEcEPJ ::text").extract()).split('|')[0].strip())
        }

class USNewsAcademicSpider(scrapy.Spider):
    name = "usnewsacademics"
    start_urls = map(lambda s: s + '/academics', open('usnews_seeds.txt', 'r').read().splitlines())

    def parse(self, response):
        yield {
            'school' : re.sub(' +', ' ', ''.join(response.css('h2.Heading__HeadingStyled-sc-1w5xk2o-0-h2.bmsqcu.Heading-sc-1w5xk2o-1.Wakanda__Title-rzha8s-10.kiCVGj ::text').extract())),
            'academics' : response.css('div.summary-box ::text').extract()[1]
        }

