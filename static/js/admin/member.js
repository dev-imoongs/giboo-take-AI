//페이지 네이션 구현
let text;
let page=1


//포스트방식
// const dataToSend = { page };
//     const data = {
//          method: 'GET',
//             headers: {
//         'Content-Type': 'application/json',
//         'X-CSRFToken': getCookie('csrftoken')  // Django CSRF 토큰 설정
//     },
//     body: JSON.stringify(dataToSend)
//     }


const showMembersByPaged =  (page)=>{

    fetch(`/admin/get-members-by-paged/?page=${page}`)
        .then(response => response.json())
        .then(result => console.log(result))
}

showMembersByPaged(page)
