from http.server import BaseHTTPRequestHandler
import json
import os
import google.generativeai as genai

# Vercel은 handler 클래스를 자동으로 찾아서 실행해요
class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        # 1. 프론트에서 보낸 데이터 받기
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        data = json.loads(body)
        ingredients = data.get('ingredients', '')

        # 2. 빈 입력 실패 처리 (필수 요구사항!)
        if not ingredients:
            self.send_error_response(400, "재료를 입력해주세요!")
            return

        try:
            # 3. Gemini API 설정 (환경변수에서 키 가져오기)
            genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))
            model = genai.GenerativeModel('gemini-flash-latest')

            # 4. AI에게 질문하기
            prompt = f"다음 재료로 만들 수 있는 요리 레시피를 추천해줘: {ingredients}"
            response = model.generate_content(prompt)

            # 5. 성공 응답 보내기
            self.send_success_response(response.text)

        except Exception as e:
            # 6. API 오류 실패 처리
            self.send_error_response(500, f"AI 오류: {str(e)}")

    # 성공 응답 함수
    def send_success_response(self, recipe):
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        result = json.dumps({"recipe": recipe})
        self.wfile.write(result.encode('utf-8'))

    # 오류 응답 함수
    def send_error_response(self, code, message):
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        result = json.dumps({"error": message})
        self.wfile.write(result.encode('utf-8'))