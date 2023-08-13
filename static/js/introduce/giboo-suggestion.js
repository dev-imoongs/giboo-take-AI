//faq 슬라이드
const $questionBoxes = $(".box_faq");
const $questionBtn = $(".btn_faq")
$questionBtn.each((i,box)=>{
    $(box).on("click",e=>{
        if($questionBoxes.eq(i).hasClass("on")){
            $questionBoxes.eq(i).removeClass("on")
        }else{
            $questionBoxes.eq(i).addClass("on")
        }
    })
    
})