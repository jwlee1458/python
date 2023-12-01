# 지정된 확장자 확인
def extend_word_included(msg):
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        # 첨부파일 이름 가져오기
        filename = part.get_filename()
        if filename:
            #여기에 스팸으로 분류하고 싶은확장자를 추가
            malicious_extend = ['php','txt','exe']
            for word in malicious_extend:
                if filename.endswith(word):
                    return True, f"- 금지된 확장자 포함 : .{word}"
            else:
                return False