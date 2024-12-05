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
    # '_tgt_session': 'db2fad20e205496d80794350df9eeab9.bf843eed4aa549dfb6ffaaa5c95519bf6e97ef6b3fdc2a66bc9d5c9c04f1e1f3489f79d3293253c9bb0522191504ef41b5352104c426653957e12c88e1453b40aa5610330cb51a7fd7cf87eed6ee9faf6d323ff2ec9e1272203f31479c9481f1a686457e24803e31fcbb8686e1a061e49ec9aae1bff81db51172f82cf90bcd6cf39c009108956aa4a5a1a79c696b052e9446b9d295c082960813a533a6dd9128bf35af5bcb04f1044d8ac066365873d6de6330b2924099a0549dc6a1715762943273a400c7fe78981b76af4bcc939323335daa8c4cc9e3c3ed96debf15bfdf1be1.0x3e84f502b5e8288e43aef44c85da1f739750ec483e7b082c2ea83dc78a94a965',
    # 'ffsession': '{%22sessionHash%22:%221798ca28b988a1732596335177%22%2C%22prevPageName%22:%22search:%20search%20results%22%2C%22prevPageType%22:%22search:%20search%20results%22%2C%22prevPageUrl%22:%22https://www.target.com/s?searchTerm=tomatoes%22%2C%22sessionHit%22:51%2C%22prevSearchTerm%22:%22tomatoes%22}',
    # '__gads': 'ID=5d5b4437689ceec9:T=1732301677:RT=1733292333:S=ALNI_MZKlJPLUNuLX5CJNSJXItRWwOAO_w',
    # '__gpi': 'UID=00000e9edab5b505:T=1732301677:RT=1733292333:S=ALNI_MbwwnDgPIZgwWG9RGUorX-pVVvmgw',
    # '__eoi': 'ID=a209cbcf5b46c1e5:T=1732301677:RT=1733292333:S=AA-AfjaGDrPLkX5i0HKy8s_pypma',
    # 'egsSessionId': '733c5963-31dd-467a-af97-f79f61c32657',
    'accessToken': 'eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwZGFiMmVhZi03NjM1LTRjY2UtYmVmYS0yYTIzMTJkYzNiMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzM0Mzg2MTMsImlhdCI6MTczMzM1MjIxMywianRpIjoiVEdULjgxYTFkOGY3MTA3MzRiYzg5YTY2ZGYyYTkxMWE0OTllLWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6IjhmMDRjMzAyMTZkYjRmMjk1MWFkNDJjYjA4ZGI5MWYwMDhkNjU4OWM0OWRhOWM3MWNiMjlkZWM3YTM2NGQ4YjkiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.JMiAkPqf4zTbvlsA23mkLxh2XbZL1rk3_BPs0I98WuylhtDGDfmAAeX2q7Dmc6DFB_FlUZ7RI4e4dJU8c7ekiOnUAboBIxfHy0IDIBDfA8bPIqzG7ymlueIEPZtFGbz56PPiUH0b5WOWAjYzYBeUlP9L2PuN4YlGmaCUcoQZDbc_HeaB0DSU_fO1QHMH5ck8NCKoX_TUfDWthFCrhVAC8MFx9Q14ETuMcpqMgj4WjvhUwNt0QcZWrr5lGCcYQQiFB8EN1Ps1bVVu2wx_fX_j-1EluCSSwc0vjyRfR7x6UIxUSmPnAWy6V6B2606ESXoFI8gNefsumP6pP2WXOM7FrA',
    'idToken': 'eyJhbGciOiJub25lIn0.eyJzdWIiOiIwZGFiMmVhZi03NjM1LTRjY2UtYmVmYS0yYTIzMTJkYzNiMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzM0Mzg2MTMsImlhdCI6MTczMzM1MjIxMywiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlLCJzdCI6Ik1BIn19.',
    'refreshToken': 'gn5ItQpAJQ5AWfEqXrv1wYKpyPVL7ucS0JD0PauMI6u2qMPLF9pwV_yGKTVrtQqJOO3UBk0kNYKXtcoJpFtW5g',
    'adScriptData': 'MA',
    'ffsession': '{%22sessionHash%22:%221798ca28b988a1732596335177%22%2C%22prevPageName%22:%22search:%20search%20results%22%2C%22prevPageType%22:%22search:%20search%20results%22%2C%22prevPageUrl%22:%22https://www.target.com/s?searchTerm=tomatoes&tref=typeahead%257Cterm%257Ctomatoes%257C%257C%257Chistory%22%2C%22sessionHit%22:52%2C%22prevSearchTerm%22:%22tomatoes%22}',
    '__gads': 'ID=5d5b4437689ceec9:T=1732301677:RT=1733352217:S=ALNI_MZKlJPLUNuLX5CJNSJXItRWwOAO_w',
    '__gpi': 'UID=00000e9edab5b505:T=1732301677:RT=1733352217:S=ALNI_MbwwnDgPIZgwWG9RGUorX-pVVvmgw',
    '__eoi': 'ID=a209cbcf5b46c1e5:T=1732301677:RT=1733352217:S=AA-AfjaGDrPLkX5i0HKy8s_pypma',
    '_tgt_session': '2346f5b1c6e24cd5a8fca4f1994dac56.d2a3bcd2f22bf2de4b70c83a852c3f29755368f2af85d43be84e712e4188815a59ed5a83489244690c178b11b3e70df4e6e93acb9d492cdc6f391ebb113c2e9df77f67876e05ab1d4987adfd70a457b56c5ce338db0e2d7f95bd331ad0f517352a936c78f560e631b23f549cd135228591abf36bde1a7f29f069bb1e6b52b96f1f2f43e20598d6898da005c958cfdaa1525a36760a4e22c604911c728d742d81277705b705a9f213c012a447635238a1348300a4bc75ab23f1b921643fc7a29a7a48bf935dfbf476db09ba2a539dd7dbaf0a05cc2c730f4e0382b097fccbecfc8c.0x6a567d3eabed4d09b438bf9a814eb6011c5302944bb4a0e84a3607700672194c',
}

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    # 'cookie': 'TealeafAkaSid=8nWV8V2AZBTi0p1XP8Dueq2fvnOiRWmX; visitorId=01935539DD6E020186FDC2C4E8530B8D; sapphire=1; UserLocation=01002|42.350|-72.530|MA|US; fiatsCookie=DSI_1839|DSN_Hadley|DSZ_01035; ci_pixmgr=dcs; _gcl_aw=GCL.1732301679.CjwKCAiA9IC6BhA3EiwAsbltOIEhj1QugyX-PArJIeD1xfl_mzhVW6ZMH4Bm_0Tiq8vtWatpKx3H2hoCByoQAvD_BwE; _gcl_dc=GCL.1732301679.CjwKCAiA9IC6BhA3EiwAsbltOIEhj1QugyX-PArJIeD1xfl_mzhVW6ZMH4Bm_0Tiq8vtWatpKx3H2hoCByoQAvD_BwE; _gcl_gs=2.1.k1$i1732301675$u85450396; _gcl_au=1.1.2012358250.1732301679; sddStore=DSI_1839|DSN_Hadley|DSZ_01002; crl8.fpcuid=d2c248d8-173e-4bc8-9ad8-bd1d06e8f2d7; _tgt_session=db2fad20e205496d80794350df9eeab9.bf843eed4aa549dfb6ffaaa5c95519bf6e97ef6b3fdc2a66bc9d5c9c04f1e1f3489f79d3293253c9bb0522191504ef41b5352104c426653957e12c88e1453b40aa5610330cb51a7fd7cf87eed6ee9faf6d323ff2ec9e1272203f31479c9481f1a686457e24803e31fcbb8686e1a061e49ec9aae1bff81db51172f82cf90bcd6cf39c009108956aa4a5a1a79c696b052e9446b9d295c082960813a533a6dd9128bf35af5bcb04f1044d8ac066365873d6de6330b2924099a0549dc6a1715762943273a400c7fe78981b76af4bcc939323335daa8c4cc9e3c3ed96debf15bfdf1be1.0x3e84f502b5e8288e43aef44c85da1f739750ec483e7b082c2ea83dc78a94a965; ffsession={%22sessionHash%22:%221798ca28b988a1732596335177%22%2C%22prevPageName%22:%22search:%20search%20results%22%2C%22prevPageType%22:%22search:%20search%20results%22%2C%22prevPageUrl%22:%22https://www.target.com/s?searchTerm=tomatoes%22%2C%22sessionHit%22:51%2C%22prevSearchTerm%22:%22tomatoes%22}; __gads=ID=5d5b4437689ceec9:T=1732301677:RT=1733292333:S=ALNI_MZKlJPLUNuLX5CJNSJXItRWwOAO_w; __gpi=UID=00000e9edab5b505:T=1732301677:RT=1733292333:S=ALNI_MbwwnDgPIZgwWG9RGUorX-pVVvmgw; __eoi=ID=a209cbcf5b46c1e5:T=1732301677:RT=1733292333:S=AA-AfjaGDrPLkX5i0HKy8s_pypma; egsSessionId=733c5963-31dd-467a-af97-f79f61c32657; accessToken=eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwZGFiMmVhZi03NjM1LTRjY2UtYmVmYS0yYTIzMTJkYzNiMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzM0Mzg2MTMsImlhdCI6MTczMzM1MjIxMywianRpIjoiVEdULjgxYTFkOGY3MTA3MzRiYzg5YTY2ZGYyYTkxMWE0OTllLWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6IjhmMDRjMzAyMTZkYjRmMjk1MWFkNDJjYjA4ZGI5MWYwMDhkNjU4OWM0OWRhOWM3MWNiMjlkZWM3YTM2NGQ4YjkiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.JMiAkPqf4zTbvlsA23mkLxh2XbZL1rk3_BPs0I98WuylhtDGDfmAAeX2q7Dmc6DFB_FlUZ7RI4e4dJU8c7ekiOnUAboBIxfHy0IDIBDfA8bPIqzG7ymlueIEPZtFGbz56PPiUH0b5WOWAjYzYBeUlP9L2PuN4YlGmaCUcoQZDbc_HeaB0DSU_fO1QHMH5ck8NCKoX_TUfDWthFCrhVAC8MFx9Q14ETuMcpqMgj4WjvhUwNt0QcZWrr5lGCcYQQiFB8EN1Ps1bVVu2wx_fX_j-1EluCSSwc0vjyRfR7x6UIxUSmPnAWy6V6B2606ESXoFI8gNefsumP6pP2WXOM7FrA; idToken=eyJhbGciOiJub25lIn0.eyJzdWIiOiIwZGFiMmVhZi03NjM1LTRjY2UtYmVmYS0yYTIzMTJkYzNiMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzM0Mzg2MTMsImlhdCI6MTczMzM1MjIxMywiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlLCJzdCI6Ik1BIn19.; refreshToken=gn5ItQpAJQ5AWfEqXrv1wYKpyPVL7ucS0JD0PauMI6u2qMPLF9pwV_yGKTVrtQqJOO3UBk0kNYKXtcoJpFtW5g; adScriptData=MA',
    'cookie': 'TealeafAkaSid=8nWV8V2AZBTi0p1XP8Dueq2fvnOiRWmX; visitorId=01935539DD6E020186FDC2C4E8530B8D; sapphire=1; UserLocation=01002|42.350|-72.530|MA|US; fiatsCookie=DSI_1839|DSN_Hadley|DSZ_01035; ci_pixmgr=dcs; _gcl_aw=GCL.1732301679.CjwKCAiA9IC6BhA3EiwAsbltOIEhj1QugyX-PArJIeD1xfl_mzhVW6ZMH4Bm_0Tiq8vtWatpKx3H2hoCByoQAvD_BwE; _gcl_dc=GCL.1732301679.CjwKCAiA9IC6BhA3EiwAsbltOIEhj1QugyX-PArJIeD1xfl_mzhVW6ZMH4Bm_0Tiq8vtWatpKx3H2hoCByoQAvD_BwE; _gcl_gs=2.1.k1$i1732301675$u85450396; _gcl_au=1.1.2012358250.1732301679; sddStore=DSI_1839|DSN_Hadley|DSZ_01002; crl8.fpcuid=d2c248d8-173e-4bc8-9ad8-bd1d06e8f2d7; accessToken=eyJraWQiOiJlYXMyIiwiYWxnIjoiUlMyNTYifQ.eyJzdWIiOiIwZGFiMmVhZi03NjM1LTRjY2UtYmVmYS0yYTIzMTJkYzNiMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzM0Mzg2MTMsImlhdCI6MTczMzM1MjIxMywianRpIjoiVEdULjgxYTFkOGY3MTA3MzRiYzg5YTY2ZGYyYTkxMWE0OTllLWwiLCJza3kiOiJlYXMyIiwic3V0IjoiRyIsImRpZCI6IjhmMDRjMzAyMTZkYjRmMjk1MWFkNDJjYjA4ZGI5MWYwMDhkNjU4OWM0OWRhOWM3MWNiMjlkZWM3YTM2NGQ4YjkiLCJzY28iOiJlY29tLm5vbmUsb3BlbmlkIiwiY2xpIjoiZWNvbS13ZWItMS4wLjAiLCJhc2wiOiJMIn0.JMiAkPqf4zTbvlsA23mkLxh2XbZL1rk3_BPs0I98WuylhtDGDfmAAeX2q7Dmc6DFB_FlUZ7RI4e4dJU8c7ekiOnUAboBIxfHy0IDIBDfA8bPIqzG7ymlueIEPZtFGbz56PPiUH0b5WOWAjYzYBeUlP9L2PuN4YlGmaCUcoQZDbc_HeaB0DSU_fO1QHMH5ck8NCKoX_TUfDWthFCrhVAC8MFx9Q14ETuMcpqMgj4WjvhUwNt0QcZWrr5lGCcYQQiFB8EN1Ps1bVVu2wx_fX_j-1EluCSSwc0vjyRfR7x6UIxUSmPnAWy6V6B2606ESXoFI8gNefsumP6pP2WXOM7FrA; idToken=eyJhbGciOiJub25lIn0.eyJzdWIiOiIwZGFiMmVhZi03NjM1LTRjY2UtYmVmYS0yYTIzMTJkYzNiMmMiLCJpc3MiOiJNSTYiLCJleHAiOjE3MzM0Mzg2MTMsImlhdCI6MTczMzM1MjIxMywiYXNzIjoiTCIsInN1dCI6IkciLCJjbGkiOiJlY29tLXdlYi0xLjAuMCIsInBybyI6eyJmbiI6bnVsbCwiZW0iOm51bGwsInBoIjpmYWxzZSwibGVkIjpudWxsLCJsdHkiOmZhbHNlLCJzdCI6Ik1BIn19.; refreshToken=gn5ItQpAJQ5AWfEqXrv1wYKpyPVL7ucS0JD0PauMI6u2qMPLF9pwV_yGKTVrtQqJOO3UBk0kNYKXtcoJpFtW5g; adScriptData=MA; ffsession={%22sessionHash%22:%221798ca28b988a1732596335177%22%2C%22prevPageName%22:%22search:%20search%20results%22%2C%22prevPageType%22:%22search:%20search%20results%22%2C%22prevPageUrl%22:%22https://www.target.com/s?searchTerm=tomatoes&tref=typeahead%257Cterm%257Ctomatoes%257C%257C%257Chistory%22%2C%22sessionHit%22:52%2C%22prevSearchTerm%22:%22tomatoes%22}; __gads=ID=5d5b4437689ceec9:T=1732301677:RT=1733352217:S=ALNI_MZKlJPLUNuLX5CJNSJXItRWwOAO_w; __gpi=UID=00000e9edab5b505:T=1732301677:RT=1733352217:S=ALNI_MbwwnDgPIZgwWG9RGUorX-pVVvmgw; __eoi=ID=a209cbcf5b46c1e5:T=1732301677:RT=1733352217:S=AA-AfjaGDrPLkX5i0HKy8s_pypma; _tgt_session=2346f5b1c6e24cd5a8fca4f1994dac56.d2a3bcd2f22bf2de4b70c83a852c3f29755368f2af85d43be84e712e4188815a59ed5a83489244690c178b11b3e70df4e6e93acb9d492cdc6f391ebb113c2e9df77f67876e05ab1d4987adfd70a457b56c5ce338db0e2d7f95bd331ad0f517352a936c78f560e631b23f549cd135228591abf36bde1a7f29f069bb1e6b52b96f1f2f43e20598d6898da005c958cfdaa1525a36760a4e22c604911c728d742d81277705b705a9f213c012a447635238a1348300a4bc75ab23f1b921643fc7a29a7a48bf935dfbf476db09ba2a539dd7dbaf0a05cc2c730f4e0382b097fccbecfc8c.0x6a567d3eabed4d09b438bf9a814eb6011c5302944bb4a0e84a3607700672194c',
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
            count += 1
        return details
    
    else:
        print(f"Failed to fetch data for {item}, status code: {response.status_code}")
        return []
