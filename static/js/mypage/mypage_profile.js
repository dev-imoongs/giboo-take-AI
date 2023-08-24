// 생년월일 selectbox 표시
$('#opAge').on("change", (e) => {
    $selectedText = $('#opAge option:selected').text();
    $('#select-age').text($selectedText)
}
)
// 시,도 selectbox 표시
$('select[name="parentRegion"]').on("change", (e) => {
    $selectedText = $('select[name="parentRegion"] option:selected').text();
    $('#select-parentRegion').text($selectedText)
}
)
// 시,군,구 selectbox 표시
$('select[name="region"]').on("change", (e) => {
    $selectedText = $('select[name="region"] option:selected').text();
    $('#select-region').text($selectedText)
    }
)

// 개인정보 방침 내용 보기 클릭 시
$('.btn-view').on("click",() =>{
    $('.btn-view').hide()
    $('.open-policy').show()
})


// 프로필 삭제 버튼 클릭 시 모달창 띄우기
$('.btn-del').on('click',()=>{
        $('#modalOFF').attr('id','modalON')
        $('.dimmed_layer').css('height','100%');
        $('.dialog-content').css('display','block');
        $('.modal-delete').css('display','block');
        $('.modal-policy').css('display','none');
})

//  취소 버튼 클릭 시 모달창 사라짐
$('.btn-type2').on("click", () =>{
        $('#modalON').attr('id','modalOFF');
        $('.dimmed_layer').css('height','0');
        $('.dialog-content').css('display','none');
        $('.modal-delete').css('display','none');
})

// 개인정보 방침 체크 안하고 저장 누를시
$('.link-step').on("click", ()=>{
    if(!$('#checkPolicy').prop("checked")){
        $('#modalOFF').attr('id','modalON')
        $('.dimmed_layer').css('height','100%');
        $('.dialog-content').css('display','block');
        $('.modal-policy').css('display','block');
        $('.modal-delete').css('display','none');
    }
})


// 개인정보 방침 미체크시 확인 버튼 클릭 시 모달창 닫기
$('.btn-confirm').on("click", () =>{
        $('#modalON').attr('id','modalOFF');
        $('.dimmed_layer').css('height','0');
        $('.dialog-content').css('display','none');
        $('.modal-policy').css('display','none');
})

// X버튼 클릭 시 모달창 닫기
$('.btn-close').on("click", () =>{
        $('#modalON').attr('id','modalOFF');
        $('.dimmed_layer').css('height','0');
        $('.dialog-content').css('display','none');
        $('.modal-policy').css('display','none');
})

// gender 라디오버튼 JS
document.addEventListener("DOMContentLoaded", function () {
    // memberGender 값을 가져옵니다.
    let memberGenderJS = "{{ member_gender }}"; // Django 템플릿 변수를 가져옵니다.

    // 라디오 버튼 요소들을 가져옵니다.
    let maleRadio = document.getElementById("genderChk1");
    let femaleRadio = document.getElementById("genderChk2");
    let noselectRadio = document.getElementById("genderChk3");

    // memberGender에 따라 라디오 버튼의 checked 속성을 설정합니다.
    if (memberGender === "male") {
        maleRadio.checked = true;
    } else if (memberGender === "female") {
        femaleRadio.checked = true;
    } else if (memberGender === "noselect") {
        noselectRadio.checked = true;
    }
});

// input 요소와 charCount 요소를 가져옵니다.
const input = document.getElementById("subTitle");
const charCount = document.getElementById("charCount");
const maxLength = 19;

// input 요소에 input 이벤트 리스너를 추가합니다.
input.addEventListener("input", updateCharCount);

function updateCharCount() {
  const currentText = input.value;
  const currentLength = currentText.length;

  if (currentLength > maxLength) {
    // 20자를 초과한 경우, 입력을 제한하고 마지막 20자까지만 유지
    input.value = currentText.slice(0, maxLength);
  }

  // 글자 수를 업데이트
  charCount.textContent = `${currentLength}/`;
}

// 페이지 로딩 시 초기 텍스트를 검사하고 표시
updateCharCount();

document.addEventListener()






