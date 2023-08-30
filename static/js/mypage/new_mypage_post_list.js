
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



//NeulhajangAPIView JS

let page = 1;
console.log(page)
function MemberNeulhajangList(currentPage, sort) {

  fetch(`/mypage/new-post-list-api/?page=${currentPage}`)
    .then(response => response.json())
    .then(result => {
      let text = "";
      let lists = JSON.parse(result.neulhajang_posts);
      // console.log(JSON.parse(lists))
        console.log(result)
      // if (!result.serialized_pagenator.has_next_data) {
      //   $('.link-other2').css('display', 'none');
      // }

      lists.forEach((list, i) => {
        console.log(list)
        text += `<li>
                        <a
                          class="link_pack"
                          ><span class="box_thumb"
                            ><span
                              class="img_thumb"
                              style="
                                background-image: url('https://t1.kakaocdn.net/together_action_prod/admin/20230707/524e91af3d734b53a65e5daebcc22f72?type=thumb&amp;opt=S600x600');
                              "
                            ></span></span
                          ><span class="box_together"
                            ><span class="bundle_tit"
                              ><strong class="tit_together ellipsis_type1">
                                ${list.fields.neulhajang_title}</strong
                              ><span class="txt_proposer"
                                >한국에너지공단
                              </span></span
                            ><span class="txt_participants_count"
                              ><i class="ico_check"></i> 3,803명 행동중
                            </span></span
                          ></a
                        >
                      </li>`;
      });

      // $('.list-donate').html(text);
      $('.ul-data').append(text);
      console.log(`Page: ${currentPage}`);
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
        console.log(keyword);

    });
});
