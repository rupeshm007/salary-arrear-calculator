function fillYear(input){

let value=input.value
let id=input.id

let year=parseInt(id.split("-")[0])

let nextYear=year+1

let months=[
year+"-10",
year+"-11",
year+"-12",
nextYear+"-01",
nextYear+"-02",
nextYear+"-03",
nextYear+"-04",
nextYear+"-05",
nextYear+"-06",
nextYear+"-07",
nextYear+"-08"
]

months.forEach(function(m){

let field=document.getElementById(m)

if(field){
field.value=value
}

})

}