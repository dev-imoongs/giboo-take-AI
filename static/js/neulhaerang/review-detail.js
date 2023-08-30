//뱃지클릭
const $linkBadges = $(".link_badge")
const $dimedLayer = $(".dimmed_layer")
const $badgeModal = $(".badge-modal")

//클릭했을시 뱃지정보 가져와서 모달 안에 컨텐츠로 삽입
$linkBadges.each((i, link) => {
    $(link).on("click", e => {
        $dimedLayer.css('height', "100%");
        $badgeModal.show();
        $badgeModal.addClass("opened_modal")
    })
})

$(".btn_close").on("click", e => {
    $dimedLayer.css('height', "");
    $badgeModal.hide();
    $badgeModal.removeClass("opened_modal")
})

// 응원하기 버튼 누를시 이벤트
$('.btn_cheer').on('click',(e)=>{
    if (!email) {
        $('#modalOFF').attr('id', 'modalON')
        $('.dimmed_layer').css('height', '100%');
        $('.dialog-content').css('display', 'block');
        $('.modal-delete').css('display', 'block');
        $('.modal-policy').css('display', 'none');
        return
    }
    $('.ico_cheer').toggleClass('on')
    neulhaerangReviewDetailLikeView()
})


//동참하기 모달
const $participate_modal = $(".participate_modal")
const $btn_participate =$(".btn_participate")
$btn_participate.on("click", e => {
    toastMsg('동참은 진행중인 늘해랑에서만 가능합니다.')
});

$(".participate_modal .btn_type1").on("click", e => {
    // neulhaerangDetailParticipateView();
    $('.ico_share').addClass('on');
    $('.txt_share').addClass('on');
    $('.txt_share .num_active').addClass('on');
    $dimedLayer.css('height', "");
    $participate_modal.hide();
    $participate_modal.removeClass("opened_modal");
});

$(".participate_modal .btn_type2").on("click", e => {
    $dimedLayer.css('height', "");
    $participate_modal.hide();
    $participate_modal.removeClass("opened_modal");
});

//로그인 모달
const $need_login_modal = $(".need_login_modal")

//로그인 필요 모달 보여주는 함수 여러개 사용하므로 함수로 사용
const show_need_login_modal = function (){
    $dimedLayer.css("height","100%")
    $need_login_modal.show()
    $need_login_modal.addClass("opened_modal")
    return
}

// 로그인 검사로직 false라면 로그인 모달 띄우기
// $(".btn_give").on("click",e=>{
//     show_need_login_modal()
// })

//
const showMoreBtn = () => {
    if (checkMoreBtn <= 0) {
        $('.link_round').hide()
    }
}


$(".need_login_modal .btn_type2").on("click",e=>{
    $dimedLayer.css('height', "");
    $need_login_modal.hide();
    $need_login_modal.removeClass("opened_modal")
})

//내 댓글 삭제 모달,
const deleteReply = (replyId) => {
    const $btn_delete = $(".btn_delete")
    const $comment_delete_modal = $(".comment_delete_modal")
    $btn_delete.on("click", e => {
        $dimedLayer.css("height", "100%")
        $comment_delete_modal.show()
        $comment_delete_modal.addClass("opened_modal")
        if($(e.target).hasClass('btn_delete'))
        replyId = $(e.target).prev().prev().attr('id')
    })

    $(".comment_delete_modal .btn_type1").on("click",(e)=>{
        neulhaerangDetailReplyDeleteView(replyId)
        $(`span[id=${replyId}]`).closest('li').hide()
        $dimedLayer.css('height', "");
        $comment_delete_modal.hide();
        $comment_delete_modal.removeClass("opened_modal")
    })

    $(".comment_delete_modal .btn_type2").on("click", e => {
        $dimedLayer.css('height', "");
        $comment_delete_modal.hide();
        $comment_delete_modal.removeClass("opened_modal")
    })
}

//기부하기 버튼 모달
const $fund_modal =$(".fund_modal")
$(".btn_give").on("click",e=>{
    if (!email) {
        $('#modalOFF').attr('id', 'modalON')
        $('.dimmed_layer').css('height', '100%');
        $('.dialog-content').css('display', 'block');
        $('.modal-delete').css('display', 'block');
        $('.modal-policy').css('display', 'none');
        return
    }
    $fund_modal.css("display","flex")
    $dimedLayer.css("height","100%")
    $fund_modal.addClass("opend_modal")
})

$(".btn_close").on("click",e=>{
    $fund_modal.hide()
    $dimedLayer.css("height","")
    $fund_modal.removeClass("opend_modal")
})

const $moneyInput= $(".box_input_num .tf_g")
$(".btn_reset").on("click",e=>{
    $moneyInput.val("")
})

$(".btn_digit").each((i,btn)=>{
    $(btn).on("click",e=>{
        let money = btn.dataset.don
        if(money ==="직접입력"){
            $moneyInput.val("")
            $moneyInput.focus()
            return
        }
            $moneyInput.val(Number($moneyInput.val())+Number(money))
    })
})

$(".box_tf .tf_g").on("input",e=>{
    $(".give_num").text($(".box_tf .tf_g").val().length)
})





//하단 픽스드 버튼
const $fund_float = $(".fund_float ")
let scrollFlag = false
$(window).on("scroll",e=> {
    if(scrollFlag)return
    scrollFlag = true
    if (window.innerHeight + window.scrollY + 400 >= document.body.scrollHeight) {

        $fund_float.addClass("btn_static")
    } else {
        $fund_float.removeClass("btn_static")
    }
    setTimeout(()=>scrollFlag=false,100)

})

//모금 플랜 누르기 슬라이드 토글
const $btn_plan = $(".btn_plan")
let $btn_plan_isClicked =false
$btn_plan.on("click",e=>{
    if($btn_plan_isClicked) return
    $btn_plan_isClicked = true
    if(document.body.offsetWidth<=767){
        if($(".slide-togle").css("display")==="none"){
        $(".info_plan .ico_arr").css("background-position","-132px -342px")
        }else{
        //클로즈
        $(".info_plan .ico_arr").css("background-position","-132px -350px")
        }
    }else{
        if($(".slide-togle").css("display")==="none"){

        $(".info_plan .ico_arr").css("background-position","-248px -116px")
        }else{
        //클로즈
        $(".info_plan .ico_arr").css("background-position","-237px -116px")
        }
    }
    $(".slide-togle").slideToggle()
    setTimeout(()=>$btn_plan_isClicked=false,500)
})


//댓글 등록
const $comment_num = $(".comment_num")
const $tf_cmt = $(".tf_cmt")
const $toast = $(".toast-bottom-center")

let toastFlag = false
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


//댓글 최소 길이 제한
$tf_cmt.on("input",e=>{
    // console.log($tf_cmt.text())
    $comment_num.text($tf_cmt.val().length + "/")
})

//등록 눌렀을때 확인
const $btn_comment = $(".btn_comment")


$btn_comment.on("click",(e)=>{
    if (!email) {
        $('#modalOFF').attr('id', 'modalON')
        $('.dimmed_layer').css('height', '100%');
        $('.dialog-content').css('display', 'block');
        $('.modal-delete').css('display', 'block');
        $('.modal-policy').css('display', 'none');
        return
    }
    if($tf_cmt.val().length<2){
        toastMsg('최소 2글자 이상 입력해주세요')
    }else{
        replyCont = $('.tf_cmt').val()
        neulhaerangReviewDetailReplyCreate(replyCont)
        $('.tf_cmt').val("")
        $comment_num.text(0+'/')
        replyPage=1

    }
})

$(document).ready(()=> {
    //왼쪽 클릭
    const $btn_prevs = $(".btn_prev")
    $btn_prevs.each((idx, btn_prev) => {
        $(btn_prev).on("click", e => {
            arrowBtnClickSlide(btn_prev, "prev")
        })
    })
    //오른쪽 클릭

    const $btn_nexts = $(".btn_next")
    $btn_nexts.each((idx, btn_next) => {
        $(btn_next).on("click", e => {
            arrowBtnClickSlide(btn_next)
        })
    })
    $(document).on('click',(e)=>{
        if ($(e.target).hasClass('ico_like')) {
            $(e.target).parent().toggleClass('on')
            reply_id = $(e.target).parent().prev().attr('id')
        } else if ($(e.target).hasClass('btn_like')) {
            $(e.target).toggleClass('on')
            reply_id = $(e.target).prev().attr('id')
        } else if ($(e.target).hasClass('num_like')) {
            return
        }
        neulhaerangReviewDetailReplyLikeView(reply_id)
    })

})
reviewInnerContent(parsedReviewInnerContents);

//사진 무한 슬라이드 1.셋팅
const $photoUls = $("ul.list_photo")
$photoUls.each((idx, photoul) => {
    $photos = $(photoul).children("li")
    $pagingSlide = $(".paging_slide").eq(idx)

    //ul태그안에 사진을 양옆으로 한개씩 더 넣었다고 가정할 때
    //각각의 사진 이동
    $photos.each((i, photo) => {
        photo.style.transform = `translateX(${i * 100 - 100}%)`
    })

    //페이징처리 사진 한개 일 때는 버튼없애기
    if ($photos.length === 3) {
        $pagingSlide.hide()
    }
    //페이징 최대 숫자
    $pagingSlide.find(".num_paging").html(` <span class="num_page">1</span> / ${$photos.length - 2}`)

})

//2.버튼 클릭
//버튼 플래그
let isClicked = false;

const arrowBtnClickSlide = function (btn, prev) {

    //버튼 누른 플래그
    if (isClicked) return
    isClicked = true

      let $list_photos = $(btn).closest(".photo_slide").find(".list_photo").children("li")
    //transition duration 주기
    $list_photos.css("transition-duration", "500ms")
    //사진 총갯수
    let total = $list_photos.length - 2


    //사진 페이징 처리
    let $num_page = $(btn).parent().find(".num_page")
        if(prev&&Number($num_page.text())===1){
            $num_page.text(total)
        }else if(!prev&&Number($num_page.text())===total ){
            $num_page.text(1)
        }else{
               $num_page.text(Number($num_page.text())+(prev ? -1 : 1))
        }




    $list_photos.each((i, photo) => {
        let translateNum = Number(photo.style.transform.replace("translateX(", "").replace("%)", ""))
        let nextNum = translateNum + (prev ? 100 : -100)
        photo.style.transform = `translateX(${nextNum}%)`

        //끝에 도달하면 원래 위치로 0.5초뒤

        if (prev ? (nextNum === (total + 1) * 100) : (nextNum === (total + 1) * (-100))) {

            setTimeout(() => {

                $list_photos.each((i, photo) => {
                    photo.style.transitionDuration = ""
                    photo.style.transform = `translateX(${prev ? 100 * (i - total) : 100 * (i - 1)}%)`
                })
                isClicked = false;
            }, 500)

        } else {
            setTimeout(() => isClicked = false, 500)
        }

    })

}

// inner content 순서에 맞게 출력
function reviewInnerContent(contents) {
    let addtext = "";
    let multiImgflag = "";
    contents.forEach((content, i) => {
        if (content.fields.neulhaerang_content_order !== multiImgflag) {
            if (content.model == 'neulhaerang_review.reviewinnertitle') {
                addtext += `<span class="tit_subject">${content.fields.inner_title_text}</span>`;
            } else if (content.model == 'neulhaerang_review.reviewinnercontent') {
                addtext += `<p class="desc_subject">${content.fields.inner_content_text}</p>`;
            } else {
                addtext += `<div class="photo_slide">
                                          <div class="inner_photo">
                                            <ul class="list_photo">
                                              <li>
                                                <span class="img_slide"
                                                      style="background-image: url('/upload/${content.fields.inner_photo}');">
                                                </span>
                                                <span class="txt_caption">${content.fields.photo_explanation}</span>
                                              </li>
                                            </ul>
                                        </div>
                                        <div class="paging_slide">
                                          <span class="num_paging">
                                            <span class="num_page">1</span>
                                            / 4
                                          </span>
                                          <button class="btn_prev" type="button">
                                            <span class="ico_together2 ico_prev">이전버튼</span>
                                          </button>
                                          <button class="btn_next" type="button">
                                            <span class="ico_together2 ico_next">다음버튼</span>
                                          </button>
                                        </div>
                                        </div>`;
            }
            $('.cont_subject').html(addtext);
        } else {
            let addtext2 = `<li>
                                              <span class="img_slide"
                                                    style="background-image: url('/upload/${content.fields.inner_photo}');">
                                              </span>
                                              <span class="txt_caption">${content.fields.photo_explanation}</span>
                                            </li>`;
            $('.list_photo').last().append(addtext2)
        }

        multiImgflag = content.fields.neulhaerang_content_order;
    });

    $('.list_photo').each((i, v) => {

        let first = $(v).children().first().clone()
        let last = $(v).children().last().clone()
        $(v).append(first)
        $(v).prepend(last)
    })
}



function fundraisedRatio(target_amounts, total_fund){
    const formattedAmount = target_amounts[0].fields.target_amount.toLocaleString('ko-KR');
    $('.txt_goal').text(`${formattedAmount}원 목표`)
    $('.num_goal').text(`${total_fund.toLocaleString()}원`)
    $('.total_fund').html(`${total_fund.toLocaleString('ko-KR')}<span class="txt_won">원</span>`)
    let percentage = Math.ceil(total_fund / target_amounts[0].fields.target_amount * 100)
    $('.mark_point').attr('style',`left:${percentage}%`)
    $('.sign_graph').attr('style',`width:${percentage}%`)
    $('.num_per').text(percentage)
    if(percentage == 100){
        $('.chart_fund').addClass('fund_end')
    }
}

fundraisedRatio(parsedAmount,parsedAmountSum);

function fundUsage(histories) {
    addText = ""
    histories.forEach((history,i)=>{
    addText += `<li>
                  <span class="num_plan">${i+1}.</span>
                  <span class="txt_plan">
                    <span class="txt_expense">${history.fields.history_name}</span
                    ><span class="emph_sign"
                      ><span class="num_type"></span>${history.fields.history_amount.toLocaleString('ko-KR')}원</span
                    ></span
                  >
                </li>`

    })
    $('.list_plan').html(addText)
}
fundUsage(parsedUsageHistory)

// function btnLikeOn(){
//     $('.btn_like').on('click',(e)=>{
//
//
//     })
// }

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

let replyPage = 1
let replyCont = ""
let replys = ""
let checkMoreBtn = replyCount - 5

// neulhaerangReviewId는 html 스크립트에서 neulhaerang_id를 받아서 이미 저장하였음
const neulhaerangReviewDetailReplyView = (replyPage, btn_more)=> {
    fetch(`/neulhaerang_review/review-detail-reply/?replyPage=${replyPage}&neulhaerangReviewId=${neulhaerangReviewId}`)
        .then(response => response.json())
        .then(result => {
            replys = result.replys
            reply_count = result.replys_count

            let replyText = ""
            replys.forEach((reply,i)=>{
            replyText += `<li>
                          <button class="link_profile">
                            <img
                              src="https://t1.kakaocdn.net/together_image/common/avatar/avatar_angel.png"
                              class="img_thumb"
                            />
                            <!--베뎃-->
                            ${reply.best_reply ? '<span class="ico_together2 ico_best"></span>':''}    
                            
                          </button>
                          <div class="cmt_info">
                            <span class="info_append"
                              ><strong class="tit_nickname"
                                ><a href="#" class="link_nickname"> ${reply.member_nickname} </a></strong
                              >`
                              if(reply.donation != null){
                                replyText += `<span class="txt_money"> ${reply.donation} </span>`
                              }else{
                                replyText += `<span class="txt_money"></span>`
                              }
                              replyText += `</span
                            ><span class="txt_cmt"
                              ><span class="desc_cmt">${reply.reply_content}</span>
                              <!--이모티콘 있을시 아래에 넣음-->
                              <span class="emoticon_pack"></span> </span
                            ><span class="info_append"
                              ><span id="${reply.id}" class="txt_time">${elapsedTime(reply.created_date)}</span>
                              <button type="button" class="btn_like ${reply.my_like?"on":""}">
                                <span class="ico_together ico_like"></span>&nbsp;좋아요&nbsp;<span
                                  class="num_like"
                                  >${reply.reply_like_count}</span
                                >
                              </button>`

                if(reply.check_my_comment){
                    replyText += `<button type="button" class="btn_delete">삭제</button></span>
                                    </div>
                                        </li>`
                }else{
                         replyText += `</span>
                                        </div>
                                        </li>`
                }
            })
            if(btn_more){
                $('.list_cmt').append(replyText)
            }
            else{
                $('.list_cmt').html(replyText)
            }
            // btnLikeOn()
            deleteReply()
            $('.inner_info .emph_sign').html(reply_count)
        })
}
neulhaerangReviewDetailReplyView(replyPage)
showMoreBtn()

const neulhaerangReviewDetailReplyCreate = (replyCont)=>{
    fetch(`/neulhaerang_review/review-detail-reply-write/?replyCont=${replyCont}&neulhaerangReviewId=${neulhaerangReviewId}`)
        .then(response => response.json())
        .then(result => {
            neulhaerangReviewDetailReplyView(replyPage)
        })
}



// 더보기 버튼 누를 시에 실행되는 이벤트
$('.link_round').on('click',()=>{
    replyPage++
    checkMoreBtn -= 5
    showMoreBtn()
    neulhaerangReviewDetailReplyView(replyPage,'btn_more')
})


// 댓글 좋아요
let reply_id = ""
const neulhaerangReviewDetailReplyLikeView = (reply_id) => {
    fetch(`/neulhaerang_review/review-detail-reply-like/?reply_id=${reply_id}`)
        .then(response => response.json())
        .then(result => {
            $(`span[id='${reply_id}']`).next().find('.num_like').text(result)
        })

}

// 댓글 삭제
const neulhaerangDetailReplyDeleteView = (reply_id) => {
    fetch(`/neulhaerang_review/review-detail-reply-delete/?reply_id=${reply_id}`)
        .then(response => response.json())
        .then(result => {

        })
}
// 늘해랑 응원하기
const neulhaerangReviewDetailLikeView = () => {
    fetch(`/neulhaerang_review/review-detail-like/?neulhaerangReviewId=${neulhaerangReviewId}`)
        .then(response => response.json())
        .then(result => {
            $(`.txt_cheer .num_active`).text(result)

        })
}