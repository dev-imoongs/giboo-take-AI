// .lab_choiced가 checkbox on
$('.inp_comm').on('click', (e) => {
    $('label.lab_comm').removeClass('lab_choiced');
    $(e.target).next().addClass('lab_choiced');
})
// 힌트보기 눌렀을때 모달창 띄우기, body_hint에 나올 글 초기값 설정
$('.txt_sign').on('click', () => {
    $('#modalOFF').attr('id', 'modalON')
    $('.dimmed_layer').css('height', '100%');
    $('.dialog-content').css('display', 'block');
    $('.body_hint').hide()
    $('.body_hint').eq(1).show()
})

//  모달창 안에 들어가서 탭 눌렀을때 해당 글은 보여주고 외에는 숨기는 기능
$('.link_hint').on('click',(e)=>{
    $('.link_hint').parent().removeClass('on')
    $(e.target).parent().addClass('on')
    $('.body_hint').hide()
    $('.body_hint').eq($(e.target).parent().index()).show()
})

// 모달창 닫기 버튼
$('.btn_close').on("click", () => {
    $('#modalON').attr('id', 'modalOFF');
    $('.dimmed_layer').css('height', '0');
    $('.dialog-content').css('display', 'none');
})

$(document).ready(function () {
    function updateIDs() {
        $('.ng-scope').each((i, value) => {
            $(value).attr('id', `planBox${i}`)
        })
    }

    function updateAmount() {
        let total = 0
        $('.amount_tf').each((i, v) => {
            let inputValue = $(v).children().val()
            if(inputValue !== "")
                total += parseInt(inputValue)
        })
        // toLocaleString 나라별 금액 단위 표시 ex) 1,000
        let amount = 5000000-total
        $('.total_sum').children().text(`-${amount.toLocaleString("ko-KR")}원`)
    }


    $(".pack_btn .btn_add").on('click', () => {
        $addContent = '<div class="group_tf ng-scope">\n' +
                      '  <div class="cont_tf">\n' +
                      '      <input type="text" classoutline="" placeholder="사용용도 및 산출근거"\n' +
                      '              title="모금액 사용용도 및 산출근거" autocomplete="off"\n' +
                      '              class="tf_write ng-valid ng-dirty ng-valid-parse ng-touched ng-untouched ng-pristine">\n' +
                      '  </div>\n' +
                      '  <div class="amount_tf">\n' +
                      '      <input type="number" classoutline="" numberonly="" step="500"\n' +
                      '              min="0" placeholder="금액(원)" title="모금액 산출 금액(원)" autocomplete="off"\n' +
                      '              class="tf_write ng-valid ng-valid-min ng-dirty ng-valid-number ng-touched ng-untouched ng-pristine">\n' +
                      '  </div>\n' +
                      '    <button type="button" class="btn_line_txt"> 삭제 </button>\n' +
                      '</div>'
        $($addContent).insertAfter($(".ng-scope").last());
        updateIDs();
    });

    // 추가버튼을 눌렀을때 동적으로 생성된 태그들 $addContent를 불러오기 위해 document를 불러옴
    $(document).on('click', (e) => {
        //
        if ($(e.target).attr('class') == 'btn_line_txt') {
            if ($('.ng-scope').length !== 1) {
                $(e.target).parent().remove()
                updateIDs()
                updateAmount()
                
            } else {
              toastMsg('1개이하로는 삭제 할 수 없습니다.')
                return
            }
        }

    });


    $(document).on('input', (e) => {
        $txtLength = $(e.target).parent().parent().next()
        let total = 0
        if ($txtLength.attr('class') == 'info_append') {
            $txtLength.children().text(`${$(e.target).val().length}/`)
        }

        if($(e.target).parent().attr('class') == 'amount_tf'){
            updateAmount()
        }

    });

// 정보 입력 안하고 다음 단계 클릭시 발생 이벤트
// 1. select box에 옵션 없을 시 경고 class 추가
// 2. checked가 3개가 아니면 해당 위치에 경고 class 추가
$('.link_step2').on('click', (e) => {

    let calendarFlag = false;

    if(calendarFlag) return;

    if($('.ng-scope input').filter((i,v)=>!$(v).val()).length >0 ){
        toastMsg('모금액 사용 계획을 빈칸 없이 작성해주세요.')
        return
    }
    console.log(updateAmount.amount)
    if(updateAmount.amount !==0){
        toastMsg('모금액의 사용내역을 전부 기입하세요.')
        return
    }

    if (!$('#checkPolicy').prop('checked')) {
        $('.lab_comm .ico_together').addClass('ico_warn')
        $('.info_policy').parent().addClass('sign_warn')
        toastMsg('개인정보 제 3자 제공 약관을 확인해주세요')
        return
    }

    // 상단 탭 현재 위치 강조 및 다음 폼 show 나머지 hide
    $('.link_tab').closest('li').removeClass('on')
    let $topIndex = $(e.target).closest('.form_cont').index()
    $('.form_cont').hide()
    $('.link_tab').eq($topIndex + 1).parent().addClass('on')
    $('.form_cont').eq($topIndex + 1).show()
    window.scrollTo(0,0)


})



})


