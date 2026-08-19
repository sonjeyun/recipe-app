// 1. HTML 요소들을 가져오기
const input = document.getElementById("ingredientInput");   // 입력창
const button = document.getElementById("submitBtn");        // 버튼
const result = document.getElementById("result");           // 결과 영역

// 2. 버튼을 클릭했을 때 실행할 함수
button.addEventListener("click", function () {
    const ingredients = input.value.trim();   // 입력값에서 앞뒤 공백 제거

    // 3. 유효성 검사 — 빈 입력 방지
    if (ingredients === "") {
        alert("재료를 하나 이상 입력해주세요! 🥕");
        return;   // 여기서 함수 종료
    }

    // 4. 입력이 정상이면 결과 영역에 표시 (지금은 확인용)
    result.innerHTML = `<p>입력한 재료: <strong>${ingredients}</strong></p>`;
    console.log("입력된 재료:", ingredients);
});