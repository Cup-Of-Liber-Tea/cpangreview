import requests
import json
import time
import random # random 라이브러리 추가

cookies = {
    'sid': '97040aab3569456bba1330679a85a1661e1e4565',
    'overrideAbTestGroup': '%5B%5D',
    'x-coupang-accept-language': 'ko-KR',
    'x-coupang-target-market': 'KR',
    'bm_ss': 'ab8e18ef4e',
    'PCID': '17477304370704860947982',
    'web-session-id': '57bbbcfc-d057-4ba4-9e17-3eba22cb3e2b',
    'bm_lso': '9C7333CF362AF62E70492261B38C4332BBE4092AE8ACE34B0D36E4A46018BD38~YAAQnjggF9AHzseWAQAAORXa7APPflBK/y7o5lzZ8gfDw79GFEyz0Y2yX+991/kQJiHZafIg00cH8GZidSKibOFNzs4SJ1+O9BazzZuTUYXdXh0ifPeiUiwb0a0ZR6G9keO02uHODXJ10w/43JDP2smxZGBYGfHCXQI7Caz4RpUPqSfbmcWajo0St2kUJ60cQ+/fV71sbyeMmzKpyaG45vuuRgH3BZzz35Diw804p04WfbxuuVh5IIDrOwfWHXPTaetHaQ6H4grNvxU391bHZ5icsOz4NIVV0qkrE/hCXG08Y5sNqVbxSdbBhLFDG2OPsOv+JWjofhcpKrk/lu25g3A+aYIRKbG9gIDWCK1By3WQjNJucxp1Pa4gIxlPTJC7NmgwDpi2PdIhna2K5ZFMm55icAKf3bxcQ4jQ6FE1JTsE3/EUP28pq3FthorJz1H3oJPmXqJ1Vq1oCo4ELBFRqg==^1747730437430',
    'MARKETID': '17477304370704860947982',
    'baby-isWide': 'small',
    'ak_bmsc': '798E4830F999DFAF433933566D15B094~000000000000000000000000000000~YAAQnjggFzEIzseWAQAAWhra7BujL4UK2iTT7O3s1NoLh2uprhx73jSV/2ujrnbL7r9pdS2CUQL3R6ahE3+KSx9mitMItautyPxqQ8kSMBpujT5p375EZUuT8M8e0ZcBAiwQUPbnrFBbMtODNP39kVZXqEUwoyddLyPeJtKAHxCi1a7p3uzv8C2Fxspku+s0Duf+bP0NfLFNAiWye9KHm8PJo7H67ZlmF/vuL3a4TliXapkzviguUI61hG/gD07fcsnL66vY/AsQuxb+hIld+86EjM4bdCGiAS2HClUHoru6/ZATGQ42z4u1vnk5ahfBOAdQMf2rB+v2lNCFDbpREPgf/6zWQxXyvKXxka5YMbSKbWQzRO6e2hDYkxSzu1woDGOEpuGeyh+QYoao',
    'bm_mi': 'B4CA97C6F2E81F2BB3F8351C714A7882~YAAQrOQ1F0VX6MiWAQAANJPd7BsooWBHJ376EXT9IVbKc0I8hsFnF/d+QlKrU5zz7Rk+LSmGgNlg8tNsZI9QaUKqp4TUEpMWWP+HOH8MJ+FNV0n6gU+hhE+im1fkas82Dy2EurvkzTjy2CdkLn7AmVsPYCyVXx8qGcIquxQnUdOj8IZiiB3JTDd/sQb8ZHYRqCwHogNOHs16N6gilXX+chp2iIvjr3e9lzG42AfXI4R3OF1MRzu0zvtYtjhcl47KahCQovYlJj66F6QSSQ85QfPLTj+JbGNl8Cg8lU47LydBkDLQZu4KMAiMLufMoaET6EqE6DlyKUTOyVQ9PFbcwOmCfUc=~1',
    'bm_s': 'YAAQrOQ1F0ZX6MiWAQAANJPd7APm7YT0e5a+wLvgBwph6Ok5J4cOhwmF7l7ebkZFWbejztDsrkWNb2K9Utcu21BKVgDpU9F1DFrmo/xXlj+ejZ0K6MpdpdjXurPnF5W41gm6ykVH0rAFcNvJhSOyTft32CMJ6rKzY5nyi6JB7nxoLhQFaz8qfd0qfgheK2GdUAomO8if71fGIhLlZ32fI18gHJwdrxPfjFW5Xird7hKx2NofNfHBzig61eQI751c5mnmON06dZ0+kwkR4AUAWFd/7V051eN2J33ngCdE/NkUxb24AORROCbai/tQ4wGMyvXlOr7fKQEbHyvudlQPzjV6X4KsZipOA8veQ2iE44YUSWnwRUsXXA0IZtAQoiXAmnSETejTB7g+19pUtiotLzov9jTgI8LmuxJAV+yuW1cAplL9BQ3EX5w+Vxw7vlY9s80ajHCrGUuFYcK6P3ww1SZFX88+rbEMLeSPyBDCTr91Kjb+QER3LkPY5wQl8TeXRlqZYlsjZJn1zTODX6pr71hxvQAaWD/35ZUujei9evAtD/t549O1pnEp+ET0lGpO2vsCcFbzvD98kK0M3MiwJQ==',
    'bm_so': 'FBE92E38C837F67F05FB2E31180753A6BCCE27BACFB0FEEC69B04B9EEBD112D9~YAAQrOQ1F0dX6MiWAQAANJPd7AOgE/G5XGcoBSwvrwofi9x0MDV4oYYeoZJgptCvPinqgl+VJPOqI5vadOoMREAd95Eokyl7uk6Dr3+PJCjVjFZZxK3olKnqqoQ+C6Xm00xnO6j0MNFRJe+1lP4aGNkUlrysByfNpyASl0j9L50bqK9us4KzBS5tIJM4PMEDGMqmPdgnnq7XFlCutPU1FhHI4ql9e9rfuJ+bp0bbDX0oL2j0vE41Y9JFBUPfJFuT2fui4ms4Re/qYeOC21w5fDFVSdn0PmUfwIHmHnkfWtAcGLv2IOrYsiLKlut1f13vTz+1Qpsrm9enxyjA7f6G5M9uWWxIpVQpBYI6+mfk6KVgxqS2sIkzCgQnm9fhfFQH2bzHHZR7/Jb9M3/jzAZQ467NaQPNefgJE4ZK9H2S88tdAzMNLOlTXrYZCFKCo0iWhHSYUco1P2KGJTv8EaSUJg==',
    'bm_sv': '0CD2A8886E19BCFA125073CE5686605C~YAAQrOQ1F0hX6MiWAQAANJPd7BuehIq2yhTlDbyM7SQvV+JGQzfWHl+o5G3dQCOvcGN4wgjGlZJmOLLs3w+2HGHqA9HpWdopFI9eQzkl86GQhu/ZqOo2jJ6y1Ju3CkjlFI2hT5sPIMoed1rceUo5/jUcEXY2JyGjexX+soxLlXnvGxr+YCoQyBJ/tvqZsw82UHxh3cGbZJ//LrrgBTswvXod28Cddzyqj0kg+oB5Xx1GJrp3sos9qw92itYppk3QB/c=~1',
    'bm_sz': 'C46F5D6F7332FE0D9AB4D1F18E359F50~YAAQrOQ1F0lX6MiWAQAANJPd7Bs/9MI8mzEHr7owYBlh57InBCRL05BtOSPb/gE2WVbMHnehbVU9R23tYcwWwWuJcZrAwXF4Z+ZPkfk6yEwBmu1mBf+vv7mgVT3raUs2uUc94OmINARO1B0YNuyWxigTFPeWXjUyM8HIK4hwA+gQW0++TTOLTsIGTevzcX2PC3DDM3MrSzXLu3QJS0mBR8fmq8bMudFOxjHsjrk7aeQS92MtR+IR9xi/kfQ+9v7+yCN+YBTTkOySw3lNe68zgP/Dq4Wc+hri08TN9W8oKOFPXa34jibRX15uO57nv7gEq5rxLgwYAMRXNdrJcztuZHwYF5FGOYAP47dyMSsOycSrLjPFYj39AQ6d0JZqKlVv/9s6ZeJ2pasfGkrIKrEd7Zmva7kFqmk8Nw==~3684146~3425090',
    '_abck': '813856D2A104668BFBB17BF2C3D60CE4~0~YAAQrOQ1F05X6MiWAQAAtZPd7A2jmVuPR6f9p8Qe07zRf/gJjnv8eKFWGgh8GxecZhf4Bt0wUmpC5lN7t7zy/QuJFGISoEYLHjHpchE6cNFIxICi0HNlVdJIX1mdalHASpV0ybWeaWuj1F8n8/ELhnGLnM/WN9kCckbBjUhmtup4XpC9gf458B5RIPNjq/JBDT91JUqIh3F5VjBsLNFy4vzF6gLTWRBDYHNTFHEh/BB3Pbg3VZu+x8eZgrIgmUHSWHjxk6d6slqN+cdBwxk0vWyuhuxZN8Hj5vjK3vPiVBAvnUY/t7FbHXbGdpNxxvyiCXkeMvfQikZuEMEZGmWoiThipLYe8j5Ttd9I68ZhFuuD/i7brq2ausE/H5xxIoD3IE6RUncSVJwbacGj1P1DW+bqL4uKunRpq6zijkkKAXDdLJFVCWOJqRrgKMGtRU5r7XWz7BKxSMGJFAWz9wOUbhO7UpIYyjUc7iQ26WlClT26BH8y9ov23onoDqVD+Exs/qbIzExRn0B7acJOJwKXpr3w6XbjT6LlfNc2lR+uqvf3l/ydvT79wL5K44Tpn+iw9AJDLlmDaI73EYpJ5gpNCZ2i38GY9IshNTWqcUng/Hk6VVcdoq/wmQ==~-1~-1~-1',
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ko',
    'dnt': '1',
    'priority': 'u=1, i',
    'referer': 'https://www.coupang.com/vp/products/8544966476?itemId=24741425756&searchId=202b73be42be481083dcaa691fa13195&sourceType=brandstore_sdp_atf-baseline_list&storeId=210629&subSourceType=brandstore_sdp_atf-baseline_list&vendorId=A01352644&vendorItemId=92060971403',
    'sec-ch-ua': '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
    # 'cookie': 'sid=97040aab3569456bba1330679a85a1661e1e4565; overrideAbTestGroup=%5B%5D; x-coupang-accept-language=ko-KR; x-coupang-target-market=KR; bm_ss=ab8e18ef4e; PCID=17477304370704860947982; web-session-id=57bbbcfc-d057-4ba4-9e17-3eba22cb3e2b; bm_lso=9C7333CF362AF62E70492261B38C4332BBE4092AE8ACE34B0D36E4A46018BD38~YAAQnjggF9AHzseWAQAAORXa7APPflBK/y7o5lzZ8gfDw79GFEyz0Y2yX+991/kQJiHZafIg00cH8GZidSKibOFNzs4SJ1+O9BazzZuTUYXdXh0ifPeiUiwb0a0ZR6G9keO02uHODXJ10w/43JDP2smxZGBYGfHCXQI7Caz4RpUPqSfbmcWajo0St2kUJ60cQ+/fV71sbyeMmzKpyaG45vuuRgH3BZzz35Diw804p04WfbxuuVh5IIDrOwfWHXPTaetHaQ6H4grNvxU391bHZ5icsOz4NIVV0qkrE/hCXG08Y5sNqVbxSdbBhLFDG2OPsOv+JWjofhcpKrk/lu25g3A+aYIRKbG9gIDWCK1By3WQjNJucxp1Pa4gIxlPTJC7NmgwDpi2PdIhna2K5ZFMm55icAKf3bxcQ4jQ6FE1JTsE3/EUP28pq3FthorJz1H3oJPmXqJ1Vq1oCo4ELBFRqg==^1747730437430; MARKETID=17477304370704860947982; baby-isWide=small; ak_bmsc=798E4830F999DFAF433933566D15B094~000000000000000000000000000000~YAAQnjggFzEIzseWAQAAWhra7BujL4UK2iTT7O3s1NoLh2uprhx73jSV/2ujrnbL7r9pdS2CUQL3R6ahE3+KSx9mitMItautyPxqQ8kSMBpujT5p375EZUuT8M8e0ZcBAiwQUPbnrFBbMtODNP39kVZXqEUwoyddLyPeJtKAHxCi1a7p3uzv8C2Fxspku+s0Duf+bP0NfLFNAiWye9KHm8PJo7H67ZlmF/vuL3a4TliXapkzviguUI61hG/gD07fcsnL66vY/AsQuxb+hIld+86EjM4bdCGiAS2HClUHoru6/ZATGQ42z4u1vnk5ahfBOAdQMf2rB+v2lNCFDbpREPgf/6zWQxXyvKXxka5YMbSKbWQzRO6e2hDYkxSzu1woDGOEpuGeyh+QYoao; bm_mi=B4CA97C6F2E81F2BB3F8351C714A7882~YAAQrOQ1F0VX6MiWAQAANJPd7BsooWBHJ376EXT9IVbKc0I8hsFnF/d+QlKrU5zz7Rk+LSmGgNlg8tNsZI9QaUKqp4TUEpMWWP+HOH8MJ+FNV0n6gU+hhE+im1fkas82Dy2EurvkzTjy2CdkLn7AmVsPYCyVXx8qGcIquxQnUdOj8IZiiB3JTDd/sQb8ZHYRqCwHogNOHs16N6gilXX+chp2iIvjr3e9lzG42AfXI4R3OF1MRzu0zvtYtjhcl47KahCQovYlJj66F6QSSQ85QfPLTj+JbGNl8Cg8lU47LydBkDLQZu4KMAiMLufMoaET6EqE6DlyKUTOyVQ9PFbcwOmCfUc=~1; bm_s=YAAQrOQ1F0ZX6MiWAQAANJPd7APm7YT0e5a+wLvgBwph6Ok5J4cOhwmF7l7ebkZFWbejztDsrkWNb2K9Utcu21BKVgDpU9F1DFrmo/xXlj+ejZ0K6MpdpdjXurPnF5W41gm6ykVH0rAFcNvJhSOyTft32CMJ6rKzY5nyi6JB7nxoLhQFaz8qfd0qfgheK2GdUAomO8if71fGIhLlZ32fI18gHJwdrxPfjFW5Xird7hKx2NofNfHBzig61eQI751c5mnmON06dZ0+kwkR4AUAWFd/7V051eN2J33ngCdE/NkUxb24AORROCbai/tQ4wGMyvXlOr7fKQEbHyvudlQPzjV6X4KsZipOA8veQ2iE44YUSWnwRUsXXA0IZtAQoiXAmnSETejTB7g+19pUtiotLzov9jTgI8LmuxJAV+yuW1cAplL9BQ3EX5w+Vxw7vlY9s80ajHCrGUuFYcK6P3ww1SZFX88+rbEMLeSPyBDCTr91Kjb+QER3LkPY5wQl8TeXRlqZYlsjZJn1zTODX6pr71hxvQAaWD/35ZUujei9evAtD/t549O1pnEp+ET0lGpO2vsCcFbzvD98kK0M3MiwJQ==; bm_so=FBE92E38C837F67F05FB2E31180753A6BCCE27BACFB0FEEC69B04B9EEBD112D9~YAAQrOQ1F0dX6MiWAQAANJPd7AOgE/G5XGcoBSwvrwofi9x0MDV4oYYeoZJgptCvPinqgl+VJPOqI5vadOoMREAd95Eokyl7uk6Dr3+PJCjVjFZZxK3olKnqqoQ+C6Xm00xnO6j0MNFRJe+1lP4aGNkUlrysByfNpyASl0j9L50bqK9us4KzBS5tIJM4PMEDGMqmPdgnnq7XFlCutPU1FhHI4ql9e9rfuJ+bp0bbDX0oL2j0vE41Y9JFBUPfJFuT2fui4ms4Re/qYeOC21w5fDFVSdn0PmUfwIHmHnkfWtAcGLv2IOrYsiLKlut1f13vTz+1Qpsrm9enxyjA7f6G5M9uWWxIpVQpBYI6+mfk6KVgxqS2sIkzCgQnm9fhfFQH2bzHHZR7/Jb9M3/jzAZQ467NaQPNefgJE4ZK9H2S88tdAzMNLOlTXrYZCFKCo0iWhHSYUco1P2KGJTv8EaSUJg==; bm_sv=0CD2A8886E19BCFA125073CE5686605C~YAAQrOQ1F0hX6MiWAQAANJPd7BuehIq2yhTlDbyM7SQvV+JGQzfWHl+o5G3dQCOvcGN4wgjGlZJmOLLs3w+2HGHqA9HpWdopFI9eQzkl86GQhu/ZqOo2jJ6y1Ju3CkjlFI2hT5sPIMoed1rceUo5/jUcEXY2JyGjexX+soxLlXnvGxr+YCoQyBJ/tvqZsw82UHxh3cGbZJ//LrrgBTswvXod28Cddzyqj0kg+oB5Xx1GJrp3sos9qw92itYppk3QB/c=~1; bm_sz=C46F5D6F7332FE0D9AB4D1F18E359F50~YAAQrOQ1F0lX6MiWAQAANJPd7Bs/9MI8mzEHr7owYBlh57InBCRL05BtOSPb/gE2WVbMHnehbVU9R23tYcwWwWuJcZrAwXF4Z+ZPkfk6yEwBmu1mBf+vv7mgVT3raUs2uUc94OmINARO1B0YNuyWxigTFPeWXjUyM8HIK4hwA+gQW0++TTOLTsIGTevzcX2PC3DDM3MrSzXLu3QJS0mBR8fmq8bMudFOxjHsjrk7aeQS92MtR+IR9xi/kfQ+9v7+yCN+YBTTkOySw3lNe68zgP/Dq4Wc+hri08TN9W8oKOFPXa34jibRX15uO57nv7gEq5rxLgwYAMRXNdrJcztuZHwYF5FGOYAP47dyMSsOycSrLjPFYj39AQ6d0JZqKlVv/9s6ZeJ2pasfGkrIKrEd7Zmva7kFqmk8Nw==~3684146~3425090; _abck=813856D2A104668BFBB17BF2C3D60CE4~0~YAAQrOQ1F05X6MiWAQAAtZPd7A2jmVuPR6f9p8Qe07zRf/gJjnv8eKFWGgh8GxecZhf4Bt0wUmpC5lN7t7zy/QuJFGISoEYLHjHpchE6cNFIxICi0HNlVdJIX1mdalHASpV0ybWeaWuj1F8n8/ELhnGLnM/WN9kCckbBjUhmtup4XpC9gf458B5RIPNjq/JBDT91JUqIh3F5VjBsLNFy4vzF6gLTWRBDYHNTFHEh/BB3Pbg3VZu+x8eZgrIgmUHSWHjxk6d6slqN+cdBwxk0vWyuhuxZN8Hj5vjK3vPiVBAvnUY/t7FbHXbGdpNxxvyiCXkeMvfQikZuEMEZGmWoiThipLYe8j5Ttd9I68ZhFuuD/i7brq2ausE/H5xxIoD3IE6RUncSVJwbacGj1P1DW+bqL4uKunRpq6zijkkKAXDdLJFVCWOJqRrgKMGtRU5r7XWz7BKxSMGJFAWz9wOUbhO7UpIYyjUc7iQ26WlClT26BH8y9ov23onoDqVD+Exs/qbIzExRn0B7acJOJwKXpr3w6XbjT6LlfNc2lR+uqvf3l/ydvT79wL5K44Tpn+iw9AJDLlmDaI73EYpJ5gpNCZ2i38GY9IshNTWqcUng/Hk6VVcdoq/wmQ==~-1~-1~-1',
}

params = {
    'productId': '7279902664', #상품의 아이디값
    'page': '1', # 초기 페이지 번호
    'size': '5',
    'sortBy': 'ORDER_SCORE_ASC',
    'ratingSummary': 'true',
    'ratings': '',
    'market': '',
}

base_url = 'https://www.coupang.com/next-api/review'
all_reviews = []
total_pages = 1 # 초기 total_pages는 1로 설정

# 첫 번째 페이지 요청 및 전체 페이지 수 확인
print("첫 번째 페이지 데이터를 가져오는 중...")
response = requests.get(base_url, params=params, cookies=cookies, headers=headers)
response_json = response.json()

# 첫 번째 페이지의 리뷰 데이터 추가
if response_json.get('rData') and response_json['rData'].get('paging') and response_json['rData']['paging'].get('contents'):
    all_reviews.extend(response_json['rData']['paging']['contents'])
    # 전체 페이지 수 업데이트
    if response_json['rData']['paging'].get('totalPage'):
        total_pages = response_json['rData']['paging']['totalPage']
    print(f"총 {total_pages} 페이지 중 1 페이지를 가져왔습니다.")
else:
    print("첫 번째 페이지에서 리뷰 데이터를 찾을 수 없습니다.")
    total_pages = 0 # 리뷰가 없으면 페이지 0으로 설정

# 나머지 페이지 순회하며 데이터 가져오기
for page_num in range(2, total_pages + 1):
    print(f"{page_num} 페이지 데이터를 가져오는 중...")
    params['page'] = str(page_num) # 페이지 번호 업데이트
    response = requests.get(base_url, params=params, cookies=cookies, headers=headers)
    response_json = response.json()

    if response_json.get('rData') and response_json['rData'].get('paging') and response_json['rData']['paging'].get('contents'):
        all_reviews.extend(response_json['rData']['paging']['contents'])
        print(f"{page_num} 페이지 리뷰 {len(response_json['rData']['paging']['contents'])}개를 추가했습니다. 현재까지 총 리뷰 수: {len(all_reviews)}")
    else:
        print(f"{page_num} 페이지에서 리뷰 데이터를 찾을 수 없습니다.")

    # 랜덤 지연 시간 설정 (예: 0.5초에서 2.0초 사이)
    delay_time = random.uniform(0.9, 1.3)
    print(f"다음 페이지 요청까지 {delay_time:.2f}초 대기합니다.")
    time.sleep(delay_time) # 랜덤 시간 지연

# 전체 리뷰 데이터를 JSON 파일로 저장
json_filename = 'raw_reviews.json'
with open(json_filename, 'w', encoding='utf-8') as f:
    json.dump(all_reviews, f, indent=4, ensure_ascii=False)

print(f"\n전체 리뷰 데이터 ({len(all_reviews)}개)가 '{json_filename}' 파일로 저장되었습니다.")