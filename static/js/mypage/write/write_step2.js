// .lab_choiced가 checkbox on
$('.inp_comm').on('click',(e)=>{
    $('label.lab_comm').removeClass('lab_choiced');
    $(e.target).next().addClass('lab_choiced');
})

$('.txt_sign').on('click',()=>{
        $('#modalOFF').attr('id','modalON')
        $('.dimmed_layer').css('height','100%');
        $('.dialog-content').css('display','block');
})