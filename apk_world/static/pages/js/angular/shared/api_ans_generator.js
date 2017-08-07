angular.module('apk_world_app').factory('api_ans_generator', function($q, $timeout) {
    var searchResults = function(){
                        var deferred = $q.defer();
                        $timeout(function() {
                            var description = "very very long description in franch blah blah blah very very long description in franch blah blah blah very very long description in franch blah blah blah very very long description in franch blah blah blah very very long description in franch blah blah blah very very long description in franch blah blah blah very very long description in franch blah blah blah very very long description in franch blah blah blah very very long description in franch blah blah blah very very long description in franch blah blah blah very very long description in franch blah blah blah very very long description in franch blah blah blah very very long description in franch blah blah blah";
                            ans=[
                                {"name":"game1","description":"1"+description},
                                {"name":"game2","description":"2"+description},
                                {"name":"game3","description":"3"+description},
                                {"name":"game4","description":"4"+description},
                                {"name":"game5","description":"5"+description},
                                {"name":"game6","description":"6"+description},
                                {"name":"game7","description":"7"+description},
                                {"name":"game8","description":"8"+description},
                                ];
                        deferred.resolve(ans);
                        }, 5000);
                        return deferred.promise;
    };
 return {
  searchResults: searchResults
 }
});