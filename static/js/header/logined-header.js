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




// 탈퇴회원 확인 모달
const deletedMemberModal = document.querySelector("#deleted-member-modal");
const deletedConfirmBtn = document.querySelector(".confirm-button");
const deletedCancelBtn = document.querySelector(".confirm-cancel-button");
function modalOn(){
  deletedMemberModal.style.display="flex";
}

function modalOff(){
  deletedMemberModal.style.display="none";
}

if (status === "NORMAL") {
    modalOff();
}else if (status === "DELETED") {
    modalOn();
}

// NORMAL로 member_status 변경
deletedConfirmBtn.addEventListener("click", e => {
    changeMemberStatus()
    modalOff();
});

// logout처리
deletedCancelBtn.addEventListener("click", e => {
   modalOff();
   $(".logout-button").trigger("click")
});

const changeMemberStatus = (status) => {
    fetch(`/member/reset/`)
}

