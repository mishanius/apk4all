angular.module('apk_world_app')
	.controller('mainCtrl', function mainCtrl($scope, $location) {
	    $scope.media = media;
	    $scope.TopGames = topgames;
	    $scope.TopApps = topapps;
	    $scope.users = ['Fabio', 'Leonardo', 'Thomas', 'Gabriele', 'Fabrizio', 'John', 'Luis', 'Kate', 'Max'];
	    $scope.search = function(kw){
                                    $location.path("/search"+kw)
                                    }
	});
