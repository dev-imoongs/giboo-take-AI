//카테고리 클릭
$(".list-cate li").each((i,cate)=>{
    $(cate).on("click",e=>{
      $(".list-cate li").each((idx,category)=>{
        if(i==idx){
          $(category).addClass("on")
        }else{
          $(category).removeClass("on")
        }
      })
    })
  })

  //정렬 클릭
  $(".box_sorting").each((i,cate)=>{
    $(cate).on("click",e=>{
      $(".box_sorting").each((idx,category)=>{
        if(i==idx){
          $(category).addClass("sort_on")
        }else{
          $(category).removeClass("sort_on")
        }
      })
    })
  })

let page = 1
let sort = "추천순"

// 클릭한 sort값 sort에 입력(추천순, 최신순, 종료임박순)
$('.lab_sort').each((i,v)=>{
    $(v).on('click',()=>{
        sort = $(v).text()
        console.log(sort)
        page=1
        showNeulhaerangReviewList(page, sort)
    })
})

const showNeulhaerangReviewList = (page, sort, scroll)=>{
  fetch(`/neulhaerang_review/review-list-api-view/?page=${page}&sort=${sort}`)
      .then(response=> response.json())
      .then(result=>{
        let text = ""
        let posts= result.posts
        let pagenator= result.pagenator

        posts.forEach((post,i)=> {

              let percentage = Math.ceil(post.donation_amount_sum / post.target_amount *100)
              const post_url2 = baseUrl2.replace(0, neulhaerang_review_id=post.id);
              text += `<li class="listcard">
                    <a href="${post_url2}" class="link_pack">
                    <span class="box_thumb">
                      <span kagetype="c203" class="img_thumb" style="background-image: url(${post.thumbnail_image});"></span>
                      </span>
                      <span class="box_together">
                      <span class="bundle_tit">
                        <strong class="tit_together ellipsis_type1">
                            ${post.review_title}
                        </strong>
                        <span class="txt_proposer"> ${post.member_nickname} </span>

                      </span>
                      <span class="wrap_state">
                        <span class="state_bar">
                          <span class="state_gage state_ing" style="width: ${percentage}%"></span>
                        </span>
                      </span>`;
                      if(post.donation_amount_sum !== null){
                        text += `<span class="price_goal">${post.donation_amount_sum.toLocaleString("ko-KR")}원</span>
                    </span>
                  </a>
              </li>`
                      } else{
                        text += `<span class="price_goal">0원</span>
                    </span>
                  </a>
              </li>`
                      }
          })
            scroll? $('.list_fund').append(text): $('.list_fund').html(text)


      })

}
showNeulhaerangReviewList(page, sort)
window.addEventListener("scroll", ()=>{
    console.log(window.innerHeight)
    console.log(window.scrollY)
    console.log(document.body.clientHeight)

    if (window.innerHeight + window.scrollY + 1 >= document.body.clientHeight) {
        page++
        showNeulhaerangReviewList(page, sort,"scroll")
}
});
