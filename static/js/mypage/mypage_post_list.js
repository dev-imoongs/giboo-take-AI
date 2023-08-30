// 삭제 버튼 클릭 시 모달창 띄우기

//  취소 버튼 클릭 시 모달창 사라짐
$('.btn-type2').on("click", () =>{
        $('#modalON').attr('id','modalOFF');
        $('.dimmed_layer').css('height','0');
        $('.dialog-content').css('display','none');
        })

// 대 카테고리 선택시 class='on' 부여 및 소 카테고리 상황에 맞게 나타냄
// $('.txt_tab').on('click',(e)=>{
//     $target = $(e.target)
//     $('.nav-top').removeClass('on')
//     $target.parent().parent().addClass('on')
//     if($target.text()=='전체'){
//         $('#nav-neulhaerang').hide()
//         $('#nav-neulhajang').hide()
//     }else if($target.text()=='늘해랑'){
//         $('#nav-neulhaerang').show()
//         $('#nav-neulhajang').hide()
//     }else{
//         $('#nav-neulhajang').show()
//         $('#nav-neulhaerang').hide()
//     }
// })
// 소 카테고리 선택시 class="sort_on" 주어서 선택 강조
// $('.lab_sort').on('click',(e)=>{
//     $target = $(e.target)
//     $('.box_sorting').removeClass('sort_on')
//     $target.parent().addClass('sort_on')
// })



let page = 1;
console.log(page)
function getFeedsList(currentPage) {

  fetch(`/mypage/get-feeds/?page=${currentPage}`)
    .then(response => response.json())
    .then(result => {
      let text = "";
      console.log(result)
      if (!result.serialized_pagenator.has_next_data) {
        $('.link-other2').css('display', 'none');
      }else{
          $('.link-other2').css('display', 'inline-block');
      }

      result.feeds.forEach((feed, i) => {
        function formatDate(dateString) {
          const options = { year: 'numeric', month: 'numeric', day: 'numeric' };
          return new Date(dateString).toLocaleDateString('ko-KR', options);
        }

        const formattedDate = formatDate(feed.created_date);

        text += `<li>
                                                <div class="action-content-card">
                                                    <a class="link-action-card"
                                                       href="/neulhajang/detail/${feed.neulhajang_id}">
                                                        <span class="thumb-action">
                                                            <img alt="이미지" class="img-thumb" src="${mediaUrl+feed.feedPhoto}"></span>
                                                        <div class="info-action">
                                                            <strong class="tit-action">${feed.neulhajang_title}</strong>
                                                            <p class="desc-action">${feed.feedContent}</p>
                                                            <span class="txt-date">${formattedDate.slice(0,-1)}</span>
                                                        </div>
                                                    </a>
                                                    <button id="${feed.id}" class="btn-delete">삭제</button>
                                                </div>
                                            </li>`;
      });

      // $('.list-donate').html(text);
      $('.list-action-card').append(text);
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
    fetch(`/mypage/delete-feed/?feed_id=${$(".btn-type1").attr('id')}`)
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

getFeedsList(page); // 페이지 번호만 전달

$('.link-other2').on("click", () => {
    if ('click') {
        page++;
        getFeedsList(page);
    }
});