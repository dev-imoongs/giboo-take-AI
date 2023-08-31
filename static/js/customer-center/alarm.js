

let page = 1
const getAlarmsByPaged = (page)=>{
    fetch(`/customer_center/get-alarms-by-paged/?page=${page}`)
        .then(response => response.json())
        .then(result =>{
            let alarms = result.alarms_paged
            let pagenator =result.pagenator
            let text = ""

            alarms.forEach((alarm,i)=>{
                let type =""
                if(alarm.type =="inquery"){
                    type="질문"
                }else if(alarm.type =="neulhaerang"){
                    type="늘해랑"
                }else if(alarm.type =="neulhajang"){
                    type="늘하장"
                }else if(alarm.type=="review"){
                    type="늘해랑 리뷰"
                }

                text+=` <li>
                    <a  ${alarm.type =="inquery"? '' : alarm.type=="review" ?`href='/${alarm.type}/review/detail/${alarm.reference_id}'` :`href='/${alarm.type}/detail/${alarm.reference_id}'`}
                            class="link_inform"
                    ><span class="thumb_inform"
                    ><span class="ico_together ico_declare"></span
                    ></span
                    ><span class="cont_inform"
                    ><strong class="tit_inform emph_sign">${alarm.type=="inquery"?'답변은 메일로 확인하세요!' : `${type} 바로가기`}</strong
                    ><span class="txt_inform" style=" white-space: pre-line;"
                    >${alarm.message}</span
                    ><span class="date_inform" style="position: relative">${alarm.created_date.split(".")[0].replace("T","-")}${alarm.isChecked ? '':
                    '<span class="pc-new-badge alarm">1</span>'}</span></span
                    ></a
                    >
                  </li>`
            })
            console.log(result)

            $(".list_inform").append(text)

            if(pagenator.has_next_data){
                $(".wrap_inform .btn_more").show()
            }else{
                 $(".wrap_inform .btn_more").hide()
            }
            if($(".list_inform li").length!=0){
                $(".desc_auto span").text("60일이 지난 알림은 자동 삭제 됩니다.")
                $(".wrap_inform .btn_delete_all").show()
            }

            fetch(`/customer_center/change-alarm-ischecked/?page=${page}`)



        })
}

getAlarmsByPaged(page)

$(".wrap_inform .btn_more").on("click",e=>{
    page++
    getAlarmsByPaged(page)
})

$(".wrap_inform .btn_delete_all").on("click",e=>{
    fetch("/customer_center/delete-all-alarm/")
        .then(response=>response.json())
        .then(result =>{
            if(result){
                location.href = "/customer_center/alarm/"
            }
        })
})
