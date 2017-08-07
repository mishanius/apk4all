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

    $scope.showDownload = showDialog;
        function showDialog(game) {
            api.post("api/itm", game).then(function (results) {
            alert(alert(JSON.stringify(game)))
	        game = results.data;
            $window.scrollTo(0, 0);
            $mdDialog.show({
                parent: angular.element(document.body),
                targetEvent: $event,
                templateUrl:static_path+'pages/angular templates/downloadPage.html',
                locals: {
                game: game
                },
            controller: DialogController
            });
        });

        function DialogController($scope, $mdDialog, game) {
            $scope.game = game;
            $scope.closeDialog = function() {
                $mdDialog.hide();
            }
        }
        }




























	}]);