//제목,본문 정렬 시작하자마자 첫번째꺼 선택
$(".box_sorting .inp_sort").eq(0).prop("checked",true)


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


//셀렉트 박스 클릭
const $selectBox = $("#opKinds")
const $selectSpan = $(".select_on")

$selectBox.on("change",e=>{
    $selectSpan.text($("#opKinds option:selected").text())
})