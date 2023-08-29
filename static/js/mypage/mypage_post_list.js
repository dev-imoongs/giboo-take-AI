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

// 대 카테고리 선택시 class='on' 부여 및 소 카테고리 상황에 맞게 나타냄
$('.txt_tab').on('click',(e)=>{
    $target = $(e.target)
    $('.nav-top').removeClass('on')
    $target.parent().parent().addClass('on')
    if($target.text()=='전체'){
        $('#nav-neulhaerang').hide()
        $('#nav-neulhajang').hide()
    }else if($target.text()=='늘해랑'){
        $('#nav-neulhaerang').show()
        $('#nav-neulhajang').hide()
    }else{
        $('#nav-neulhajang').show()
        $('#nav-neulhaerang').hide()
    }
})
// 소 카테고리 선택시 class="sort_on" 주어서 선택 강조
$('.lab_sort').on('click',(e)=>{
    $target = $(e.target)
    $('.box_sorting').removeClass('sort_on')
    $target.parent().addClass('sort_on')
})



let page = 1;
console.log(page)
function MemberNeulhaerangList(currentPage) {

  fetch(`/mypage/member_neulhaerang_list/?page=${currentPage}`)
    .then(response => response.json())
    .then(result => {
      let text = "";
      let lists = result.member_nickname;
        console.log(result)
      if (!result.serialized_pagenator.has_next_data) {
        $('.link-other2').css('display', 'none');
      }

      lists.forEach((list, i) => {
        function formatDate(dateString) {
          const options = { year: 'numeric', month: 'numeric', day: 'numeric' };
          return new Date(dateString).toLocaleDateString('ko-KR', options);
        }

        const formattedDate = formatDate(list.updated_date);

        text += `<li>
                   <div class="action-content-card">
                      <a class="link-action-card"
                         href=>
                           <span class="thumb-action">
                              <img alt="이미지" class="img-thumb" src=${list.thumbnail_image}></span>
                             <div class="info-action">
                             <strong class="tit-action">${list.neulhaerang_title}</strong>
                              <p class="desc-action">내가 입력한 인증 피드 내용(비우기?)</p>
                              <span class="txt-date">${formattedDate}</span>
                           </div>
                        </a>
<!--                           <button class="btn-delete">삭제</button>-->
                        </div>
                      </li>`;
      });

      // $('.list-donate').html(text);
      $('.list-action-card').append(text);
      console.log(`Page: ${currentPage}`);
    })
}

MemberNeulhaerangList(page); // 페이지 번호만 전달

$('.link-other2').on("click", () => {
    if ('click') {
        page++;
        MemberNeulhaerangList(page);
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