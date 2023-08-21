// 게시물, 댓글 삭제 버튼 클릭 시 모달창 띄우기
$('.btn-delete').each((i, value) => {
        $(value).on("click", (e) => {
                $('#modalOFF').attr('id', 'modalON')
                $('.dimmed_layer').css('height', '100%');
                $('.dialog-content').css('display', 'block');
                $('.modal-delete').css('display', 'block');
                $('.modal-badge').css('display', 'none');
                $targetName = e.target.parentElement.className;
                if ($targetName == "info-append") {
                    console.log($targetName)
                    $('.txt-desc').html('댓글 삭제시 복구가 불가능합니다.<br>정말 삭제하시겠습니까?')
                } else {
                    console.log($targetName)
                    $('.txt-desc').html('행동 삭제시 복구가 불가능합니다.<br>정말 삭제하시겠습니까?')
                }
            }
        )
    }
)
//  취소 버튼 클릭 시 모달창 사라짐
$('.btn-type2').on("click", () => {
    $('#modalON').attr('id', 'modalOFF');
    $('.dimmed_layer').css('height', '0');
    $('.dialog-content').css('display', 'none');
})

// 뱃지 클릭시 모달 창 띄우기
$('.link-badge').each((i, value) => {
        $(value).on("click", () => {
                $('#modalOFF').attr('id', 'modalON')
                $('.dimmed_layer').css('height', '100%');
                $('.dialog-content').css('display', 'block');
                $('.modal-badge').css('display', 'block');
                $('.modal-delete').css('display', 'none');
            }
        )
    }
)
// X버튼 클릭 시 모달창 닫기
$('.btn-close').on("click", () => {
    $('#modalON').attr('id', 'modalOFF');
    $('.dimmed_layer').css('height', '0');
    $('.dialog-content').css('display', 'none');
})

// 비공개 버튼 클릭시 기부내역 비공개 공개로 하면 저장된 값을 불러와야함


let firstPageFlag = false
$('.btn-release').on("click", () => {
    if (firstPageFlag) return


    fetch('/mypage/change-member-donation-status/').then(response =>{


        if ($('.btn-release').text() == '공개') {
        $('.btn-release').text('비공개')
        toastMsg('기부내역을 비공개 합니다.')
    }else{
        $totalDonation = $('.num-total').text()
        $('.btn-release').text('공개')
        toastMsg('기부내역을 공개 합니다.')
        }
    })

})

// 비공개 - 공개

const toastMsg = function (text) {
    if (!firstPageFlag) {
        $('.toast-bottom-center').show()
        firstPageFlag = true
        $('.toast-message').eq(0).text(text)
        setTimeout(function () {
            firstPageFlag = false
            $('.toast-bottom-center').hide()
        }, 1000)
    }
}


// ~분전 관련 스크립트
document.addEventListener("DOMContentLoaded", function () {
    // 모든 .txt-time 요소를 찾음
    let timeElements = document.querySelectorAll(".txt-time");

    // 각 요소에 대해 시간을 계산하여 텍스트로 표시
    timeElements.forEach(function (element) {
        let timestamp = element.getAttribute("data-timestamp");
        let currentTime = Math.floor(Date.now() / 1000); // 현재 시간(초)을 가져옴
        let timeDifference = currentTime - timestamp;

        let timeText;
        if (timeDifference < 60) {
            timeText = timeDifference + "초 전";
        } else if (timeDifference < 3600) {
            let minutes = Math.floor(timeDifference / 60);
            timeText = minutes + "분 전";
        } else if (timeDifference < 86400) {
            let hours = Math.floor(timeDifference / 3600);
            timeText = hours + "시간 전";
        } else if (timeDifference < 2592000) {  // 30일 이하
            let days = Math.floor(timeDifference / 86400);
            if (days == 1) {
                timeText = "어제";
            } else {
                timeText = days + "일 전";
            }
        } else if (timeDifference < 7776000) {  // 3달 이하 (90일 * 24시간 * 60분 * 60초)
            let months = Math.floor(timeDifference / 2592000);
            if (months == 1) {
                timeText = "한 달 전";
            } else if (months == 2) {
                timeText = "두 달 전";
            } else if (months == 3) {
                timeText = "세 달 전";
            } else {
                timeText = element.getAttribute("data-timestamp");
            }
        } else {
            let date = new Date(timestamp * 1000);
            timeText = date.getFullYear() + "." + (date.getMonth() + 1) + "." + date.getDate();
        }

        // 텍스트를 업데이트
        element.textContent = timeText;
    });
});
