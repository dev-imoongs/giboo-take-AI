const getNeulhaerangByPaged = () => {
    fetch(`/main/get-neulhaerangs-by-paged/`)
        .then(response => response.json())
        .then(result => {
            console.log(result)
            let text1 = ''
            let text2 = ''

            result.neulhaerangs.forEach((neulhaerang, i) => {
                if (i <= 2) {
                    text1 += `<div class="neulhearang-funding-card">
    <a href="/neulhaerang/detail/${neulhaerang.id}" class="neulhearang-funding-card-link">
        <div src=${mediaUrl+neulhaerang.thumbnail_image}
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
        <div src=${mediaUrl+neulhaerang.thumbnail_image}
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


