import openai
import os

# 환경변수에서 API Key 가져오기
API_KEY = os.getenv("OPENAI_API_KEY")

# OpenAI 클라이언트 객체 생성
client = openai.OpenAI(api_key=API_KEY)

# 사용 가능한 모델 리스트 가져오기
models = client.models.list()

# 모델 목록 출력
for model in models.data:
    print(model.id)
