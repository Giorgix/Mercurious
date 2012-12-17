require(["dojo/dom", "dojo/on", "dojo/request", "dojo/query", "dojo/domReady!"],
    function(dom, on, request, query){
        
 		edit_buttons = query(".edit").on("click", function(evt){
 			
 			evt.stopPropagation();
            evt.preventDefault();
        	
        	edit_button = evt.target;
        	result_li = edit_button.parentNode;
        	
            request.get("/bookmarks/save/",{
            	  	
            	query: {
            		ajax: "true",
            		url:   edit_button.href.replace(/.*?:\/\//g, ""),
            		timeout: 2000
            	}
            	
            }).then(
                function(response){
                    // Display the text file content
                    result_li.innerHTML = "<pre>"+response+"</pre>";
                },
                function(error){
                    // Display the error returned
                    result_li.innerHTML = "<div class=\"error\">"+error+"<div>";
                }
            );			
 			
 		});
    }
);