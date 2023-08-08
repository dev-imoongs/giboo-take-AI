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