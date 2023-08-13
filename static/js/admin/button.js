document.addEventListener("DOMContentLoaded", function() {
    const inputText = document.getElementById("inputText");
    const consentButton = document.getElementById("consentButton");
    const refuseButton = document.getElementById("refuseButton");

    consentButton.addEventListener("click", function (event) {
        if (inputText.value === "") {
            consentButton.removeEventListener("click", preventConsent);
        } else {
            consentButton.addEventListener("click", preventConsent);
            event.preventDefault();
        }
    });

    function preventConsent() {
        alert("등록 거부사유가 적혀있어 승낙을 수 없습니다!");


    }
        refuseButton.addEventListener("click", function(event){
        if (inputText.value === "") {
            refuseButton.addEventListener("click", preventRefuse);
            event.preventDefault();
        } else {
            refuseButton.removeEventListener("click", preventRefuse);
        }
    });
    function preventRefuse(event) {
        alert("등록 거부사유를 작성해주세요!")
    }
});