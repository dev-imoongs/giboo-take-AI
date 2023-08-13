

//사진 무한 슬라이드 1.셋팅
const $photoUls = $("ul.list_slide")
const $innerPaging = $(".inner_paging")
$photoUls.each((idx, photoul) => {
    let $photos = $(photoul).children("li")

    //ul태그안에 사진을 양옆으로 한개씩 더 넣었다고 가정할 때
    //각각의 사진 이동
    $photos.each((i, photo) => {
        photo.style.transform = `translateX(${i * 100 - 100}%)`
    })

    //배너 하단 버튼 갯수 생성
    let total = $photos.length-2
   
    let text = '<em class="num_page">1</em>'
    for(let i = 0 ; i <total-1; i++){
        text+=`<button type="button" class="num_page">${i+2}</button>`
    }
    $innerPaging.append(text)

})




//2.버튼 클릭
//버튼 플래그
let isClicked = false;

const arrowBtnClickSlide = function (btn, prev) {

    //버튼 누른 플래그
    if (isClicked) return
    isClicked = true

      let $list_photos = $(".slide_pannel")
    //transition duration 주기
    $list_photos.css("transition-duration", "500ms")
    //사진 총갯수
    let total = $list_photos.length - 2


    //하단 버튼 조정
    let em = $("em.num_page")
    let count = Number(em.text())
    
    if(prev){
        if(count == 1){
            count = total
        }else{
            count -=1
        }
    }else{
        if(count == total){
            count =1
        }else{
            count+=1
        }
    }

    let text = ''
    for(let i = 0 ; i <total; i++){
        if(i+1==count){
            text+=`<em class="num_page">${i+1}</em>`
            continue;
        }
        text+=`<button type="button" class="num_page">${i+1}</button>`
    }
    $innerPaging.html(text)
    pagingBtnClick()



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


//하단 페이지 버튼 클릭 버튼 만들어주는 함수
const pagingBtnClick = function(){
    let $btns = $("button.num_page")
    $btns.each((i,btn)=>{
        $(btn).on("click",e=>{
            if(isClicked) return
            let $list_photos = $(".slide_pannel")
            $list_photos.css("transition-duration", "500ms")
            let total = $list_photos.length-2
           let count = Number($(btn).text())
           let text =''
            for(let i = 0 ; i <total; i++){
                if(i+1==count){
                    text+=`<em class="num_page">${i+1}</em>`
                    continue;
                }
                text+=`<button type="button" class="num_page">${i+1}</button>`
            }
            $innerPaging.html(text)
            
            $list_photos.each((i,photo)=>{
                photo.style.transform = `translateX(${-(count-i)*100}%)`
            })

            setTimeout(()=>{
                isClicked=false
                pagingBtnClick()
            },500)
        })
    })

}

pagingBtnClick()

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