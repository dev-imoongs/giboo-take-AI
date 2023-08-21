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


//내 댓글 삭제 모달,
const $btn_delete = $(".btn_delete")
const $comment_delete_modal = $(".comment_delete_modal")
$btn_delete.on("click",e=>{
    $dimedLayer.css("height","100%")
    $comment_delete_modal.show()
    $comment_delete_modal.addClass("opened_modal")
})

$(".comment_delete_modal .btn_type2").on("click",e=>{
    $dimedLayer.css('height', "");
    $comment_delete_modal.hide();
    $comment_delete_modal.removeClass("opened_modal")
})

//동참하기 모달
const $participate_modal = $(".participate_modal")
const $btn_participate =$(".btn_participate")
$btn_participate.on("click",e=>{
    $dimedLayer.css("height","100%")
    $participate_modal.show()
    $participate_modal.addClass("opened_modal")
})

$(".participate_modal .btn_type2").on("click",e=>{
    $dimedLayer.css('height', "");
    $participate_modal.hide();
    $participate_modal.removeClass("opened_modal")
})

//로그인 모달
const $need_login_modal = $(".need_login_modal")

//로그인 필요 모달 보여주는 함수 여러개 사용하므로 함수로 사용
const show_need_login_modal = function (){
    $dimedLayer.css("height","100%")
    $need_login_modal.show()
    $need_login_modal.addClass("opened_modal")
}

// 로그인 검사로직 false라면 로그인 모달 띄우기
$(".btn_give").on("click",e=>{
    show_need_login_modal()
})


$(".need_login_modal .btn_type2").on("click",e=>{
    $dimedLayer.css('height', "");
    $need_login_modal.hide();
    $need_login_modal.removeClass("opened_modal")
})




//기부하기 버튼 모달
const $fund_modal =$(".fund_modal")
$(".btn_give").on("click",e=>{
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
// setInterval(()=>{
//      if (window.innerHeight + window.scrollY + 240 >= document.body.scrollHeight) {
//
//         $fund_float.addClass("btn_static")
//     } else {
//         $fund_float.removeClass("btn_static")
//     }
// },100)





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

//댓글 숫자 제한
$tf_cmt.on("input",e=>{
    console.log($tf_cmt.text())
    $comment_num.text($tf_cmt.val().length + "/")
})

//등록 눌렀을때 확인
const $btn_comment = $(".btn_comment")

let toastFlag = false
$btn_comment.on("click",e=>{
    if($tf_cmt.val().length<2){
        if (toastFlag) return
        toastFlag=true
        $toast.show()
        setTimeout(()=> {
            $toast.hide()
            toastFlag = false

        },2000)
    }
})



















//사진 무한 슬라이드 1.셋팅
$photoUls = $("ul.list_photo")
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

$(document).ready(()=>{
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


function Function(temps) {
    let addtext = ""
    let multiImgflag = ""
    temps.forEach((temp,i)=>{
        console.log(temp)
        if(temp.fields.neulhaerang_content_order !== multiImgflag) {
            if (temp.model == 'neulhaerang.neulhaeranginnertitle') {
                addtext += `<span class="tit_subject">${temp.fields.inner_title_text}</span>`
            } else if (temp.model == 'neulhaerang.neulhaeranginnercontent') {
                addtext += `<p class="desc_subject">${temp.fields.inner_content_text}</p>`
            } else {
                addtext += `<div class="photo_slide">
                              <div class="inner_photo">
                                <ul class="list_photo">
                                <li>
                                <span
                                  class="img_slide"
                                  style="
                                    background-image: url(${temp.fields.inner_photo});
                                  "
                                ></span
                                ><span class="txt_caption">${temp.fields.photo_explanation}</span>
                              </li>
                              </ul>
                              </div>
                            </div>`
            }
        }else{
            addList = `<li>
                        <span
                          class="img_slide"
                          style="
                            background-image: url(${temp.fields.inner_photo});
                          "
                        ></span
                        ><span class="txt_caption">${temp.fields.photo_explanation}</span>
                      </li>`
            $('.list_photo').append(addList)
        }
        multiImgflag = temp.fields.neulhaerang_content_order;
        })
    $('.cont_subject').html(addtext)
}


})


// my_script.js
// function Function(temps) {
//     let addtext = ""
//     let multiImgflag = ""
//     temps.forEach((temp,i)=>{
//         console.log(temp)
//         if(temp.fields.neulhaerang_content_order !== multiImgflag) {
//             if (temp.model == 'neulhaerang.neulhaeranginnertitle') {
//                 addtext += `<span class="tit_subject">${temp.fields.inner_title_text}</span>`
//             } else if (temp.model == 'neulhaerang.neulhaeranginnercontent') {
//                 addtext += `<p class="desc_subject">${temp.fields.inner_content_text}</p>`
//             } else {
//                 addtext += `<div class="photo_slide">
//                               <div class="inner_photo">
//                                 <ul class="list_photo">
//                                 <li>
//                                 <span
//                                   class="img_slide"
//                                   style="
//                                     background-image: url(${temp.fields.inner_photo});
//                                   "
//                                 ></span
//                                 ><span class="txt_caption">${temp.fields.photo_explanation}</span>
//                               </li>
//                               </ul>
//                               </div>
//                             </div>`
//             }
//         }else{
//             addtext += `<li>
//                         <span
//                           class="img_slide"
//                           style="
//                             background-image: url(${temp.fields.inner_photo});
//                           "
//                         ></span
//                         ><span class="txt_caption">${temp.fields.photo_explanation}</span>
//                       </li>`
//
//         }
//         multiImgflag = temp.fields.neulhaerang_content_order;
//         })
//     $('.cont_subject').html(addtext)
// }

//

function Function4(total_fund){
        $('.total_fund').html(`${total_fund.toLocaleString('ko-KR')}<span class="txt_won">원</span>`)
}

function Function3(plans) {
    addText = ""
    plans.forEach((plan,i)=>{

    addText += `<li>
                  <span class="num_plan">${i+1}.</span>
                  <span class="txt_plan">
                    <span class="txt_expense">${plan.fields.plan_name}</span
                    ><span class="emph_sign"
                      ><span class="num_type"></span>${plan.fields.plan_amount.toLocaleString('ko-KR')}원</span
                    ></span
                  >
                </li>`

    })
    $('.list_plan').html(addText)
}

function Function2(post){
    const formattedAmount = post[0].fields.target_amount.toLocaleString('ko-KR');
    $('.txt_goal').text(`${formattedAmount}원 목표`)
    $('.num_goal').text(`${formattedAmount}원`)
}
function Function(temps) {
    let addtext = "";
    let multiImgflag = "";
    temps.forEach((temp, i) => {
        if (temp.fields.neulhaerang_content_order !== multiImgflag) {
            if (temp.model == 'neulhaerang.neulhaeranginnertitle') {
                addtext += `<span class="tit_subject">${temp.fields.inner_title_text}</span>`;
            } else if (temp.model == 'neulhaerang.neulhaeranginnercontent') {
                addtext += `<p class="desc_subject">${temp.fields.inner_content_text}</p>`;
            } else {
                addtext += `<div class="photo_slide">
                              <div class="inner_photo">
                                <ul class="list_photo">
                                  <li>
                                    <span class="img_slide"
                                          style="background-image: url(${temp.fields.inner_photo});">
                                    </span>
                                    <span class="txt_caption">${temp.fields.photo_explanation}</span>
                                  </li>`;

                let j = i;
                while (j < temps.length && temps[j].fields.neulhaerang_content_order == multiImgflag) {
                    console.log('아아아ㅏㅇ')
                    addtext += `<li>
                                  <span class="img_slide"
                                        style="background-image: url(${temps[j].fields.inner_photo});">
                                  </span>
                                  <span class="txt_caption">${temps[j].fields.photo_explanation}</span>
                                </li>`;
                    j++;
                }
                addtext += `</ul>
                            </div>
                          </div>`;

            }
       }
        multiImgflag = temp.fields.neulhaerang_content_order;
    });

    $('.cont_subject').html(addtext);
}