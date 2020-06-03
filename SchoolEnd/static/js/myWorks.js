$("#choise1").css("background-color","#061334")
$("#choise2").css("background-color","#050c1c")
//初始化高度
var height=document.documentElement.clientHeight
$("#myContent").css("height",height)
var csrf=$("input[name=csrfmiddlewaretoken]").val()

$(document).click(function(e){
    console.log("e.click")
    if($(e.target).attr("class")=="title"){
        console.log("clicked")
        worksId=$(e.target).attr("id")
        url="/worksInfo/"+worksId+"/"
        window.location.assign(url)
    }
})