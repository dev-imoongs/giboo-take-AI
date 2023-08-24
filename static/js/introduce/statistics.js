//셀렉트박스
let year = (new Date()).getFullYear()
const $chatrs = $(".chartjs-render-monitor")
$("#selectedYear").on("change", e => {
    $(".select_on").text(e.target.value)
    year = e.target.value
    geChartsByYear(year)

})

let myDoughnutChart1

let myDoughnutChart2
let data1 = {
    datasets: [{
        data: new Array(10).fill(0),
        backgroundColor: [
            '#dc287c',
            '#f7d14f',
            '#7969cc',
            '#0276da',
            '#19aab6',
            '#85f869',
            '#57f3c2',
            '#2d2828',
            '#7b7e7e',
            '#d843fa',
        ],
        cutout: "40%",
        radius: "90%"
    }]
};


let data2 = {
    datasets: [{
        data: new Array(5).fill(0),
        backgroundColor: [
            '#dc287c',
            '#f7d14f',
            '#7969cc',
            '#0276da',
            '#19aab6'
        ],
        cutout: "40%",
        radius: "90%"
    }]
};

const geChartsByYear = (year) => {
    fetch(`/introduce/get-charts-by-year/?year=${year}`)
        .then(response => response.json())
        .then(result => {
            console.log(result)
            let donation_total = 0
            let all_total = 0
            if (result.donation_total_by_category_list.length == 0) {
                data1.datasets[0].data = new Array(10).fill(0)
            }

            result.donation_total_by_category_list.forEach((category, i) => {
                data1.datasets[0].data[category.category - 1] = category.donation_total_by_category
                donation_total += category.donation_total_by_category
            })

            result.participate_all.forEach((count, i) => {
                data2.datasets[0].data[i] = count
                all_total += count
            })
            if (myDoughnutChart1) {
                myDoughnutChart1.destroy()
            }

            if (myDoughnutChart2) {
                myDoughnutChart2.destroy()
            }


            myDoughnutChart1 = new Chart($chatrs.eq(0), {
                type: 'doughnut',
                data: data1,
                options: {
                    percentageInnerCutout: 100
                }
            });


            myDoughnutChart2 = new Chart($chatrs.eq(1), {
                type: 'doughnut',
                data: data2,
            });


            $(".tit_graph .num_total").each((i, text) => {
                if (i == 0) {

                    $(text).text(donation_total.toLocaleString() + "원")
                } else {

                    $(text).text(all_total.toLocaleString() + "건")
                }
            })
            $(".txt_year").text(`(${year}.01.01 ~ ${year}.12.31)`)
            let text = ""
            result.top_five_neulhaerang.forEach((neulhaerang, i) => {

                text += `<li>
                          <a class="link_thumb" href="/neulhaerang/detail/${neulhaerang.id}/"
                            ><img
                              class="img_thumb"
                              src="/upload/${neulhaerang.thumbnail_image}" /></a
                          ><span class="info_best"
                            ><span class="inner_info"
                              ><strong class="tit_best"
                                ><a class="link_best" href="/neulhaerang/detail/${neulhaerang.id}"
                                  >${neulhaerang.neulhaerang_title}</a
                                ></strong
                              ><span class="num_total"
                                >${neulhaerang.total_donation.toLocaleString()}원 <span class="txt_num">(${neulhaerang.donation_count.toLocaleString()}명)</span></span
                              ></span
                            ></span
                          >
                        </li>`
            })

            $(".list_fundbest").html(text)


        })
}

geChartsByYear(year)
// 차트 통계


window.onload = () => {
    // 카운트를 적용시킬 요소
    const $counters = $(".list_total .num_total")

    $counters.each((i, counter) => {
        counting($(counter), i)
    })
}

//숫자 올라가기
const counting = ($counter, i) => {
    let max = Number($counter.text().replace("건", "").replace("명", "").replace("개", "").replace("원", "").replace(/,/g, ""))
    let now = max


    const handle = setInterval(() => {
        let number = Number(Math.ceil(max - now)).toLocaleString("ko-KR")

        if (i == 1) {
            $counter.text(`${number}개`)
        } else if (i == 2) {
            $counter.text(`${number}원`)
        } else if (i == 3 || i == 4) {
            $counter.text(`${number}건`)
        } else if (i == 5) {
            $counter.text(`${number}명`)
        } else {
            $counter.text(`${number}`)
        }
        // 목표수치에 도달하면 정지
        if (now < 1) {
            clearInterval(handle);
        }

        // 증가되는 값이 계속하여 작아짐
        let step = now / 10;

        // 값을 적용시키면서 다음 차례에 영향을 끼침
        now -= step;

    }, 10);


}


  

