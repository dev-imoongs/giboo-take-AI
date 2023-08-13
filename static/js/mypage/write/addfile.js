 // 대표이미지 추가 트리거 이벤트
 const $representingImgInput = $('#attachImage')
 const $representingThumbnail = $('.cont_visual')

$(".btn_select").on('click',(e)=>{
  $representingImgInput.trigger('click');
})
 
$representingImgInput.on('change',(eChange)=>{
  const reader = new FileReader();

  reader.readAsDataURL(eChange.target.files[0]);
  reader.addEventListener('load',(eLoad)=>{
    $('.cont_visual').removeClass('no_img')
    const path = eLoad.target.result;
    if(path.includes('image')){
      $representingThumbnail.css("backgroundImage",`url('${path}')`);
    }else{
      eChange.target.value = "";
      toastMsg('이미지 파일만 업로드 가능합니다.')
    }
  })
})
 

  $(document).on('change',(eChange)=>{
    const reader = new FileReader();

    reader.readAsDataURL(eChange.target.files[0]);
    reader.addEventListener('load',(eLoad)=>{
      const path = eLoad.target.result;
      if(path.includes('image')){
        $(eChange.target).closest('.info_group').next().find('li').removeClass('on')
        let createImgTag = $(document.createElement("img")).addClass('img_photo').attr('src',`${path}`)
        let photoCount = $(eChange.target).closest('.info_group').next().find('img').length
        $(eChange.target).closest('.info_group').next().find('li').eq(photoCount).addClass('on').find('button').append(createImgTag)
        $(eChange.target).closest('.info_group').next().next().next().find('input').eq(photoCount).attr('readonly',false)
        $(eChange.target).closest('.info_group').next().next().next().find('input').hide()
        $(eChange.target).closest('.info_group').next().next().next().find('input').eq(photoCount).show()
        
        $(eChange.target).closest('.info_group').next().next().find('.img_photo').attr("src",`${path}`)
        $(eChange.target).closest('.info_group').next().next().find('.img_photo').show()
        $(eChange.target).closest('dd').addClass('media_on')
      }else{
        eChange.target.value = "";
        toastMsg('이미지 파일만 업로드 가능합니다.')
      }
    })
  })
