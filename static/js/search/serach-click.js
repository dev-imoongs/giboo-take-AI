let page = 1
let post_status = "전체"


//처음 페이지로딩시 전체 선택
$(".inp_sort").eq(0).prop("checked",true)


// 카테고리 검색결과 리스트 가져오기
$(document).ready(function (){
    ShowSearchListOfTag(tag_name, post_status);
})

// 전체
$("#sortCate0").on("click", function() {
    let attr = $("#sortCate0").attr("id")
    page = 1
    post_status = $("label[for='" + attr + "'").text()
    console.log(post_status)
    ShowSearchListOfTag(tag_name, post_status)
})


// 모금중
$("#sortCate1").on("click", function() {
    let attr = $("#sortCate1").attr("id")
    page = 1
    post_status = $("label[for='" + attr + "'").text()
    console.log(post_status)
    ShowSearchListOfTag(tag_name, post_status)
})


// 봉사중
$("#sortCate2").on("click", function() {
    let attr = $("#sortCate2").attr("id")
    page = 1
    post_status = $("label[for='" + attr + "'").text()
    console.log(post_status)
    ShowSearchListOfTag(tag_name, post_status)
})


// 검토중
$("#sortCate3").on("click", function() {
    let attr = $("#sortCate3").attr("id")
    page = 1
    post_status = $("label[for='" + attr + "'").text()
    console.log(post_status)
    ShowSearchListOfTag(tag_name, post_status)
})


// 후기
$("#sortCate4").on("click", function() {
    let attr = $("#sortCate4").attr("id")
    page = 1
    post_status = $("label[for='" + attr + "'").text()
    console.log(post_status)
    ShowSearchListOfTag(tag_name, post_status)
})


// 미선정
$("#sortCate5").on("click", function() {
    let attr = $("#sortCate5").attr("id")
    page = 1
    post_status = $("label[for='" + attr + "'").text()
    console.log(post_status)
    ShowSearchListOfTag(tag_name, post_status)
})

// 태그 검색데이터 요청해서 가져오기
const ShowSearchListOfTag = (tag_name, post_status, scroll) => {
    fetch(`/search/tag/api/?tag_name=${tag_name}&page=${page}&status=${post_status}`)
        .then(response => response.json())
        .then(result => {
            let posts = result.posts;
            let text = "";
            let review_status = result.post_status;
            posts.forEach((post,i) => {
                let post_status = post.neulhaerang_status;
                let percentage = Math.ceil((post.donation_amount_sum / post.target_amount) * 100)
                console.log(post)
                if(review_status ==='후기'){
                    text += `
                        <li>
                            <fundraising-card>
                                <a class="link_pack">
                                    <span class="box_thumb">
                                        <span kagetype="c203" class="img_thumb" style="background-image: url('${post.thumbnail_image}');"></span>
                                    </span>
                                    <span class="box_together">
                                        <span class="bundle_tit">
                                            <strong class="tit_together ellipsis_type1">
                                                <span class="tag_bundle">
                                                    <span class="tag_state tag_state_default">${review_status}</span>
                                                </span>
                                                ${post.review_title}
                                            </strong>
                                            <span class="txt_proposer">${post.member_nickname}</span>
                                        </span>
                                        <span class="wrap_state">
                                            <span class="state_bar">
                                                <span class="state_gage state_end" style="width: 100%"></span>
                                            </span>
                                            <span class="txt_per">100%</span>
                                        </span>
                                        <span class="price_goal"> ${post.donation_amount_sum ? post.donation_amount_sum : 0}원 </span>
                                    </span>
                                </a>
                            </fundraising-card>
                        </li>
                    `
                }
                else if (post_status === '모금중') {
                    text += `
                        <li>
                            <fundraising-card>
                                <a class="link_pack" href="/neulhaerang/detail/${post.id}">
                                    <span class="box_thumb">
                                        <span class="img_thumb" style="background-image: url('${post.thumbnail_image}');"></span>
                                    </span>
                                    <span class="box_together">
                                        <span class="bundle_tit">
                                            <strong class="tit_together ellipsis_type1"><span class="tag_bundle"></span>${post.neulhaerang_title}</strong>
                                            <span class="txt_proposer">${post.member_nickname}</span>
                                        </span>
                                        <span class="wrap_state">
                                            <span class="state_bar">
                                                <span class="state_gage state_ing" style="width: ${post.donation_amount_sum ? percentage : 0}%"></span>
                                            </span>
                                            <span class="txt_per">${post.donation_amount_sum ? percentage : 0}%</span>
                                        </span>
                                        <span class="price_goal"> ${post.donation_amount_sum ? percentage : 0}원 </span>
                                    </span>
                                </a>
                            </fundraising-card>
                        </li>
                    `
                }
                else if (post_status === '봉사중') {
                    text += `
                        <li>
                            <fundraising-card>
                                <a class="link_pack" href="/neulhaerang/detail/${post.id}">
                                    <span class="box_thumb">
                                        <span class="img_thumb" style="background-image: url('${post.thumbnail_image}');"></span>
                                    </span>
                                    <span class="box_together">
                                        <span class="bundle_tit">
                                            <strong class="tit_together ellipsis_type1"><span class="tag_bundle"></span>${post.neulhaerang_title}</strong>
                                            <span class="txt_proposer">${post.member_nickname}</span>
                                        </span>
                                         <span class="wrap_state">
                                            <span class="state_bar">
                                                <span class="state_gage state_end" style="width: ${post.donation_amount_sum ? percentage : 0}%"></span>
                                            </span>
                                            <span class="txt_per">${post.donation_amount_sum ? percentage : 0}%</span>
                                        </span>
                                        <span class="price_goal"> ${post.donation_amount_sum ? percentage : 0}원 </span>
                                    </span>
                                </a>
                            </fundraising-card>
                        </li>
                    `
                }
                else if(post_status === '검토중') {
                    text += `
                        <li>
                            <fundraising-card>
                                <a class="link_pack" href="neulhaerang/detail/${post.id}">
                                    <span class="box_thumb">
                                        <span class="img_thumb" style="background-image: url('${post.thumbnail_image}');"></span>
                                    </span>
                                    <span class="box_together">
                                        <span class="bundle_tit">
                                            <strong class="tit_together ellipsis_type1"><span class="tag_bundle"></span> ${post.neulhaerang_title} </strong>
                                            <span class="txt_proposer">${post.member_nickname}</span>
                                        </span>
                                        <span class="price_goal">
                                            <span class="txt_goal">${post_status}</span>
                                            ${post.target_amount}원
                                        </span>
                                    </span>
                                </a>
                            </fundraising-card>
                        </li>
                    `
                }
                else if(post_status === '미선정') {
                    text += `
                        <li>
                            <fundraising-card>
                                <a class="link_pack" href="neulhaerang/detail/${post.id}">
                                    <span class="box_thumb">
                                        <span class="img_thumb" style="background-image: url('${post.thumbnail_image}');"></span>
                                    </span>
                                    <span class="box_together">
                                        <span class="bundle_tit">
                                            <strong class="tit_together ellipsis_type1"><span class="tag_bundle"></span> ${post.neulhaerang_title} </strong>
                                            <span class="txt_proposer">${post.member_nickname}</span>
                                        </span>
                                        <span class="price_goal">
                                            <span class="txt_goal">${post_status}</span>
                                            ${post.target_amount}원
                                        </span>
                                    </span>
                                </a>
                            </fundraising-card>
                        </li>
                    `
                }
                 else if(post_status === '후기') {
                    text += `
                        <li>
                            <fundraising-card>
                                <a class="link_pack">
                                    <span class="box_thumb">
                                        <span kagetype="c203" class="img_thumb" style="background-image: url('${post.thumbnail_image}');"></span>
                                    </span>
                                    <span class="box_together">
                                        <span class="bundle_tit">
                                            <strong class="tit_together ellipsis_type1">
                                                <span class="tag_bundle">
                                                    <span class="tag_state tag_state_default">${post_status}</span>
                                                </span>
                                                ${post.review_title}
                                            </strong>
                                            <span class="txt_proposer">${post.member_nickname}</span>
                                        </span>
                                        <span class="wrap_state">
                                            <span class="state_bar">
                                                <span class="state_gage state_end" style="width: 100%"></span>
                                            </span>
                                            <span class="txt_per">100%</span>
                                        </span>
                                        <span class="price_goal"> ${post.donation_amount_sum ? post.donation_amount_sum : 0}원 </span>
                                    </span>
                                </a>
                            </fundraising-card>
                        </li>
                    `
                 }
            })
            console.log(text)
            scroll? $('.list_fund').append(text): $('.list_fund').html(text)


        })
}



let timeoutId
window.addEventListener("scroll", ()=>{
    clearTimeout(timeoutId)
    console.log(page)
            timeoutId = setTimeout(()=>{
         if (window.innerHeight + window.scrollY + 500>= document.body.offsetHeight) {
    page++
    ShowSearchListOfTag(tag_name, post_status, scroll);
             }
    },50)
});


