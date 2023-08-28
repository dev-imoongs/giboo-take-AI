// 글작성 버튼
    const writeBtn = document.querySelector(".project-active-button");
    // 글작성모달
    const writeModal = document.querySelector(".action-write-modal-base");
    const writeCancelBtn = document.querySelector(".cancel-button");
    const $modalCloseBtn = $('.modal-close-button')
    // 글작성 취소확인 모달
    const confirmModal = document.querySelector(".confirm-modal");
    const $confirmBtn = $('.confirm-button');
    const $confirmCancelBtn = $('.confirm-cancel-button');

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

    writeBtn.addEventListener("click", e => {
        writeModalOn();
    });

    writeCancelBtn.addEventListener("click", e => {
        confirmModalOn();
    });

    $modalCloseBtn.on("click",e=>{
       writeModalOff();
    })

    $confirmBtn.on("click", e => {
       confirmModalOff();
       writeModalOff();
    });

    $confirmCancelBtn.on("click", e => {
       confirmModalOff()
    });

    //우측 인증 피드 목록 늘하장 좋아요 클릭시 이벤트

    $(document).on("click",e=>{
        // 미션소개, 행동보드, 새소식 탭에 대한 클릭 이벤트
        let tabIndex = $(e.target).closest('.tab-menu-item').index()
        if($(e.target).hasClass('tab-menu-item-button')){
            $('.tab-menu-item').removeClass('tab-selected')
            $('.tab-menu-item-text').removeClass('text-selected')
            $(e.target).parent().addClass('tab-selected')
            $(e.target).children().addClass('text-selected')
        }
        else if($(e.target).hasClass('tab-menu-item-text')){
            $('.tab-menu-item').removeClass('tab-selected')
            $('.tab-menu-item-text').removeClass('text-selected')
            $(e.target).parent().parent().addClass('tab-selected')
            $(e.target).addClass('text-selected')
        }
        if(tabIndex==0){
            $('#action-board').hide()
            $('#mission-tab').show()
        }else if(tabIndex==1){
            $('#mission-tab').hide()
            $('#action-board').show()
        }else{
        }

        // 행동보드에 동적으로 생성된 좋아요 버튼 클릭 위함

        // 모달 취소확인 X버튼
        $('.confirm-modal-close-button').on('click',e=>{
            confirmModalOff()
        })

        // 인증피드 좋아요 클릭시 이벤트
        $('.authen-feed-like-icon').on('click',e=>{
        $(e.target).toggleClass('animated')
    })
})

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
//  최신순, 응원순 선택시 나타내는 div에 입력
    $('.sort-button').on('click',e=>{
        let selectOption = $(e.target).text()
        $('.display-selected').text(selectOption)
        $('.option-menu').toggle()
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




let page = 1

const participantsRatio = Math.ceil(authenticationFeedCount/participateTargetAmount*100)

$('.participants-ratio-count').text(`${participantsRatio}%`)
$('.participants-count-textline').text(authenticationFeedCount.toLocaleString())
$('.participants-goal-count').text(`${participateTargetAmount.toLocaleString()}명`)
$('.current-progress-bar').attr('style',`width:${participantsRatio}%`)

function postContent(contents) {
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
                                <img class="image-item" src="/upload/${content.fields.inner_photo}"/>
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

postContent(parsedInnerContents)

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
                                    <img src="/upload/${image.feedPhoto}"
                                          class="action-participation-image">
                                </button>
                            </li>`
            })
            $('.action-image-list').html(addText)
        })
}
authenFeedImageListAPIView()

const neulhajangLikeView = () =>{
        fetch(`/neulhajang/neulhajang-like/?neulhajangId=${neulhajangId}`)
        .then(response => response.json())
        .then(result => {
            $('.action-count-label').text(result)
            $('.action-like-icon').toggleClass('animated')
        })
}
const neulhajangActionFeedListAPIView = (page) => {
            fetch(`/neulhajang/neulhajang-action-feed-list/?neulhajangId=${neulhajangId}&page=${page}`)
        .then(response => response.json())
        .then(result => {
            let addFeed1 = ""
            let addFeed2 = ""
            let images = result.action_feed_images
            images.forEach((image,i)=>{
                if(i%2==0){
                     addFeed1 += `<div class="action-image-article">
                              <div class="image_single">
                                  <img src="/upload/${image.feedPhoto}" alt="${image.member_nickname}님이 올리신 행동이미지입니다." class="authen_image">
                                  <div class="authen-feed-like">
                                      <div class="authen-feed-like-main">
                                          <div class="authen-feed-like-selections">
                                              <button class="authen-feed-like-selection">
                                                  <div data-animation="BGSLIDE" class="authen-feed-like-icon"></div>
                                                  <span class="authen-feed-like-count-label">${image.like_count}</span>
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
                              </div>
                            </div>`
                }else{
                    addFeed2+=`<div class="action-image-article">
                              <div class="image_single">
                                  <img src="/upload/${image.feedPhoto}" alt="${image.member_nickname}님이 올리신 행동이미지입니다." class="authen_image">
                                  <div class="authen-feed-like">
                                      <div class="authen-feed-like-main">
                                          <div class="authen-feed-like-selections">
                                              <button class="authen-feed-like-selection">
                                                  <div data-animation="BGSLIDE" class="authen-feed-like-icon"></div>
                                                  <span class="authen-feed-like-count-label">${image.like_count}</span>
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
                              </div>
                            </div>`
                }
        })
            $('.action-image-wrap').eq(0).append(addFeed1)
            $('.action-image-wrap').eq(1).append(addFeed2)
        })
}
neulhajangActionFeedListAPIView(page)