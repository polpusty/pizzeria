app.controller('PizzaListCtrl', function ($scope, Pizza) {
    Pizza.list().then(function (data) {
        $scope.pizzas = data.data;
    });
});