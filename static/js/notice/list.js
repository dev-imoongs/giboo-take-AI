let page = 1




const getNoticesByPaged = (page,type,tab)=>{
    let queryStringParams = new URLSearchParams({
        page,
        type
    })

    fetch(`/notice/get-notices-by-paged/?${queryStringParams}`)
        .then(response => response.json())
        .then(result =>{
           let notices = result.notices
           let pagenator = result.pagenator
            let text =''
            notices.forEach((notice,i)=>{
                  text += `<li>
                  <a class="link-official" href="/notice/detail/?notice_id=${notice.id}">
                    <strong class="subject-official">
                      ${notice.notice_status=="FIXED"? '<span class="icon-pin"></span>':''}${notice.notice_title}
                    </strong>
                      <span class="notice-target">${notice.type}</span>
                      <span class="date-official">
                        ${notice.created_date}
                      </span>
                      </a>
                    </li>`
            })
            if(tab){
                 $("ul.list-official").html(text)
            }else{
                  $("ul.list-official").append(text)
            }


        })
}

getNoticesByPaged(page,type)



$(".link-tab").each((i,tab)=>{
    $(tab).on("click",e=>{
        type = $(tab).find(".txt-tab").text()
        page=1
        getNoticesByPaged(page,type,"tab")
    })
})

let timeoutId
window.addEventListener("scroll", ()=>{
    clearTimeout(timeoutId)
            timeoutId = setTimeout(()=>{
         if (window.innerHeight + window.scrollY +500>= document.body.offsetHeight) {
    page++
    getNoticesByPaged(page,type)
             }
    },50)


});