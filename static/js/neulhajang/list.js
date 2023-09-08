let page = 1
const showNeulhajangList = (page) => {
        fetch(`/neulhajang/neulhajang-list-api-view/?Page=${page}`)
        .then(response => response.json())
        .then(result => {
            let addText = ""
            let posts = result.posts
            posts.forEach((post,i)=>{
                console.log(post)
                let percentage = Math.ceil(post.authentication_count/post.participants_target_amount * 100);
                if(!percentage) percentage=0
                const post_url = baseUrl.replace(0, neulhajang_id=post.id);
                addText += `<div class="card-base">
                              <div class="card-header">
                                <div class="card-thumbnail" style="background-image: url(${post.thumnail_image})"></div>
                                <div class="card-top-label" aria-hidden="true">
                                  <em type="circle" class="top-label-text">${percentage}% 달성</em>
                                </div>
                              </div>
                              <div class="card-content">
                                <h4 class="card-title" aria-hidden="true">${post.neulhajang_title}</h4>
                                <div class="card-bottom-label-container">
                                  <em type="rect" class="card-botton-label-count-text" aria-hidden="true"><i class="card-botton-label-count-text-icon"><svg class="card-botton-label-count-text-icon-svg" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 28 28"><g fill="none" fill-rule="evenodd"><path d="m15.414.566 2.934 2.933L22.5 3.5a2 2 0 0 1 2 2v4.15l2.934 2.936a2 2 0 0 1 0 2.828L24.5 18.35 24.5 22.5a2 2 0 0 1-2 2h-4.15l-2.936 2.934a2 2 0 0 1-2.828 0L9.65 24.5 5.5 24.5a2 2 0 0 1-2-2v-4.152L.565 15.414a2 2 0 0 1 0-2.828L3.499 9.65 3.5 5.5a2 2 0 0 1 2-2h4.151L12.586.565a2 2 0 0 1 2.828 0z" fill="#bb6bff"></path><path d="M18.02 9.62a1 1 0 0 1 1.677 1.082l-.068.106-6.066 8.21a1 1 0 0 1-1.443.175l-.09-.085-3.506-3.73a1 1 0 0 1 1.366-1.456l.091.086 2.685 2.857 5.354-7.246z" fill="#fff" fill-rule="nonzero"></path></g></svg></i>${post.authentication_count} 명 행동중</em>
                                  ${post.representing_tag?`<a type="tag" class="card-botton-label-link" href=""><div role="text" class="card-botton-label-link-text"># ${post.representing_tag}</div></a>`:''}
                                  
                                </div>
                                <div class="card-description" aria-hidden="true">
                                  <!-- 반응형일때 보여지는 p태그 -->
                                  <p class="mobile-card-mission-text">
                                    우리가 잊고 지내던 태극기의 소중함을 되새기며, 독립유공자
                                    후손에게 마음을 전하는 태극기 달기! 함께 행동해 볼까요?
                                  </p>
                                  <div class="card-proposer-container">
                                    <div class="card-proposer-profile" style="background-image: url('${post.member_profile_image?post.member_profile_choice == "user"?`${mediaUrl}${post.member_profile_image}`:post.member_profile_image:`${staticUrl}image/avatar.png`}')"></div>
                                    <strong class="card-proposer-name">${post.member_nickname}</strong>
                                  </div>
                                </div>
                              </div>
                              <a href="${post_url}" class="card-button-link"></a>
                            </div>`

            })
            $('.action-card-section').append(addText)
        })
}


showNeulhajangList(page)

let timeoutId
window.addEventListener("scroll", ()=>{
    clearTimeout(timeoutId)
    console.log(page)
            timeoutId = setTimeout(()=>{
         if (window.innerHeight + window.scrollY +600>= document.body.offsetHeight) {
    page++
    showNeulhajangList(page)
             }
    },100)
});