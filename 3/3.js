function loadFile(blob)
{
	var reader = new FileReader();
	reader.addEventListener("loadend", function() {
		dateDict = {};
		var lines = reader.result.split("\n");
		for (line of lines) {
			var dates = line.split(",");
			dateDict[dates[0]] = {open: dates[1], close: dates[4]};
		}
		console.log("done");
	});
	reader.readAsText(blob);
}

function twoDigitLeftPad(i)
{
	return i > 9 ? "" + i : "0" + i;
}

function parseDate(date)
{
	return date.getFullYear() + "-" + twoDigitLeftPad(date.getMonth()+1) + "-" + twoDigitLeftPad(date.getDay());
}

//if you place a buy/sell order on a date, it'll either pull
//the las
function getOpenClose(dateString)
{
	if (dateString in dateDict){
		return dateDict[dateString];
	}
	forwardDate = new Date(dateString)
	for (i = 0; i < 7; i++)
	{
		forwardDate.setDate(forwardDate.getDate() + 1);
		if (parseDate(forwardDate) in dateDict)
		{
			return dateDict[parseDate(forwardDate)];
		}
	}
	throw "Could not find day within one week of any data point";

}

function getMarketChange(start, end)
{
	var a = parseFloat(getOpenClose(start).open);
	var b = parseFloat(getOpenClose(end).close);
	var elapsed = new Date(end) - new Date(start);

	return {initial: a, final: b, delta: b-a, deltaT: parseInt(elapsed/82400000) }
}

function initializeMap()
{
	var file = null;
	var xhr = new XMLHttpRequest()
	xhr.open("GET", "../2/table.csv")
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
	var dateStart = document.getElementById("stock-market-start").value;
	var dateEnd = document.getElementById("stock-market-end").value;
	if (dateStart == "" || dateEnd == "")
	{
		document.getElementById("stock-market-results").innerHTML="Error: Missing date.";
		return;
	}
	if (dateEnd < dateStart)
		document.getElementById("stock-market-results").innerHTML="Error: Start date is after end date";
	else
	{
		var results = getMarketChange(dateStart, dateEnd);
		var resultString = dateStart + ": Opened at " + results.initial + ".\n";
		resultString += dateEnd + ": Closed at " + results.final + ".\n";
		resultString += "Change:" + results.delta + ".\n";
		resultString += "Total days:" + results.deltaT + ".\n";
		resultString += "Average annual return: " + (Math.pow(results.final/results.initial, 365/results.deltaT) - 1) + "%.";
		document.getElementById("stock-market-results").innerHTML = resultString;
		document.getElementById("stock-market-button").innerHTML = "Recalculate";

	}
}