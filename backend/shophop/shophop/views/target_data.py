import requests
import pandas as pd
import re
import html

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
    'accessToken': 'eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwZGFiMmVhZi03NjM1LTRjY2UtYmVmYS0yYTIzMTJkYzNiMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzMzMzc1ODYsImlhdCI6MTczMzI1MTE4NiwianRpIjoiVEdULjgxOWRkYmZjNGVlZDQzMDhhZjViYzVmZmU4ZjIyODBiLWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6IjhmMDRjMzAyMTZkYjRmMjk1MWFkNDJjYjA4ZGI5MWYwMDhkNjU4OWM0OWRhOWM3MWNiMjlkZWM3YTM2NGQ4YjkiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.DhTE485f5JK-fHKTiM_VeHrE4H77OPo9rAQWZz4tJiwdN3STQukUOlWRDzJ0tz9H1Ht4YKamk5zTBVBpN6C6cMH9SJ67TkjfM64-o9rKINYuH8SwqCzKSpOq75hGkMYUxVop7fXX44xJWElwGll20DoKVM-u-5PETEtOIQo6RoJkuHtRUdqmGgjdqqe6oXN5iCSMVs8L7ZTS361fWheoDMXqTC9RCv4rb5xVMaqv2U3PkbsLKoJQ9tGSkYP2po75FmcAq1wPUM-yYic4OiZMz-jkssm_fW5HoM8wLFnld313S-Tf7FwJCf1e9atRko6xy0HZ6xkM5GqgZg335THeOg',
    'idToken': 'eyJhbGciOiJub25lIn0.eyJzdWIiOiIwZGFiMmVhZi03NjM1LTRjY2UtYmVmYS0yYTIzMTJkYzNiMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzMzMzc1ODYsImlhdCI6MTczMzI1MTE4NiwiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlLCJzdCI6Ik1BIn19.',
    'refreshToken': 'ovx-rN-VTxOLONyo7GuYzftiGBJ18PhkXbfN9CDfIKjg3cX9X8U-6SujpAvg20nkvUJOss9tEQ3s6Dt-bG3VlA',
    'adScriptData': 'MA',
    '_tgt_session': '6b970f9751234d6bb5ac00ba985b8877.371fdca32d11277b1839a51fd5a1c97ae9b0ca11e49ec4f862a598cca665c9825487a48a79a5cc4c5e7a0f955d57f38ac1f569e73dbd640c5dda0b9025ae2d811a29a0a3cf1e14772347a3fc96f93ea5bb0fbf19bd3474fda7211a29ef1fc80594f9f255a6eae903f9646d69284fe637a9f8285cf932bccd4f195ce3a59e59475415ffb339116e68cf098169c1e18906de4dc424ae3ec311733c540c032d7493e544286ff0a941372d759e5a1c7dc4b0d4be57cf9b10c69a1658b3f3f0a26bc086afb37cc48c1cfd11142bdd924fee25ba9325f90e857c3e30ac502cbddaa03a0f.0xe8c9820293c7fbe6950eadede26eaea6a4161716cf6950195cdf25000ec1de47',
    '__gads': 'ID=5d5b4437689ceec9:T=1732301677:RT=1733274723:S=ALNI_MZKlJPLUNuLX5CJNSJXItRWwOAO_w',
    '__gpi': 'UID=00000e9edab5b505:T=1732301677:RT=1733274723:S=ALNI_MbwwnDgPIZgwWG9RGUorX-pVVvmgw',
    '__eoi': 'ID=a209cbcf5b46c1e5:T=1732301677:RT=1733274723:S=AA-AfjaGDrPLkX5i0HKy8s_pypma',
    'ffsession': '{%22sessionHash%22:%221798ca28b988a1732596335177%22%2C%22prevPageName%22:%22search:%20search%20results%22%2C%22prevPageType%22:%22search:%20search%20results%22%2C%22prevPageUrl%22:%22https://www.target.com/s?searchTerm=tomato&tref=typeahead%257Cterm%257Ctomato%257C%257C%257Chistory%22%2C%22sessionHit%22:49%2C%22prevSearchTerm%22:%22tomato%22}',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'TealeafAkaSid=8nWV8V2AZBTi0p1XP8Dueq2fvnOiRWmX; visitorId=01935539DD6E020186FDC2C4E8530B8D; sapphire=1; UserLocation=01002|42.350|-72.530|MA|US; fiatsCookie=DSI_1839|DSN_Hadley|DSZ_01035; ci_pixmgr=dcs; _gcl_aw=GCL.1732301679.CjwKCAiA9IC6BhA3EiwAsbltOIEhj1QugyX-PArJIeD1xfl_mzhVW6ZMH4Bm_0Tiq8vtWatpKx3H2hoCByoQAvD_BwE; _gcl_dc=GCL.1732301679.CjwKCAiA9IC6BhA3EiwAsbltOIEhj1QugyX-PArJIeD1xfl_mzhVW6ZMH4Bm_0Tiq8vtWatpKx3H2hoCByoQAvD_BwE; _gcl_gs=2.1.k1$i1732301675$u85450396; _gcl_au=1.1.2012358250.1732301679; sddStore=DSI_1839|DSN_Hadley|DSZ_01002; crl8.fpcuid=d2c248d8-173e-4bc8-9ad8-bd1d06e8f2d7; accessToken=eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwZGFiMmVhZi03NjM1LTRjY2UtYmVmYS0yYTIzMTJkYzNiMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzMzMzc1ODYsImlhdCI6MTczMzI1MTE4NiwianRpIjoiVEdULjgxOWRkYmZjNGVlZDQzMDhhZjViYzVmZmU4ZjIyODBiLWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6IjhmMDRjMzAyMTZkYjRmMjk1MWFkNDJjYjA4ZGI5MWYwMDhkNjU4OWM0OWRhOWM3MWNiMjlkZWM3YTM2NGQ4YjkiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.DhTE485f5JK-fHKTiM_VeHrE4H77OPo9rAQWZz4tJiwdN3STQukUOlWRDzJ0tz9H1Ht4YKamk5zTBVBpN6C6cMH9SJ67TkjfM64-o9rKINYuH8SwqCzKSpOq75hGkMYUxVop7fXX44xJWElwGll20DoKVM-u-5PETEtOIQo6RoJkuHtRUdqmGgjdqqe6oXN5iCSMVs8L7ZTS361fWheoDMXqTC9RCv4rb5xVMaqv2U3PkbsLKoJQ9tGSkYP2po75FmcAq1wPUM-yYic4OiZMz-jkssm_fW5HoM8wLFnld313S-Tf7FwJCf1e9atRko6xy0HZ6xkM5GqgZg335THeOg; idToken=eyJhbGciOiJub25lIn0.eyJzdWIiOiIwZGFiMmVhZi03NjM1LTRjY2UtYmVmYS0yYTIzMTJkYzNiMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzMzMzc1ODYsImlhdCI6MTczMzI1MTE4NiwiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlLCJzdCI6Ik1BIn19.; refreshToken=ovx-rN-VTxOLONyo7GuYzftiGBJ18PhkXbfN9CDfIKjg3cX9X8U-6SujpAvg20nkvUJOss9tEQ3s6Dt-bG3VlA; adScriptData=MA; _tgt_session=6b970f9751234d6bb5ac00ba985b8877.371fdca32d11277b1839a51fd5a1c97ae9b0ca11e49ec4f862a598cca665c9825487a48a79a5cc4c5e7a0f955d57f38ac1f569e73dbd640c5dda0b9025ae2d811a29a0a3cf1e14772347a3fc96f93ea5bb0fbf19bd3474fda7211a29ef1fc80594f9f255a6eae903f9646d69284fe637a9f8285cf932bccd4f195ce3a59e59475415ffb339116e68cf098169c1e18906de4dc424ae3ec311733c540c032d7493e544286ff0a941372d759e5a1c7dc4b0d4be57cf9b10c69a1658b3f3f0a26bc086afb37cc48c1cfd11142bdd924fee25ba9325f90e857c3e30ac502cbddaa03a0f.0xe8c9820293c7fbe6950eadede26eaea6a4161716cf6950195cdf25000ec1de47; __gads=ID=5d5b4437689ceec9:T=1732301677:RT=1733274723:S=ALNI_MZKlJPLUNuLX5CJNSJXItRWwOAO_w; __gpi=UID=00000e9edab5b505:T=1732301677:RT=1733274723:S=ALNI_MbwwnDgPIZgwWG9RGUorX-pVVvmgw; __eoi=ID=a209cbcf5b46c1e5:T=1732301677:RT=1733274723:S=AA-AfjaGDrPLkX5i0HKy8s_pypma; ffsession={%22sessionHash%22:%221798ca28b988a1732596335177%22%2C%22prevPageName%22:%22search:%20search%20results%22%2C%22prevPageType%22:%22search:%20search%20results%22%2C%22prevPageUrl%22:%22https://www.target.com/s?searchTerm=tomato&tref=typeahead%257Cterm%257Ctomato%257C%257C%257Chistory%22%2C%22sessionHit%22:49%2C%22prevSearchTerm%22:%22tomato%22}',
    'origin': 'https://www.target.com',
    'priority': 'u=1, i',
    'referer': 'https://www.target.com/s?searchTerm=tomatoes&category=0%7CAll%7Cmatchallpartial%7Call+categories&tref=typeahead%7Cterm%7C0%7Ctomatoes%7Ctomatoes%7C%7C%7Cservice%7C%7C%7C%7C%7Ccontext&searchTermRaw=tomato',
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

response = requests.get(
    'https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2',
    params=params,
    cookies=cookies,
    headers=headers,
)


response = requests.get(
    'https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2',
    params=params,
    cookies=cookies,
    headers=headers,
)



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
        
        
        for result in result_items:

          try:
            

              title = result['item']['product_description']['title']
            
              # Decode HTML entities
              decoded_title = html.unescape(title)
              
              # Clean title: remove everything after the first " - "
              cleaned_title = re.split(r'\s+-\s+', decoded_title)[0]
              
            
              product_title = cleaned_title
          except:
            
              product_title = None


          # price
          try:
            
            price = result['price']['formatted_current_price'].lstrip('$')
          except:
            
              price = None

          # extract quantity
          try:
              title_lower = title.lower()
              
              # Check for "each" in the title
              if "each" in title_lower:
                #   quantity.append("1 Count")
                  quantity = "1 Count"
              else:
                  # Extract standard quantities like "5lb", "32oz", etc.
                  #match = re.search(r'(\d+\.?\d*)\s?(oz|lb|g|count|ct|gal|)', title_lower)
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
                        "store": "Target"
                })

        return details
    
    else:
        print(f"Failed to fetch data for {item}, status code: {response.status_code}")
        return []
