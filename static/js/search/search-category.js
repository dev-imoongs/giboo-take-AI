//처음 페이지로딩시 전체 선택
$(".inp_sort").eq(0).prop("checked",true)

$(document).ready(function (){
    ShowSearchListOfCategory();
})

// 카테고리 검색 결과 리스트 가져오기
const ShowSearchListOfCategory = () => {
    console.log("여기는 들어옴? 들어옴 확인함")
    fetch(`/search/category/api/`)
        .then(response => response.json())
        .then(result => {
            let posts = result.posts;
            let text = "";
            console.log(posts)
            posts.forEach((post,i) => {
                let status = post.neulhaerang_status;
                if (status === '모금중') {
                    text += `
                        <li>
                          <fundraising-card>
                            <a class="link_pack" href="">
                              <span class="box_thumb">
                                <span class="img_thumb" style="background-image: url('https://mud-kage.kakaocdn.net/dn/htilZ/btshbd2X8sp/086nhwGrgNP8eTDvbiXRhK/c203.jpg');"></span>
                              </span>
                              <span class="box_together">
                                <span class="bundle_tit">
                                  <strong class="tit_together ellipsis_type1">
                                    <span class="tag_bundle"></span> {{ post.neulhaerang_title }} </strong>
                                  <span class="txt_proposer">사단법인 여성환경연대</span>
                                </span>
                                <span class="wrap_state">
                                  <span class="state_bar">
                                    <span class="state_gage state_ing" style="width: 21%"></span>
                                  </span>
                                  <span class="txt_per">21%</span>
                                </span>
                                <span class="price_goal"> {{ post.target_amount }}원 </span>
                              </span>
                            </a>
                          </fundraising-card>
                        </li>
                    `
                }
                if (status === '봉사중') {
                    text += `
                        <li>
                            <fundraising-card>
                                <a className="link_pack" href="/fundraisings/104067">
                              <span className="box_thumb">
                                <span className="img_thumb" style="
                                    background-image: url('https://mud-kage.kakaocdn.net/dn/bSkrNV/btr5Blj0Ba4/KiW1JirlAtqwaHL05HxE90/c203.jpg');
                                  "></span>
                              </span>
                                    <span className="box_together">
                                <span className="bundle_tit">
                                  <strong className="tit_together ellipsis_type1">
                                    <span className="tag_bundle"></span> 지구 환경 위하는 함께하는 쓰담쓰담 </strong>
                                  <span className="txt_proposer">수원시정자동장애인주간보호시설</span>
                                </span>
                                <span className="wrap_state">
                                  <span className="state_bar">
                                    <span className="state_gage state_end" style="width: 100%"></span>
                                  </span>
                                  <span className="txt_per">100%</span></span>
                                <span className="price_goal"> 288,500원 </span></span>
                                </a>
                            </fundraising-card>
                        </li>
                    `
                }
                if(status === '검토중') {
                    text += `
                        <li>
                          <fundraising-card>
                            <a class="link_pack" href="/fundraisings/102188">
                              <span class="box_thumb">
                                <span class="img_thumb" style="
                                    background-image: url('https://mud-kage.kakaocdn.net/dn/rdTNw/btrVVIh88rU/CGrdK9xFseo7Ji91w5pNY1/c203.jpg');
                                  "></span>
                              </span>
                              <span class="box_together">
                                <span class="bundle_tit">
                                  <strong class="tit_together ellipsis_type1">
                                    <span class="tag_bundle"></span> 불타는 지구에서 청년으로 산다는 것 </strong>
                                  <span class="txt_proposer">오늘, 잇다</span>
                                </span>
                                <span class="price_goal">
                                  <span class="txt_goal">{{status}}</span>
                                  7,000,000원
                                </span>
                              </span>
                            </a>
                          </fundraising-card>
                        </li>
                    `
                }
                if(status === '후기') {
                    text += `
                        <li>
                          <fundraising-card>
                            <a class="link_pack">
                              <span class="box_thumb">
                                <span kagetype="c203" class="img_thumb" style="
                                    background-image: url('https://mud-kage.kakaocdn.net/dn/IIewG/btqKMO8a8aO/CRaVyoyMmy1lqpIsu6BGYK/c203.jpg');
                                  "></span>
                              </span>
                              <span class="box_together">
                                <span class="bundle_tit">
                                  <strong class="tit_together ellipsis_type1">
                                    <span class="tag_bundle">
                                      <span class="tag_state tag_state_default">후기</span>
                                    </span>
                                    지구를 지키는 환경교육, 온라인으로 만나요 </strong>
                                  <span class="txt_proposer">지구시민연합</span>
                                </span>
                                <span class="wrap_state">
                                  <span class="state_bar">
                                    <span class="state_gage state_end" style="width: 100%"></span>
                                  </span>
                                  <span class="txt_per">100%</span>
                                </span>
                                <span class="price_goal"> 4,550,000원 </span>
                              </span>
                            </a>
                          </fundraising-card>
                        </li>
                    `
                }

            })
            $(".list_fund").html(text)

        })
}
