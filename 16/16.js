
var app = angular.module('counterApp', []);
app.controller('CounterController', function($scope, $http) {
    $scope.test = 5;
	$http({
		method: 'GET',
		url: '/svc/counter/get'
	}).then(function successCallback(response) {
		$scope.counter = response.data;
	}, function errorCallback(response) {
		console.log("Service not found.")
	});

    $scope.addCounter = function() {
		$http({
			method: 'GET',
			url: '/svc/counter/add'
		}).then(function successCallback(response) {
			$scope.counter = response.data;
		}, function errorCallback(response) {
			console.log("Service not found.")
		});
	};
});