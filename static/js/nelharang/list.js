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

// 페이지네이터
let category = "전체"
let page = 1
let sort = '추천순'

$('.lab_sort').each((i,v)=>{
    $(v).on('click',()=>{
        sort = $(v).text()
        page=1
        showNeulhaerang(page, category, sort)
    })
})


$('.link-cate').each((i,v)=>{
    $(v).on('click',()=>{
        category = $(v).find('.txt-cate').text()
        page=1
        showNeulhaerang(page, category, sort)
    })
})

const showNeulhaerang =  (page, category, sort,scroll)=>{

    fetch(`/neulhaerang/list-api-view/?page=${page}&category=${category}&sort=${sort}`)
        .then(response => response.json())
        .then(result =>{
          let text = ""
          let posts= result.posts
          let pagenator= result.pagenator

          posts.forEach((post,i)=> {
              let now_date = new Date()
              let fund_end_date = new Date(post.fund_duration_end_date)
              let timeDifference = Math.abs(fund_end_date.getTime() - now_date.getTime())
              let dayDifference = Math.ceil(timeDifference / (1000*3600*24))

              let percentage = Math.ceil(post.donation_amount_sum / post.target_amount *100)

              console.log(post)
              const post_url = baseUrl.replace("0", neulhaerang_id=post.id);
              text += `<li class="listcard">
                    <a href="${post_url}" class="link_pack">
                    <span class="box_thumb">
                      <span kagetype="c203" class="img_thumb" style="background-image: url(${post.thumbnail_image});"></span>
                      </span>
                      <span class="box_together">
                      <span class="bundle_tit">
                        <strong class="tit_together ellipsis_type1">
                          ${dayDifference<=3 ?
                  '<span class="tag_bundle"><span class="tag_state tag_state_default">종료임박</span></span>':''}
                            ${post.neulhaerang_title}
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

showNeulhaerang(page, category, sort)

window.addEventListener("scroll", ()=>{
    if (window.innerHeight + window.scrollY >= document.body.clientHeight) {
    page++
    showNeulhaerang(page, category, sort,"scroll")
}
});
