// select box selected 값을 span에 추가, 값이 추가되면
$('#selectTarget').on('change',()=>{
    $textSelect = $('#selectTarget option:selected').text()
    $('.select_on').text($textSelect)
    $('.opt_comm').removeClass('sign_warn')
})


// 정보 입력 안하고 다음 단계 클릭시 발생 이벤트
// 1. select box에 옵션 없을 시 경고 class 추가
// 2. checked가 3개가 아니면 해당 위치에 경고 class 추가
$('.link_step').on('click', () => {
    if ($('.select_option').text() == '카테고리') {
        $('.opt_comm').addClass('sign_warn')
        return
    }

    if ($('.inp_comm').filter((i, v) => $(v).prop('checked')).length !== 3) {
        $('.lab_comm .ico_together').addClass('ico_warn')
        $('.desc_form').parent().addClass('sign_warn')
        return
    }
})

// 체크박스 3개 체크시 경고 아이콘 class 제거
$('.inp_comm').on('change',()=>{
    if ($('.inp_comm').filter((i, v) => $(v).prop('checked')).length == 3) {
        $('.lab_comm .ico_together').removeClass('ico_warn')
        $('.desc_form').parent().removeClass('sign_warn')
    }
})