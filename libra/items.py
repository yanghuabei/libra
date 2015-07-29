# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LibraItem(scrapy.Item):
    # 平台id
    platformId = scrapy.Field()
    # 平台名称
    platformName = scrapy.Field()
    # 发展指数 0
    developNumber = scrapy.Field()
    # 上线时间 1
    onlineDate = scrapy.Field()
    # 所在城市 2
    city = scrapy.Field()
    # 所在区域 3
    district = scrapy.Field()
    # 成交量 4
    turnover = scrapy.Field()
    # 人气 5
    popularity = scrapy.Field()
    # 收益 6
    income = scrapy.Field()
    # 分散度 7
    divergence = scrapy.Field()
    # 流动性 8
    fluidity = scrapy.Field()
    # 透明度 9
    transparency = scrapy.Field()
    # 时间
    datetime = scrapy.Field()
