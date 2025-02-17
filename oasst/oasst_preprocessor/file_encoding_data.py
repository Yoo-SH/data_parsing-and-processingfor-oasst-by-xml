import chardet  # 문자 인코딩을 감지하는 라이브러리
import logging

GLOBAL_ENCODING_UNIFICATION = None


def get_encoding(file_path):
    """
    파일의 문자 인코딩을 감지합니다.

    Args:
        file_path (str): 인코딩을 감지할 파일의 경로.

    Returns:
        None

    Side Effects:
        글로벌 변수 GLOBAL_ENCODING_UNIFICATION을 설정합니다.
    """
    global GLOBAL_ENCODING_UNIFICATION

    logging.info(f"파일의 인코딩을 값을 감지하는 중입니다: {file_path}")
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    GLOBAL_ENCODING_UNIFICATION = result['encoding']
    logging.info(f"파일의 인코딩 값: {GLOBAL_ENCODING_UNIFICATION}")
