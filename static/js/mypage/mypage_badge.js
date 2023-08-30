// 삭제 버튼 클릭 시 모달창 띄우기

//  취소 버튼 클릭 시 모달창 사라짐
$('.btn-close').on("click", () =>{
        $('#modalON').attr('id','modalOFF');
        $('.dimmed_layer').css('height','0');
        $('.dialog-content').css('display','none');
        })

$('.link-badge').each((i, value) => {
        $(value).on("click", () => {
                fetch(`/mypage/get-badge-info/?badge_id=${$(value).attr('id')}`)
                    .then(response=> response.json())
                    .then(result =>{
                        console.log(result)
                        badge = result.badge
                        $(".modal-badge .thumb-badge").attr("src",`${staticUrl+badge.badge_image}`)
                        $(".modal-badge .name-badge").text(`${badge.badge_name}`)
                        $(".modal-badge .txt-badge").text(`${badge.badge_content}`)
                        $(".modal-badge .link-look").text(`#${badge.category_name}봉사 둘러보기`)

                        // $(".modal-badge .link-look").attr('href','')



                         $('#modalOFF').attr('id', 'modalON')
                        $('.dimmed_layer').css('height', '100%');
                        $('.dialog-content').css('display', 'block');
                        $('.modal-badge').css('display', 'block');
                        $('.modal-delete').css('display', 'none');
                    })


            }
        )
    }
)