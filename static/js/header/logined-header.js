//더보기 버튼
const $moreMenu= $(".more-menu-list")
const $moreBtn = $(".more")

$moreBtn.on("click",e=>{
    $moreMenu.toggle()
})
//프로필 버튼
const $userBtn =$(".pc-user-button")
$userBtn.on("click",e=>{
    $(".pc-user-sub-menu").toggle()
})



//미디어 도시락 버튼 클릭
const $mobileMenuBtn = $(".mobile-menu-button")
const $mobileSideBar = $(".side-menu-drawer")

$mobileMenuBtn.on("click",e=>{
     $mobileSideBar.addClass("open")
})

const $mobileSideBarCloseBtn = $(".side-menu-close-button")
$mobileSideBarCloseBtn.on("click",e=>{
    $mobileSideBar.removeClass("open")
})


