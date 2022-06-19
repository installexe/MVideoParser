
import encodings
import requests
import json




def get_data():
    cookies = {
    '_ym_d': '1644574447',
    '_ym_uid': '1644574447602028032',
    'cfidsgib-w-mvideo': 'e0JwGT02rlis/1NgfpeC3oCw9i+FravW47dKUhsA++4PykDkZrk2DxK4qd6FjVHyoMTZhrNPaWOPUk8v1v2WdF3VXjvRDtvO+x26PC1FoevGG5MxpVmAn6O0VOviHNgKYLMU2z/+SqOYdjnBGZRQbQC18D7vTUG0iOWyCuE=',
    '__lhash_': '33364dcda7e9c1200918d05b849f19c4',
    'CACHE_INDICATOR': 'false',
    'COMPARISON_INDICATOR': 'false',
    'HINTS_FIO_COOKIE_NAME': '1',
    'MAIN_PAGE_VARIATION_1': '1',
    'MVID_2_exp_in_1': '1',
    'MVID_AB_SERVICES_DESCRIPTION': 'var4',
    'MVID_ADDRESS_COMMENT_AB_TEST': '2',
    'MVID_BLACK_FRIDAY_ENABLED': 'true',
    'MVID_CALC_BONUS_RUBLES_PROFIT': 'true',
    'MVID_CART_MULTI_DELETE': 'true',
    'MVID_CATALOG_STATE': '1',
    'MVID_CITY_ID': 'CityCZ_975',
    'MVID_FILTER_CODES': 'true',
    'MVID_FILTER_TOOLTIP': '1',
    'MVID_FLOCKTORY_ON': 'true',
    'MVID_GEOLOCATION_NEEDED': 'true',
    'MVID_GET_LOCATION_BY_DADATA': 'DaData',
    'MVID_GIFT_KIT': 'true',
    'MVID_GUEST_ID': '20907421026',
    'MVID_IS_NEW_BR_WIDGET': 'true',
    'MVID_KLADR_ID': '7700000000000',
    'MVID_LAYOUT_TYPE': '1',
    'MVID_LP_SOLD_VARIANTS': '3',
    'MVID_NEW_ACCESSORY': 'true',
    'MVID_NEW_DESKTOP_FILTERS': 'true',
    'MVID_NEW_LK': 'true',
    'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
    'MVID_NEW_LK_LOGIN': 'true',
    'MVID_NEW_LK_MENU_BUTTON': 'true',
    'MVID_NEW_LK_OTP_TIMER': 'true',
    'MVID_NEW_MBONUS_BLOCK': 'true',
    'MVID_NEW_SUGGESTIONS': 'true',
    'MVID_PDP_MAP_DEFAULT': 'true',
    'MVID_PROMO_CATALOG_ON': 'true',
    'MVID_REGION_ID': '1',
    'MVID_REGION_SHOP': 'S002',
    'MVID_SERVICES': '111',
    'MVID_SERVICES_MINI_BLOCK': 'var2',
    'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'old',
    'MVID_TIMEZONE_OFFSET': '3',
    'MVID_WEBP_ENABLED': 'true',
    'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
    'PICKUP_SEAMLESS_AB_TEST': '2',
    'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'false',
    'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
    'flacktory': 'no',
    'searchType2': '2',
    'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
    'SMSError': '',
    'authError': '',
    'advcake_track_id': '1a802648-7741-af45-6753-b09e7e1de8ba',
    'advcake_session_id': '70e6eab1-fafd-d173-e012-d9c8d603c2fa',
    '_gid': 'GA1.2.1192785618.1655630019',
    'tmr_lvid': '846f2c4fef1859024160015154a81c89',
    'tmr_lvidTS': '1644574460413',
    '_ym_isad': '1',
    'flocktory-uuid': '52f0ab63-20fe-4ab4-8960-5672369ab898-1',
    'afUserId': 'ad14a9d2-5265-47d1-b1b5-8a2ccedbbfdf-p',
    'AF_SYNC': '1655630020032',
    'BIGipServeratg-ps-prod_tcp80': '1694817290.20480.0000',
    'bIPs': '1613809182',
    'wurfl_device_id': 'generic_web_browser',
    'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
    'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
    'BIGipServeratg-ps-prod_tcp80_clone': '1694817290.20480.0000',
    'mindboxDeviceUUID': '950547bb-5dfc-4065-9ab8-8da5be85c063',
    'directCrm-session': '%7B%22deviceGuid%22%3A%22950547bb-5dfc-4065-9ab8-8da5be85c063%22%7D',
    '_ga': 'GA1.1.198893861.1655630019',
    'tmr_detect': '1%7C1655630057436',
    'MVID_ENVCLOUD': 'primary',
    '_dc_gtm_UA-1873769-37': '1',
    'JSESSIONID': 'jlPMvnzDqYJNnBp3J42jBq1C1J85XmJhXgJgM2v2SC4wFGgLnkGc!-1247462178',
    'tmr_reqNum': '214',
    '_ga_CFMZTSS5FM': 'GS1.1.1655632720.2.1.1655632772.0',
    '_ga_BNX5WPP3YK': 'GS1.1.1655632720.2.1.1655632772.8',
    'ADRUM_BT': 'R:92|g:433fbf9e-2893-4426-9590-f8bc2d4cf4828194345',
}

    headers = {
    'authority': 'www.mvideo.ru',
    'accept': 'application/json',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': '_ym_d=1644574447; _ym_uid=1644574447602028032; cfidsgib-w-mvideo=e0JwGT02rlis/1NgfpeC3oCw9i+FravW47dKUhsA++4PykDkZrk2DxK4qd6FjVHyoMTZhrNPaWOPUk8v1v2WdF3VXjvRDtvO+x26PC1FoevGG5MxpVmAn6O0VOviHNgKYLMU2z/+SqOYdjnBGZRQbQC18D7vTUG0iOWyCuE=; __lhash_=33364dcda7e9c1200918d05b849f19c4; CACHE_INDICATOR=false; COMPARISON_INDICATOR=false; HINTS_FIO_COOKIE_NAME=1; MAIN_PAGE_VARIATION_1=1; MVID_2_exp_in_1=1; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_CALC_BONUS_RUBLES_PROFIT=true; MVID_CART_MULTI_DELETE=true; MVID_CATALOG_STATE=1; MVID_CITY_ID=CityCZ_975; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GEOLOCATION_NEEDED=true; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GIFT_KIT=true; MVID_GUEST_ID=20907421026; MVID_IS_NEW_BR_WIDGET=true; MVID_KLADR_ID=7700000000000; MVID_LAYOUT_TYPE=1; MVID_LP_SOLD_VARIANTS=3; MVID_NEW_ACCESSORY=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_LK=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_LK_LOGIN=true; MVID_NEW_LK_MENU_BUTTON=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_SUGGESTIONS=true; MVID_PDP_MAP_DEFAULT=true; MVID_PROMO_CATALOG_ON=true; MVID_REGION_ID=1; MVID_REGION_SHOP=S002; MVID_SERVICES=111; MVID_SERVICES_MINI_BLOCK=var2; MVID_TAXI_DELIVERY_INTERVALS_VIEW=old; MVID_TIMEZONE_OFFSET=3; MVID_WEBP_ENABLED=true; NEED_REQUIRE_APPLY_DISCOUNT=true; PICKUP_SEAMLESS_AB_TEST=2; PRESELECT_COURIER_DELIVERY_FOR_KBT=false; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; flacktory=no; searchType2=2; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; SMSError=; authError=; advcake_track_id=1a802648-7741-af45-6753-b09e7e1de8ba; advcake_session_id=70e6eab1-fafd-d173-e012-d9c8d603c2fa; _gid=GA1.2.1192785618.1655630019; tmr_lvid=846f2c4fef1859024160015154a81c89; tmr_lvidTS=1644574460413; _ym_isad=1; flocktory-uuid=52f0ab63-20fe-4ab4-8960-5672369ab898-1; afUserId=ad14a9d2-5265-47d1-b1b5-8a2ccedbbfdf-p; AF_SYNC=1655630020032; BIGipServeratg-ps-prod_tcp80=1694817290.20480.0000; bIPs=1613809182; wurfl_device_id=generic_web_browser; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; BIGipServeratg-ps-prod_tcp80_clone=1694817290.20480.0000; mindboxDeviceUUID=950547bb-5dfc-4065-9ab8-8da5be85c063; directCrm-session=%7B%22deviceGuid%22%3A%22950547bb-5dfc-4065-9ab8-8da5be85c063%22%7D; _ga=GA1.1.198893861.1655630019; tmr_detect=1%7C1655630057436; MVID_ENVCLOUD=primary; _dc_gtm_UA-1873769-37=1; JSESSIONID=jlPMvnzDqYJNnBp3J42jBq1C1J85XmJhXgJgM2v2SC4wFGgLnkGc!-1247462178; tmr_reqNum=214; _ga_CFMZTSS5FM=GS1.1.1655632720.2.1.1655632772.0; _ga_BNX5WPP3YK=GS1.1.1655632720.2.1.1655632772.8; ADRUM_BT=R:92|g:433fbf9e-2893-4426-9590-f8bc2d4cf4828194345',
    'referer': 'https://www.mvideo.ru/komputernye-komplektuushhie-5427/videokarty-5429/f/tolko-v-nalichii=da',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'x-set-application-id': '77183666-eca7-4a81-a9b9-f6a87cfdf1b9',
}

    params = {
    'categoryId': '5429',
    'offset': '0',
    'limit': '24',
    'filterParams': 'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
    'doTranslit': 'true',
}

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies, headers=headers).json()
    # print(response)

    products_ids = response.get('body').get('products')
    with open('1_productsids.json', 'w') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)
    json_data = {
      'productIds': products_ids,
      'mediaTypes': [
          'images',
      ],
      'category': True,
      'status': True,
      'brand': True,
      'propertyTypes': [
          'KEY',
      ],
      'propertiesConfig': {
          'propertiesPortionSize': 5,
      },
      'multioffer': False,
}

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers, json=json_data).json()
   
    with open('2_items.json', 'w', encoding='utf-8') as file:
       json.dump(response, file, indent=4, ensure_ascii=False)
    prod_ids_str = ','.join(products_ids)
    params = {
    'productIds': prod_ids_str,
    'addBonusRubles': 'true',
    'isPromoApplied': 'true',
}

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies, headers=headers).json()
    with open('3_prices.json', 'w', encoding='utf-8') as file:
       json.dump(response, file, indent=4, ensure_ascii=False)


    items_prices = {}
    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }
    with open('result.json', 'w', encoding='utf-8') as file:
       json.dump(items_prices, file, indent=4, ensure_ascii=False)    

def main():
    get_data()

if __name__ == '__main__':
    main()