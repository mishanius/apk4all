angular.module('apk_world_app').config(['$httpProvider', function($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    }]);
angular.module('apk_world_app').factory('api', function($q, $http) {
    var searchResults = function searchResults(apiPath, keyword){
        var deferred = $q.defer();
        $http.get("/"+apiPath+"/"+keyword).then(function(result){
            deferred.resolve({
                data: result.data,
            });
        });
        return deferred.promise;
    };
    var post = function(api_path, data){
        console.log("post");
        var deferred = $q.defer();
        $http({
            method: "POST",
            url: "/"+api_path+"/",
            data: data
            }).then(function(result){
                        deferred.resolve({
                            data: result.data,
                        });
                });
        return deferred.promise;
    };
 return {
  searchResults: searchResults,
  post: post
 }
});