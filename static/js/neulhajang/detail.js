// 글작성 버튼
    const writeBtn = document.querySelector(".project-active-button");
    // 글작성모달
    const writeModal = document.querySelector(".action-write-modal-base");
    const writeCancelBtn = document.querySelector(".cancel-button");
    const $modalCloseBtn = $('.modal-close-button')
    const formSubmitBtn = document.querySelector('.multi-action-form')
    // 글작성 취소확인 모달
    const confirmModal = document.querySelector(".confirm-modal");
    const $confirmBtn = $('.confirm-button');
    const $confirmCancelBtn = $('.confirm-cancel-button');
    // 글작성 모달 사진 첨부
    const inputFile = document.querySelector("#file-input")
    const displyFile = document.querySelector('.upload-image')
    const $deleteImageButton = $('.image-file-delete-button')
    const $ = document.querySelector('.image-file-upload-item')

    let page = 1
    let sort = '최신순'

    function writeModalOn() {
        writeModal.style.display="flex";
    }
    function writeModalOff() {
        writeModal.style.display="none";
    }



    function confirmModalOn(){
      confirmModal.style.display="flex";
    }

    function confirmModalOff(){
      confirmModal.style.display="none";
    }

    writeBtn.addEventListener("click", (e) => {
      if(!email) {
          $('#modalOFF').attr('id', 'modalON')
          $('.dimmed_layer').css('height', '100%');
          $('.dialog-content').css('display', 'block');
          $('.modal-delete').css('display', 'block');
          $('.modal-policy').css('display', 'none');
          return
      }
      authenFeedApplyAPIView()
      writeModalOn();
    });
    // 2번째 행동하기 버튼
    $('.floating-action-button').on("click", e=>{
        writeBtn.click()
    })

    writeCancelBtn.addEventListener("click", e => {
        console.log(displyFile.src.length)
        confirmModalOn();
    });

    $modalCloseBtn.on("click",e=>{
       writeModalOff();
    })

    $confirmBtn.on("click", e => {
       confirmModalOff();
       writeModalOff();
       $deleteImageButton.click()
    });

    $confirmCancelBtn.on("click", e => {
       confirmModalOff()
    });


    $(document).ready(()=>{


        $(document).on("click", e => {
            // 미션소개, 행동보드, 새소식 탭에 대한 클릭 이벤트
            let tabIndex = $(e.target).closest('.tab-menu-item').index()
            if ($(e.target).hasClass('tab-menu-item-button')) {
                $('.tab-menu-item').removeClass('tab-selected')
                $('.tab-menu-item-text').removeClass('text-selected')
                $(e.target).parent().addClass('tab-selected')
                $(e.target).children().addClass('text-selected')
            } else if ($(e.target).hasClass('tab-menu-item-text')) {
                $('.tab-menu-item').removeClass('tab-selected')
                $('.tab-menu-item-text').removeClass('text-selected')
                $(e.target).parent().parent().addClass('tab-selected')
                $(e.target).addClass('text-selected')
            }
            if (tabIndex == 0) {
                $('#action-board').hide()
                $('#mission-tab').show()
                missionTab(parsedInnerContents)
            } else if (tabIndex == 1) {
                $('#mission-tab').hide()
                $('#action-board').show()
            } else if (tabIndex ==2) {
                newsAPIView()
            }

            // 행동보드에 동적으로 생성된 좋아요 버튼 클릭 위함

            // 모달 취소확인 X버튼
            $('.confirm-modal-close-button').on('click', e => {
                confirmModalOff()
            })
            // 행동보드 좋아요 클릭 이벤트
            if ($(e.target).hasClass('authen-feed-like-selection')) {
              if(!email) {
                  $('#modalOFF').attr('id', 'modalON')
                  $('.dimmed_layer').css('height', '100%');
                  $('.dialog-content').css('display', 'block');
                  $('.modal-delete').css('display', 'block');
                  $('.modal-policy').css('display', 'none');
                  return
              }
                let feedId = $(e.target).find('div').attr('id')
                actionFeedLikeAPIView(feedId)
            }else if ($(e.target).hasClass('authen-feed-like-icon')) {
              if(!email) {
                  $('#modalOFF').attr('id', 'modalON')
                  $('.dimmed_layer').css('height', '100%');
                  $('.dialog-content').css('display', 'block');
                  $('.modal-delete').css('display', 'block');
                  $('.modal-policy').css('display', 'none');
                  return
              }
                let feedId = $(e.target).attr('id')
                actionFeedLikeAPIView(feedId)
            }

        })


    })
// 늘하장 게시물 응원
    $('.action-like-button').on("click",e=>{
      if(!email) {
          $('#modalOFF').attr('id', 'modalON')
          $('.dimmed_layer').css('height', '100%');
          $('.dialog-content').css('display', 'block');
          $('.modal-delete').css('display', 'block');
          $('.modal-policy').css('display', 'none');
          return
      }
        neulhajangLikeView()
    })

//  행동보드 최신순, 응원순 셀렉트박스 옵션메뉴 토글
    $('.select-box-list').on('click',e=>{
        $('.option-menu').toggle()
    })
//  최신순, 응원순 선택시 나타내는 div에 입력 및 행동보드 정렬
    $('.sort-button').on('click',e=>{
        let selectOption = $(e.target).text()
        $('.display-selected').text(selectOption)
        $('.option-menu').toggle()
        sort = $(e.target).text()
        page=1
        neulhajangActionFeedListAPIView(page,sort)
    })
// 행동보드 더보기 버튼
$('.more_list_button').on("click",e=>{
    page++
    neulhajangActionFeedListAPIView(page,sort)
})

// 행동하기 파일 넣기
$('.image-file-upload-button').on("click", () => {
    inputFile.click();
});
// 업로드한 file의 url을 가져오는 과정
inputFile.addEventListener("change", (e) => {
    if($('.image-file-upload-item').children())
    $('.image-file-upload-item').prepend()

    // 파일이 선택되면 원하는 작업을 수행
    console.log("파일 선택됨:", inputFile.files[0]);
    $deleteImageButton.show();
    let reader = new FileReader();
    reader.readAsDataURL(e.target.files[0])
    reader.onload = e => {
        displyFile.src = `${e.target.result}`
        console.log(e.target.result)
    }
});
// 업로드한 사진 취소 버튼
$deleteImageButton.on("click",(e)=>{
    inputFile.value = "";
    displyFile.src = "";
    $deleteImageButton.hide();
})

// 텍스트 에어리어 글자수 세기
$('.textarea-field').on("input",()=>{
    let textLength = $('.textarea-field').val().length
    $('.written-character-number').text(textLength)
})

formSubmitBtn.addEventListener("submit",(e )=>{
    if($('.textarea-field').val().length>300){
        console.log($('.textarea-field').val().length>300)
        toastMsg('피드의 내용은 최대 300자까지 입니다.')
        return
    }

})






function elapsedTime(date) {
  const start = new Date(date);
  const end = new Date();

  const diff = (end - start) / 1000;

  const times = [
    { name: '년', milliSeconds: 60 * 60 * 24 * 365 },
    { name: '개월', milliSeconds: 60 * 60 * 24 * 30 },
    { name: '일', milliSeconds: 60 * 60 * 24 },
    { name: '시간', milliSeconds: 60 * 60 },
    { name: '분', milliSeconds: 60 },
  ];

  for (const value of times) {
    const betweenTime = Math.floor(diff / value.milliSeconds);

    if (betweenTime > 0) {
      return `${betweenTime}${value.name} 전`;
    }
  }
  return '방금 전';
}

let toastFlag = false
const $toast = $(".toast-bottom-center")

const toastMsg = function (text) {
    if (!toastFlag) {
        $toast.show()
        toastFlag = true
        $('.toast-message').eq(0).text(text)
        setTimeout(function () {
            toastFlag = false
            $toast.hide()
        }, 2000)
    }
}





function missionTab(contents) {
    let addText = "";
    contents.forEach((content, i) => {
        if (content.model == "neulhajang.neulhajanginnertitle") {
            if(content.fields.neulhajang_content_order == 1){
                addText += `<h5 class="mission-tab-together-document-bullet-subtitle">${content.fields.inner_title_text}</h5>`
            }else{
                addText += `<h5 class="mission-tab-together-subtitle-document">${content.fields.inner_title_text}</h5>`;
            }
        } else if (content.model == "neulhajang.neulhajanginnercontent") {
                addText += `<p class="mission-tab-together-document-text">${content.fields.inner_content_text}</p>`;
        } else {
            addText += `<div class="mission-tab-together-document-image">
                            <div class="image-group">
                                <img class="image-item" src="${mediaUrl}${content.fields.inner_photo}"/>
                                ${content.fields.photo_explanation?`<p class="image_caption">${content.fields.photo_explanation}</p>`:''}
                            </div>
                        </div>`
        }
    })
    addText += `<h5 class="mission-tab-together-document-bullet-sub-title">인증 시 참고하세요!</h5>
                <div class="mission-tab-together-document-note">
                    <p class="note-text">① 위 제시된 인증 예시를 참고 후 인증해 주세요.<br>② 소중한 개인 정보가 담긴 내용은 지우고 올려주세요.<br>③ 프로젝트 의도에 벗어나는 악성, 유해 게시물 업로드 시 관리자에 의해 삭제될 수 있습니다.</p>
                </div>
                <div class="mission-tab-together-image-document">
                    <div class="image-group">
                        <a href="" target="_blank" class="mission-tab-banner-link">
                            <div class="mission-tab-banner-container">
                                <img class="mission-tab-banner-image" src="https://t1.kakaocdn.net/together_action_prod/admin/20230523/5f3a493a97f947589cb745b65b5c442a?type=thumb&amp;opt=R2240x0a"/>
                                <p class="mission-tab-banner-caption">
                                [이미지 클릭 시 프로모션 페이지로 이동합니다.]
                                </p>
                            </div>
                        </a>
                    </div>
                </div>`
    $('.mission-tab-together-document').html(addText)

}

missionTab(parsedInnerContents)

window.onload = function () {
    // HTML상단에서 해당 클래스 요소까지의 거리 계산
    let limitHeight = $('.tag-cloud-container').offset().top;
    // 높이 적용
    $('.project-detail-information').css('height', limitHeight + 'px')
};



const authenFeedImageListAPIView = () => {
    fetch(`/neulhajang/neulhajang-authentic-list/?neulhajangId=${neulhajangId}`)
        .then(response => response.json())
        .then(result => {
            let addText = ""
            let images = result.authen_feed_images
            images.forEach((image, i) => {
                addText += `<li class="action-image-list-item">
                                <button type="button" class="image-button-box">
                                    <img src="${mediaUrl}${image.feedPhoto}"
                                          class="action-participation-image">
                                </button>
                            </li>`
            })
            $('.action-image-list').html(addText)
        })
}
authenFeedImageListAPIView()

const authenFeedApplyAPIView = () => {

    fetch(`/neulhajang/neulhajang-authentic-apply/?neulhajangId=${neulhajangId}`)
        .then(response => response.json())
        .then(result => {
            const post = result.post[0]
            // 인원 관련
            const participants_count = result.participants_count
            const participants_target_amount = post.participants_target_amount
            const participantsRatio = Math.ceil(participants_count/participants_target_amount*100)

            $('.participants-count-textline').text(participants_count.toLocaleString())
            $('.participants-ratio-count').text(participantsRatio+'%')
            $('.participants-goal-count').text(participants_target_amount.toLocaleString()+'명')
            $('.current-progress-bar').attr('style',`width:${participantsRatio}%`)

            // 시간 관련
            let currentDate = new Date();
            const endDateString = post.neulhajang_duration_end_date;
            console.log(currentDate)
            const endDate = new Date(endDateString)
            console.log(endDate)
            // 두 날짜 객체 간의 시간 차이 계산 (밀리초 단위)
            let timeDifference = endDate - currentDate;
            console.log(timeDifference)

            // 시간 차이를 일 단위로 변환
            let daysDifference = timeDifference / (1000 * 60 * 60 * 24);
            console.log(daysDifference)
            // 시간 차이가 0이하가 되면 종료
            if(daysDifference<=0){
                daysDifference = "종료"
            }
        })
}
authenFeedApplyAPIView()

const neulhajangLikeView = () =>{
        fetch(`/neulhajang/neulhajang-like/?neulhajangId=${neulhajangId}`)
        .then(response => response.json())
        .then(result => {
            $('.action-count-label').text(result)
            $('.action-like-icon').toggleClass('animated')
        })
}
const neulhajangActionFeedListAPIView = (page, sort) => {
        fetch(`/neulhajang/neulhajang-action-feed-list/?neulhajangId=${neulhajangId}&page=${page}&sort=${sort}`)
        .then(response => response.json())
        .then(result => {
            let addFeed1 = ""
            let addFeed2 = ""
            let images = result.action_images
            let pagenator = result.serialized_pagenator
            images.forEach((image,i)=>{
                if(i%2==0){
                     addFeed1 += `<div class="action-image-article">
                              <div class="image_single">
                                  <img src="${mediaUrl}${image.image_url}" alt="${image.member_nickname}님이 올리신 행동이미지입니다." class="authen_image">
                                  <div class="authen-feed-like">
                                      <div class="authen-feed-like-main">
                                          <div class="authen-feed-like-selections">
                                              <button class="authen-feed-like-selection">
                                                  <div id="${image.id}" data-animation="BGSLIDE" class="authen-feed-like-icon ${image.my_like?'animated':''}"></div>
                                                  <span class="authen-feed-like-count-label">${image.feed_like_count}</span>
                                              </button>
                                          </div>
                                      </div>
                                  </div>
                              </div>
                              <div class="write-info-wrap">
                                  <em class="writer-wrap">
                                      <span class="writer-nickname">작성자 아이디</span>${image.member_nickname}</em>
                                  <span class="fBbmHT">
                                      <span class="writer-nickname">작성 일자</span>
                                      <span>${elapsedTime(image.created_date)}</span>
                                  </span>
                                  <p class="action-feed-content-wrap"><span class="WfZZU">행동 상세 글</span>${image.feedContent}</p>
                              </div>
                            </div>`
                }else{
                    addFeed2+=`<div class="action-image-article">
                              <div class="image_single">
                                  <img src="${mediaUrl}${image.image_url}" alt="${image.member_nickname}님이 올리신 행동이미지입니다." class="authen_image">
                                  <div class="authen-feed-like">
                                      <div class="authen-feed-like-main">
                                          <div class="authen-feed-like-selections">
                                              <button class="authen-feed-like-selection">
                                                  <div id="${image.id}" data-animation="BGSLIDE" class="authen-feed-like-icon ${image.my_like?'animated':''}"></div>
                                                  <span class="authen-feed-like-count-label">${image.feed_like_count}</span>
                                              </button>
                                          </div>
                                      </div>
                                  </div>
                              </div>
                              <div class="write-info-wrap">
                                  <em color="#333" class="writer-wrap">
                                      <span class="writer-nickname">작성자 아이디</span>${image.member_nickname}</em>
                                  <span color="gray60" class="sc-8aeb359-0 hFOIQn sc-5dc55ca7-0 sc-516de41-3 qPkKe fBbmHT">
                                      <span class="writer-nickname">작성 일자</span>
                                      <span>${elapsedTime(image.created_date)}</span>
                                  </span>
                                  <p class="action-feed-content-wrap"><span class="WfZZU">행동 상세 글</span>${image.feedContent}</p>
                              </div>
                            </div>`
                }
        })
            if(page == 1){
            $('.action-image-wrap').eq(0).html(addFeed1)
            $('.action-image-wrap').eq(1).html(addFeed2)
            }else{
            $('.action-image-wrap').eq(0).append(addFeed1)
            $('.action-image-wrap').eq(1).append(addFeed2)
            }

            if(pagenator.has_next){
                $('.more_action_list_button').show()
            }else{
                $('.more_action_list_button').hide()
            }
        })
}
neulhajangActionFeedListAPIView(page,sort)

const actionFeedLikeAPIView = (feedId) => {
    fetch(`/neulhajang/neulhajang-action-feed-like/?feedId=${feedId}`)
        .then(response => response.json())
        .then(result => {
                $(`div[id=${feedId}]`).toggleClass('animated')
                $(`div[id=${feedId}]`).next().text(result)
        })
}

const newsAPIView = () => {
    fetch(`/neulhajang/neulhajang-news/?neulhajangId=${neulhajangId}`)
        .then(response => response.json())
        .then(result => {
            const commitment = result.commitment[0]
            const contents = JSON.parse(result.sorted_contents)

            // 작성 날짜
            const createdDate = new Date(commitment.created_date);
            const year = createdDate.getFullYear()
            const month = String(createdDate.getMonth() + 1).padStart(2, '0');
            const day = String(createdDate.getDate()).padStart(2, '0');

            // let timeDifference =

            const formattedDate = year + '.' + month + '.' + day;


            let addText = `<div class="news-write-info-wrap">
                                      <div style="background-image: url(${commitment.writer_profile_image?commitment.writer_profile_choice=='user'?mediaUrl+commitment.writer_profile_image:commitment.writer_kakao_image:staticUrl+'image/avatar.png'})" class="writer-image"></div>
                                      <div role="text" class="news-write-info-item">
                                        <strong class="news-writer-nickname"><span class="WfZZU">제안자 이름</span>${commitment.member_nickname}</strong>
                                          <span class="commitment-date">
                                            <span class="WfZZU">작성 일자</span>
                                            ${formattedDate}
                                          </span>
                                      </div>
                                    </div>`
            contents.forEach((content,i)=>{
                if (content.model == "neulhajang.commitmentinnertitle") {
                    if(content.fields.commitment_content_order == 1){
                        addText += `<h5 class="mission-tab-together-document-bullet-subtitle">${content.fields.inner_title_text}</h5>`
                    }else{
                        addText += `<h5 class="mission-tab-together-subtitle-document">${content.fields.inner_title_text}</h5>`;
                    }
                } else if (content.model == "neulhajang.commitmentinnercontent") {
                    addText += `<p class="mission-tab-together-document-text">${content.fields.inner_content_text}</p>`;
                } else {
                    addText += `<div class="mission-tab-together-document-image">
                                    <div class="image-group">
                                        <img class="image-item" src="${mediaUrl}${content.fields.inner_photo}"/>
                                        ${content.fields.photo_explanation?`<p class="image_caption">${content.fields.photo_explanation}</p>`:''}
                                    </div>
                                </div>`
                }
            })
            $('.mission-tab-together-document').html(addText)
            $('#mission-tab').show()
            $('#action-board').hide()
        })
}
