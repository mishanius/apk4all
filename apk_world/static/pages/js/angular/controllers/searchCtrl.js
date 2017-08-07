angular.module('apk_world_app')
	.controller('searchCtrl', ['$scope','api','$mdDialog','$window','$routeParams','$location',
	function($scope, api, $mdDialog, $window, $routeParams, $location) {
	    $scope.media = media;
	    $scope.static_path = static_path;
	    $scope.isLoading = true;
//	    api_ans_generator.searchResults().then(function(results){
	    api.searchResults("api/search",$routeParams.kw).then(function (results) {
	        $scope.games = results.data;
	        $scope.isLoading = false;
	    });
        $scope.goToApp = function(hash){
                                    $location.path("/app"+hash);
                                    }
	}]);//end of controller