$http({
	method: 'GET',
	url: '/svc/counter/get'
}).then(function successCallback(response) {
	document.getElementById("counter_value").innerHTML = counter;
}, function errorCallback(response) {
	console.log("Service not found.")
});


window.onload = function() {
	document.getElementById("counter_button").onclick = function() {
			$http({
				method: 'GET',
				url: '/svc/counter/add'
			}).then(function successCallback(response) {
				document.getElementById("counter_value").innerHTML = counter;
			}, function errorCallback(response) {
				console.log("Service not found.")
			});
		};
}