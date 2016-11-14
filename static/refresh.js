function refreshFeed(id){
	console.log("kkk");
    	console.log(id);
    	//await.sleep(5000);
       $.post("/", {id:id}, function(result){ 
       	var response = jQuery.parseJSON(result);


        
        $(response).each(function(i,val){

          console.log("tweet:" + val.tweet); 
          console.log($("#list .panel-heading").val());
          console.log("<li class=list-group-item>"+val.tweet+"</li>"); 
          //$("").append(val.tweet);
          $("ul.tab.list-group").prepend("<li class=list-group-item>"+val.tweet+"</li>");
           id = id+1; 
		});
		  
	});
    window.setTimeout(function() { refreshFeed(id) }, 50000)
}

$(document).ready(function(){
	 var id=0;
	refreshFeed(id);
   
    
});