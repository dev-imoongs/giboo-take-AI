// 삭제 버튼 클릭 시 모달창 띄우기
$('.btn-delete').each((i, value)=>{
    $(value).on("click", () => {
        $('#modalOFF').attr('id','modalON')
        $('.dimmed_layer').css('height','100%');
        $('.dialog-content').css('display','block');
        }
        )
    }
)
//  취소 버튼 클릭 시 모달창 사라짐
$('.btn-type2').on("click", () =>{
        $('#modalON').attr('id','modalOFF');
        $('.dimmed_layer').css('height','0');
        $('.dialog-content').css('display','none');
        })

// 대 카테고리 선택시 class='on' 부여 및 소 카테고리 상황에 맞게 나타냄
$('.txt_tab').on('click',(e)=>{
    $target = $(e.target)
    $('.nav-top').removeClass('on')
    $target.parent().parent().addClass('on')
    if($target.text()=='전체'){
        $('#nav-neulhaerang').hide()
        $('#nav-neulhajang').hide()
    }else if($target.text()=='늘해랑'){
        $('#nav-neulhaerang').show()
        $('#nav-neulhajang').hide()
    }else{
        $('#nav-neulhajang').show()
        $('#nav-neulhaerang').hide()
    }
})
// 소 카테고리 선택시 class="sort_on" 주어서 선택 강조
$('.lab_sort').on('click',(e)=>{
    $target = $(e.target)
    $('.box_sorting').removeClass('sort_on')
    $target.parent().addClass('sort_on')
})



$('.nav-neulhajang')