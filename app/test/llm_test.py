import app.common.config as config

def test2(enabled: bool = False):
    #  # LLM 모델 로드 실패 테스트 코드
    if not enabled:
        return
    config.whisperAI_MODEL_NAME = "except_test"