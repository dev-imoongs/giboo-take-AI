
let count = 0
let reviewCount =0
const getNeulhaerangByPaged = () => {
    fetch(`/main/get-neulhaerangs-by-paged/`)
        .then(response => response.json())
        .then(result => {

            let text1 = ''
            let text2 = ''

            result.neulhaerangs.forEach((neulhaerang, i) => {
                if (i <= 2) {
                    text1 += `<div class="neulhearang-funding-card">
    <a href="/neulhaerang/detail/${neulhaerang.id}" class="neulhearang-funding-card-link">
        <div style="background: url('${mediaUrl+neulhaerang.thumbnail_image}') 50% 50% / cover no-repeat"
             class="neulhearang-funding-card-thumbnail first"></div>
        <div class="neulhearang-funding-card-content">
            <strong class="neulhearang-funding-card-title">${neulhaerang.neulhaerang_title}</strong>
            <span class="neulhearang-funding-card-subtext">${result.inner_contents[i]}....</span>
            <em type="tag" class="neulhearang-funding-card-tag">
                <div role="text" class="neulhearang-funding-card-tag-text"># ${result.tags[i]}</div>
            </em>
            <em type="rect" class="neulhearang-funding-card-label"><i
                class="neulhearang-funding-card-label-icon"></i>${neulhaerang.donation_sum?neulhaerang.donation_sum.toLocaleString():0}원 모금중</em>
        </div>
    </a>
</div>`
                } else {
                    text2 += `<div class="neulhearang-funding-card">
    <a href="/neulhaerang/detail/${neulhaerang.id}" class="neulhearang-funding-card-link">
        <div style="background: url('${mediaUrl+neulhaerang.thumbnail_image}') 50% 50% / cover no-repeat"
             class="neulhearang-funding-card-thumbnail first"></div>
        <div class="neulhearang-funding-card-content">
            <strong class="neulhearang-funding-card-title">${neulhaerang.neulhaerang_title}</strong>
            <span class="neulhearang-funding-card-subtext">${result.inner_contents[i]}....</span>
            <em type="tag" class="neulhearang-funding-card-tag">
                <div role="text" class="neulhearang-funding-card-tag-text"># ${result.tags[i]}</div>
            </em>
            <em type="rect" class="neulhearang-funding-card-label"><i
                class="neulhearang-funding-card-label-icon"></i>${neulhaerang.donation_sum?neulhaerang.donation_sum.toLocaleString():0}원 모금중</em>
        </div>
    </a>
</div>`
                }
            })


            $(".neulhearang-card-group").each((i,card)=>{
                $(card).append(i==0?text1:text2)
            })

        })
}

getNeulhaerangByPaged()

const getNeulhajangSlide = ()=>{
    fetch("/main/get-neulhajang-slider/")
        .then(response => response.json())
        .then(result =>{
            let text=``
            let text1=''
                // console.log(result)
            result.neulhajangs.forEach((neulhajang,i)=>{
                text+=`<div class="slide">
                                <div class="slide-card-wrap">
                                    <a href="/neulhajang/detail/${neulhajang.id}" class="slide-card-link">
                                        <div style="background: url('${mediaUrl+neulhajang.thumnail_image}') 50% 50% / cover no-repeat" class="card-thumbnail"></div>
                                        <div class="card-content">
                                            <strong class="card-title">${neulhajang.neulhajang_title}</strong>
                                            <span class="card-subtext">${result.inner_contents[i]}</span>
                                            <em class="card-tag"><div class="card-tag-text"># ${neulhajang.representing_tag}</div></em>
                                            <em type="rect" class="card-label"><svg class="card-label-icon" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 28 28"><g fill="none" fill-rule="evenodd"><path d="m15.414.566 2.934 2.933L22.5 3.5a2 2 0 0 1 2 2v4.15l2.934 2.936a2 2 0 0 1 0 2.828L24.5 18.35 24.5 22.5a2 2 0 0 1-2 2h-4.15l-2.936 2.934a2 2 0 0 1-2.828 0L9.65 24.5 5.5 24.5a2 2 0 0 1-2-2v-4.152L.565 15.414a2 2 0 0 1 0-2.828L3.499 9.65 3.5 5.5a2 2 0 0 1 2-2h4.151L12.586.565a2 2 0 0 1 2.828 0z" fill="#ad4cfe"></path><path d="M18.02 9.62a1 1 0 0 1 1.677 1.082l-.068.106-6.066 8.21a1 1 0 0 1-1.443.175l-.09-.085-3.506-3.73a1 1 0 0 1 1.366-1.456l.091.086 2.685 2.857 5.354-7.246z" fill="#fff" fill-rule="nonzero"></path></g></svg>${neulhajang.feed_sum.toLocaleString()}명 행동중</em>
                                        </div>
                                    </a>
                                </div>
                            </div>`
                if(i==0){
                    text1+=`<div class="slide">
                                <div class="slide-card-wrap">
                                    <a href="/neulhajang/detail/${neulhajang.id}" class="slide-card-link">
                                        <div style="background:  url('${mediaUrl+neulhajang.thumnail_image}') 50% 50% / cover no-repeat" class="card-thumbnail"></div>
                                        <div class="card-content">
                                            <strong class="card-title">${neulhajang.neulhajang_title}</strong>
                                            <span class="card-subtext">${result.inner_contents[i]}</span>
                                            <em class="card-tag"><div class="card-tag-text"># ${neulhajang.representing_tag}</div></em>
                                            <em type="rect" class="card-label"><svg class="card-label-icon" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 28 28"><g fill="none" fill-rule="evenodd"><path d="m15.414.566 2.934 2.933L22.5 3.5a2 2 0 0 1 2 2v4.15l2.934 2.936a2 2 0 0 1 0 2.828L24.5 18.35 24.5 22.5a2 2 0 0 1-2 2h-4.15l-2.936 2.934a2 2 0 0 1-2.828 0L9.65 24.5 5.5 24.5a2 2 0 0 1-2-2v-4.152L.565 15.414a2 2 0 0 1 0-2.828L3.499 9.65 3.5 5.5a2 2 0 0 1 2-2h4.151L12.586.565a2 2 0 0 1 2.828 0z" fill="#ad4cfe"></path><path d="M18.02 9.62a1 1 0 0 1 1.677 1.082l-.068.106-6.066 8.21a1 1 0 0 1-1.443.175l-.09-.085-3.506-3.73a1 1 0 0 1 1.366-1.456l.091.086 2.685 2.857 5.354-7.246z" fill="#fff" fill-rule="nonzero"></path></g></svg>${neulhajang.feed_sum.toLocaleString()}명 행동중</em>
                                        </div>
                                    </a>
                                </div>
                            </div>`
                }
            })

            $(".slider-list").append(text+text1)
            $(".slider-list").css("width",`${$(".slide").length}00%`)

            let slide_text = ''

                for(let i = 0;i<result.neulhajangs.length;i++){
                    slide_text+=` <li>
                                    <button type="button" class="paging-button"></button>
                                </li>`
                }

                // console.log(slide_text)
            $(".neulhajang-slide").append(slide_text)
            $(".neulhajang-slide li").eq(0).addClass("active")


            let inter_id = setInterval(autoslide,5000)
            $(".neulhajang-slide li").each((i,li)=>{
                $(li).on("click",e=>{
                    clearInterval(inter_id)
                    $(".neulhajang-slide li").each((i2,li2)=>{
                        if(i==i2){
                            $(li2).addClass("active")
                        }else{
                            $(li2).removeClass("active")
                        }
                    })
                    $(".slider-list").css('transition-duration','500ms')
                     $(".slider-list").css('transform',`translate3d(-${(100 / $(".slider-list div.slide").length) * i}%, 0px, 0px)`)
                    count = i
                    inter_id = setInterval(autoslide,5000)

                })
            })


        })
}
getNeulhajangSlide()

const autoslide = ()=>{
    let slides = $(".slider-list div.slide")
    let length = slides.length
    count++
    let transformValue = `translate3d(-${(100 / length) * count}%, 0px, 0px)`
    if(count==length-1){
        $(".slider-list").css('transform',transformValue)
        setTimeout(()=>{
            $(".slider-list").css('transition-duration','')
            $(".slider-list").css('transform',`translate3d(0%, 0px, 0px)`)

        },500)
         count= 0
    }else{
        $(".slider-list").css('transition-duration','500ms')
         $(".slider-list").css('transform',transformValue)
    }
    $(".neulhajang-slide li").each((i,slide)=>{
        if(i==count){
            $(slide).addClass("active")
        }else{
             $(slide).removeClass("active")
        }
    })


}


const getTagNeulhaerangs = ()=>{
    fetch("/main/get-tag-neulhaerangs")
        .then(response => response.json())
        .then(result=>{
            // console.log(result)
            let text =''
            result.random_tags.forEach((tag,i)=>{
                text+=`<button id="totalTab${i+1}" class="tab-button ${i==0?'active':''}"># ${tag.tag_name}</button>`
            })
            $(".tag-tab-list").append(text)

            $(".tag-tab-list .tab-button").each((i,btn)=>{
                $(btn).on("click",e=>{
                    showTagNeulhaerangs($(btn).text().replace("# ",""),btn)




                })
            })
            $(".tag-tab-list .tab-button").eq(0).trigger("click")

        })
}
getTagNeulhaerangs()


const showTagNeulhaerangs = (tag,btn)=>{
    fetch(`/main/get-click-tag-neulhaerangs/?tag=${tag}`)
        .then(response => response.json())
        .then(result =>{
            // console.log(result)
            let text =''

            result.random_neulhaerangs.forEach((neulhaerang,i)=>{
                text+=` <div class="tab-panel-content-card ${i!=0?'space':''}">
                        <a href="/neulhaerang/detail/${neulhaerang.id}" class="tab-panel-content-card-link">
                            <div class="tab-panel-content-card-thumbnail thumbnail1" style="background: url('${mediaUrl+neulhaerang.thumbnail_image}') 50% 50% / cover no-repeat"></div>
                            <div class="tab-panel-content-card-text-wrap">
                                <strong class="tab-panel-content-card-title">${neulhaerang.neulhaerang_title}</strong>
                                <em class="tab-panel-content-card-label">${neulhaerang.donation_sum?neulhaerang.donation_sum.toLocaleString():0}원 모금중</em>
                            </div>
                        </a>
                    </div>`

            })
            $(".tab-panel").html(text)
              $(".tag-tab-list .tab-button").removeClass("active")
            $(btn).addClass("active")
        })
}


const getReviewSlide = ()=>{
    fetch("/main/get-review-slide")
        .then(response=>response.json())
        .then(result=>{
            let text=''
            let text1 =''
            // console.log(result)
            result.reviews.forEach((review,i)=>{
                text+=`<div class="neulhearang-review-slide">
                                        <a href="/neulhaerang_review/review/detail/${review.id}" class="neulhearang-review-slide-link">
                                            <div class="neulhearang-review-slide-content">
                                                <strong class="neulhearang-review-slide-title">${review.review_title}</strong>
                                                <p class="neulhearang-review-slide-description">${result.innercontents[i]}</p>
                                            </div>
                                        </a>
                                    </div>`
                if(i==0){
                    text1+=text
                }
            })


            $(".neulhearang-review-slider-list").append(text+text1)
            $(".neulhearang-review-slider-list").css("width",`${$(".neulhearang-review-slide").length}00%`)

            let slide_text = ''

                for(let i = 0;i<result.reviews.length;i++){
                    slide_text+=` <li>
                                            <button type="button" class="neulhearang-review-paging-button"></button>
                                        </li>`
                }

            $(".neulhearang-review-paging-button-list").append(slide_text)
            $(".neulhearang-review-paging-button-list li").eq(0).addClass("active")


            let review_inter_id = setInterval(reviewAutoslide,5000)
            $(".neulhearang-review-paging-button-list li").each((i,li)=>{
                $(li).on("click",e=>{
                    clearInterval(review_inter_id)
                    $(".neulhearang-review-paging-button-list li").each((i2,li2)=>{
                        if(i==i2){
                            $(li2).addClass("active")
                        }else{
                            $(li2).removeClass("active")
                        }
                    })

                    $(".neulhearang-review-slider-list").css('transition-duration','500ms')
                     $(".neulhearang-review-slider-list").css('transform',`translate3d(-${(100 / $(".neulhearang-review-slide").length) * i}%, 0px, 0px)`)
                    reviewCount = i
                    review_inter_id = setInterval(reviewAutoslide,5000)

                })
            })





        })
}

getReviewSlide()
const reviewAutoslide = ()=>{
    let slides = $(".neulhearang-review-slide")
    let length = slides.length
    reviewCount++
    let transformValue = `translate3d(-${(100 / length) * reviewCount}%, 0px, 0px)`
    if(reviewCount==length-1){
        $(".neulhearang-review-slider-list").css('transform',transformValue)
        setTimeout(()=>{
            $(".neulhearang-review-slider-list").css('transition-duration','')
            $(".neulhearang-review-slider-list").css('transform',`translate3d(0%, 0px, 0px)`)

        },500)
         reviewCount= 0
    }else{
        $(".neulhearang-review-slider-list").css('transition-duration','500ms')
         $(".neulhearang-review-slider-list").css('transform',transformValue)
    }
    $(".neulhearang-review-paging-button-list li").each((i,slide)=>{
        if(i==reviewCount){
            $(slide).addClass("active")
        }else{
             $(slide).removeClass("active")
        }
    })


}




$(".aside-rectangle-banner-link").on("click",e=>{
    e.preventDefault()
    let tag_name = $(".aside-rectangle-banner-subtext").text().split(" ")[0].replace("#","")
    fetch(`/main/get-random-tag-one-neulhaerang/?tag=${tag_name}`)
        .then(response=>response.json())
        .then(result=>{
            if(result){
                location.href = `/neulhaerang/detail/${result}`
            }else{

            }
        })

})



const showDonationRanking = ()=>{
    fetch("/main/get-member-ranking")
        .then(response => response.json())
        .then(result =>{
            // console.log(result)
            let text=''
            result.members.forEach((member,i)=>{
                text+=`<li class="aside-list-item">
                        <a href="/myapge/otherslink/${member.id}" class="aside-list-item-link top-link">`

                    if(member.profile_image){
                        if(member.profile_image_choice =="kakao"){
                             text+=`<div style="background: url('${member.profile_image}') 50% 50% / cover no-repeat" `
                        }else{
                            text+=`<div style="background: url('${mediaUrl+member.profile_image}') 50% 50% / cover no-repeat" `
                        }
                    }else{
                        text+=`<div style="background: url('${staticUrl}image/avatar.png') 50% 50% / cover no-repeat" `
                    }

                    text+=`class="aside-list-item-thumbnail aside-thumbnail1"></div>
                            <div class="aside-list-content-container">
                                <strong class="aside-list-content-title title-text">${member.member_nickname}</strong>
                                <p class="aside-list-content-subtext">${member.donation_sum.toLocaleString()}원 기부</p>
                            </div>
                        </a>
                    </li>`
            })

            $(".aside-list").append(text)
        })
}
showDonationRanking()

