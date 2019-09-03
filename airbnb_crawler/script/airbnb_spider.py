# coding=utf8

import requests
import json
import csv


class Airbnb():
    def __init__(self):
        pass

    def crawl(self):
        with open('detail_urls.txt', 'r') as f:
            urls = f.readlines()
            for i, url in enumerate(urls):
                try:
                    print('爬取第%d个url' % i)
                    print('url = ' + url)
                    self.crawl_detail(url)
                except:
                    print('bug url = ' + url)
                    continue

    def crawl_detail(self, url):
        room_id = url.split('?')[0].split('/')[-1]
        # print(room_id)
        detail_link = 'https://www.airbnb.cn/api/v2/pdp_listing_details/' + room_id + '?_format=for_rooms_show&adults=1&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&'
        ret = json.loads(requests.get(detail_link).content)
        pdp_listing_detail = ret.get('pdp_listing_detail')
        # 名称
        room_name = pdp_listing_detail.get('name').replace('\n', '').replace('\t', '').strip()
        room_type = pdp_listing_detail.get('room_and_property_type')
        bathroom_label = pdp_listing_detail.get('bathroom_label')
        bed_label = pdp_listing_detail.get('bed_label')
        bedroom_label = pdp_listing_detail.get('bedroom_label')
        guest_label = pdp_listing_detail.get('guest_label')
        visible_review_count = pdp_listing_detail.get('visible_review_count')
        sorted_reviews = pdp_listing_detail.get('sorted_reviews')
        summary = pdp_listing_detail.get('sectioned_description').get('summary')
        neighborhood_overview = pdp_listing_detail.get('sectioned_description').get('neighborhood_overview')
        transit = pdp_listing_detail.get('sectioned_description').get('transit')


        # print(room_name)
        # print(room_type)
        # print(bathroom_label)
        # print(bed_label)
        # print(bedroom_label)
        # print(guest_label)
        # print(visible_review_count)

        comment_writer = csv.writer(open('room_review.csv', 'a', encoding='utf-8-sig'))
        for review in sorted_reviews:
            comment = review.get('comments')
            created_at = review.get('created_at').strip()

            comment_writer.writerow([room_name, created_at, comment])

        visible_review_count = int(visible_review_count)
        comment_page_num = visible_review_count // 7 + 1
        for i in range(1, comment_page_num):
            more_comment_link = 'https://www.airbnb.cn/api/v2/reviews?currency=CNY&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&locale=zh&listing_id=%s&role=guest&_format=for_p3&_limit=7&_offset=%d&_order=language_country' % (
                room_id, 7 * i)
            reviews = json.loads(requests.get(more_comment_link).content).get('reviews')
            for review in reviews:
                comment = review.get('comments')
                created_at = review.get('created_at').strip()

                comment_writer.writerow([room_name, created_at, comment])

        price_url = 'https://www.airbnb.cn/api/v2/pdp_listing_booking_details?_format=for_web_dateless&_intents=p3_book_it&_interaction_type=pageload&currency=CNY&force_boost_unc_priority_message_type=&guests=1&listing_id=%s&locale=zh&number_of_adults=1&number_of_children=0&number_of_infants=0&show_smart_promotion=0&key=d306zoyjsyarp7ifhu67rjxn52tv0t20' % room_id
        price_ret = json.loads(requests.get(price_url).content)
        price = price_ret.get('pdp_listing_booking_details')[0].get('p3_display_rate').get('amount')
        # print(price)

        detail_write = csv.writer(open('room_detail.csv', 'a', encoding='utf-8-sig'))
        # f.write(room_name + ',')
        # f.write(room_type)
        # f.write(bathroom_label)
        # f.write(bed_label)
        # f.write(bedroom_label)
        # f.write(guest_label)
        # f.write(price)
        # f.write(visible_review_count)
        detail_write.writerow(
            [room_name, url, room_type, bathroom_label, bed_label, bedroom_label, guest_label, price, visible_review_count, summary, neighborhood_overview, transit])


def main():
    airbnb = Airbnb()
    airbnb.crawl()


if __name__ == '__main__':
    main()
