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
console.log(page)
function getRepliesByPaged(currentPage) {

  fetch(`/mypage/get-replies/?page=${currentPage}`)
    .then(response => response.json())
    .then(result => {
      let text = "";
      console.log(result)
      if (!result.serialized_pagenator.has_next_data) {
        $('.link-other2').css('display', 'none');
      }else{
            $('.link-other2').css('display', 'inline-block');
      }

      result.total_reply_sorted.forEach((reply, i) => {
        function formatDate(dateString) {
          const options = { year: 'numeric', month: 'numeric', day: 'numeric' };
          return new Date(dateString).toLocaleDateString('ko-KR', options);
        }

        const formattedDate = formatDate(reply.created_date);

        text += `<li>
                          <div class="cmt-info">
                            <span class="info-append">
                              <em class="emph-sign">${reply.type}</em>
                              <a class="link-fund" href="${reply.type=="후기"?`/neulhaerang_review/review/detail/${reply.neulhaerang_review_id}`:`/neulhaerang/detail/${reply.neulhaerang_id}`}">
                                ${reply.title} </a>
                            </span>
                            <span class="txt-cmt">
                              <span class="desc-cmt">${reply.reply_content}</span>
                            </span>
                            <span class="info-append">
                              <span class="txt-time">${elapsedTime(reply.created_date)}</span>
                              <like-comment>
                                <button type="button" class="btn-like">
                                  <span class="ico-together ico-like"></span>
                                  &nbsp;좋아요&nbsp;
                                  <span class="num-like">${reply.like_count}</span>
                                </button>
                              </like-comment>
                              <button id="${reply.id +"-" +reply.type}" type="button" class="btn-delete"> 삭제 </button>
                            </span>
                          </div>
                        </li>`;
      });

      $('.list-cmt').append(text);

      $('.btn-delete').each((i, value)=>{
         $(value).on("click", () => {
        $(".btn-type1").attr('id',$(value).attr('id'))
        $('#modalOFF').attr('id','modalON')
        $('.dimmed_layer').css('height','100%');
        $('.dialog-content').css('display','block');
        }
        )
    }
)
    })
}

$(".btn-type1").on("click",e=>{
    fetch(`/mypage/delete-reply/?reply_id=${$(".btn-type1").attr('id').split("-")[0]}&type=${$(".btn-type1").attr('id').split("-")[1]}`)
        .then(response => response.json())
        .then(result =>{
            if(result){
                $(".btn-type2").trigger('click')
                $('.btn-delete').each((i,btn)=>{
                    if($(btn).attr('id')==$(".btn-type1").attr('id')){
                        $(btn).closest("li").hide()
                        $(".color-g1").text(` ${Number($(".color-g1").text().trim())-1}`)
                    }

                })
            }
        })

})

getRepliesByPaged(page); // 페이지 번호만 전달

$('.link-other2').on("click", () => {
    if ('click') {
        page++;
        getRepliesByPaged(page);
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