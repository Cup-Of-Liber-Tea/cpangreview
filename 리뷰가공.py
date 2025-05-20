import json
from datetime import datetime
import pandas as pd

# 원시 리뷰 데이터를 저장한 JSON 파일 경로 및 파일명
json_filename = '7279902664.json'

# JSON 파일 읽어오기
try:
    with open(json_filename, 'r', encoding='utf-8') as f:
        raw_data = json.load(f) # 파일을 읽어서 raw_data 변수에 저장
    print(f"'{json_filename}' 파일을 성공적으로 읽어왔습니다.")
except FileNotFoundError:
    print(f"오류: '{json_filename}' 파일을 찾을 수 없습니다. '1.py'를 먼저 실행하여 파일을 생성해주세요.")
    exit() # 파일이 없으면 프로그램 종료
except json.JSONDecodeError:
    print(f"오류: '{json_filename}' 파일이 올바른 JSON 형식이 아닙니다.")
    exit() # JSON 형식이 잘못되었으면 프로그램 종료

# raw_reviews.json 파일에는 이제 리뷰 목록(리스트)만 저장되어 있으므로 raw_data 자체가 리뷰 목록입니다.
reviews = raw_data # raw_data를 바로 reviews 변수에 할당

# 데이터를 저장할 리스트 초기화
data_list = []

for review in reviews: # reviews 리스트를 순회
    review_id = review.get('reviewId', '')
    product_id = review.get('productId', '')

    # reviewAt 타임스탬프 처리
    review_at_timestamp = review.get('reviewAt')
    if review_at_timestamp:
        dt_object = datetime.fromtimestamp(review_at_timestamp / 1000)
        review_date = dt_object.strftime('%Y-%m-%d')
        review_time = dt_object.strftime('%H:%M:%S')
    else:
        review_date = ''
        review_time = ''

    # 작성자명 (display name 사용)
    reviewer_name = review.get('displayName', '')

    review_title = review.get('title', '')
    review_content = review.get('content', '')
    review_rating = review.get('rating', '')
    admin_comment = '' # 관리자 댓글 필드는 JSON에 없음

    # 구매옵션 추출 (itemName 필드 사용)
    item_name = review.get('itemName', '')
    item_name_parts = item_name.split(',', 1) # 첫 번째 쉼표를 기준으로 분리
    purchase_option_name = item_name_parts[0].strip() if item_name_parts else ''
    purchase_option_value = item_name_parts[1].strip() if len(item_name_parts) > 1 else ''

    # 고객정보 (reviewSurveyAnswers에서 추출)
    survey_answers = review.get('reviewSurveyAnswers', [])
    
    # 고객정보를 위한 딕셔너리 초기화
    customer_info = {}

    if isinstance(survey_answers, list):
        # reviewSurveyAnswers의 처음 5개 항목을 고객 정보로 추출
        for i in range(min(len(survey_answers), 5)): # survey_answers 길이 또는 5 중 작은 값까지 반복
            survey = survey_answers[i]
            customer_info_index = i + 1 # 고객정보는 인덱스 1부터 시작
            customer_info[f'고객정보_정보명{customer_info_index}'] = survey.get('question', '')
            customer_info[f'고객정보_답변값{customer_info_index}'] = survey.get('answer', '')


    # 이미지 URL 추출 및 개별 칼럼에 할당 (최대 10개)
    image_urls = [attachment.get('imgSrcOrigin', '') for attachment in review.get('attachments', []) if attachment.get('attachmentType') == 'IMAGE']
    image_data = {}
    for i in range(10):
        image_data[f'URL_이미지 {i+1}'] = image_urls[i] if i < len(image_urls) else ''

    # 동영상 URL 추출 및 개별 칼럼에 할당 (최대 10개)
    video_urls = [video_attachment.get('videoUrl', '') for video_attachment in review.get('videoAttachments', []) if video_attachment.get('attachmentType') == 'VIDEO']
    video_data = {}
    for i in range(10):
        video_data[f'URL_동영상 {i+1}'] = video_urls[i] if i < len(video_urls) else ''


    # 추출한 데이터를 딕셔너리로 저장
    review_data = {
        '리뷰_id': review_id,
        '상품_id': product_id,
        '리뷰 작성일자': review_date,
        '리뷰 작성 시간': review_time,
        '리뷰 작성자명': reviewer_name,
        '리뷰 제목': review_title,
        '리뷰_내용': review_content,
        '리뷰_별점': review_rating,
        '관리자_댓글': admin_comment,
        '구매옵션_옵션명1': purchase_option_name, # itemName에서 추출한 구매옵션명
        '구매옵션_옵션값1': purchase_option_value, # itemName에서 추출한 구매옵션값
        **customer_info, # 고객정보 딕셔너리 언팩
        **image_data, # 이미지 데이터 딕셔너리 언팩
        **video_data # 동영상 데이터 딕셔너리 언팩
    }
    data_list.append(review_data)

# pandas DataFrame 생성
df = pd.DataFrame(data_list)

# 필요한 경우, 칼럼 순서를 이미지와 동일하게 재배치할 수 있습니다.
# 현재는 딕셔너리 키 순서대로 DataFrame 칼럼이 생성됩니다.

# 콘솔에 테이블 형태로 출력 (pandas의 to_markdown은 tabulate 필요)
print("\n콘솔 출력 (테이블 형태):")
try:
    print(df.to_markdown(index=False)) # index=False로 인덱스 제외하고 출력
except ImportError:
    print("tabulate 라이브러리가 설치되지 않아 테이블 형태로 출력할 수 없습니다. 'pip install tabulate' 명령어로 설치해주세요.")

# Excel 파일로 저장
excel_filename = f'{json_filename}.xlsx' # 파일명 변경하여 기존 파일과 구분
df.to_excel(excel_filename, index=False)
print(f"\n데이터가 '{excel_filename}' 파일로 저장되었습니다.")
