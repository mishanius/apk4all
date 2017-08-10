angular.module('apk_world_app')
	.controller('app_pageCtrl', ['$scope','api','$mdDialog','$window','$routeParams',
	function($scope, api, $mdDialog, $window, $routeParams) {
	    $scope.media = media;
	    $scope.static_path = static_path;
	    $scope.isLoading = true;
//	    api_ans_generator.searchResults().then(function(results){
	    api.searchResults("api/itm",$routeParams.hash).then(function (results) {
	        $scope.game = results.data;
	        $scope.isLoading = false;
	    });


    $scope.showDownload = function(event) {
               $mdDialog.show ({
                  clickOutsideToClose: true,
                  scope: $scope,
                  preserveScope: true,
                  templateUrl:static_path+'pages/angular templates/downloadPage1.html',
                  controller: function DialogController($scope, $mdDialog) {
                     $scope.closeDialog = function() {
                        $mdDialog.hide();
                     }
                  }
               });
            };




























	}]);