import re
import time
import scrapy

class DBpediaSpider(scrapy.Spider):
    name = "dbpedia"
    start_urls = open('dbpedia_seed.txt', 'r').read().splitlines()

    def parse(self, response):

        affiliation = []
        athletics = []
        campus = None
        president = None
        state = None
        website = None
        schoolColor = []
        motto = []
        numberOfStudents = None
        founded = None
        mascot = None

        item = response.xpath('/html/body/div/div/div/table/tr/td[2]/ul/li/span/a').extract()
        for i in range(len(item)):
            if list(re.finditer('rel="dbo:affiliation"', item[i])):
                affiliation.append(' '.join(response.xpath('/html/body/div/div/div/table/tr/td[2]/ul/li/span/a/text()').extract()[i][1:].split('_')))
            if list(re.finditer('rel="dbo:athletics"', item[i])):
                athletics.append(' '.join(response.xpath('/html/body/div/div/div/table/tr/td[2]/ul/li/span/a/text()').extract()[i][1:].split('_')))
            if list(re.finditer('rel="dbo:campus"', item[i])):
                campus = ' '.join(response.xpath('/html/body/div/div/div/table/tr/td[2]/ul/li/span/a/text()').extract()[i][1:].split('_'))
            if list(re.finditer('rel="dbo:president"', item[i])):
                president = ' '.join(response.xpath('/html/body/div/div/div/table/tr/td[2]/ul/li/span/a/text()').extract()[i][1:].split('_'))
            if list(re.finditer('rel="dbo:state"', item[i])):
                state = response.xpath('/html/body/div/div/div/table/tr/td[2]/ul/li/span/a/text()').extract()[i][1:]
            if list(re.finditer('rel="foaf:homepage nofollow"', item[i])):
                website = response.xpath('/html/body/div/div/div/table/tr/td[2]/ul/li/span/a/text()').extract()[i]

        item = response.xpath('/html/body/div/div/div/table/tr/td[2]/ul/li/span/span').extract()
        for i in range(len(item)):
            if list(re.finditer('span property="dbo:officialSchoolColour"', item[i])):
                schoolColor.append(response.xpath('/html/body/div/div/div/table/tr/td[2]/ul/li/span/span/text()').extract()[i])
            if list(re.finditer('span property="dbo:motto"', item[i])):
                motto.append(response.xpath('/html/body/div/div/div/table/tr/td[2]/ul/li/span/span/text()').extract()[i])
            if list(re.finditer('span property="dbo:numberOfStudents"', item[i])):
                numberOfStudents = int(response.xpath('/html/body/div/div/div/table/tr/td[2]/ul/li/span/span/text()').extract()[i])
            if list(re.finditer('span property="dbo:foundingDate"', item[i])):
                founded = response.xpath('/html/body/div/div/div/table/tr/td[2]/ul/li/span/span/text()').extract()[i]
            if list(re.finditer('span property="dbo:mascot"', item[i])):
                mascot = response.xpath('/html/body/div/div/div/table/tr/td[2]/ul/li/span/span/text()').extract()[i]

        yield {
            'url' : response.url,
            'school' : ' '.join(response.css('h1 a::text').extract()).strip(),
            'affiliation' : affiliation,
            'athletics' : athletics,
            'setting' : campus,
            'president' : president,
            'state' : state,
            'website' : website,
            'schoolColor': schoolColor,
            'motto' : motto,
            'numberOfStudents' : numberOfStudents,
            'founded' : founded,
            'mascot' : mascot
        }
