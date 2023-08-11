

// 차트 통계
const $chatrs =$(".chartjs-render-monitor")
let data1 = {
    datasets: [{
        data: [10, 20, 30],
        backgroundColor: [
            '#dc287c',
            '#f7d14f',
            '#7969cc',
        ],
        cutout: "40%",
        radius:"90%"
    }]
};  


let data2 = {
    datasets: [{
        data: [101241, 50123, 10000,123145,12325],
        backgroundColor: [
            '#dc287c',
            '#f7d14f',
            '#7969cc',
            '#0276da',
            '#19aab6'
        ],
        cutout: "40%",
        radius:"90%"
    }]
};  



let myDoughnutChart1 = new Chart($chatrs.eq(0), {
    type: 'doughnut',
    data: data1,
    options: {
        percentageInnerCutout: 100
     }
});




let myDoughnutChart2 = new Chart($chatrs.eq(1), {
    type: 'doughnut',
    data: data2,
});


window.onload = () => {
    // 카운트를 적용시킬 요소
    const $counters = $(".list_total .num_total")
    
    $counters.each((i,counter)=>{
        counting($(counter),i)
    })
  }

//숫자 올라가기
const counting = ($counter,i) => {
    let max = Number($counter.text().replace("건","").replace("시간","").replace("개","").replace("원","").replace(/,/g,""))
    let now = max

    
    const handle = setInterval(() => {
        let number = Number(Math.ceil(max - now)).toLocaleString("ko-KR")
       
        if(i==1){
            $counter.text(`${number}개`)
        }else if(i==2){
            $counter.text(`${number}원`)
        }else if(i==3||i==4){
            $counter.text(`${number}건`)
        }else if(i==5){
            $counter.text(`${number}시간`)
        }else{
            $counter.text(`${number}`)
        }
        // 목표수치에 도달하면 정지
        if ( now < 1) {
            clearInterval(handle);
        }
        
        // 증가되는 값이 계속하여 작아짐
        let step = now / 10;
        
        // 값을 적용시키면서 다음 차례에 영향을 끼침
        now -= step;
               
    }, 10);
 
    
  
    
  }
  
