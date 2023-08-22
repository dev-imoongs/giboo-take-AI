$("#refuseButton").on("click",e=>{
    if(!$("#inputText").val()){
        $("#inputText").focus()
        alert("등록 거부 사유를 작성해주세요")
        return
    }

    $("form").submit()
})

$("#consentButton").on("click",e=>{
    if($("#inputText").val()){
         $("#inputText").focus()
        alert("등록 거부 사유가 없어야합니다.")
        return;
    }
    $("form").submit()

})

