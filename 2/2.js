	function loadFile(blob)
	{
		console.log("Not implemented yet.")
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