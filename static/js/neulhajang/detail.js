// 글작성 버튼
    const writeBtn = document.querySelector(".project-active-button");
    // 글작성모달
    const writeModal = document.querySelector(".action-write-modal-base");
    const writeCancelBtn = document.querySelector(".cancel-button");
    // 글작성 취소확인 모달
    const confirmModal = document.querySelector(".confirm-modal-base");
    const confirmBtn = document.querySelector(".confirm-button");
    const confirmCancelBtn = document.querySelector(".confirm-cancel-button");

    function writeModalOn() {
        writeModal.style.display="flex";
    }
    function writeModalOff() {
        writeModal.style.display="none";
    }



    function confirmModalOn(){
      confirmModal.style.display="flex";
    }

    function confirmModalOff(){
      confirmModal.style.display="none";
    }

    writeBtn.addEventListener("click", e => {
        writeModalOn();
    });

    writeCancelBtn.addEventListener("click", e => {
        confirmModalOn();
    });

    confirmBtn.addEventListener("click", e => {
       confirmModalOff();
       writeModalOff();
    });

    confirmCancelBtn.addEventListener("click", e => {
       confirmModalOff()
    });
let page = 1