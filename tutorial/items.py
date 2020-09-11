# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field
from scrapy.loader.processors import MapCompose, TakeFirst
from datetime import datetime


def remove_quotes(text):
    # strip the unicode quotes
    text = text.strip(u'\u201c'u'\u201d')
    return text


def convert_date(text):
    # convert string March 14, 1879 to Python date
    return datetime.strptime(text, '%B %d, %Y')


def parse_location(text):
    # parse location "in Ulm, Germany"
    # this simply remove "in ", you can further parse city, state, country, etc.
    return text[3:]


# class QuoteItem(Item):
#     quote_content = Field(
#         input_processor=MapCompose(remove_quotes),
#         # TakeFirst return the first value not the whole list
#         output_processor=TakeFirst()
#         )
#     author_name = Field(
#         input_processor=MapCompose(str.strip),
#         output_processor=TakeFirst()
#         )
#     author_birthday = Field(
#         input_processor=MapCompose(convert_date),
#         output_processor=TakeFirst()
#     )
#     author_bornlocation = Field(
#         input_processor=MapCompose(parse_location),
#         output_processor=TakeFirst()
#     )
#     author_bio = Field(
#         input_processor=MapCompose(str.strip),
#         output_processor=TakeFirst()
#         )
#     tags = Field()

class CarSparePart(Item):
    _id = Field()
    ad_id = Field()
    image = Field()
    category_name =Field()
    category_id =Field()
    images_count = Field()
    is_boost = Field()
    is_top = Field()
    paid_info = Field()
    price=Field()
    price_obj=Field()
    region_name=Field()
    region_slug=Field()
    short_description=Field()
    title=Field()
    api_url=Field()
    web_url=Field()
    user_id=Field()
    user_phone=Field()
    tops_count=Field()
    attributes=Field()
    badge_info=Field()
    booster_info=Field()
    count_views=Field()
    date_created=Field()
    date_edited=Field()
    date_moderated=Field()
    fav_count=Field()
    description=Field()
    images=Field()
    images_data=Field()
    is_active= Field()
    is_closed=Field()
    is_request_seller_to_call_back_show=Field()
    price_history=Field()
    services_info=Field()
    similar_ads_href=Field()
    status_color=Field()
    status=Field()
    seller=Field()
    og_title=Field()
    og_url=Field()
    og_product_data=Field()
    breadcrumbs_data=Field()
    crawled_at=Field()
    price_currency=Field()
