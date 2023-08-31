
let order = 3


function randMintoMax(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// 힌트보기 눌렀을때 모달창 띄우기, body_hint에 나올 글 초기값 설정
$('.btn_hint1').on('click', () => {
    $('#modalOFF').attr('id', 'modalON')
    $('.dimmed_layer').css('height', '100%');
    $('.dialog-content').css('display', 'block');
    $('.body_hint').hide()
    console.log($('.list_tab').children())
    $('.tab_hint').children().removeClass('on')
    $('.tab_hint').children().eq(0).addClass('on')
    $('.body_hint').eq(0).show()
})
// 힌트보기 눌렀을때 모달창 띄우기, body_hint에 나올 글 초기값 설정
$('.btn_hint2').on('click', () => {
    $('#modalOFF').attr('id', 'modalON')
    $('.dimmed_layer').css('height', '100%');
    $('.dialog-content').css('display', 'block');
    $('.body_hint').hide()
    $('.tab_hint').children().removeClass('on')
    $('.tab_hint').children().eq(2).addClass('on')
    $('.body_hint').eq(2).show()
})

//  모달창 안에 들어가서 탭 눌렀을때 해당 글은 보여주고 외에는 숨기는 기능
$('.link_hint').on('click',(e)=>{
    $('.link_hint').parent().removeClass('on')
    $(e.target).parent().addClass('on')
    $('.body_hint').hide()
    $('.body_hint').eq($(e.target).parent().index()).show()
})

// 모달창 닫기 버튼
$('.btn_close').on("click", () => {
    $('#modalON').attr('id', 'modalOFF');
    $('.dimmed_layer').css('height', '0');
    $('.dialog-content').css('display', 'none');
})

// 개설 완료 버튼 눌렀을 때 이벤트
$('.link_step3').on('click',(e)=>{
    if($('.front_pack').find('.txt_num').text() == 0){
        toastMsg('제목을 입력해주세요.')
        $('span.inner_tit').focus()
        return
    }

    if($('.cont_visual').hasClass('no_img')){
        toastMsg('대표사진을 선택해주세요.')
        return
    }

    let innerTitFlag = false
    $('input[placeholder="소제목"]').each((i,v)=>{
        if(!$(v).val()){
            $(v).focus()
            innerTitFlag =true
        }

    })
    if(innerTitFlag){
        toastMsg('소제목을 입력해주세요.')
        return
    }

    $('textarea[placeholder="본문"]').each((i,v)=>{
        if(!$(v).val()){
            $(v).focus()
            innerTitFlag =true
        }

    })
    if(innerTitFlag){
        toastMsg('본문을 입력해주세요.')
        return
    }
    if(!$('input[placeholder="http://"]').val()){
        toastMsg('참가자들을 위한 오픈채팅 링크를 걸어주세요')
         return
    }
    $('.add_byeol input').each((i,v)=>{
        if(!$(v).val()){
            innerTitFlag = true
            $(v).focus()
            toastMsg('별찌 목록을 최소 1개 이상 작성해주세요')
        }

    })
    if(innerTitFlag) {
        return
    }




    //마지막 폼 되기전에 데이터들 input에 삽입하기
    // $(".start-date span").text
    $("input[name='title']").val($(".inner_tit").text())


    //사진 갯수구하기
    $("input[name='inner_photo_content_order']").each((i,order)=>{
        console.log("들어옴")
        let count =$(order).closest("dd").find("input[name='inner_photo']").length
        console.log(count)
        $(order).val($(order).val()+`_${count}`)
    })

    //태그 필수
    if($(".tag").filter((i,v)=>!$(v).val()).length!=0){
        toastMsg("태그 갯수대로 모두 입력해주세요")
        return;
    }




    $("form").eq(0).submit()


















})

$(document).ready(function () {
    function updateIDs(e) {
        $index = $(e.target).closest('.thumb_photo').prev().find('.txt_num')
        $index.each((i,v)=>$(v).text(i+1))
    }
    //최대 최소 범위 내 난수 생성하는 함수

// keyup 되었을때 textarea 글자 수 계산
    $(document).on('input', (e) => {
        $titLength = $(e.target).parent().parent().prev()
        $txtLength = $(e.target).parent().parent().next()
        $imgdescLength = $(e.target).parent().next()

        if($(e.target).hasClass('tag')){
            $index = $(e.target).parent().parent().index()
            $('.link_hash').eq($index-1).text(`#${$(e.target).val()}`)
        }

        if ($titLength.attr('class') == 'info_append') {
            $titLength.children().text(`${$(e.target).text().length}/`)
        }
        if ($txtLength.attr('class') == 'info_append') {
            $txtLength.children().text(`${$(e.target).val().length}/`)
        }
        if ($imgdescLength.attr('class') == 'info_append') {
            $imgdescLength.children().text(`${$(e.target).val().length}/`)
        }
    })

    $(document).on('click', (e) => {
        // 삭제버튼
        if($(e.target).hasClass('btn_del')){
            if($(e.target).parent().is('.inner_media')){
                let index = $(e.target).closest('.thumb_photo').prev().find('li.on').index()
                let addInput = `<input type="text" name="caption" autocomplete="off" classoutline="" maxlength="30" readonly
                class="tf_write ng-dirty ng-touched" style="display: none;"
                placeholder="이미지 설명을 입력하세요.">`

                $(e.target).closest('.thumb_photo').next().find('input').eq(index).remove()
                $(addInput).insertAfter($(e.target).closest('.thumb_photo').next().find('input').last())

                $(e.target).closest('.thumb_photo').next().find('input').last().show()
                $(e.target).closest('.thumb_photo').prev().find('li.on').remove()
                $addContent = '<li>\n' +
                    '  <div class="ico_together photo_preview">\n' +
                    '    <span class="txt_num">10</span>\n' +
                    '    <button type="button" class="btn_photo"></button>\n' +
                    '  </div>\n' +
                    '</li>'
                $($addContent).insertAfter($(e.target).closest('.thumb_photo').prev().find('.list_photo').children().last());
                updateIDs(e)
                $(e.target).closest('.desc_photo').removeClass('media_on')
            }


            // 별찌목록에 있는 삭제버튼을 눌렀을 경우 (별찌목록 부모가 add_byeol을 갖고있음)
            if($(e.target).parent().hasClass('add_byeol')){
                if($('#byeoljji-list .add_byeol').length > 1) {
                    $(e.target).parent().remove()
                }else{
                    toastMsg('기부자에게 제공 할 별찌 목록을 최소 1개 이상 입력해야합니다.')
                    return
                }
            }
            // 태그목록에 있는 삭제버튼을 눌렀을 경우 (태그목록 부모가 add_tag을 갖고있음)
            if($(e.target).parent().hasClass('add_tag')){
                index = $(e.target).parent().index()
                $('.list_write .hash_group').children().eq(index-1).remove()
                $(e.target).parent().remove()
            }


            if($(e.target).parent().is('.inner_group,.area_caption')){

                $(e.target).closest('dd').remove()
            }


        }

        if ($(e.target).hasClass('img_photo')||$(e.target).hasClass('btn_photo')) {
            $(e.target).closest('.list_photo').children().removeClass('on')
            $(e.target).closest('li').addClass('on')
            let index = $(e.target).closest('li').index()
            $(e.target).closest('.photo_gallery').next().next().find('input').hide()
            $(e.target).closest('.photo_gallery').next().next().find('input').eq(index).show()
            $(e.target).closest('.photo_gallery').next().next().find('input').eq(index).trigger('keyup')

            if ($(e.target).is('button')) {
                $(e.target).closest('.desc_photo').removeClass('media_on')
            }else if($(e.target).is('img')) {
                $thumbImg = $(e.target).attr('src')
                $(e.target).closest('.desc_photo').addClass('media_on')
                $(e.target).closest('.photo_gallery').next().find('.img_photo').attr("src", $thumbImg)
            }
        }

        if ($(e.target).hasClass('tf_write')) {
            $(e.target).addClass('tf_active')
        } else {
            $('.tf_write').removeClass('tf_active')
        }

    })

})

// 소제목 추가
$('.btn-subhead').on('click',()=>{
    $addContent = '<dd>\n' +
                  '  <div class="group_tf">\n' +
                  '    <div class="inner_group">\n' +
                  '      <input type="text"  name="inner_title" classoutline="" multibyte="" autocomplete="off" class="tf_write ng-valid ng-touched ng-dirty" id="subTitle3" placeholder="소제목">\n' +
                  ` <input type="hidden" name="inner_title_content_order" value="${order++}">\n` +
                  '      <button type="button" class="ico_together2 btn_del"> 내용삭제 </button>\n' +
                  '    </div>\n' +
                  '  </div>\n' +
                  '  <div class="info_append">\n' +
                  '    <span class="txt_num">0 /</span>60\n' +
                  '  </div>\n' +
                  '</dd>'
    $($addContent).insertAfter($('.add-form').children().last())
})
// 본문 추가
$('.btn-maintext').on('click',()=>{
    $addContent = '<dd>\n' +
                  '  <div class="group_tf">\n' +
                  '    <div class="inner_group">\n' +
                  '      <textarea cols="30" name="inner_content" rows="10" multibyte="" autocomplete="off" expandabletextarea="" class="tf_write tf_intro ng-valid ng-dirty ng-touched" id="tfIntro4" placeholder="본문" style="height: 80px; overflow: hidden;"></textarea>' +
        `<input type="hidden" name="inner_content_content_order" value="${order++}">` +
        '<button type="button" class="ico_together2 btn_del"> 내용삭제 </button><!----></div><!---->\n' +
                  '  </div>\n' +
                  '  <div class="info_append"><span class="txt_num">0 /</span>1000 </div>\n' +
                  '</dd>'
    $($addContent).insertAfter($('.add-form').children().last())
})
// 이미지 추가
$('.btn-addimg').on('click',()=>{
    $addContent = `<dd class="desc_media desc_photo">
            <input type="hidden" name="inner_photo_content_order" value="${order++}">
    <photo-box>
      <div class="info_group">
        <img src="//t1.kakaocdn.net/together_image/m640/bg_suggest_media_170327.png"
             alt=""
             class="img_blank mo_show">
        <div class="media_info">
          <div class="inner_info">
            <p class="txt_size"> 이미지 사이즈
              <br>최소 : 가로 640px, 세로 360px
            </p>
            <div class="info_attach">
              <label for="attachImage">
                <span class="ico_together2 ico_photo">관련이미지 추가하기 (최대 10장)</span>
              </label>
              <input type="file" id="attachImage" ngfileselect=""
                     maxsize="10MB" class="tf_attach" 
                     accept="image/*, .jpg, .jpeg, .png, .gif, .bmp">
            </div>
          </div>
        </div>
      </div>
      <div class="photo_gallery">
        <ul class="list_photo">
          <li class="on">
            <div class="ico_together photo_preview">
              <span class="txt_num">1</span>
              <button type="button" class="btn_photo">
              </button>
            </div>
          </li>
          <li class="">
            <div class="ico_together photo_preview">
              <span class="txt_num">2</span>
              <button type="button" class="btn_photo">
              </button>
            </div>
          </li>
          <li class="">
            <div class="ico_together photo_preview">
              <span class="txt_num">3</span>
              <button type="button" class="btn_photo">
              </button>
            </div>
          </li>
          <li>
            <div class="ico_together photo_preview">
              <span class="txt_num">4</span>
              <button type="button" class="btn_photo">
                <!-- 이 안에 img 태그로 들어감 -->
              </button>
            </div>
          </li>
          <li>
            <div class="ico_together photo_preview">
              <span class="txt_num">5</span>
              <button type="button" class="btn_photo">
</button>
            </div>
          </li>
          <li>
            <div class="ico_together photo_preview">
              <span class="txt_num">6</span>
              <button type="button" class="btn_photo"></button>
            </div>
          </li>
          <li>
            <div class="ico_together photo_preview">
              <span class="txt_num">7</span>
              <button type="button" class="btn_photo"></button>
            </div>
          </li>
          <li>
            <div class="ico_together photo_preview">
              <span class="txt_num">8</span>
              <button type="button" class="btn_photo"></button>
            </div>
          </li>
          <li>
            <div class="ico_together photo_preview">
              <span class="txt_num">9</span>
              <button type="button" class="btn_photo"></button>
            </div>
          </li>
          <li>
            <div class="ico_together photo_preview">
              <span class="txt_num">10</span>
              <button type="button" class="btn_photo"></button>
            </div>
          </li>
        </ul>
      </div>
      <div class="thumb_photo">
        <img src="//t1.kakaocdn.net/together_image/m640/bg_suggest_media_170327.png"
             class="img_blank mo_show">
        <div class="inner_media">
          <!-- src경로에 click한 이미지 경로로 바꿔줘야함 -->
          <img alt="1번째 이미지 확대보기" class="img_photo"
               src="">
          <button type="button" class="ico_together2 btn_del"> 선택된 사진 삭제
          </button>
        </div>
      </div>
      <div class="area_caption">
        <div class="group_tf">
           <input type="text" name="caption" classoutline="" maxlength="30" readonly
                 class="tf_write ng-dirty ng-touched ng-valid" autocomplete="off"
                 placeholder="이미지 설명을 입력하세요.">
                <input type="text" name="caption" classoutline="" maxlength="30" readonly
                 class="tf_write ng-dirty ng-touched ng-valid" style="display: none;" autocomplete="off"
                 placeholder="이미지 설명을 입력하세요.">
                 <input type="text" name="caption" classoutline="" maxlength="30" readonly
                 class="tf_write ng-dirty ng-touched ng-valid" style="display: none;" autocomplete="off"
                 placeholder="이미지 설명을 입력하세요.">
                 <input type="text" name="caption" classoutline="" maxlength="30" readonly
                 class="tf_write ng-dirty ng-touched ng-valid" style="display: none;" autocomplete="off"
                 placeholder="이미지 설명을 입력하세요.">
                 <input type="text" name="caption" classoutline="" maxlength="30" readonly
                 class="tf_write ng-dirty ng-touched ng-valid" style="display: none;" autocomplete="off"
                 placeholder="이미지 설명을 입력하세요.">
                 <input type="text" name="caption" classoutline="" maxlength="30" readonly
                 class="tf_write ng-dirty ng-touched ng-valid" style="display: none;" autocomplete="off"
                 placeholder="이미지 설명을 입력하세요.">
                 <input type="text" name="caption" classoutline="" maxlength="30" readonly
                 class="tf_write ng-dirty ng-touched ng-valid" style="display: none;" autocomplete="off"
                 placeholder="이미지 설명을 입력하세요.">
                 <input type="text" name="caption" classoutline="" maxlength="30" readonly
                 class="tf_write ng-dirty ng-touched ng-valid" style="display: none;" autocomplete="off"
                 placeholder="이미지 설명을 입력하세요.">
                 <input type="text" name="caption" classoutline="" maxlength="30" readonly
                 class="tf_write ng-dirty ng-touched ng-valid" style="display: none;" autocomplete="off"
                 placeholder="이미지 설명을 입력하세요.">
                 <input type="text" name="caption" classoutline="" maxlength="30" readonly
                 class="tf_write ng-dirty ng-touched ng-valid" style="display: none;" autocomplete="off"
                 placeholder="이미지 설명을 입력하세요.">
                
                              
        </div>
        <div class="info_append">
          <span class="txt_num">0/</span>
          30
        </div>
        <button type="button" class="ico_together2 btn_del"> 내용삭제 </button>
      </div>
    </photo-box>
  </dd>`
    $($addContent).insertAfter($('.add-form').children().last())
})
// 태그 추가 기능
$('.box_open .list_write .relate_url').first().find('button.box_add').on('click',(e)=>{
    // 태그명 적는 박스
    $addContent = '<div class="add_link add_tag">\n' +
                    '  <div class="group_tf"><label class="lab_link" for="relateTitle0">태그</label>\n' +
                    '      <input placeholder="추가할 태그명을 입력해주세요"\n' +
                    '             type="text" autocomplete="off" name="tag" \n' +
                    '             class="tf_link tag ng-untouched ng-pristine ng-valid"\n' +
                    '             id="relateTitle0" focus="false" blur="true">\n' +
                    '  </div>\n' +
                    '  <button type="button" class="ico_together2 btn_del tag_del"> 내용삭제 </button>\n' +
                    '</div>'
    // 해쉬태그
    $addContent2 = '<a class="link_hash"></a>'
    i = randMintoMax(1,10)


    if($('#tag-list .add_link').length < 10){

        if ($('.list_write .hash_group').children().length == 0) {
            $('.list_write .hash_group').append($addContent2)
        } else {
            $($addContent2).insertAfter($('.list_write .hash_group').children().last())
        }

        $('.list_write .hash_group').children().last().addClass(`hash_type${i}`)
        $($addContent).insertAfter($('.box_open .list_write .relate_url').first().children().last())
    }else{
        toastMsg('태그는 최대 10개까지만 가능합니다.')
    }
})




// line:264 아래로 갈 시에 btn_static 클래스 추가 (소제목, 본문, 이미지추가 버튼 fixed 위치)