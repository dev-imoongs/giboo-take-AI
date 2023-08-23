//페이지 네이션 구현

page = page ? page :1
search = search=='None' ? '' :search
const showinquerysByPaged =  (page,search)=>{

    fetch(`/admin/get-inquerys-by-paged/?page=${page}&search=${search}`)
        .then(response => response.json())
        .then(result =>{
            console.log(result)
            let text=''
            let pageText=''
           let inquerys= result.inquerys
           let pagenator= result.pagenator
            text+=`   <thead>
                            <tr>
                                <th class="checkbox-line">
                                    <input type="checkbox" id="selectAll">
                                </th>
                                <th>No</th>
                                <th>문의자</th>
                                <th style="font-weight: bold">문의 제목</th>
                                <th>작성 날짜</th>
                                <th>답변 상태</th>
                            </tr>
                            </thead>`
            inquerys.forEach((inquery,i)=>{
                text+=`<tr>
                                <td class="checkbox-line">
                                    <input class="subCheckbox" type="checkbox" name="check">
                                </td>
                                <td class="noticeId">
                                    ${inquery.id}
                                </td>
                                <td>${inquery.member_nickname}</td>
                                <td>  
                                    <a style="font-weight: bold;" href="/admin/inquery/detail/?inquery_id=${inquery.id}&page=${page}&search=${search}">
                                         ${inquery.inquery_title}
                                    </a>
                                  
                                </td>
                                <td>
                                    ${inquery.created_date}
                                </td>
                                <td class="color-icon">
                                    <span class="icon-wrap">
                                        <img class="green" src="${staticUrl}image/admin/${inquery.response_status =="답변대기"? 'caution':'check'}.png">
                                    </span>
                                </td>
                            </tr>`
            })

            $(".inquery-table").html(text)

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

showinquerysByPaged(page,search)

//하단 페이지 버튼 클릭시 이동
const pageBtnAddEvent = (pagenator)=>{
    $(".page-button").each((i,btn)=>{
    $(btn).on("click",e=>{
        page = Number($(btn).find("span").text())
        showinquerysByPaged(page,search)
    })
})
    $(".left-page-button").on("click",e=>{
        page = pagenator.start_page-1
        showinquerysByPaged(page,search)
    })
      $(".right-page-button").on("click",e=>{
        page = pagenator.end_page+1
        showinquerysByPaged(page,search)
    })
}


//게시판 선택 삭제
$(".delete-button").on("click",e=>{
    let inquery_ids = []
    $(".subCheckbox").filter((i,checkbox)=> $(checkbox).prop("checked")).each((i,checkbox)=>{
        let member_id = Number($(checkbox).closest(".checkbox-line").next().text())
        inquery_ids.push(member_id)
    })

    let datas = {
            method: "POST",
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify({
            inquery_ids
             }),
    }

    fetch("/admin/delete-inquerys/", datas)
        .then(response=>response.json())
        .then(result =>{
            if(result){
                showinquerysByPaged(page,search)
            }
        })

})


//검색
$(".search-icon").on("click",e=>{
    search = $(".admin-search-box").val()
    page = 1
    showinquerysByPaged(page,search)
})
