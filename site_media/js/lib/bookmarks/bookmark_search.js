require(["dojo/dom", "dojo/on", "dojo/request", "dojo/domReady!"],
    function(dom, on, request){
        // Results will be displayed in resultDiv
        var resultDiv = dom.byId("search-results");
 
        // Attach the onclick event handler to the textButton
        on(dom.byId("search-button"), "click", function(evt){
        	// prevent the page from navigating after submit
            evt.stopPropagation();
            evt.preventDefault();
            request.get("/bookmarks/search/",{
            	  	
            	query: {
            		ajax: "true",
            		query: dom.byId("id_query").value,
            		timeout: 2000
            	}
            	
            }).then(
                function(response){
                    // Display the text file content
                    resultDiv.innerHTML = "<pre>"+response+"</pre>";
                },
                function(error){
                    // Display the error returned
                    resultDiv.innerHTML = "<div class=\"error\">"+error+"<div>";
                }
            );
        });
    }
);