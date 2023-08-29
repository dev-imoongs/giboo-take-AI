// $('#op-period').on('change', function() {
//   const selectedText = $(this).find('option:selected').text();
//   $('.select-option').text(selectedText);
// });
//
//
//
// let page = 1
// const list = (page) => {
//   fetch(`/mypage/donation_list/?page=${page}`)
//     .then(response => response.json())
//     .then(result => {
//       let text = "";
//       let lists = result.donation_list;
//
//       console.log(result.serialized_pagenator)
//       if (!result.serialized_pagenator.has_next_data) {
//           $('.link-other2').css('display', 'none')
//       }
//
//
//
//       lists.forEach((list, i) => {
//
//
//           function formatDate(dateString) {
//           const options = { year: 'numeric', month: 'numeric', day: 'numeric' };
//           return new Date(dateString).toLocaleDateString('ko-KR', options);
//         }
//
//           const formattedDate = formatDate(list.updated_date);
//
//         //   title = list.neulhaerang_id.neulhaerang_title
//         // console.log(title)
//
//         // const post_url = baseUrl.replace(0, neulhaerang_dontaion);
//         // console.log(post_url);
//         text += `<li className="item-donate">
//                      <p class="txt-sumdata"> ${formattedDate} </p>
//                      <p class="tit-sum">
//                        <a class="link-sum" href="">${list.neulhaerang}</a>
//                      </p>
//                      <div class="donate-numinfo">
//                        <strong class="num-sumprice">${list.donation_amount}원</strong>
//                        <span class="txt-sumprice">${list.donation_content}</span>
//                      </div>
//                      <div class="box-link"></div>
//                    </li>`;
//
//       });
//
// // document.querySelector('.list-donate').innerHTML = text;
// $('.list-donate').append(text);
//       // scroll 매개변수 확인
//       // scroll ? $('.list_fund').append(text) : $('.list_fund').html(text);
//     });
//
// };
//
//
//
// list(page)
//
// $('.link-other2').on("click", () => {
//     if ('click') {
//         page++
//         list(page, "click")
//     }
//
// })
let page = 1; // 페이지 변수를 전역 범위에서 정의

// $('#op-period').on('change', function() {
//   const selectedText = $(this).find('option:selected').text();
//   $('.select-option').text(selectedText);
//   page=1
//   loadYearlyData(selectedText)
// });



// 셀렉트 박스의 change 이벤트 핸들러
$('#op-period').on('change', function() {
  page = 1;
  const selectedText = $(this).find('option:selected').text();
  $('.select-option').text(selectedText);

  const selectedOptionValue = $(this).val();
  const selectedYear = selectedOptionValue.split(':')[0];
  initializePage();
  loadYearlyData(selectedYear);
});

function initializePage() {
  $('.list-donate').empty();
  $('.loading-spinner').show();
}

function loadYearlyData(year) {
    let apiUrl = ''
    if(year){
         apiUrl = `/mypage/donation_list/?page=${page}&year=${year}`;
    }else{
         apiUrl = `/mypage/donation_list/?page=${page}`;
    }


  fetch(apiUrl)
    .then(response => response.json())
    .then(result => {
      let text = "";
      let lists = result.donation_list;

      if (!result.serialized_pagenator.has_next_data) {
        $('.link-other2').css('display', 'none');
      }else{
          $('.link-other2').css('display', 'inline-block');
      }
      if(lists.length==0){
          $('.list-donate').append(`<div style="margin-top: 13px;">기부 내역이 없어요 기부천사님!!</div>`);
      }

      lists.forEach((list, i) => {
        function formatDate(dateString) {
          const options = { year: 'numeric', month: 'numeric', day: 'numeric' };
          return new Date(dateString).toLocaleDateString('ko-KR', options);
        }

        const formattedDate = formatDate(list.updated_date);

        text += `<li className="item-donate">
                     <p class="txt-sumdata"> ${formattedDate} </p>
                     <p class="tit-sum">
                       <a class="link-sum" href="">${list.neulhaerang}</a>
                     </p>
                     <div class="donate-numinfo">
                       <strong class="num-sumprice">${list.donation_amount}원</strong>
                       <span class="txt-sumprice">${list.donation_content}</span>
                     </div>
                     <div class="box-link"></div>
                   </li>`;
      });

      // $('.list-donate').html(text);
      $('.list-donate').append(text);
      console.log(`Year: ${year}, Page: ${page}`);
    })

}

$('.link-other2').on("click", () => {
    if ('click') {
        page++
        loadYearlyData(""); // 페이지를 증가시키며 데이터 로드
    }
});

// 초기 페이지 로드 시 전체 데이터를 불러옵니다.
loadYearlyData();