gcd = function(a, b){
	if (a < 0)
		a = -a;
	if (b < 0)
		b = -b;
	if (a == 0) {
		return b;
	}
	else if (b == 0) {
		return a;
	}
	else if (a >= b) {
		return gcd (a % b, b);
	}
	else {
		return gcd(b % a, a);
	}
};

var app = angular.module('gcd-app', []);
app.controller('gcd-controller', function($scope) {
    $scope.a = 15;
    $scope.b = 24;
    $scope.gcd = function() {
    	return gcd($scope.a, $scope.b);
    };
});
