import requests
import pandas as pd
import re
import html

import requests
import requests

cookies = {
    'TealeafAkaSid': '8nWV8V2AZBTi0p1XP8Dueq2fvnOiRWmX',
    'visitorId': '01935539DD6E020186FDC2C4E8530B8D',
    'sapphire': '1',
    'UserLocation': '01002|42.350|-72.530|MA|US',
    'fiatsCookie': 'DSI_1839|DSN_Hadley|DSZ_01035',
    'ci_pixmgr': 'dcs',
    '_gcl_aw': 'GCL.1732301679.CjwKCAiA9IC6BhA3EiwAsbltOIEhj1QugyX-PArJIeD1xfl_mzhVW6ZMH4Bm_0Tiq8vtWatpKx3H2hoCByoQAvD_BwE',
    '_gcl_dc': 'GCL.1732301679.CjwKCAiA9IC6BhA3EiwAsbltOIEhj1QugyX-PArJIeD1xfl_mzhVW6ZMH4Bm_0Tiq8vtWatpKx3H2hoCByoQAvD_BwE',
    '_gcl_gs': '2.1.k1$i1732301675$u85450396',
    '_gcl_au': '1.1.2012358250.1732301679',
    'sddStore': 'DSI_1839|DSN_Hadley|DSZ_01002',
    'crl8.fpcuid': 'd2c248d8-173e-4bc8-9ad8-bd1d06e8f2d7',
    'accessToken': 'eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwZGFiMmVhZi03NjM1LTRjY2UtYmVmYS0yYTIzMTJkYzNiMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzM0Mzg2MTMsImlhdCI6MTczMzM1MjIxMywianRpIjoiVEdULjgxYTFkOGY3MTA3MzRiYzg5YTY2ZGYyYTkxMWE0OTllLWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6IjhmMDRjMzAyMTZkYjRmMjk1MWFkNDJjYjA4ZGI5MWYwMDhkNjU4OWM0OWRhOWM3MWNiMjlkZWM3YTM2NGQ4YjkiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.JMiAkPqf4zTbvlsA23mkLxh2XbZL1rk3_BPs0I98WuylhtDGDfmAAeX2q7Dmc6DFB_FlUZ7RI4e4dJU8c7ekiOnUAboBIxfHy0IDIBDfA8bPIqzG7ymlueIEPZtFGbz56PPiUH0b5WOWAjYzYBeUlP9L2PuN4YlGmaCUcoQZDbc_HeaB0DSU_fO1QHMH5ck8NCKoX_TUfDWthFCrhVAC8MFx9Q14ETuMcpqMgj4WjvhUwNt0QcZWrr5lGCcYQQiFB8EN1Ps1bVVu2wx_fX_j-1EluCSSwc0vjyRfR7x6UIxUSmPnAWy6V6B2606ESXoFI8gNefsumP6pP2WXOM7FrA',
    'idToken': 'eyJhbGciOiJub25lIn0.eyJzdWIiOiIwZGFiMmVhZi03NjM1LTRjY2UtYmVmYS0yYTIzMTJkYzNiMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzM0Mzg2MTMsImlhdCI6MTczMzM1MjIxMywiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlLCJzdCI6Ik1BIn19.',
    'refreshToken': 'gn5ItQpAJQ5AWfEqXrv1wYKpyPVL7ucS0JD0PauMI6u2qMPLF9pwV_yGKTVrtQqJOO3UBk0kNYKXtcoJpFtW5g',
    'adScriptData': 'MA',
    '_tgt_session': '864a129140904b06a7e316cd601bad50.6f902a3e42cff74b45f208c3b4165f422e8ab2547fd540424737373c5abff0e5da6be7ff739f7d2e21afba33948e75ff20af28f1159ef8ec4471abeb4a17c76bf56ad84b3e3de443f3d6125294bd7a31ca1fe6c13feccff887a522beb3e9d32eadbc08ec2aa47e0ed952c915bc84695af3af0c199e4af28dcef84e6a0efae070882c1145a15939b6bfaf84acde762b85d72cc7d4dbf32ccf87bfc1151a92de5901f74c13c5f0344cdd216ea5e1bf8c792e4d4df6ad622b06b6a978e63f43e6989f1c7e31cfc4c0b5ee8e351d15ab54e1ea524d29c7919d9b5dbba0197dafa701cb.0x1536f349938309b38069d954ecb7dd99ddc837f0fef9f47f04574108236f4927',
    'ffsession': '{%22sessionHash%22:%221798ca28b988a1732596335177%22%2C%22prevPageName%22:%22search:%20search%20results%22%2C%22prevPageType%22:%22search:%20search%20results%22%2C%22prevPageUrl%22:%22https://www.target.com/s?searchTerm=tomatoes&tref=typeahead%257Cterm%257Ctomatoes%257C%257C%257Chistory%22%2C%22sessionHit%22:54%2C%22prevSearchTerm%22:%22tomatoes%22}',
    '__gads': 'ID=5d5b4437689ceec9:T=1732301677:RT=1733411273:S=ALNI_MZKlJPLUNuLX5CJNSJXItRWwOAO_w',
    '__gpi': 'UID=00000e9edab5b505:T=1732301677:RT=1733411273:S=ALNI_MbwwnDgPIZgwWG9RGUorX-pVVvmgw',
    '__eoi': 'ID=a209cbcf5b46c1e5:T=1732301677:RT=1733411273:S=AA-AfjaGDrPLkX5i0HKy8s_pypma',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'TealeafAkaSid=8nWV8V2AZBTi0p1XP8Dueq2fvnOiRWmX; visitorId=01935539DD6E020186FDC2C4E8530B8D; sapphire=1; UserLocation=01002|42.350|-72.530|MA|US; fiatsCookie=DSI_1839|DSN_Hadley|DSZ_01035; ci_pixmgr=dcs; _gcl_aw=GCL.1732301679.CjwKCAiA9IC6BhA3EiwAsbltOIEhj1QugyX-PArJIeD1xfl_mzhVW6ZMH4Bm_0Tiq8vtWatpKx3H2hoCByoQAvD_BwE; _gcl_dc=GCL.1732301679.CjwKCAiA9IC6BhA3EiwAsbltOIEhj1QugyX-PArJIeD1xfl_mzhVW6ZMH4Bm_0Tiq8vtWatpKx3H2hoCByoQAvD_BwE; _gcl_gs=2.1.k1$i1732301675$u85450396; _gcl_au=1.1.2012358250.1732301679; sddStore=DSI_1839|DSN_Hadley|DSZ_01002; crl8.fpcuid=d2c248d8-173e-4bc8-9ad8-bd1d06e8f2d7; accessToken=eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwZGFiMmVhZi03NjM1LTRjY2UtYmVmYS0yYTIzMTJkYzNiMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzM0Mzg2MTMsImlhdCI6MTczMzM1MjIxMywianRpIjoiVEdULjgxYTFkOGY3MTA3MzRiYzg5YTY2ZGYyYTkxMWE0OTllLWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6IjhmMDRjMzAyMTZkYjRmMjk1MWFkNDJjYjA4ZGI5MWYwMDhkNjU4OWM0OWRhOWM3MWNiMjlkZWM3YTM2NGQ4YjkiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.JMiAkPqf4zTbvlsA23mkLxh2XbZL1rk3_BPs0I98WuylhtDGDfmAAeX2q7Dmc6DFB_FlUZ7RI4e4dJU8c7ekiOnUAboBIxfHy0IDIBDfA8bPIqzG7ymlueIEPZtFGbz56PPiUH0b5WOWAjYzYBeUlP9L2PuN4YlGmaCUcoQZDbc_HeaB0DSU_fO1QHMH5ck8NCKoX_TUfDWthFCrhVAC8MFx9Q14ETuMcpqMgj4WjvhUwNt0QcZWrr5lGCcYQQiFB8EN1Ps1bVVu2wx_fX_j-1EluCSSwc0vjyRfR7x6UIxUSmPnAWy6V6B2606ESXoFI8gNefsumP6pP2WXOM7FrA; idToken=eyJhbGciOiJub25lIn0.eyJzdWIiOiIwZGFiMmVhZi03NjM1LTRjY2UtYmVmYS0yYTIzMTJkYzNiMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzM0Mzg2MTMsImlhdCI6MTczMzM1MjIxMywiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlLCJzdCI6Ik1BIn19.; refreshToken=gn5ItQpAJQ5AWfEqXrv1wYKpyPVL7ucS0JD0PauMI6u2qMPLF9pwV_yGKTVrtQqJOO3UBk0kNYKXtcoJpFtW5g; adScriptData=MA; _tgt_session=864a129140904b06a7e316cd601bad50.6f902a3e42cff74b45f208c3b4165f422e8ab2547fd540424737373c5abff0e5da6be7ff739f7d2e21afba33948e75ff20af28f1159ef8ec4471abeb4a17c76bf56ad84b3e3de443f3d6125294bd7a31ca1fe6c13feccff887a522beb3e9d32eadbc08ec2aa47e0ed952c915bc84695af3af0c199e4af28dcef84e6a0efae070882c1145a15939b6bfaf84acde762b85d72cc7d4dbf32ccf87bfc1151a92de5901f74c13c5f0344cdd216ea5e1bf8c792e4d4df6ad622b06b6a978e63f43e6989f1c7e31cfc4c0b5ee8e351d15ab54e1ea524d29c7919d9b5dbba0197dafa701cb.0x1536f349938309b38069d954ecb7dd99ddc837f0fef9f47f04574108236f4927; ffsession={%22sessionHash%22:%221798ca28b988a1732596335177%22%2C%22prevPageName%22:%22search:%20search%20results%22%2C%22prevPageType%22:%22search:%20search%20results%22%2C%22prevPageUrl%22:%22https://www.target.com/s?searchTerm=tomatoes&tref=typeahead%257Cterm%257Ctomatoes%257C%257C%257Chistory%22%2C%22sessionHit%22:54%2C%22prevSearchTerm%22:%22tomatoes%22}; __gads=ID=5d5b4437689ceec9:T=1732301677:RT=1733411273:S=ALNI_MZKlJPLUNuLX5CJNSJXItRWwOAO_w; __gpi=UID=00000e9edab5b505:T=1732301677:RT=1733411273:S=ALNI_MbwwnDgPIZgwWG9RGUorX-pVVvmgw; __eoi=ID=a209cbcf5b46c1e5:T=1732301677:RT=1733411273:S=AA-AfjaGDrPLkX5i0HKy8s_pypma',
    'origin': 'https://www.target.com',
    'priority': 'u=1, i',
    'referer': 'https://www.target.com/s?searchTerm=tomatoes&tref=typeahead%7Cterm%7Ctomatoes%7C%7C%7Chistory',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
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
    'scheduled_delivery_store_id': '1839',
    'spellcheck': 'true',
    'store_ids': '1839,1232,1255,2213,2127',
    'useragent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    'visitor_id': '01935539DD6E020186FDC2C4E8530B8D',
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

            print('keys:', result.keys())

            try:
                image = result['item']['enrichment']['images']['primary_image_url']
            except:
                print(result['item']['enrichment']['images'])
                image = None

            try:
                url = result['item']['enrichment']['buy_url']
            except:
                print(result['item']['enrichment']['buy_url'])
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

        print('target data:', details)
        return details
    
    else:
        print(f"Failed to fetch data for {item}, status code: {response.status_code}")
        return []
