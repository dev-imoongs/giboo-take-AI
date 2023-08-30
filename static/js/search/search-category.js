//처음 페이지로딩시 전체 선택
$(".inp_sort").eq(0).prop("checked",true)

$(document).ready(function (){
    ShowSearchListOfCategory();
})

let page = 1
let post_status = "전체"
// 카테고리 검색 결과 리스트 가져오기
const ShowSearchListOfCategory = () => {
    fetch(`/search/category/api/?category_name=${category_name}&page=${page}&status=${post_status}`)
        .then(response => response.json())
        .then(result => {
            let posts = result.posts;
            let text = "";
            console.log(posts)
            posts.forEach((post,i) => {
                let post_status = post.neulhaerang_status;
                if (post_status === '모금중') {
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
                                                <span class="state_gage state_ing" style="width: ${post.donation_amount_sum? post.donation_amount_sum/post.target_amount : 0}%"></span>
                                            </span>
                                            <span class="txt_per">${post.donation_amount_sum? post.donation_amount_sum/post.target_amount : 0}%</span>
                                        </span>
                                        <span class="price_goal"> ${post.target_amount}원 </span>
                                    </span>
                                </a>
                            </fundraising-card>
                        </li>
                    `
                }
                if (post_status === '봉사중') {
                    text += `
                        <li>
                            <fundraising-card>
                                <a class="link_pack" href="/neulhaerang/detail/${post.id}">
                                    <span class="box_thumb">
                                        <span class="img_thumb" style="background-image: url('${post.thumbnail_image}');"></span>
                                    </span>
                                    <span class="box_together">
                                        <span class="bundle_tit">
                                            <strong class="tit_together ellipsis_type1"><span class="tag_bundle"></span> ${} </strong>
                                            <span class="txt_proposer">${post.member_nickname}</span>
                                        </span>
                                         <span class="wrap_state">
                                            <span class="state_bar">
                                                <span class="state_gage state_end" style="width: ${post.donation_amount_sum? post.donation_amount_sum/post.target_amount : 0}%"></span>
                                            </span>
                                            <span class="txt_per">${post.donation_amount_sum? post.donation_amount_sum/post.target_amount : 0}%</span>
                                        </span>
                                        <span class="price_goal"> ${post.target_amount}원 </span>
                                    </span>
                                </a>
                            </fundraising-card>
                        </li>
                    `
                }
                if(post_status === '검토중') {
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
                if(post_status === '미선정') {
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
                                                ${post.neulhaerang_title}
                                            </strong>
                                            <span class="txt_proposer">${post.member_nickname}</span>
                                        </span>
                                        <span class="wrap_state">
                                            <span class="state_bar">
                                                <span class="state_gage state_end" style="width: ${post.donation_amount_sum? post.donation_amount_sum/post.target_amount : 0}%"></span>
                                            </span>
                                            <span class="txt_per">${post.donation_amount_sum? post.donation_amount_sum/post.target_amount : 0}%</span>
                                        </span>
                                        <span class="price_goal"> ${post.target_amount}원 </span>
                                    </span>
                                </a>
                            </fundraising-card>
                        </li>
                    `
                }
                //  if(post_status === '후기') {
                //     text += `
                //         <li>
                //             <fundraising-card>
                //                 <a class="link_pack">
                //                     <span class="box_thumb">
                //                         <span kagetype="c203" class="img_thumb" style="background-image: url('https://mud-kage.kakaocdn.net/dn/IIewG/btqKMO8a8aO/CRaVyoyMmy1lqpIsu6BGYK/c203.jpg');"></span>
                //                     </span>
                //                     <span class="box_together">
                //                         <span class="bundle_tit">
                //                             <strong class="tit_together ellipsis_type1">
                //                                 <span class="tag_bundle">
                //                                     <span class="tag_state tag_state_default">후기</span>
                //                                 </span>
                //                                 지구를 지키는 환경교육, 온라인으로 만나요
                //                             </strong>
                //                             <span class="txt_proposer">지구시민연합</span>
                //                         </span>
                //                         <span class="wrap_state">
                //                             <span class="state_bar">
                //                                 <span class="state_gage state_end" style="width: 100%"></span>
                //                             </span>
                //                             <span class="txt_per">100%</span>
                //                         </span>
                //                         <span class="price_goal"> 4,550,000원 </span>
                //                     </span>
                //                 </a>
                //             </fundraising-card>
                //         </li>
                //     `
                // }

            })
            $(".list_fund").html(text)

        })
}
