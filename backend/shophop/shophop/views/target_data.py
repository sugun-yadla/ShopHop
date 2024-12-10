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
    '_tgt_session': 'a10e9c7c09e94a6c96235453063cb685.996adb1f068530d8d85dfd256f7dfc508a910d2f4ee0608d6fbeb2336f8fabdc26b1e22b232f332eaf22888550d9c2befb4ba451a8b3633da4997e6d034d55f07d7ce1faf52dee22a54330cacf8dc4731a0b4a45195e3b4871e07dff9e47334a6b847a4ee3ebeb5434c4549cfa1cde996376b6eb5eb60b4b5d0a4717883a09506dbf3309bf9186b07d23f50bfd0a88bbd4a3db62114fe84e74678a548d14206469adad9029044a11322b46722beaf8b64658ef459e9773606af5a947e5fda5eeb20823dca3c5cd167a8d3884e1ec9ed52772cb628680c59dc7f4fbe8dd511be4a0.0xbe1c56944fbf11bcb3c9448a59711c2973e5b6c9ab536bc337987313003de0fb',
    'egsSessionId': '23fa43ff-c5bf-410a-9976-04be06e4915a',
    'accessToken': 'eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJjN2NlMmNjNy02MmJmLTRjM2MtOTQyOS0xZTFkOWNjYTVhMDgiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzM4ODI4MjMsImlhdCI6MTczMzc5NjQyMywianRpIjoiVEdULmM3MWFiNDU1ZWRlMTRmNTZiYTM0MzYyYTA0NTZlZjI1LWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6ImZiYzk0YzVkNGJhMTYxMjM4Njc5YjUzNjFjZDk2MDJjNWM1MTgxZTQ2M2JhN2RkZDg1ZDEwMDRiN2I1YjhiMzUiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.bLMQn2nShonLMc-G1aUvZwKKJ2fJn8HyufntOmyH5YM69BoFYfCUhGvjNlUITa57T5WRXuvylMMJ9xmrVmJ4XK1sQHwrOxBAqKYZodQejFUAk8ievlcS6uyNq7A13saytUwHn_bWPZpulosLLAPOT1IPNbnkV_ZM6uGINUbULE3laYeBbaOj2Y_VzI33qFnO3PuY45TR1PsOsdl96tSHKfg5IWnwCvWSHouJ0Uk9H2VOfGBJQQzHW311DJ03evFbeqNSvwlaQYKF7IrG5X5PlW8qAMtNmorHxFHPP9b3JTK6EIeWSa4OoSXkCsdBNiQfxBZKDCXpbfF5D5PnwzkThg',
    'idToken': 'eyJhbGciOiJub25lIn0.eyJzdWIiOiJjN2NlMmNjNy02MmJmLTRjM2MtOTQyOS0xZTFkOWNjYTVhMDgiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzM4ODI4MjMsImlhdCI6MTczMzc5NjQyMywiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlLCJzdCI6Ik1BIn19.',
    'refreshToken': '69n8ryUVUNg6ONEddu8m0dsUaqSTuxdhdNuUFp7ByJuIx_stS3CwxUsdoRIPsxI3CorGrkeP-ACYBBX7qQyrUA',
    'adScriptData': 'MA',
    'sddStore': 'DSI_1839|DSN_Hadley|DSZ_01002',
    '__gads': 'ID=27b43f83d7f53b5a:T=1733796426:RT=1733796426:S=ALNI_MZMg9V2ujgWRSD5gfhd6UBfJXpp-Q',
    '__gpi': 'UID=00000fac927939b2:T=1733796426:RT=1733796426:S=ALNI_MZ8Jx2ByP4oE-J8j843MB49aq8a6g',
    '__eoi': 'ID=6873981fc76d670f:T=1733796426:RT=1733796426:S=AA-Afja-i70ULNLF5GQqW3RTfZtL',
    'ffsession': '{%22sessionHash%22:%221015eb1fc26c781733796422656%22%2C%22prevPageName%22:%22search:%20search%20results%22%2C%22prevPageType%22:%22search:%20search%20results%22%2C%22prevPageUrl%22:%22https://www.target.com/s?searchTerm=eggs&Nao=24&moveTo=product-list-grid%22%2C%22prevSearchTerm%22:%22eggs%22%2C%22sessionHit%22:2}',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    # 'cookie': 'TealeafAkaSid=079Apk3fD13FyApI3rXFaddt2MME4N6F; visitorId=01938389D1260201900F001E95FE9EA6; sapphire=1; UserLocation=01002|42.370|-72.500|MA|US; fiatsCookie=DSI_1839|DSN_Hadley|DSZ_01035; ci_pixmgr=other; _gcl_au=1.1.2132203859.1733078676; _tgt_session=a10e9c7c09e94a6c96235453063cb685.996adb1f068530d8d85dfd256f7dfc508a910d2f4ee0608d6fbeb2336f8fabdc26b1e22b232f332eaf22888550d9c2befb4ba451a8b3633da4997e6d034d55f07d7ce1faf52dee22a54330cacf8dc4731a0b4a45195e3b4871e07dff9e47334a6b847a4ee3ebeb5434c4549cfa1cde996376b6eb5eb60b4b5d0a4717883a09506dbf3309bf9186b07d23f50bfd0a88bbd4a3db62114fe84e74678a548d14206469adad9029044a11322b46722beaf8b64658ef459e9773606af5a947e5fda5eeb20823dca3c5cd167a8d3884e1ec9ed52772cb628680c59dc7f4fbe8dd511be4a0.0xbe1c56944fbf11bcb3c9448a59711c2973e5b6c9ab536bc337987313003de0fb; egsSessionId=23fa43ff-c5bf-410a-9976-04be06e4915a; accessToken=eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiJjN2NlMmNjNy02MmJmLTRjM2MtOTQyOS0xZTFkOWNjYTVhMDgiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzM4ODI4MjMsImlhdCI6MTczMzc5NjQyMywianRpIjoiVEdULmM3MWFiNDU1ZWRlMTRmNTZiYTM0MzYyYTA0NTZlZjI1LWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6ImZiYzk0YzVkNGJhMTYxMjM4Njc5YjUzNjFjZDk2MDJjNWM1MTgxZTQ2M2JhN2RkZDg1ZDEwMDRiN2I1YjhiMzUiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.bLMQn2nShonLMc-G1aUvZwKKJ2fJn8HyufntOmyH5YM69BoFYfCUhGvjNlUITa57T5WRXuvylMMJ9xmrVmJ4XK1sQHwrOxBAqKYZodQejFUAk8ievlcS6uyNq7A13saytUwHn_bWPZpulosLLAPOT1IPNbnkV_ZM6uGINUbULE3laYeBbaOj2Y_VzI33qFnO3PuY45TR1PsOsdl96tSHKfg5IWnwCvWSHouJ0Uk9H2VOfGBJQQzHW311DJ03evFbeqNSvwlaQYKF7IrG5X5PlW8qAMtNmorHxFHPP9b3JTK6EIeWSa4OoSXkCsdBNiQfxBZKDCXpbfF5D5PnwzkThg; idToken=eyJhbGciOiJub25lIn0.eyJzdWIiOiJjN2NlMmNjNy02MmJmLTRjM2MtOTQyOS0xZTFkOWNjYTVhMDgiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzM4ODI4MjMsImlhdCI6MTczMzc5NjQyMywiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlLCJzdCI6Ik1BIn19.; refreshToken=69n8ryUVUNg6ONEddu8m0dsUaqSTuxdhdNuUFp7ByJuIx_stS3CwxUsdoRIPsxI3CorGrkeP-ACYBBX7qQyrUA; adScriptData=MA; sddStore=DSI_1839|DSN_Hadley|DSZ_01002; __gads=ID=27b43f83d7f53b5a:T=1733796426:RT=1733796426:S=ALNI_MZMg9V2ujgWRSD5gfhd6UBfJXpp-Q; __gpi=UID=00000fac927939b2:T=1733796426:RT=1733796426:S=ALNI_MZ8Jx2ByP4oE-J8j843MB49aq8a6g; __eoi=ID=6873981fc76d670f:T=1733796426:RT=1733796426:S=AA-Afja-i70ULNLF5GQqW3RTfZtL; ffsession={%22sessionHash%22:%221015eb1fc26c781733796422656%22%2C%22prevPageName%22:%22search:%20search%20results%22%2C%22prevPageType%22:%22search:%20search%20results%22%2C%22prevPageUrl%22:%22https://www.target.com/s?searchTerm=eggs&Nao=24&moveTo=product-list-grid%22%2C%22prevSearchTerm%22:%22eggs%22%2C%22sessionHit%22:2}',
    'origin': 'https://www.target.com',
    'priority': 'u=1, i',
    'referer': 'https://www.target.com/s?searchTerm=eggs&Nao=24&moveTo=product-list-grid',
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
    'keyword': 'eggs',
    'new_search': 'true',
    'offset': '0',
    'page': '/s/eggs',
    'platform': 'desktop',
    'pricing_store_id': '1839',
    'scheduled_delivery_store_id': '1839',
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
        print(f"Failed to fetch data for {item}, status code: {response.status_code}")
        return []
