	function loadFile(blob)
	{
		var reader = new FileReader();
		reader.addEventListener("loadend", function() {
			console.log(reader.result)
			console.log("done");
		});
		reader.readAsText(blob);
	}

	function initializeMap()
	{
		var file = null;
		var xhr = new XMLHttpRequest()
		xhr.open("GET", "table.csv")
		xhr.responseType = "blob"
		xhr.onload = function() 
		{
		    blob = xhr.response
		    loadFile(blob)
		}
		xhr.send()
  	}

  	initializeMap()	

  	function computeAverageAnnualReturn()
  	{
  		document.getElementById("submit-button").innerHTML="This button does nothing.";
  	}