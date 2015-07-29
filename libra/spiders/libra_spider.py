import scrapy
import re
import datetime as date
import urlparse

from libra.items import LibraItem

class LibraSpider(scrapy.Spider):
    name = "libra"
    start_urls = []
    urlPrefix = 'http://shuju.wangdaizhijia.com/pingji_'
    startTime = date.date(2013, 4, 1)
    endTime = date.date(2013, 4, 1)

    def __init__(self):
        currentTime = self.startTime
        timeDelta = date.timedelta(months=1)
        while(currentTime <= self.endTime):
            ratingDate = currentTime.strftime('%Y%m')
            urlStr = self.urlPrefix + ratingDate
            self.start_urls.append(urlStr)
            currentTime += timeDelta

        print self.start_urls

    def parse(self, response):
        items = []
        # get all rows
        rows = response.xpath('//table[@class="ratetable"]/tr')

        # iterate all row
        for i, row in enumerate(rows):
            # drop title
            if i == 0:
                continue

            # start to extract data
            item = self.extractRowData(row)
            # add datetime
            datetime = self.getURLDateTime(response.url)
            item['datetime'] = datetime
            items.append(item)

        return items

    def extractRowData(self, row):
        item = LibraItem()
        cells = row.xpath('td')
        # get platformId
        linkHref = cells[1].css('a::attr(href)').extract()[0]
        item['platformId'] = self.getInt(linkHref)
        # get platformName
        item['platformName'] = cells[1].css('a::text').extract()[0]
        # get developNumber
        cellContent = cells[2].css('span b::text').extract()[0]
        developNumber = self.getFloat(developNumber)
        item['developNumber'] = developNumber
        # get onlineDate
        cellContent = cells[3].xpath('text()').extract();
        item['onlineDate'] = self.getOnlineDate(cellContent)
        # get city
        cellContent = cells[4].css('span::text').extract()[0]
        cellContents = cellContent.split('|')
        item['city'] = cellContents[0]
        item['district'] = cellContents[1]
        # get turnover
        cellContent = cells[5].xpath('text()').extract()
        item['turnover'] = self.getFloat(cellContent)
        # get popularity
        cellContent = cells[6].xpath('text()').extract()
        item['popularity'] = self.getFloat(cellContent)
        # get income
        cellContent = cells[7].css('label::text').extract()[0]
        item['income'] = self.getFloat(cellContent)
        # get divergence
        cellContent = cells[8].xpath('text()').extract()
        item['divergence'] = self.getFloat(cellContent)
        # get fluidity
        cellContent = cells[9].xpath('text()').extract()
        item['fluidity'] = self.getFloat(cellContent)
        # get transparency
        cellContent = cells[10].xpath('text()').extract()
        item['transparency'] = self.getFloat(cellContent)

        # print item

        return item

    def getInt(self, str):
        str = str.replace(',', '')
        intPattern = re.compile(r'\d+')
        match = intPattern.search(str)
        if match:
            return int(match.group())
        else:
            return 0

    def getFloat(self, str):
        str = str.replace(',', '')
        floatPattern = re.compile(r'\d+\.\d*')
        match = floatPattern.search(str)
        if match:
            return float(match.group())
        else:
            return 0

    def getOnlineDate(self, str):
        dates = str.split('.')
        return date.date(int(dates[0]), int(dates[1]))

    def getURLDateTime(self, url):
        datePattern = re.compile(r'\d+')
        match = datePattern.search(url)
        if match:
            return date.date(int(match.group()[0:4]), int(match.group()[4:]))
        else:
            return date.date()



