//검색 삭제 버튼
const $searchDeleteBtn = $(".group_schkeyword .btn_delete")
const $searchInput = $("#schKeyword")
$searchDeleteBtn.on("click",e=>{
    $searchInput.val("")
    $searchDeleteBtn.hide()
})


$searchInput.on("input",e=>{
    if($searchInput.val()){
        $searchDeleteBtn.show()
    }else{
        $searchDeleteBtn.hide()
    }
})


// 태그버튼들
const $hashtags = $(".link_hash")
$(document).ready(function() {
    showTag();
    showCategory();
});

// 태그검색
const showTag = () => {
    fetch(`/search/tag/`)
        .then(response => response.json())
        .then(result => {
            let tags = result.tags;
            let text = "";

            tags.forEach((tag, i) => {
                let name = tag.tag_name;  // 'tag_name'을 직접 가져옴
                let type = tag.tag_type;  // 'tag_type'을 직접 가져옴
                text += `<tag-card><a href="/search/tag/result/${name}/${type}/" class="link_hash hash_type${type}">#${name}</a></tag-card>`;
            })
            $('.hash_group').html(text);
        });
};

// 카테고리 검색
const showCategory = () => {
    fetch(`/search/category/`)
        .then(response => response.json())
        .then(result => {
            let categories = result.categories
            let text = "";

            categories.forEach((category, i) => {
                let name = category.category_name;
                let image = category.category_image;

                text += `
                    <li>
                      <a href="/search/category/result/${name}/" class="link_category">
                        <img class="img_thumb" src="${image}"/>
                        ${name}
                      </a>
                    </li>`
            })
            $(".list_category").html(text)
        })

}



