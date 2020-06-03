$(document).click(function(e){
    if($(e.target).attr("class")=="contentView"){
        worksId=$(e.target).attr("id")
        url="/worksInfo/"+worksId+"/"
        window.location.assign(url)
    }
})


