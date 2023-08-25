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


$(document).ready(()=> {
    showTag();
    showCategory();
})


const showTag = () => {
    fetch(`/search/tag/`)
        .then(response => response.json())
        .then(result => {
            let tags = result.tags;
            let text = "";

            tags.forEach((tag, i) => {
                let name = tag.tag_name;  // 'tag_name'을 직접 가져옴
                let type = tag.tag_type;  // 'tag_type'을 직접 가져옴

                text += `<tag-card><a class="link_hash hash_type${type}">#${name}</a></tag-card>`;
            })
            $('.hash_group').html(text);
        });
};


const showCategory = () => {
    fetch(`/search/category/`)
        .then(response => response.json())
        .then(result => {
            let categories = result.categories
            let text = "";

            categories.forEach((category, i) => {
                let name = category.category_name;

                text += `
                    <li>
                      <a class="link_category">
                        <img class="img_thumb" src="https://mud-kage.kakaocdn.net/dn/eE4eDt/btqeTEvo1oi/i3hCyjx9BasmNFN6Qnewz0/c160.jpg"/>
                        ${name}
                      </a>
                    </li>`
            })
            $(".list_category").html(text)
        })

}