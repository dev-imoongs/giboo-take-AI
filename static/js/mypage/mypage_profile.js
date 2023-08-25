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
// $('.btn-del').on('click',()=>{
//         $('#modalOFF').attr('id','modalON')
//         $('.dimmed_layer').css('height','100%');
//         $('.dialog-content').css('display','block');
//         $('.modal-delete').css('display','block');
//         $('.modal-policy').css('display','none');
// })

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
document.addEventListener("DOMContentLoaded", function (e) {
    let memberGenderJS = "{{ member_gender }}"; 

    let maleRadio = document.getElementById("genderChk1");
    let femaleRadio = document.getElementById("genderChk2");
    let notselectRadio = document.getElementById("genderChk3");

    if (memberGender === "male") {
        maleRadio.checked = true;
    } else if (memberGender === "female") {
        femaleRadio.checked = true;
    } else if (memberGender === "notselect") {
        notselectRadio.checked = true;
    }
});

const input = document.getElementById("subTitle");
const charCount = document.getElementById("charCount");
const maxLength = 19;

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






// 파일 입력 필드와 이미지 태그 엘리먼트를 가져옴
const imageInput = document.getElementById('upload-profile-img');
const checkProfileImg = document.getElementById('checkProfileImg');

// 파일 입력 필드의 값이 변경될 때 호출되는 함수
imageInput.addEventListener('change', function() {

    const reader = new FileReader();
    reader.onload = function (e) {
        checkProfileImg.src = e.target.result;
    };

      reader.readAsDataURL(imageInput.files[0]);
    });

    //삭제버튼을 누르면 src가 지워짐
    const deleteButton = document.querySelector('.btn-del');
    const input_file = document.querySelector(".upload-profile-img");
     $("input[name='xFlag']").val(false)
    console.log(deleteButton)
    console.log(checkProfileImg)
    deleteButton.addEventListener('click', function() {
        console.log("e")
      // 이미지 태그의 src 속성을 삭제
      checkProfileImg.src = '';
      input_file.value = "";
      $("input[name='xFlag']").val(true)
      console.log($("input[name='xFlag']"))
    });

document.addEventListener('DOMContentLoaded', function() {
  const submitButton = document.getElementById('submitButton');
  const checkPolicy = document.getElementById('checkPolicy');



  submitButton.addEventListener('click', function(e) {
    if (!checkPolicy.checked) {
        console.log('체크박스가 체크되지 않았습니다.');
      return;
    }
    $("#save_data").submit()
      console.log('확인버튼 눌림')


  });
});

