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




let page = 1;
function getByeoljjisByPaged(currentPage) {

  fetch(`/mypage/get-byeoljjis/?page=${currentPage}`)
    .then(response => response.json())
    .then(result => {
      let text = "";
      console.log(result)
      if (!result.serialized_pagenator.has_next_data) {
        $('.link-other2').css('display', 'none');
      }else{
            $('.link-other2').css('display', 'inline-block');
      }

      result.byeoljjis.forEach((byeoljji, i) => {
        text += `  <li>
                          <a class="link_meditation" href="/neulhaerang_review/review/detail/${byeoljji.review_id}">
                              <span>
                                  <img class="thumb_img" src="${mediaUrl+byeoljji.byeoljji_img}">
                              </span>
                              <strong class="tit_meditation">${byeoljji.byeoljji_name}</strong>
                              <span class="txt_option">${byeoljji.byeoljji_rank == 1 ? '최고의 기부천사' : byeoljji.byeoljji_rank == 2 ? '감동의 기부천사' : '은은한 기부천사'}</span>
                          </a>
                      </li>`;
      });

      $('.list_meditation').append(text);


    })
}

// $(".btn-type1").on("click",e=>{
//     fetch(`/mypage/delete-reply/?reply_id=${$(".btn-type1").attr('id').split("-")[0]}&type=${$(".btn-type1").attr('id').split("-")[1]}`)
//         .then(response => response.json())
//         .then(result =>{
//             if(result){
//                 $(".btn-type2").trigger('click')
//                 $('.btn-delete').each((i,btn)=>{
//                     if($(btn).attr('id')==$(".btn-type1").attr('id')){
//                         $(btn).closest("li").hide()
//                         $(".color-g1").text(` ${Number($(".color-g1").text().trim())-1}`)
//                     }
//
//                 })
//             }
//         })
//
// })

getByeoljjisByPaged(page); // 페이지 번호만 전달

$('.link-other2').on("click", () => {
    if ('click') {
        page++;
        getByeoljjisByPaged(page);
    }
});


function elapsedTime(date) {
  const start = new Date(date);
  const end = new Date();

  const diff = (end - start) / 1000;

  const times = [
    { name: '년', milliSeconds: 60 * 60 * 24 * 365 },
    { name: '개월', milliSeconds: 60 * 60 * 24 * 30 },
    { name: '일', milliSeconds: 60 * 60 * 24 },
    { name: '시간', milliSeconds: 60 * 60 },
    { name: '분', milliSeconds: 60 },
  ];

  for (const value of times) {
    const betweenTime = Math.floor(diff / value.milliSeconds);

    if (betweenTime > 0) {
      return `${betweenTime}${value.name} 전`;
    }
  }
  return '방금 전';
}