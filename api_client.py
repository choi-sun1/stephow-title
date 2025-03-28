import requests

def fetch_manual_detail(workspace_id, manual_id, api_token):
    url = f"https://dev.api.guideflo.com/workspaces/{workspace_id}/manuals/{manual_id}"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Accept": "application/json"
    }

    # 🔍 헤더 출력 위치는 여기!
    print("🧪 Authorization 헤더:")
    print(headers)

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("매뉴얼 API 응답 성공")
        return response.json()
    else:
        print(f"API 요청 실패, 상태코드: {response.status_code}")
        print("응답 내용:", response.text)
        return None
