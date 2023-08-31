// select box selected 값을 span에 추가, 값이 추가되면
$('#selectTarget').on('change',()=>{
    $textSelect = $('#selectTarget option:selected').text()
    $('.select_on').text($textSelect)
    $('.opt_comm').removeClass('sign_warn')
})


let firstPageFlag = false
const toastMsg = function (text) {
    if (!firstPageFlag) {
        $('.toast-bottom-center').show()
        firstPageFlag = true
        $('.toast-message').eq(0).text(text)
        setTimeout(function () {
            firstPageFlag = false
            $('.toast-bottom-center').hide()
        }, 3000)
    }
}



// 정보 입력 안하고 다음 단계 클릭시 발생 이벤트
// 1. select box에 옵션 없을 시 경고 class 추가
// 2. checked가 3개가 아니면 해당 위치에 경고 class 추가

// 위에서 return 되서 아래거까지 한번에 안나옴
$('.link_step1').on('click', (e) => {
    let condition1 = $('.select_option').text() == '카테고리'
    let condition2 = $('.form_cont1 .inp_comm').filter((i, v) => $(v).prop('checked')).length !== 3
    // 각 조건이 true if문을 수행하고
    if (condition1) {
        $('.opt_comm').addClass('sign_warn')
        toastMsg('카테고리를 선택해주세요')
        return;
    }

    if (condition2) {
        $('.lab_comm .ico_together').addClass('ico_warn')
        $('.desc_form').parent().addClass('sign_warn')
        toastMsg('모금검토기준 약관 사항을 동의해주세요.')
        return
    }
    $('.link_tab').closest('li').removeClass('on')
    let $topIndex = $(e.target).closest('.form_cont').index()
    $('.form_cont').hide()
    $('.link_tab').eq($topIndex).parent().addClass('on')
    $('.form_cont').eq($topIndex).show()
    window.scrollTo(0,0)

})
// 확인용 상단탭 눌러서 해당 페이지 띄우기
// $('.link_tab').on('click',(e)=>{
//     $('.form_cont').eq($(e.target).parent().parent().index()).show()
// })

// 체크박스 3개 체크시 경고 아이콘 class 제거
$('.inp_comm').on('change',()=>{
    if ($('.inp_comm').filter((i, v) => $(v).prop('checked')).length == 3) {
        $('.lab_comm .ico_together').removeClass('ico_warn')
        $('.desc_form').parent().removeClass('sign_warn')
    }
})

// 상단탭 클릭시 li
