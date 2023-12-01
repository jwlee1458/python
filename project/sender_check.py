# 금지된 사용자 확인
def is_banned_sender(sender):
    banned_senders = ["@naver.com","@naver.com"]
    
    for banned_sender in banned_senders:
        if sender in banned_sender:
            return True, f"- 스팸으로 분류된 송신자 : {sender}"
    else:
        return False