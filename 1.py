import requests
import json
import time
import random # random 라이브러리 추가
import os # os 라이브러리 추가
import subprocess # subprocess 라이브러리 추가
import requests

cookies = {
    'x-coupang-target-market': 'KR',
    'x-coupang-accept-language': 'ko-KR',
    'PCID': '17593377736643510956028',
    '__cf_bm': 'xbSK3Nv9u4M_UWthvhkIyRtKWXIbmEVDnfqo6TPqa6g-1759337774-1.0.1.1-uf43v3yFaYYH.rKzANO3ln2NbsSg2r77E78lOYG6zjNN7BTOqSttpieUvy2JAKc71WGtbHbor7EWVyc8zRdiCx2hyROgkC2_1o3DYOnesxs',
    'cf_clearance': 'n0VHOMkge0kWJ_QL0zVOlH4IQjG.c8xLsIUnTQ6XZp8-1759337774-1.2.1.1-rGz.p5K82hgvLktMviCXGFrZZAN52zxYW3qByuOtZRD5m94J6aSGVxbGIduJGzRq4jnhxnWnrsjgd_biLvzsLuiWFgyfrjuEEnpHQXNKomYo13ag6nslrw9OxBclQqivudtw70oqZ4WwPIaC2cXGRWY59KJI9HZsRY72_oQ9Ro14NfuOwfwKI8fe7TX6Ls6IX0oVUCxNDKdV7beYntKJuV_HdqSRnq4ISmp6Lykvzao',
    'sid': '5521f4aba29f4bab81897c1104fdc65ab27e90c4',
    '_abck': '428F4221E304BB557ED076A24958B540~-1~YAAQyjpvPUsoJpqZAQAA5f6zoA6tpHRvU3FUqt+givDkHG5zmrmqQQtSaT6nXj/rlmiwMGT3ILqSsGzb6isJXo5FObAXFPHkghAh3vCenv0X9eiHiUVbQzLVO2dUN3iseLasadLUb5fwB0k8ipURjcKLZh6On5dzKnAn5M0V3ChN/knUvHvSZDN28T2k9kICRZOSXb9oSPTo/P/hYhfi7y8HIqJiK4iriHrdZlC8SGk7HWlFyl/fVtnfhUWNBnMwIQ2dxpxotdsQaVkCN8zW88OJrdr/hgECxcaww3v74M6xmHH2hmPtw2jgocXD+PFVyYaBJFw//LkCFnxKZxicGSQFxxiYhNzDx9V+viY5q2qKueRvAZZq2Vy9jPFyE9amVSY7D9BGkzL7li8zvLwdnBuIaI9z4ftwlgpQm3b6NqCvyvqqv0sZGbJ069ZnU/kxlAVe2wJrVcO7TBJUx2clZPzKzcSOIQ==~-1~-1~-1~-1~-1',
    'ak_bmsc': '37B2438432BE5CC75B42F1F09E789002~000000000000000000000000000000~YAAQyjpvPUwoJpqZAQAA5f6zoB3hmxJps20PPIZJWCyIVCDk64BTZoMNjTv0fvaXeojrV7xyh77zpqGEvjTHrFCR/uEk4sKauPlr43UsFAcBqPNnvLk1tkl21NVhFu+yAqunCPPVPga9lWwSFMtnf3EDv8A+W8sLPaYeBHF6ONHEBoxRRgYXbcULhlajbFBDSfhqavOrLF+yg3oATHy+4JYpAmQQgVAuYsnQWujdnh2dskIdMg0TwMD4UTfxn32ON7C2oo3obtu54Q9o5whK+hSp1MSsf91eqR3BTiNY/iMGqf+9NbyGqujihhwjf/Alqb0i670MvLnApQAFC580/BWEaq2G4/6noa/t6FALaqGvFbBeyvEHfa77udzWUgn9kKYqUeT1wCu5IJ8Mzw==',
    'bm_sz': 'A0B8B889A4096CB9B49412D0A160B4E2~YAAQyjpvPU0oJpqZAQAA5f6zoB0CL+vADe5GhlsUwtFoO1BQPkgCxShNpkI816JDaM9lAP8DrRjbPQe9wdhDTdH0Vk3U4d1IptxI0tAwhLFJDtsRxAFMwqWntAp1tqVJ5gdzbMAPkbEtgGF+BHn/1iBhOVc8eu+DKdCdIV/3AbbXumKju6XpPs6i9ub4sCb5zPFeU9jZt/CRvoxZ7tzHcjR4rDcQdrmk6DGWqmT54nOdVKXnizjxoOIeL0yX9aZmJcEDU0YNfuYSoH6U0Es9RkA8I2qDz2aXrhkUC0A57YmqsA4aiDCkcPNA4N3CTjb4SVEcFeOPVCd2h0hSJQoBXH2mXOJfRm30aB3Uue2Z6x6Jnm+si/n9HGXy~3752771~3356981',
    '_fbp': 'fb.1.1759337775597.162847419422531698',
    'cto_bundle': '1xw5Al9ZYk5uVzFUQUxjJTJGTGRHRjBWVGZTWEdFYmJOSnl6aFJubzZ6cHdtTjdjOGN1dUMlMkZxa0FFYlhjYldJV2MwcWJGUmtVUXJpRkV6bWZ6bTVyOG94RXh5VG9pQzNseXlCV0Fkdk9ySWU1MXVyU1RxUWc5R05NQ29rcyUyQmlyYnpranlOSjBITGRWOTBUYmw1SHU1cHVTSW1rZkRwMGJhc3BIc2I5MDhiR0JGa1hIczQlM0Q',
    'bm_sv': '6D8B5E6855B27E0BDD06993884A035D7~YAAQNq0sF2mpW26ZAQAAsYG5oB1rSmm+CVX+rjANjUvjGTLocHD1XTOvuAd2Z6Xv4NMgERolVuMurxjUSD8ya+3CBWzF2vXdjbMt/qPUi4T76KvJt0CJTmWIDV9/dzTujpz4FRpVmDBVYhjGc4T48OBqBa3a6ImbDOE1TrnU7QPPy/88tEgE6zc0KRMp3nVznP17eFOCqVnxacW8ysHjCJzG6P6rahapgrnx0swkHWTYjzHMcLPr6yVQCgIG7yPr2A==~1'
}

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
    'cache-control': 'no-cache',
    'pragma': 'no-cache',
    'priority': 'u=0',
    'referer': 'https://www.coupang.com/vp/products/8286306299?itemId=23894228861&vendorItemId=90916887599&sourceType=CAMPAIGN&campaignId=82&categoryId=0&traceId=mg87674u',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:143.0) Gecko/20100101 Firefox/143.0',
    'te': 'trailers',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'connection': 'keep-alive'
}

params = {
    'productId': '8286306299',
    'page': '1',
    'size': '10',
    'sortBy': 'DATE_DESC',
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

# 영상을 저장할 디렉토리 생성
video_output_dir = 'videos'
os.makedirs(video_output_dir, exist_ok=True)

# 각 리뷰에서 영상 링크를 찾아 다운로드
print("\n영상 다운로드를 시작합니다...")
for review in all_reviews:
    if 'videoAttachments' in review and review['videoAttachments']:
        for idx, video_attachment in enumerate(review['videoAttachments']):
            video_url = video_attachment.get('videoUrl')
            if video_url:
                review_id = review.get('reviewId', 'unknown_review')
                # 파일 이름 형식: 리뷰ID_video_인덱스.mp4
                output_filename = os.path.join(video_output_dir, f"{review_id}_video_{idx}.mp4")
                
                print(f"리뷰 ID {review_id}의 영상 {idx} 다운로드 중: {video_url} -> {output_filename}")
                
                try:
                    # ffmpeg을 사용하여 m3u8 스트림을 mp4로 변환 및 저장
                    subprocess.run(
                        ['ffmpeg', '-i', video_url, '-c', 'copy', '-bsf:a', 'aac_adtstoasc', output_filename],
                        check=True,
                        capture_output=True,
                        text=True
                    )
                    print(f"성공적으로 다운로드 및 저장되었습니다: {output_filename}")
                except subprocess.CalledProcessError as e:
                    print(f"영상 다운로드 실패 (리뷰 ID: {review_id}, 영상 인덱스: {idx}): {e.stderr}")
                except FileNotFoundError:
                    print("오류: ffmpeg이 설치되어 있지 않거나 PATH에 추가되어 있지 않습니다. ffmpeg을 설치해주세요.")
                except Exception as e:
                    print(f"예상치 못한 오류 발생 (리뷰 ID: {review_id}, 영상 인덱스: {idx}): {e}")

# 전체 리뷰 데이터를 JSON 파일로 저장
json_filename = 'raw_reviews.json'
with open(json_filename, 'w', encoding='utf-8') as f:
    json.dump(all_reviews, f, indent=4, ensure_ascii=False)

print(f"\n전체 리뷰 데이터 ({len(all_reviews)}개)가 '{json_filename}' 파일로 저장되었습니다.")