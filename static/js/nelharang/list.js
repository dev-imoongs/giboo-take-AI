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
let text
let page = 1

const showNeulhaerang =  (page)=>{

    fetch(`/neulhaerang/list-api-view/?page=${page}`)
        .then(response => response.json())
        .then(result =>{
          let text = ""
          let posts= result.posts
          let pagenator= result.pagenator

          posts.forEach((post,i)=> {
              const post_url = baseUrl.replace("0", neulhaerang_id=post.id);
              text += `<li class="listcard">
                    <a href="${post_url}" class="link_pack">
                    <span class="box_thumb">
                      <span kagetype="c203" class="img_thumb" style="background-image: url('https://mud-kage.kakaocdn.net/dn/bf22U9/btsf2G0mHF9/PRklKTaLsSkb7ySBTOrkBK/c203.jpg');"></span>
                      </span>
                      <span class="box_together">
                      <span class="bundle_tit">
                        <strong class="tit_together ellipsis_type1">
                          <span class="tag_bundle"><span class="tag_state tag_state_default">종료임박</span></span>
                            ${post.neulhaerang_title}
                        </strong>
                        <span class="txt_proposer"> ${post.member_nickname} </span>
                        
                      </span>
                      <span class="wrap_state">
                        <span class="state_bar">
                          <span class="state_gage state_ing" style="width: 95%"></span>
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
          $('.list_fund').html(text)
  })
}

showNeulhaerang(page)

