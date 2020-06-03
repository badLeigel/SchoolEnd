if($.cookie("password")){
    console.log("i hava Cookie")
   // $.cookie("id",$.cookie("id"),{expires:7,path:'/'})
   // $.cookie("password",$.cookie("password"),{expires:7,path:'/'})
	$.ajax({
		url:/topLogin/,
		type:'GET',
		success:function(data){
		    console.log(data)
			$("#userName p").text(data)
			if($("#userName p").text()!=""){
                console.log($("#userName p").text())
                $("#userName").css({"height": "100px","padding-left":"39px","float": "left"})
                $("#userName p").css({"line-height":"38px","font-size":"24px","color":"#BFC0C1"})
                $("#login").hide();
            }else{
                $("#username").hide();
            }
		}
	});
}else{
    console.log("i don't have Cookie")
}





    //

$( "#choise1").click( function(){
window.location.assign("/xiaoxiong/");
} )
$("#choise2").click(function(){
window.location.assign("/myWorks/");
})
$("#choise3").click(function(){
window.location.assign("/uploadWorks/");
})
$("#login").click(function(){
window.location.assign("/login/")
})
$("#search").keydown(function(event){
    if(event.keyCode==13){
        window.location.assign("/search/")
    }
})
$('#userName p').click(function(){
    window.location.assign("/userAdmin/")
})
