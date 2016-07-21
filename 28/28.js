
var app = angular.module('counterApp', []);
app.controller('CounterController', function($scope, $http) {
	var updateCounter = function() {
		$http({
			method: 'GET',
			url: '/svc/counter/get'
		}).then(function successCallback(response) {
			$scope.counter = response.data;
		}, function errorCallback(response) {
			console.log("Service not found.")
		});
	};

	updateCounter();

	var incrementMsg = {"message_type" : "increment" };
	var socket = new WebSocket("ws://ivoirians.me/ws/counter");
	socket.onmessage = function(evt) {
		if (JSON.parse(evt.data).message_type == "increment_notification")
			updateCounter();
	}

    $scope.addCounter = function() {
		$http({
			method: 'GET',
			url: '/svc/counter/add'
		}).then(function successCallback(response) {
			$scope.counter = response.data;
		}, function errorCallback(response) {
			console.log("Service not found.")
		});

		socket.send(JSON.stringify(incrementMsg));
	};
});