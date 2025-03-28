from dotenv import load_dotenv
import os
from api_client import fetch_manual_detail
from claude_prompt import build_prompt_from_steps
from claude_client import call_claude

# 1. .env에서 API_TOKEN 불러오기
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

# 2. 매뉴얼 정보
WORKSPACE_ID = 17
MANUAL_ID = 2808

def main():
    # 3. API 호출
    data = fetch_manual_detail(WORKSPACE_ID, MANUAL_ID, API_TOKEN)
    if not data:
        print("매뉴얼 데이터를 불러오지 못했습니다.")
        return

    # 4. steps 추출 + 프롬프트 생성
    steps = data.get("steps", [])
    domain = data.get("manual_name", "stephow.com")

    prompt = build_prompt_from_steps(steps, domain)
    print("Claude 프롬프트:\n")
    print(prompt)

    # 5. Claude 호출
    response = call_claude(prompt)
    print("\n Claude 응답:\n")
    print(response)

if __name__ == "__main__":
    main()
