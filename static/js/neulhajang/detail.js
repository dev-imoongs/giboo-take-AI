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
let page = 1

const participantsRatio = Math.ceil(authenticationFeedCount/participateTargetAmount*100)

$('.participants-ratio-count').text(`${participantsRatio}%`)
$('.participants-count-textline').text(authenticationFeedCount.toLocaleString())
$('.participants-goal-count').text(`${participateTargetAmount.toLocaleString()}명`)

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
    let limitHeight = $('.project-related-link-item').offset().top;
    // 높이 적용
    $('.project-detail-information').css('height', limitHeight + 'px')
};

const authenFeedImageListView = () => {
    fetch(`/neulhajang/neulhajang-authentic-list/?neulhajangId=${neulhajangId}`)
        .then(response => response.json())
        .then(result => {
        let addText = ""
        let images = result.authen_feed_images
            images.forEach((image,i)=>{
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
authenFeedImageListView()

const neulhajangLikeView = () =>{
        fetch(`/neulhajang/neulhajang-authentic-list/?neulhajangId=${neulhajangId}`)
        .then(response => response.json())
        .then(result => {
        })
}