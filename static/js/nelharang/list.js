let text
let page = 1

const showNeulhaerang =  (page)=>{

    fetch(`/neulhaerang/list-api-view/?page=${page}`)
        // .then(response => response.json())
        .then(result => console.log(result))
}

showNeulhaerang(page)


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