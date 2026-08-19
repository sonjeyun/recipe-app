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

    // 4. 로딩 표시
    result.innerHTML = "<p>🍳 레시피를 만들고 있어요... 잠깐만요!</p>";

    // 5. 백엔드로 재료 전송
    fetch("/api/recipe", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ ingredients: ingredients })
    })
    .then(response => response.json())
    .then(data => {
        result.innerHTML = `<p>${data.recipe}</p>`;
    })
    .catch(error => {
        result.innerHTML = "<p>😢 오류가 발생했어요. 다시 시도해주세요!</p>";
        console.error("에러:", error);
    });