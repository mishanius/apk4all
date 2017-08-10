angular.module('apk_world_app', ['ngRoute','ngMaterial','ui.carousel'])
.config(function($routeProvider) {
		var main = {
            controller: 'mainCtrl',
			templateUrl : static_path+'pages/angular templates/main.html',
//			resolve: {
//				store: function (todoStorage) {
//					// Get the correct module (API or localStorage).
//					return todoStorage.then(function (module) {
//						module.get(); // Fetch the todo records in the background.
//						return module;
//					});
//				}
//			}
		};

		var search = {
            controller: 'searchCtrl',
			templateUrl : static_path+'pages/angular templates/search.html',
		};
		var appPage = {
            controller: 'app_pageCtrl',
			templateUrl : static_path+'pages/angular templates/gamePage3.html',
		};
		$routeProvider
			.when('/', main)
			.when('/search:kw?', search)
			.when('/app:hash?', appPage)
			.otherwise({
				redirectTo: '/'
			});
    });
