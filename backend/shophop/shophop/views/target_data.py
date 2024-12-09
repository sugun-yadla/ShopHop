import requests
import pandas as pd
import re
import html

import requests
import requests

cookies = {
    'TealeafAkaSid': '079Apk3fD13FyApI3rXFaddt2MME4N6F',
    'visitorId': '01938389D1260201900F001E95FE9EA6',
    'sapphire': '1',
    'UserLocation': '01002|42.370|-72.500|MA|US',
    'fiatsCookie': 'DSI_1839|DSN_Hadley|DSZ_01035',
    'ci_pixmgr': 'other',
    '_gcl_au': '1.1.2132203859.1733078676',
    'egsSessionId': '9ee10197-8f76-458f-8b87-1b0f15f7eac3',
    'accessToken': 'eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIyMzEwZGMwYS04ZTRlLTQ3OTYtYTAwZi1hOGFlZmJlODQ2ZDAiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzM4NjA4NzIsImlhdCI6MTczMzc3NDQ3MiwianRpIjoiVEdULjQwZjQwZTAwMDEzMzRjODY5YmE2YmJiZWZmZDA1MWZkLWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6ImZiYzk0YzVkNGJhMTYxMjM4Njc5YjUzNjFjZDk2MDJjNWM1MTgxZTQ2M2JhN2RkZDg1ZDEwMDRiN2I1YjhiMzUiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.huIcuCcWB1x3HB7QQ_I755PJW0OXX4w6nP5NZGN6zqamChgjCgyPVl1QLMt6bglUYJbxExkwCNdNZzwwpkwMB-GKKN7J5w0qGoeAJonu_kCafXw_Ib0fEWU7F9vo5BXan1cXyIDfETLVy839iWJ1QeqGBgAojXZTseiAkNBlIeqaR-Pp4SmiHnX-4yvA6y5miCtmgOiwBzheclDHMukLaGrH3n_kGqq4HfMbxoKH8XJMrfBBPr78_prT7CznWoB_23DouGDE4xCgGrRlAfVclK4KUV0S2ko_P3RuAtnLrQyxztK7jcfa-gcLuH8tw-MjI3g2i52o65PVFUs3JmqInA',
    'idToken': 'eyJhbGciOiJub25lIn0.eyJzdWIiOiIyMzEwZGMwYS04ZTRlLTQ3OTYtYTAwZi1hOGFlZmJlODQ2ZDAiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzM4NjA4NzIsImlhdCI6MTczMzc3NDQ3MiwiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlLCJzdCI6Ik1BIn19.',
    'refreshToken': '66HgEqlILxnaVKWbLG-IKj7Rq58Zu3sTIvupjGnrUEnV81WIbU_XUnvAnySTbEpfICTEOsmE0732UDYpBcXTQg',
    'adScriptData': 'MA',
    'sddStore': 'DSI_1839|DSN_Hadley|DSZ_01002',
    '__gads': 'ID=94645fefedabe027:T=1733078672:RT=1733774934:S=ALNI_MYjQ4D2JnplW9H03wlaTQij3swfEA',
    '__gpi': 'UID=00000ea4f1c5663d:T=1733078672:RT=1733774934:S=ALNI_Maa1OC__DTdPBQ8GOduDrHsLL4pow',
    '__eoi': 'ID=ac11fe5589fcc23f:T=1733078672:RT=1733774934:S=AA-AfjavZcdU32pyiPiQXH_bhR1G',
    '_tgt_session': 'c90fb9d39baa421eb5c0048706769814.fdbfb71e65341ec6fb0474aeef9a5cbfdc92b9e2be1d18fc0ac02ea429d074dad01fc307a258be5a62288b83b3bf8b054a273b5f8136093fba66c70ed06b7cf269156561a6c85641cfa2e94328aec73cb21476036939e28871882b550e875dc6a3e41a12d8ed2dbb60c82870452a8aa81d198e39d8b581b6cca42e5d53c8c12cba2fb355b53ac7ff1e19de22d26bd036d572e3e5fb67f4d237d2aad0f97bc42588b909a2bd7930bba64bf16139f4e8233b66d17f0103b77da89f40d8bf86a34fc769cbe929a9b471e9ad5ddad6b1830cc253c57d949b0cc9e75da838f82a9b3a16.0x61b73c245b297eb7fb00215d4456d1f150549a616eb48af0af3ef736f491b1e3',
    'ffsession': '{%22sessionHash%22:%22480cdc799c3c41733774471579%22%2C%22prevPageName%22:%22search:%20search%20results%22%2C%22prevPageType%22:%22search:%20search%20results%22%2C%22prevPageUrl%22:%22https://www.target.com/s?searchTerm=tomatoes&category=0%257CAll%257Cmatchallpartial%257Call+categories&tref=typeahead%257Cterm%257C0%257Ctomatoes%257Ctomatoes%257C%257C%257Cservice%257C%257C%257C%257C%257Ccontext%257Efacets_sb&searchTermRaw=tom%22%2C%22prevSearchTerm%22:%22tomatoes%22%2C%22sessionHit%22:8}',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    # 'cookie': 'TealeafAkaSid=079Apk3fD13FyApI3rXFaddt2MME4N6F; visitorId=01938389D1260201900F001E95FE9EA6; sapphire=1; UserLocation=01002|42.370|-72.500|MA|US; fiatsCookie=DSI_1839|DSN_Hadley|DSZ_01035; ci_pixmgr=other; _gcl_au=1.1.2132203859.1733078676; egsSessionId=9ee10197-8f76-458f-8b87-1b0f15f7eac3; accessToken=eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIyMzEwZGMwYS04ZTRlLTQ3OTYtYTAwZi1hOGFlZmJlODQ2ZDAiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzM4NjA4NzIsImlhdCI6MTczMzc3NDQ3MiwianRpIjoiVEdULjQwZjQwZTAwMDEzMzRjODY5YmE2YmJiZWZmZDA1MWZkLWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6ImZiYzk0YzVkNGJhMTYxMjM4Njc5YjUzNjFjZDk2MDJjNWM1MTgxZTQ2M2JhN2RkZDg1ZDEwMDRiN2I1YjhiMzUiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.huIcuCcWB1x3HB7QQ_I755PJW0OXX4w6nP5NZGN6zqamChgjCgyPVl1QLMt6bglUYJbxExkwCNdNZzwwpkwMB-GKKN7J5w0qGoeAJonu_kCafXw_Ib0fEWU7F9vo5BXan1cXyIDfETLVy839iWJ1QeqGBgAojXZTseiAkNBlIeqaR-Pp4SmiHnX-4yvA6y5miCtmgOiwBzheclDHMukLaGrH3n_kGqq4HfMbxoKH8XJMrfBBPr78_prT7CznWoB_23DouGDE4xCgGrRlAfVclK4KUV0S2ko_P3RuAtnLrQyxztK7jcfa-gcLuH8tw-MjI3g2i52o65PVFUs3JmqInA; idToken=eyJhbGciOiJub25lIn0.eyJzdWIiOiIyMzEwZGMwYS04ZTRlLTQ3OTYtYTAwZi1hOGFlZmJlODQ2ZDAiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzM4NjA4NzIsImlhdCI6MTczMzc3NDQ3MiwiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlLCJzdCI6Ik1BIn19.; refreshToken=66HgEqlILxnaVKWbLG-IKj7Rq58Zu3sTIvupjGnrUEnV81WIbU_XUnvAnySTbEpfICTEOsmE0732UDYpBcXTQg; adScriptData=MA; sddStore=DSI_1839|DSN_Hadley|DSZ_01002; __gads=ID=94645fefedabe027:T=1733078672:RT=1733774934:S=ALNI_MYjQ4D2JnplW9H03wlaTQij3swfEA; __gpi=UID=00000ea4f1c5663d:T=1733078672:RT=1733774934:S=ALNI_Maa1OC__DTdPBQ8GOduDrHsLL4pow; __eoi=ID=ac11fe5589fcc23f:T=1733078672:RT=1733774934:S=AA-AfjavZcdU32pyiPiQXH_bhR1G; _tgt_session=c90fb9d39baa421eb5c0048706769814.fdbfb71e65341ec6fb0474aeef9a5cbfdc92b9e2be1d18fc0ac02ea429d074dad01fc307a258be5a62288b83b3bf8b054a273b5f8136093fba66c70ed06b7cf269156561a6c85641cfa2e94328aec73cb21476036939e28871882b550e875dc6a3e41a12d8ed2dbb60c82870452a8aa81d198e39d8b581b6cca42e5d53c8c12cba2fb355b53ac7ff1e19de22d26bd036d572e3e5fb67f4d237d2aad0f97bc42588b909a2bd7930bba64bf16139f4e8233b66d17f0103b77da89f40d8bf86a34fc769cbe929a9b471e9ad5ddad6b1830cc253c57d949b0cc9e75da838f82a9b3a16.0x61b73c245b297eb7fb00215d4456d1f150549a616eb48af0af3ef736f491b1e3; ffsession={%22sessionHash%22:%22480cdc799c3c41733774471579%22%2C%22prevPageName%22:%22search:%20search%20results%22%2C%22prevPageType%22:%22search:%20search%20results%22%2C%22prevPageUrl%22:%22https://www.target.com/s?searchTerm=tomatoes&category=0%257CAll%257Cmatchallpartial%257Call+categories&tref=typeahead%257Cterm%257C0%257Ctomatoes%257Ctomatoes%257C%257C%257Cservice%257C%257C%257C%257C%257Ccontext%257Efacets_sb&searchTermRaw=tom%22%2C%22prevSearchTerm%22:%22tomatoes%22%2C%22sessionHit%22:8}',
    'origin': 'https://www.target.com',
    'priority': 'u=1, i',
    'referer': 'https://www.target.com/s?searchTerm=tomatoes&category=0%7CAll%7Cmatchallpartial%7Call+categories&tref=typeahead%7Cterm%7C0%7Ctomatoes%7Ctomatoes%7C%7C%7Cservice%7C%7C%7C%7C%7Ccontext%7Efacets_sb&searchTermRaw=tom',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
}

params = {
    'key': '9f36aeafbe60771e321a7cc95a78140772ab3e96',
    'channel': 'WEB',
    'count': '24',
    'default_purchasability_filter': 'true',
    'include_dmc_dmr': 'true',
    'include_sponsored': 'true',
    'keyword': 'tomatoes',
    'new_search': 'true',
    'offset': '0',
    'page': '/s/tomatoes',
    'platform': 'desktop',
    'pricing_store_id': '1839',
    'spellcheck': 'true',
    'store_ids': '1839,1232,1255,2213,2127',
    'useragent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'visitor_id': '01938389D1260201900F001E95FE9EA6',
    'zip': '01002',
}


def get_target_data(item):
    details = []
    cookies['ffsession'] = f'{{"sessionHash":"1798ca28b988a1732596335177","prevPageName":"search: search results","prevPageType":"search: search results","prevPageUrl":"https://www.target.com/s?searchTerm={item}","sessionHit":41,"prevSearchTerm":"{item}"}}'

    params['keyword'] = item  # Update the keyword for each grocery item
    params['page'] = f'/s/{item}'  # Set the page field to the item without a page number
    
    # Update the referer in headers dynamically
    headers['referer'] = f'https://www.target.com/s?searchTerm={item}'
    
    # Make the GET request with updated cookies
    response = requests.get(
      'https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2',
      params=params,
      cookies=cookies,
      headers=headers,
    )

    if response.status_code == 200:
        results_json = response.json()
        result_items = results_json['data']['search']['products']
        
        count = 0
        for result in result_items:
            if count >= 10:
                break  

            try:
                title = result['item']['product_description']['title']
                decoded_title = html.unescape(title)
                cleaned_title = re.split(r'\s+-\s+', decoded_title)[0]
                product_title = cleaned_title
            except:
                product_title = None

            try:
                price = result['price']['formatted_current_price'].lstrip('$')
            except:
                price = None

            #print('keys:', result.keys())

            try:
                image = result['item']['enrichment']['images']['primary_image_url']
            except:
                #print(result['item']['enrichment']['images'])
                image = None

            try:
                url = result['item']['enrichment']['buy_url']
            except:
                #print(result['item']['enrichment']['buy_url'])
                url = None

            # extract quantity
            try:
                title_lower = title.lower()
                # Check for "each" in the title
                if "each" in title_lower:
                    #   quantity.append("1 Count")
                    quantity = "1 Count"
                else:
                    # Extract standard quantities like "5lb", "32oz", etc.
                    # match = re.search(r'(\d+\.?\d*)\s?(oz|lb|g|count|ct|gal|)', title_lower)
                    match = re.search(r'([\d.]+)\s*(fl oz|gallon|gal|oz|carton|ct|dozen|count|lb|pk|pack)', title_lower)
                    if match:
                        quantity = match.group(0)
                    else:
                        # No quantity found
                        quantity = None
            except:
                quantity.append(None)

            details.append({
                "Product": product_title,
                "Price": price,
                "Quantity": quantity,
                "Category": item,
                "store": "Target",
                "Image": image,
                "URL": url
            })
            count += 1

        #print('target data:', details)
        return details
    
    else:
        #print(f"Failed to fetch data for {item}, status code: {response.status_code}")
        return []
