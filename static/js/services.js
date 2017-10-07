app.factory('Pizza', function ($http) {
    return {
        list: list
    };

    function list() {
        return $http.get('/api/v1/pizzas/');
    }
});