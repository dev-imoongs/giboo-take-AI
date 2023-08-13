// .lab_choiced가 checkbox on
$('.inp_comm').on('click', (e) => {
    $('label.lab_comm').removeClass('lab_choiced');
    $(e.target).next().addClass('lab_choiced');
})
// 힌트보기 눌렀을때 모달창 띄우기, body_hint에 나올 글 초기값 설정
$('.txt_sign').on('click', () => {
    $('#modalOFF').attr('id', 'modalON')
    $('.dimmed_layer').css('height', '100%');
    $('.dialog-content').css('display', 'block');
    $('.body_hint').hide()
    $('.body_hint').eq(1).show()
})

//  모달창 안에 들어가서 탭 눌렀을때 해당 글은 보여주고 외에는 숨기는 기능
$('.link_hint').on('click',(e)=>{
    $('.link_hint').parent().removeClass('on')
    $(e.target).parent().addClass('on')
    $('.body_hint').hide()
    $('.body_hint').eq($(e.target).parent().index()).show()
})

// 모달창 닫기 버튼
$('.btn_close').on("click", () => {
    $('#modalON').attr('id', 'modalOFF');
    $('.dimmed_layer').css('height', '0');
    $('.dialog-content').css('display', 'none');
})

$(document).ready(function () {
    function updateIDs() {
        $('.ng-scope').each((i, value) => {
            $(value).attr('id', `planBox${i}`)
        })
    }

    function updateAmount() {
        let total = 0
        $('.amount_tf').each((i, v) => {
            let inputValue = $(v).children().val()
            if(inputValue !== "")
                total += parseInt(inputValue)
        })
        // toLocaleString 나라별 금액 단위 표시 ex) 1,000
        amount = total.toLocaleString("ko-KR")
        $('.total_sum').children().text(`${amount}원`)
    }


    $(".btn_add").on('click', () => {
        $addContent = '<div class="group_tf ng-scope">\n' +
                      '  <div class="cont_tf">\n' +
                      '      <input type="text" classoutline="" placeholder="사용용도 및 산출근거"\n' +
                      '              title="모금액 사용용도 및 산출근거"\n' +
                      '              class="tf_write ng-valid ng-dirty ng-valid-parse ng-touched ng-untouched ng-pristine">\n' +
                      '  </div>\n' +
                      '  <div class="amount_tf">\n' +
                      '      <input type="number" classoutline="" numberonly="" step="500"\n' +
                      '              min="0" placeholder="금액(원)" title="모금액 산출 금액(원)"\n' +
                      '              class="tf_write ng-valid ng-valid-min ng-dirty ng-valid-number ng-touched ng-untouched ng-pristine">\n' +
                      '  </div>\n' +
                      '    <button type="button" class="btn_line_txt"> 삭제 </button>\n' +
                      '</div>'
        $($addContent).insertAfter($(".ng-scope").last());
        updateIDs();
    });

    // 위에서 동적으로 생성된 $addContent를 불러오기 위해 document를 불러옴
    $(document).on('click', (e) => {
        if ($(e.target).attr('class') == 'btn_line_txt') {
            if ($('.ng-scope').length !== 1) {
                $(e.target).parent().remove()
                updateIDs()
                updateAmount()
            } else {
                return alert('더이상 지울 수 없습니다. (모달 띄워야함)')
            }
        }
        if ($(e.target).hasClass('ico_together')){
            let $calendar1 = $('#calendar1')
            let $buttonOffsetLeft = $(e.target).offset().left
            $('.my-calendar').css('left', $buttonOffsetLeft-220+"px");
            $calendar1.show()

        }
    });

    $(document).on('keyup', (e) => {
        $txtLength = $(e.target).parent().parent().next()
        let total = 0
        if ($txtLength.attr('class') == 'info_append') {
            $txtLength.children().text(`${$(e.target).val().length}/`)
        }

        if($(e.target).parent().attr('class') == 'amount_tf'){
            updateAmount()
        }

    });



})

// 정보 입력 안하고 다음 단계 클릭시 발생 이벤트
// 1. select box에 옵션 없을 시 경고 class 추가
// 2. checked가 3개가 아니면 해당 위치에 경고 class 추가
$('.link_step').on('click', () => {
    if (!$('#checkPolicy').prop('checked')) {
        // $('.lab_comm .ico_together').addClass('ico_warn')

        $('.info_policy').parent().addClass('sign_warn')
        // alert('히히 못가')
        // return
    }

})

// 캘린더 위치 버튼 아래로 이동


// 캘린더
// ================================
// START YOUR APP HERE
// ================================
const init = {
  monList: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
  dayList: ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'],
  today: new Date(),
  monForChange: new Date().getMonth(),
  activeDate: new Date(),
  getFirstDay: (yy, mm) => new Date(yy, mm, 1),
  getLastDay: (yy, mm) => new Date(yy, mm + 1, 0),
  nextMonth: function () {
    let d = new Date();
    d.setDate(1);
    d.setMonth(++this.monForChange);
    this.activeDate = d;
    return d;
  },
  prevMonth: function () {
    let d = new Date();
    d.setDate(1);
    d.setMonth(--this.monForChange);
    this.activeDate = d;
    return d;
  },
  addZero: (num) => (num < 10) ? '0' + num : num,
  activeDTag: null,
  getIndex: function (node) {
    let index = 0;
    while (node = node.previousElementSibling) {
      index++;
    }
    return index;
  }
};

const $calBody = document.querySelector('.cal-body');
const $btnNext = document.querySelector('.btn-cal.next');
const $btnPrev = document.querySelector('.btn-cal.prev');

/**
 * @param {number} date
 * @param {number} dayIn
*/
function loadDate (date, dayIn) {
  document.querySelector('.cal-date').textContent = date;
  document.querySelector('.cal-day').textContent = init.dayList[dayIn];
}

/**
 * @param {date} fullDate
 */
function loadYYMM (fullDate) {
  let yy = fullDate.getFullYear();
  let mm = fullDate.getMonth();
  let firstDay = init.getFirstDay(yy, mm);
  let lastDay = init.getLastDay(yy, mm);
  let markToday;  // for marking today date

  if (mm === init.today.getMonth() && yy === init.today.getFullYear()) {
    markToday = init.today.getDate();
  }

  document.querySelector('.cal-month').textContent = init.monList[mm];
  document.querySelector('.cal-year').textContent = yy;

  let trtd = '';
  let startCount;
  let countDay = 0;
  for (let i = 0; i < 6; i++) {
    trtd += '<tr>';
    for (let j = 0; j < 7; j++) {
      if (i === 0 && !startCount && j === firstDay.getDay()) {
        startCount = 1;
      }
      if (!startCount) {
        trtd += '<td>'
      } else {
        let fullDate = yy + '.' + init.addZero(mm + 1) + '.' + init.addZero(countDay + 1);
        trtd += '<td class="day';
        trtd += (markToday && markToday === countDay + 1) ? ' today" ' : '"';
        trtd += ` data-date="${countDay + 1}" data-fdate="${fullDate}">`;
      }
      trtd += (startCount) ? ++countDay : '';
      if (countDay === lastDay.getDate()) {
        startCount = 0;
      }
      trtd += '</td>';
    }
    trtd += '</tr>';
  }
  $calBody.innerHTML = trtd;
}

/**
 * @param {string} val
 */
function createNewList (val) {
  let id = new Date().getTime() + '';
  let yy = init.activeDate.getFullYear();
  let mm = init.activeDate.getMonth() + 1;
  let dd = init.activeDate.getDate();
  const $target = $calBody.querySelector(`.day[data-date="${dd}"]`);

  let date = yy + '.' + init.addZero(mm) + '.' + init.addZero(dd);

  let eventData = {};
  eventData['date'] = date;
  eventData['memo'] = val;
  eventData['complete'] = false;
  eventData['id'] = id;
  init.event.push(eventData);
  $todoList.appendChild(createLi(id, val, date));
}

loadYYMM(init.today);
loadDate(init.today.getDate(), init.today.getDay());

$btnNext.addEventListener('click', () => loadYYMM(init.nextMonth()));
$btnPrev.addEventListener('click', () => loadYYMM(init.prevMonth()));

$calBody.addEventListener('click', (e) => {
  if (e.target.classList.contains('day')) {
    if (init.activeDTag) {
      init.activeDTag.classList.remove('day-active');
    }
    let day = Number(e.target.textContent);
    console.log(day)
    console.log(new Date().getMonth())
    loadDate(day, e.target.cellIndex);
    e.target.classList.add('day-active');
    init.activeDTag = e.target;
    init.activeDate.setDate(day);
    // reloadTodo();
  }
});

