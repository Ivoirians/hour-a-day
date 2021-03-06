var app = angular.module('commentsApp', []);
var pageNumber = window.location.pathname
app.controller('CommentController', function($scope, $http) {

	var updateCommentSection = function() {
	    $scope.comments = [];
		$http({
			method: 'GET',
			url: '/svc/comments/get?page_number=' + pageNumber
		}).then(function successCallback(response) {
			$scope.comments = response.data;
		}, function errorCallback(response) {
			console.log("Service not found.")
		});
	};

	updateCommentSection();

    $scope.addComment = function() {
    	if ($scope.comment)
    	{
			$http({
				method: 'POST',
				url: '/svc/comments/add',
				data: {
					username: $scope.username,
					page_number: pageNumber,
					comment_text: $scope.comment
				}

			}).then(function successCallback(response) {
				$scope.comment = "";
				updateCommentSection();
			}, function errorCallback(response) {
				console.log("Service not found.")
			});
		}
	};
});