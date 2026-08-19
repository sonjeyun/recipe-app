from http.server import BaseHTTPRequestHandler
import json
import os
import google.generativeai as genai

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. 프론트에서 보낸 데이터 받기
        length = int(self.headers.get('Content-Length'))
        body = json.loads(self.rfile.read(length))
        ingredients = body.get('ingredients', '')

        # 2. 빈 입력 체크 (실패 처리!)
        if not ingredients:
            self.send_error_response(400, "재료를 입력해주세요!")
            return

        try:
            # 3. Gemini API 설정 (환경변수에서 키 읽기)
            genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
            model = genai.GenerativeModel('gemini-1.5-flash')

            # 4. AI에게 요청할 질문(프롬프트)
            prompt = f"""너는 자취생을 위한 요리 전문가야.
다음 재료로 만들 수 있는 간단한 요리 1개를 추천해줘: {ingredients}
- 요리 이름
- 필요한 추가 재료
- 조리 순서 (3~5단계)
초보자도 쉽게 따라할 수 있게 알려줘."""

            # 5. AI 응답 받기
            response = model.generate_content(prompt)

            # 6. 프론트로 결과 전송
            self.send_success_response(response.text)

        except Exception as e:
            # API 오류 처리!
            self.send_error_response(500, "AI 호출 중 오류가 발생했어요.")

    def send_success_response(self, text):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"recipe": text}, ensure_ascii=False).encode('utf-8'))

    def send_error_response(self, code, message):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"error": message}, ensure_ascii=False).encode('utf-8'))