// .lab_choiced가 checkbox on

$('.inp_comm').on('click',(e)=>{
    $('label.lab_comm').removeClass('lab_choiced');
    $(e.target).next().addClass('lab_choiced');
})
