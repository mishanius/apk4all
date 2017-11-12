angular.module('apk_world_app')
	.controller('app_pageCtrl', ['$scope','api','$mdDialog','$window','$routeParams','$sce','$cookieStore',
	function($scope, api, $mdDialog, $window, $routeParams, $sce, $cookieStore) {
	    $scope.media = media;
	    $scope.static_path = static_path;
	    $scope.isLoading = true;
//	    api_ans_generator.searchResults().then(function(results){
	    api.searchResults("api/itm",$routeParams.hash).then(function (results) {
	        $scope.game = results.data;
	        $scope.game.FrDescription= $sce.trustAsHtml($scope.game.FrDescription);
	        $scope.isLoading = false;
	    });
    var expireDate = new Date();
    expireDate.setDate(expireDate.getDate() + 30);
    var dialog={};
    if(typeof $cookieStore.get("gavno")!== "undefined" ){
        dialog = {
                  clickOutsideToClose: true,
                  scope: $scope,
                  preserveScope: true,
                  templateUrl:static_path+'pages/angular templates/downloadPage5.html',
                  controller: function DialogController($scope, $mdDialog) {
                    $scope.ready=false;
                    api.post("download",$scope.game).then(function (results) {
                    dialog.scope.game.DownloadLink=results.data.DownloadLink;
                    $scope.ready=true;
                    });
                    $scope.closeDialog = function() {
                        $mdDialog.hide();
                    }
                  }
               }
    }
    else{
        dialog = {
                  clickOutsideToClose: true,
                  scope: $scope,
                  preserveScope: true,
                  templateUrl:static_path+'pages/angular templates/downloadPage6.html',
                  controller: function DialogController($scope, $mdDialog) {
                    $scope.ready=false;
                    $scope.gavno = function() {
                        alert($cookieStore.get("gavno"));
                        $cookieStore.put("gavno","123", {'expires': expireDate});
                    }
                    api.post("download",$scope.game).then(function (results) {
                    dialog.scope.game.DownloadLink=results.data.DownloadLink;
                    $scope.ready=true;
                    });
                    $scope.closeDialog = function() {
                        $mdDialog.hide();
                    }
                  }
               }
    }

    $scope.showDownload = function(event) {
                $mdDialog.show (dialog);
//                if ( !LockyLuke.noOffers ) {
//                    $mdDialog.show (dialog);
//                } else {
//                    dialog.templateUrl=static_path+'pages/angular templates/downloadPageNfr.html';
//                    $mdDialog.show (dialog);
//                }
            };




























	}]);