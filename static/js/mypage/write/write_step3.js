// 힌트보기 눌렀을때 모달창 띄우기, body_hint에 나올 글 초기값 설정
$('.btn_hint').on('click', () => {
    $('#modalOFF').attr('id', 'modalON')
    $('.dimmed_layer').css('height', '100%');
    $('.dialog-content').css('display', 'block');
    $('.body_hint').hide()
    $('.body_hint').eq(1).show()
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

$(document).ready(function () {
    function updateIDs(e) {
        $index = $(e.target).closest('.thumb_photo').prev().find('.txt_num')
        console.log($index)
        $index.each((i,v)=>$(v).text(i+1))
    }

    $(document).on('keyup', (e) => {
        $titLength = $(e.target).parent().parent().prev()
        $txtLength = $(e.target).parent().parent().next()
        $imgdescLength = $(e.target).parent().next()

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

            console.log($(e.target))
            if($(e.target).parent().is('.inner_group,.area_caption')){

                $(e.target).closest('dd').remove()
            }
        }

        if ($(e.target).hasClass('img_photo')||$(e.target).hasClass('btn_photo')) {
            $(e.target).closest('.list_photo').children().removeClass('on')
            $(e.target).closest('li').addClass('on')
            // $(e.target).closest('ul').find('.img_photo').each((i,v)=>{
            //     console.log(i)
            // })
            if ($(e.target).is('button')) {
                $(e.target).closest('.desc_photo').removeClass('media_on')
            } else if ($(e.target).is('img')) {
                $thumbImg = $(e.target).attr('src')
                $(e.target).closest('.desc_photo').addClass('media_on')
                $(e.target).closest('.photo_gallery').next().find('.img_photo').attr("src", $thumbImg)
            }
        }

        if ($(e.target).hasClass('tf_write')) {
            console.log($(e.target))
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
                  '      <input type="text" classoutline="" multibyte="" class="tf_write ng-valid ng-touched ng-dirty" id="subTitle3" placeholder="소제목">\n' +
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
                  '      <textarea cols="30" rows="10" multibyte="" expandabletextarea="" class="tf_write tf_intro ng-valid ng-dirty ng-touched" id="tfIntro4" placeholder="본문" style="height: 80px; overflow: hidden;"></textarea><button type="button" class="ico_together2 btn_del"> 내용삭제 </button><!----></div><!---->\n' +
                  '  </div>\n' +
                  '  <div class="info_append"><span class="txt_num">0 /</span>1000 </div>\n' +
                  '</dd>'
    $($addContent).insertAfter($('.add-form').children().last())
})
// 이미지 추가
$('.btn-addimg').on('click',()=>{
    $addContent = '<dd class="desc_media desc_photo">\n' +
        '  <photo-box>\n' +
        '    <div class="info_group">\n' +
        '      <img src="//t1.kakaocdn.net/together_image/m640/bg_suggest_media_170327.png" alt="" class="img_blank mo_show">\n' +
        '      <div class="media_info">\n' +
        '        <div class="inner_info">\n' +
        '          <p class="txt_size"> 이미지 사이즈\n' +
        '            <br>최소 : 가로 640px, 세로 360px\n' +
        '          </p>\n' +
        '          <div class="info_attach">\n' +
        '            <label for="attachImage">\n' +
        '              <span class="ico_together2 ico_photo">관련이미지 추가하기 (최대 10장)</span>\n' +
        '            </label>\n' +
        '            <input type="file" id="attachImage" ngfileselect="" maxsize="10MB" class="tf_attach" accept="image/*, .jpg, .jpeg, .png, .gif, .bmp">\n' +
        '          </div>\n' +
        '        </div>\n' +
        '      </div>\n' +
        '    </div>\n' +
        '    <div class="photo_gallery">\n' +
        '      <ul class="list_photo">\n' +
        '        <li class="">\n' +
        '          <div class="ico_together photo_preview">\n' +
        '            <span class="txt_num">1</span>\n' +
        '            <button type="button" class="btn_photo">\n' +
        '            </button>\n' +
        '          </div>\n' +
        '        </li>\n' +
        '        <li class="">\n' +
        '          <div class="ico_together photo_preview">\n' +
        '            <span class="txt_num">2</span>\n' +
        '            <button type="button" class="btn_photo">\n' +
        '            </button>\n' +
        '          </div>\n' +
        '        </li>\n' +
        '        <li class="">\n' +
        '          <div class="ico_together photo_preview">\n' +
        '            <span class="txt_num">3</span>\n' +
        '            <button type="button" class="btn_photo">\n' +
        '            </button>\n' +
        '          </div>\n' +
        '        </li>\n' +
        '        <li>\n' +
        '          <div class="ico_together photo_preview">\n' +
        '            <span class="txt_num">4</span>\n' +
        '            <button type="button" class="btn_photo">\n' +
        '            </button>\n' +
        '          </div>\n' +
        '        </li>\n' +
        '        <li>\n' +
        '          <div class="ico_together photo_preview">\n' +
        '            <span class="txt_num">5</span>\n' +
        '            <button type="button" class="btn_photo"></button>\n' +
        '          </div>\n' +
        '        </li>\n' +
        '        <li>\n' +
        '          <div class="ico_together photo_preview">\n' +
        '            <span class="txt_num">6</span>\n' +
        '            <button type="button" class="btn_photo"></button>\n' +
        '          </div>\n' +
        '        </li>\n' +
        '        <li>\n' +
        '          <div class="ico_together photo_preview">\n' +
        '            <span class="txt_num">7</span>\n' +
        '            <button type="button" class="btn_photo"></button>\n' +
        '          </div>\n' +
        '        </li>\n' +
        '        <li>\n' +
        '          <div class="ico_together photo_preview">\n' +
        '            <span class="txt_num">8</span>\n' +
        '            <button type="button" class="btn_photo"></button>\n' +
        '          </div>\n' +
        '        </li>\n' +
        '        <li>\n' +
        '          <div class="ico_together photo_preview">\n' +
        '            <span class="txt_num">9</span>\n' +
        '            <button type="button" class="btn_photo"></button>\n' +
        '          </div>\n' +
        '        </li>\n' +
        '        <li>\n' +
        '          <div class="ico_together photo_preview">\n' +
        '            <span class="txt_num">10</span>\n' +
        '            <button type="button" class="btn_photo"></button>\n' +
        '          </div>\n' +
        '        </li>\n' +
        '      </ul>\n' +
        '    </div>\n' +
        '    <div class="thumb_photo">\n' +
        '      <img src="//t1.kakaocdn.net/together_image/m640/bg_suggest_media_170327.png" class="img_blank mo_show">\n' +
        '      <div class="inner_media">\n' +
        '        <img alt="1번째 이미지 확대보기" class="img_photo" src="">\n' +
        '        <button type="button" class="ico_together2 btn_del"> 선택된 사진 삭제\n' +
        '        </button>\n' +
        '      </div>\n' +
        '    </div>\n' +
        '    <div class="area_caption">\n' +
        '      <div class="group_tf">\n' +
        '        <input type="text" name="caption" classoutline="" maxlength="30" class="tf_write ng-dirty ng-touched ng-valid" id="albumTitle2" placeholder="이미지 설명을 입력하세요.">\n' +
        '      </div>\n' +
        '      <div class="info_append">\n' +
        '        <span class="txt_num">0/</span>\n' +
        '        30\n' +
        '      </div>\n' +
        '      <button type="button" class="ico_together2 btn_del"> 내용삭제 </button>\n' +
        '    </div>\n' +
        '  </photo-box>\n' +
        '</dd>'
    $($addContent).insertAfter($('.add-form').children().last())
})


// 파일 추가하는 기능

// line:264 아래로 갈 시에 btn_static 클래스 추가 (소제목, 본문, 이미지추가 버튼 fixed 위치)

// 파일 추가했을때 정렬 기능

// 제목에 썸네일 추가 기능