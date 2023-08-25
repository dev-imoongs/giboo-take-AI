
const getAlarmsByPaged = (page)=>{
    fetch(`/get-alarms-by-paged/?page=${page}`)
        .then(response => response.json())
        .then(result =>{
            console.log(result)
        })
}