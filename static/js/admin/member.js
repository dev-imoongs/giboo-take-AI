//페이지 네이션 구현
let page=1
const showMembersByPaged =  (page)=>{

    fetch(`/admin/get-members-by-paged/?page=${page}`)
        .then(response => response.json())
        .then(result =>{
            console.log(result)
            let text=''
            let pageText=''
           let members= result.members
           let pagenator= result.pagenator
            text+=`   <thead>
                            <tr>
                                <th class="checkbox-line">
                                    <input type="checkbox" id="selectAll">
                                </th>
                                <th>No</th>
                                <th>이메일</th>
                                <th style="font-weight: bold">닉네임</th>
                                <th>가입날짜</th>
                                <th>상태</th>
                            </tr>
                            </thead>`
            members.forEach((member,i)=>{
                text+=`<tr>
                                <td class="checkbox-line">
                                    <input class="subCheckbox" type="checkbox" name="check">
                                </td>
                                <td class="noticeId">
                                    ${member.id}
                                </td>
                                <td>${member.member_email}</td>
                                <td>
                                   ${member.member_nickname}
                                </td>
                                <td>
                                    ${member.created_date}
                                </td>
                                <td class="color-icon">
                                    <span class="icon-wrap">
                                        <img class="green" src="${staticUrl}image/admin/${ member.member_status =="NORMAL"?'check':'x-icon'}.png">
                                    </span>
                                </td>
                            </tr>`
            })

            $(".member-table").html(text)

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

showMembersByPaged(page)

//하단 페이지 버튼 클릭시 이동
const pageBtnAddEvent = (pagenator)=>{
    $(".page-button").each((i,btn)=>{
    $(btn).on("click",e=>{
        page = Number($(btn).find("span").text())
        showMembersByPaged(page)
    })
})
    $(".left-page-button").on("click",e=>{
        page = pagenator.start_page-1
        showMembersByPaged(page)
    })
      $(".right-page-button").on("click",e=>{
        page = pagenator.end_page+1
        showMembersByPaged(page)
    })
}


//회원 선택 삭제
$(".delete-button").on("click",e=>{
    let member_ids = []
    $(".subCheckbox").filter((i,checkbox)=> $(checkbox).prop("checked")).each((i,checkbox)=>{
        let member_id = Number($(checkbox).closest(".checkbox-line").next().text())
        member_ids.push(member_id)
    })

    let datas = {
            method: "POST",
            headers: {
            "Content-Type": "application/json",
            },
            body: JSON.stringify({
            member_ids
             }),
    }

    fetch("/admin/change-member-status/", datas)
        .then(response=>response.json())
        .then(result =>{
            if(result){
                showMembersByPaged(page)
            }
        })

})
