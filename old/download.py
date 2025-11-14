import json
import os
import requests
from urllib.parse import urlparse

def download_file(url, folder_path, filename):
    """
    URL에서 파일을 다운로드하여 지정된 폴더에 저장합니다.
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filepath = os.path.join(folder_path, filename)
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status() # HTTP 오류 발생 시 예외를 발생시킵니다.

        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"다운로드 완료: {filepath}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"다운로드 실패: {url} - {e}")
        return False

def process_json_file(json_filepath, output_base_dir):
    """
    단일 JSON 파일을 처리하여 미디어 링크를 추출하고 다운로드합니다.
    """
    print(f"'{json_filepath}' 파일 처리 중...")
    try:
        with open(json_filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"오류: '{json_filepath}' 파일을 찾을 수 없습니다.")
        return
    except json.JSONDecodeError as e:
        print(f"오류: '{json_filepath}' JSON 파싱 실패 - {e}")
        return

    for review in data:
        review_id = review.get('reviewId')
        if not review_id:
            continue

        review_output_dir = os.path.join(output_base_dir, str(review_id))
        
        # attachments 처리 (이미지/영상)
        attachments = review.get('attachments', [])
        for i, attachment in enumerate(attachments):
            attachment_type = attachment.get('attachmentType')
            img_src_origin = attachment.get('imgSrcOrigin')
            
            if img_src_origin and attachment_type in ["IMAGE", "VIDEO"]:
                # URL에서 파일명 추출
                parsed_url = urlparse(img_src_origin)
                path_segments = parsed_url.path.split('/')
                original_filename = path_segments[-1] if path_segments else f"{review_id}_{attachment['id']}.{'jpg' if attachment_type == 'IMAGE' else 'mp4'}"
                
                # 파일명이 너무 길거나 특수문자가 많을 경우 안전한 이름으로 변경
                filename_base, file_extension = os.path.splitext(original_filename)
                safe_filename = f"{filename_base[:50]}{file_extension}" # 파일명 길이 제한
                
                # 중복 파일명 방지를 위해 인덱스 추가
                filename = f"{review_id}_{i+1}_{safe_filename}"


                download_file(img_src_origin, review_output_dir, filename)

def main():
    json_dir = './' # JSON 파일들이 있는 디렉토리
    output_base_dir = 'downloaded_media/' # 다운로드된 미디어가 저장될 기본 디렉토리

    if not os.path.exists(output_base_dir):
        os.makedirs(output_base_dir)

    # json_dir 내의 모든 JSON 파일을 찾습니다.
    json_files = [f for f in os.listdir(json_dir) if f.endswith('.json')]

    if not json_files:
        print(f"'{json_dir}' 디렉토리에서 JSON 파일을 찾을 수 없습니다.")
        return

    for json_file in json_files:
        json_filepath = os.path.join(json_dir, json_file)
        process_json_file(json_filepath, output_base_dir)

    print("모든 JSON 파일 처리 완료.")

if __name__ == "__main__":
    main()