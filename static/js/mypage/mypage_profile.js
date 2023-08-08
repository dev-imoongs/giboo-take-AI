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