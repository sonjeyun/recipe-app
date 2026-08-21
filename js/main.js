// 1. HTML 요소들을 가져오기
const input = document.getElementById("ingredientInput");
const button = document.getElementById("submitBtn");
const result = document.getElementById("result");

// ⭐ if 열기!
if (button) {
    button.addEventListener("click", function () {
        const ingredients = input.value.trim();

        if (ingredients === "") {
            alert("재료를 하나 이상 입력해주세요! 🥕");
            return;
        }

        result.innerHTML = "<p>🍳 레시피를 만들고 있어요... 잠깐만요!</p>";

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
    });
}   // ⭐ if 닫기!

// ===== 다크 모드 =====
const darkBtn = document.getElementById("darkModeBtn");

if (darkBtn) {
    darkBtn.addEventListener("click", function () {
        document.body.classList.toggle("dark");
        
        if (document.body.classList.contains("dark")) {
            darkBtn.textContent = "☀️";
        } else {
            darkBtn.textContent = "🌙";
        }
    });
}