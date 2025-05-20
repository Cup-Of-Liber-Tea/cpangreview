import json
from datetime import datetime
import pandas as pd

# 원시 리뷰 데이터를 저장한 JSON 파일 경로 및 파일명
json_filename = 'raw_reviews.json'

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

    # 구매옵션 및 고객정보 (reviewSurveyAnswers에서 추출)
    survey_answers = review.get('reviewSurveyAnswers', [])
    
    # 구매옵션 및 고객정보를 위한 딕셔너리 초기화
    purchase_options = {}
    customer_info = {}

    if isinstance(survey_answers, list):
        for i, survey in enumerate(survey_answers):
            # 첫 번째 항목은 구매옵션, 두 번째 항목부터는 고객정보로 간주 (이전 논리 유지)
            if i == 0:
                purchase_options[f'구매옵션_옵션명1'] = survey.get('question', '')
                purchase_options[f'구매옵션_옵션값1'] = survey.get('answer', '')
            elif i > 0 and i < 6: # 최대 5개의 구매옵션/고객정보 항목 처리
                 # 이미지를 보니 구매옵션이 여러개 올 수 있는 구조 같아 구매옵션2~5, 고객정보1~5로 분리합니다.
                 # 실제 데이터 구조에 따라 이 부분은 조정이 필요할 수 있습니다.
                 # 현재는 surveyAnswers의 첫번째가 구매옵션, 나머지가 고객정보로 간주합니다.
                customer_info_index = i # 고객정보는 인덱스 1부터 시작
                customer_info[f'고객정보_정보명{customer_info_index}'] = survey.get('question', '')
                customer_info[f'고객정보_답변값{customer_info_index}'] = survey.get('answer', '')
            # 이미지를 보니 구매옵션도 여러개 올 수 있도록 되어 있어서, surveyAnswers의 question 내용을 보고 판단하는 것이 더 정확할 수 있습니다.
            # 하지만 현재 데이터와 이전 요청을 바탕으로 첫번째 surveyAnswers는 구매옵션, 나머지는 고객정보로 처리합니다.
            # 만약 필요하다면 이 로직을 survey['question'] 내용을 보고 구매옵션과 고객정보를 구분하도록 변경할 수 있습니다.

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
        **purchase_options, # 구매옵션 딕셔너리 언팩
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
excel_filename = 'reviews_processed.xlsx' # 파일명 변경하여 기존 파일과 구분
df.to_excel(excel_filename, index=False)
print(f"\n데이터가 '{excel_filename}' 파일로 저장되었습니다.")
