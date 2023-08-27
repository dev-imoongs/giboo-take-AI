//페이지 네이션 구현

page = page ? page :1
search = search=='None' ? '' :search
const shownoticesByPaged =  (page,search)=>{

    fetch(`/admin/get-notices-by-paged/?page=${page}&search=${search}`)
        .then(response => response.json())
        .then(result =>{
            console.log(result)
            let text=''
            let pageText=''
           let notices= result.notices
           let pagenator= result.pagenator
            text+=`   <thead>
                            <tr>
                                <th class="checkbox-line">
                                    <input type="checkbox" id="selectAll">
                                </th>
                                <th>No</th>
                                <th>작성자</th>
                                <th style="font-weight: bold">공지사항 제목</th>
                                <th>작성 날짜</th>
                                <th>공지 대상</th>
                            </tr>
                            </thead>`
            notices.forEach((notice,i)=>{
                text+=`<tr>
                                <td class="checkbox-line">
                                    <input class="subCheckbox" type="checkbox" name="check">
                                </td>
                                <td class="noticeId">
                                    ${notice.id}
                                </td>
                                <td>${notice.member_nickname}</td>
                                <td>  
                                    <a style="font-weight: bold;" href="/admin/notice/detail/?notice_id=${notice.id}&page=${page}&search=${search}">
                                         ${notice.notice_title}
                                    </a>
                                  
                                </td>
                                <td>
                                    ${notice.created_date.split(".")[0].replace("T","-")}
                                </td>
                                <td class="color-icon">
                                    ${notice.type}
                                </td>
                            </tr>`
            })

            $(".notice-table").html(text)

            pageText+=`<div class="page-button-box">`

            pageText+= pagenator.has_prev ?`<div class="left-page-button">
                        <div class="page-button-margin">
                            <div>
                                <img src="${staticUrl}image/admin/left_icon.png"
                                     class="left-button">
                            </div>
                        </div>
                    </div>`:``

                for(let i = pagenator.start_page;i<=pagenator.end_page ; i++){
                    pageText+=

                    `<div class="${page == i ? 'page-button-active':''} page-button">
                        <div class="page-button-margin">
                            <div>
                                <span>${i}</span>
                            </div>
                        </div>
                    </div>`
                }


                 pageText+= pagenator.has_next? `<div class="right-page-button">
                        <div class="page-button-margin">
                            <div>
                                <img src="${staticUrl}image/admin/right_icon.png"
                                     class="right-button">
                            </div>
                        </div>
                    </div>
                </div>`:``


                $(".page-button-box-layout").html(pageText)
                pageBtnAddEvent(pagenator)
                checkboxEvent()

        })
}

shownoticesByPaged(page,search)

//하단 페이지 버튼 클릭시 이동
const pageBtnAddEvent = (pagenator)=>{
    $(".page-button").each((i,btn)=>{
    $(btn).on("click",e=>{
        page = Number($(btn).find("span").text())
        shownoticesByPaged(page,search)
    })
})
    $(".left-page-button").on("click",e=>{
        page = pagenator.start_page-1
        shownoticesByPaged(page,search)
    })
      $(".right-page-button").on("click",e=>{
        page = pagenator.end_page+1
        shownoticesByPaged(page,search)
    })
}


//게시판 선택 삭제
$(".delete-button").on("click",e=>{
    let notice_ids = []
    $(".subCheckbox").filter((i,checkbox)=> $(checkbox).prop("checked")).each((i,checkbox)=>{
        let member_id = Number($(checkbox).closest(".checkbox-line").next().text())
        notice_ids.push(member_id)
    })

    let datas = {
            method: "POST",
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify({
            notice_ids
             }),
    }

    fetch("/admin/delete-notices/", datas)
        .then(response=>response.json())
        .then(result =>{
            if(result){
                shownoticesByPaged(page,search)
            }
        })

})


//검색
$(".search-icon").on("click",e=>{
    search = $(".admin-search-box").val()
    page = 1
    shownoticesByPaged(page,search)
})
