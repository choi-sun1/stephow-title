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

## 🛠️ 실행 방법

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

## 📦 예시 응답

```json
<response>
{"title": "stephow.com에서 계정에 로그인하기"}
</response>
```

---

## 🌐 Multilingual Support (다국어 지원)

이 프로젝트는 매뉴얼 제목 생성 시 **언어 설정**을 통해 다국어 출력을 지원합니다.

- 기본 언어는 **Korean (ko)** 입니다.
- 사용자는 `language` 파라미터를 통해 출력 언어를 선택할 수 있습니다.
- Claude는 프롬프트 내부 지시에 따라 해당 언어로 제목을 생성합니다.

### 🔤 사용 가능한 언어 예시

| Language | Code | Example Output |
|----------|------|----------------|
| Korean   | `ko` | `"stephow.com에서 계정에 로그인하기"` |
| English  | `en` | `"How to Log In to Your Account on stephow.com"` |

### ✍️ 사용 예시

```json
{
  "steps": [
    { "step_title": "로그인", "step_description": "로그인 버튼 클릭" },
    { "step_title": "정보 입력", "step_description": "아이디와 비밀번호 입력" }
  ],
  "domain": "stephow.com",
  "language": "ko"
}
```

→ Claude가 한국어로 제목 생성:  
`"stephow.com에서 계정에 로그인하기"`

---

## ✅ Prompt Design Checklist

Claude 3.5 Sonnet 모델을 대상으로 **적합한 결과**를 위해 아래 항목들을 반영했습니다:

- [x] **사용자 목표 인식 유도**
- [x] **명령형 제목 구조 지시**
- [x] **단어 수 제한 (10단어 이하)**
- [x] **도메인 정보 포함 지시**
- [x] **모호한 표현 금지**
- [x] **언어 출력 명시 (Multilingual Output)**
- [x] **다국어 예시 포함 (EN & KO)**
- [x] **출력 형식 고정 (JSON + <response>)**
- [x] **단일 결과만 생성 지시**

---

## 🔒 참고

- `.env` 파일과 `venv/`는 `.gitignore`로 업로드 제외됩니다.
- Claude 3.5는 Amazon Bedrock API를 통해 연결됩니다.

---

## 🙋‍♀️ 기여자

- 인턴: 최해찬  
- 담당 역할: 프롬프트 설계, Claude 연동 자동화, Swagger API 연동
