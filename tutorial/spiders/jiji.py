import scrapy
import json
from tutorial.items import CarSparePart

class QuotesSpider(scrapy.Spider):
    name = "jiji"
    start_urls = [
        'https://jiji.co.ke/api_web/v1/listing?slug=car-parts-and-accessories&page=0'
        ]

    def get_item_api_url(self, full_url):
        item_api_url_base = 'https://jiji.co.ke/api_web/v1/item/'
        root_url = full_url.split('.html')[0]
        url = item_api_url_base + root_url.split('-')[len(root_url.split('-')) - 1]
        return url
         
    def parse(self, response):
        page_res = json.loads(response.body)
        if len(page_res['adverts_list']['adverts']) > 0:
            for ad in page_res['adverts_list']['adverts']:
                item_url = self.get_item_api_url(ad['url'])
                print('Fetching: ', item_url)
                yield response.follow(item_url, callback=self.process_item)

        if page_res['next_url'] is not None:
            print("Next fetch:", page_res['next_url'])
            yield response.follow(page_res['next_url'], self.parse)

    def process_item(self, response):
        advert_data_full = json.loads(response.body)
        advert_data = advert_data_full['advert']
        ad_category = advert_data['category_slug']
        if ad_category != 'car-parts-and-accessories':
            print('Ad from different category', ad_category)
        else:
            item = CarSparePart()
            
            item['ad_id'] = advert_data['id']
            item['_id'] = advert_data['id']
            item['images'] = advert_data['images']
            item['og_url'] = advert_data_full['seo']['og_url']
            item['api_url'] = advert_data_full['seo']['web_url']
            item['og_product_data'] = advert_data_full['seo']['og_product_data']
            item['og_title'] = advert_data_full['seo']['og_title']
            item['description'] = advert_data['description']
            item['category_name'] = advert_data['category_name']
            item['category_id'] = advert_data['category_id']
            item['seller']=advert_data_full['seller']
            item['price_obj'] = advert_data['price']
            item['region_name'] = advert_data['region_name']
            item['region_slug'] = advert_data['region_slug']
            item['price_history'] = advert_data['price_history']
            item['status_color'] = advert_data['status_color']
            item['breadcrumbs_data'] = advert_data_full['breadcrumbs_data']
            item['is_active'] = advert_data['is_active']
            item['is_closed'] = advert_data['is_closed']
            item['price'] = advert_data_full['seller']['advert_price']
            item['date_created'] = advert_data['date_created']
            item['date_edited'] = advert_data['date_edited']
            item['date_moderated'] = advert_data['date_moderated']
            item['fav_count'] = advert_data['fav_count']
            item['user_phone'] = advert_data_full['seller']['phone']
            item['services_info'] = advert_data['services_info']
            item['images_count'] = advert_data['count_images']
            item['count_views'] = advert_data['count_views']
            item['attributes'] = advert_data['attributes']
            item['similar_ads_href'] = advert_data['similar_ads_href']
            item['status'] = advert_data['status']
            yield item