let opK1='전체';
let opK2='전체';
let opK3='전체';
let opK4='전체';


console.log(opK1)

//제목,본문 정렬 시작하자마자 첫번째꺼 선택
$(".box_sorting .inp_sort").eq(0).prop("checked",true)


//검색 삭제 버튼
const $searchDeleteBtn = $(".group_schkeyword .btn_delete")
const $searchInput = $("#schKeyword")
$searchDeleteBtn.on("click",e=>{
    $searchInput.val("")
    $searchDeleteBtn.hide()
})


$searchInput.on("input",e=>{
    if($searchInput.val()){
        $searchDeleteBtn.show()
    }else{
        $searchDeleteBtn.hide()
    }
})


//셀렉트 박스 클릭
//1
const $selectBox1 = $("#opKinds1")
const $selectSpan1 = $(".select_on1")
$selectBox1.on("change",e=>{
    $selectSpan1.text($("#opKinds1 option:selected").text())
})
//2
const $selectBox2 = $("#opKinds2")
const $selectSpan2 = $(".select_on2")
$selectBox2.on("change",e=>{
    $selectSpan2.text($("#opKinds2 option:selected").text())
})

//3
const $selectBox3 = $("#opKinds3")
const $selectSpan3 = $(".select_on3")
$selectBox3.on("change",e=>{
    $selectSpan3.text($("#opKinds3 option:selected").text())
})

//4
const $selectBox4 = $("#opKinds4")
const $selectSpan4 = $(".select_on4")
$selectBox4.on("change",e=>{
    $selectSpan4.text($("#opKinds4 option:selected").text())
})

console.log(opK1)

//NeulhajangAPIView JS

let page = 1;
function MemberNeulhajangList(currentPage, sort, opK3, opK4) {
  fetch(`/mypage/new-post-neulhajang-list-api/?page=${currentPage}&opK3=${opK3}&opK4=${opK4}`)
    .then(response => response.json())
    .then(result => {
      let text = "";
      let lists = result.neulhajang_posts;
      let neulhajangCountJson = result.neulhajang_count_json;
      // console.log(JSON.parse(lists))
      // if (!result.serialized_pagenator.has_next_data) {
      //   $('.link-other2').css('display', 'none');
      // }

      lists.forEach((jlist, i) => {

        let countInfo = neulhajangCountJson[i];
        text += `<li>
                        <a
                          class="link_pack"
                          ><span class="box_thumb"
                            ><span
                              class="img_thumb"
                              style="
                                background-image: url('${mediaUrl}${jlist.thumnail_image}');
                              "
                            ></span></span
                          ><span class="box_together"
                            ><span class="bundle_tit"
                              ><strong class="tit_together ellipsis_type1">
                                ${jlist.neulhajang_title}</strong
                              ><span class="txt_proposer"
                                >${jlist.member_nickname}
                              </span></span
                            ><span class="txt_participants_count"
                              ><i class="ico_check"></i> ${countInfo.neulhajang_count}명 행동중
                            </span></span
                          ></a
                        >
                      </li>`;
      });

      $('.ul-data2').html(text);
      //$('.ul-data2').append(text);
    })
}

MemberNeulhajangList(page); // 페이지 번호만 전달

$('.link-other2').on("click", () => {
    if ('click') {
        page++;
        MemberNeulhajangList(page);
    }
});

const labels = document.querySelectorAll('.lab_sort');
const keywordInput = document.getElementById('keywordInput');
const keywordForm = document.getElementById('keywordForm');

labels.forEach(label => {
    label.addEventListener('click', () => {
        const keyword = label.getAttribute('data-key');


    });
});

console.log(opK1)

// let page = 1;
// console.log(page)
function MemberNeulhaerangList(currentPage, opK1, opK2) {

console.log(opK1)
  fetch(`/mypage/new-post-neulhaerang-list-api/?page=${currentPage}&opK1=${opK1}&opK2=${opK2}`)
    .then(response => response.json())
    .then(result => {
      let text = "";
      let lists = result.neulhaerang_posts;
      let neulhaerangCountJson = result.neulhaerang_count_json;
        console.log(result)
      // console.log(JSON.parse(lists))

      // if (!result.serialized_pagenator.has_next_data) {
      //   $('.link-other2').css('display', 'none');
      // }

      lists.forEach((rlist, i) => {
        let neulhaerang_status = rlist.neulhaerang_status
          console.log(neulhaerang_status)
        let countInfo = neulhaerangCountJson[i];
        if (neulhaerang_status === '모금중'){
                    text +=`<li>
                      <fundraising-card
                        ><a
                          class="link_pack"
                          href="/fundraisings/106019"
                          ><span class="box_thumb"
                            ><span
                          class="img_thumb"
                          style="
                                background-image: url('${mediaUrl}${rlist.thumbnail_image}');
                              "
                            ></span></span
                          ><span class="box_together"
                      ><span class="bundle_tit"
                      ><strong class="tit_together ellipsis_type1"
                      ><span class="tag_bundle"></span
                      >
                                ${rlist.neulhaerang_title}</strong
                      ><span class="txt_proposer"
                                >${rlist.member_nickname}</span
                              ></span
                      ><span class="wrap_state"
                      ><span class="state_bar"
                                ><span class="state_gage state_ing" style="width: 21%"></span></span
                              ><span class="txt_per">21%</span></span
                            ><span class="price_goal"
                              >
                              ${rlist.target_amount.toLocaleString()}원
                            </span></span
                          ></a
                        ></fundraising-card
                      >
                    </li>`
        }
        else if (neulhaerang_status === '봉사중'){
                    text +=`<li>
                      <fundraising-card
                        ><a class="link_pack" href="/fundraisings/104067"
                          ><span class="box_thumb"
                      ><span
                          class="img_thumb"
                          style="
                                background-image: url('${mediaUrl}${rlist.thumbnail_image}');
                              "
                            ></span></span
                          ><span class="box_together"
                            ><span class="bundle_tit"
                              ><strong class="tit_together ellipsis_type1"
                      ><span class="tag_bundle"></span> ${rlist.neulhaerang_title} </strong
                              ><span class="txt_proposer"
                      >${rlist.member_nickname}</span
                              ></span
                      ><span class="wrap_state"
                              ><span class="state_bar"
                                ><span
                          class="state_gage state_end"
                          style="width: 100%"
                                ></span></span
                              ><span class="txt_per">100%</span></span
                            ><span class="price_goal"> ${rlist.target_amount.toLocaleString()}원 </span></span
                          ></a
                        ></fundraising-card
                      >
                    </li>`
          }
        else if (neulhaerang_status === '검토중'){
                    text +=`<li>
                      <fundraising-card
                        ><a class="link_pack" href="/fundraisings/102188"
                          ><span class="box_thumb"
                            ><span
                              class="img_thumb"
                              style="
                                background-image: url('${mediaUrl}${rlist.thumbnail_image}');
                              "
                            ></span></span
                          ><span class="box_together"
                            ><span class="bundle_tit"
                              ><strong class="tit_together ellipsis_type1"
                                ><span class="tag_bundle"></span> ${rlist.neulhaerang_title} </strong
                              ><span class="txt_proposer">${rlist.member_nickname}</span></span
                            ><span class="price_goal"
                              ><span class="txt_goal">준비중</span>
                              ${rlist.target_amount.toLocaleString()}원
                            </span></span
                          ></a
                        ></fundraising-card
                      >
                    </li>`
          }
        else if (neulhaerang_status === '후기'){
                    text += `<li>
                      <fundraising-card
                        ><a class="link_pack"
                          ><span class="box_thumb"
                            ><span
                              kagetype="c203"
                              class="img_thumb"
                              style="
                                background-image: url('${mediaUrl}${rlist.thumbnail_image}');
                              "
                            ></span></span
                          ><span class="box_together"
                            ><span class="bundle_tit"
                              ><strong class="tit_together ellipsis_type1"
                                ><span class="tag_bundle"
                                  ><span class="tag_state tag_state_default">후기</span></span
                                >
                                ${rlist.neulhaerang_title} </strong
                              ><span class="txt_proposer">${rlist.member_nickname}</span></span
                            ><span class="wrap_state"
                              ><span class="state_bar"
                                ><span
                                  class="state_gage state_end"
                                  style="width: 100%"
                                ></span></span
                              ><span class="txt_per">100%</span></span
                            ><span class="price_goal"> ${rlist.target_amount.toLocaleString()}원 </span></span
                          ></a
                        ></fundraising-card
                      >
                    </li>`;
          }
        else if (neulhaerang_status === '미선정'){
                    text +=`<li>
                      <fundraising-card
                        ><a class="link_pack"
                          ><span class="box_thumb"
                            ><span
                              kagetype="c203"
                              class="img_thumb"
                              style="
                                background-image: url('${mediaUrl}${rlist.thumbnail_image}');
                              "
                            ></span></span
                          ><span class="box_together"
                            ><span class="bundle_tit"
                              ><strong class="tit_together ellipsis_type1"
                                ><span class="tag_bundle"></span> ${rlist.neulhaerang_title} </strong
                              ><span class="txt_proposer">${rlist.member_nickname}</span></span
                            ><span class="price_goal"
                              ><span class="txt_goal">미선정</span>
                              ${rlist.target_amount.toLocaleString()}원
                            </span></span
                          ></a
                        ></fundraising-card
                      >
                    </li>`
          }

      });

      $('.ul-data1').html(text);
      //$('.ul-data1').append(text);
    })
}
//
MemberNeulhaerangList(page, opK1, opK2); // 페이지 번호만 전달
//
// $('.link-other2').on("click", () => {
//     if ('click') {
//         page++;
//         MemberNeulhajangList(page);
//     }
// });
//
// const labels = document.querySelectorAll('.lab_sort');
// const keywordInput = document.getElementById('keywordInput');
// const keywordForm = document.getElementById('keywordForm');
//
// labels.forEach(label => {
//     label.addEventListener('click', () => {
//         const keyword = label.getAttribute('data-key');
//         console.log(keyword);
//
//     });
// });


$('#opKinds1').on('change', function() {

  const selectedOptionValue = $(this).val();
  page = 1;
  opK1 = selectedOptionValue;
  MemberNeulhaerangList(page, opK1, opK2)
});

$('#opKinds2').on('change', function() {
  page = 1;
  const selectedOptionValue = $(this).val();

  opK2 = selectedOptionValue;
  MemberNeulhaerangList(page, opK1, opK2)
});

$('#opKinds3').on('change', function() {
  page = 1;
  const selectedOptionValue = $(this).val();

  opK3 = selectedOptionValue;
  MemberNeulhajangList(page, opK3, opK4)
});

$('#opKinds4').on('change', function() {
  const selectedOptionValue = $(this).val();

  opK4 = selectedOptionValue;
  page = 1;
  MemberNeulhajangList(page, opK3, opK4)

});

