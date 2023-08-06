//카테고리 클릭
  $(".list-cate li").each((i,cate)=>{
    $(cate).on("click",e=>{
      $(".list-cate li").each((idx,category)=>{
        if(i==idx){
          $(category).addClass("on")
        }else{
          $(category).removeClass("on")
        }
      })
    })
  })

  //정렬 클릭
  $(".box_sorting").each((i,cate)=>{
    $(cate).on("click",e=>{
      $(".box_sorting").each((idx,category)=>{
        if(i==idx){
          $(category).addClass("sort_on")
        }else{
          $(category).removeClass("sort_on")
        }
      })
    })
  })