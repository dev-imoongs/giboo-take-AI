let flag = false
$('.wrap_btns .btn_set').on('click',async (e) => {
    let inputPrice = $('input[name="amount"]').val()
    if (inputPrice < 1000) {
        toastMsg('1,000원 이하의 금액은 기부할 수 없습니다')
        return
    }

    // 현재 금액을 확인 할 수 있는 API뷰가 필요, 지금은 DetailView에서 렌더했을때 기준
       await reciveRealtimeFundAmount(inputPrice)


})

// $(document).on('click',(e)=> {
//     if($(e.target).hasClass('success-btn')) {
//         $('.fund_float').show()
//     }
// })
const reciveRealtimeFundAmount = async (inputPrice) => {
    fetch(`/neulhaerang/detail-realtime-fundamount/?neulhaerangId=${neulhaerangId}&`)
        .then(response => response.json())
        .then(async result => {
            let post = result.post
            let post_donation_sum = result.post_donation_sum
            if (post.target_amount - post_donation_sum < inputPrice) {
                toastMsg('기부 금액이 현재 남아있는 목표 금액보다 높습니다.')
                flag = true
            }else{
                 if (flag){
      return
    }
    $('.btn_close').trigger('click')
    $('.fund_float').hide()
    let donationContent = $('#tfReply').val()
    let donationAnonymous =  $('.choice_g .inp_g').prop('checked')?'비공개':'공개'

    try {
    const response = await Bootpay.requestPayment({
        "application_id": "64eafe2400c78a001cbf6896",
        "price": inputPrice,
        "order_name": "테스트결제",
        "order_id": "TEST_ORDER_ID",
    })
    switch (response.event) {
        case 'issued':
            // 가상계좌 입금 완료 처리
            break
        case 'done':
            console.log(response)
               successPayment(donationContent, inputPrice, donationAnonymous)
               $('.fund_float').show()

            break
        case 'confirm': //payload.extra.separately_confirmed = true; 일 경우 승인  전 해당 이벤트가호출됨
            console.log(response.receipt_id)
            /**
             * 1. 클라이언트 승인을 하고자 할때
             * // validationQuantityFromServer(); //예시) 재고확인과 같은 내부 로직을 처리하기 한다.
             */
            const confirmedData = await Bootpay.confirm() //결제를 승인한다
            if(confirmedData.event === 'done') {

               // page reloading location reload
            }

            /**
             * 2. 서버 승인을 하고자 할때
             * // requestServerConfirm(); //예시) 서버 승인을 할 수 있도록  API를 호출한다. 서버에서는 재고확인과 로직 검증 후 서버승인을 요청한다.
             * Bootpay.destroy(); //결제창을 닫는다.
             */
            break
    }
} catch (e) {
    // 결제 진행중 오류 발생
    // e.error_code - 부트페이 오류 코드
    // e.pg_error_code - PG 오류 코드
    // e.message - 오류 내용
    console.log(e.message)
    switch (e.event) {
        case 'cancel':
            // 사용자가 결제창을 닫을때 호출
            console.log(e.message);
            $('.fund_float').show()
            break
        case 'error':
            // 결제 승인 중 오류 발생시 호출
            console.log(e.error_code);
            $('.fund_float').show()
            break
    }
}
                flag = false
            }
        })

}

const successPayment = (donationContent, donationAmount, donationAnonymous) => {
    fetch(`/neulhaerang/detail-success-payment/?neulhaerangId=${neulhaerangId}&donationContent=${donationContent}&donationAmount=${donationAmount}&donationAnonymous=${donationAnonymous}`)
        .then(response => response.json())
        .then(result => {
            if(result){
                 location.href= `/neulhaerang/detail/${neulhaerangId}/`
            }
        })
}