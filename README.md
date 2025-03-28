# Stephow 제목 생성기

Claude 3.5 + Swagger API를 활용해  
매뉴얼의 step 데이터를 분석하고 **자동으로 제목을 생성**하는 프로젝트입니다.

---

## ✅ 주요 기능

- Swagger API로 매뉴얼 상세 정보(step 포함) 가져오기
- Claude 3.5 (Amazon Bedrock)를 통해 워크플로우 요약
- `steps` 기반 프롬프트 자동 생성
- Claude 응답에서 매뉴얼 제목 추출

---

## 📁 프로젝트 구조

```
stephow-auto-title/
├── main.py                # 실행 진입점
├── api_client.py          # Swagger API 호출 로직
├── claude_prompt.py       # Claude 프롬프트 생성 로직
├── claude_client.py       # Claude 3.5 API 호출 (boto3)
├── .env                   # API 토큰 (업로드 금지)
├── .gitignore             # .env, venv 제외 설정
├── README.md              # 프로젝트 설명
└── requirements.txt       # 설치 의존성
```

---

## 🚀 실행 방법

### 1. 필수 설치

```bash
pip install -r requirements.txt
```

### 2. `.env` 파일 생성

```env
API_TOKEN=eyJhbGciOi... (Bearer 제외한 순수 토큰만)
```

### 3. 실행

```bash
python main.py
```

---

## 🧪 예시 응답

```json
<response>
{"title": "How to Connect Your Gmail Account"}
</response>
```

---

## 🔒 참고

- `.env` 파일과 `venv/`는 `.gitignore`로 업로드 제외됩니다.
- Claude 3.5는 Amazon Bedrock API를 통해 연결됩니다.

---

## 🙋‍♀️ 기여자

- 인턴: 최해찬  
- 담당 역할: 프롬프트 설계, Claude 연동 자동화, Swagger API 연동
