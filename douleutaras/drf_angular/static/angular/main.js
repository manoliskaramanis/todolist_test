var app = angular.module('todo-app', [
	'ui.router'
]);
app.value('current_user', {
    user_id : 0
});
app.constant('TODO_URL', 'http://127.0.0.1:8000/api/todos/');
app.constant('USER_URL', 'http://127.0.0.1:8000/api/users/');

app.config(function($stateProvider, $urlRouterProvider){
	$stateProvider
	    .state('home', {
			url: '/',
			templateUrl: '/static/templates/login.html',
			controller: 'MainCtrl'
		})
		.state('todolist', {
			url: '/todolist',
			templateUrl: '/static/templates/list.html',
			controller: 'MainCtrl'
		})
		.state('add-todo', {
			url: "/add",
			templateUrl: 'static/templates/add.html',
			controller: 'MainCtrl'
		});

	$urlRouterProvider.otherwise('/');
});

app.controller('MainCtrl', function($scope, Todos, User, $state, current_user){
    $scope.newUser = {};
	$scope.signup = function() {
		User.checkUsername($scope.newUser).then(function(res){
				if(JSON.stringify(res.data).length > 2){
                    alert('Username already exists')
                }else{
                    User.signup($scope.newUser).then(function(res){
				        current_user.user_id = JSON.parse(JSON.stringify(res)).data.id;
				        $state.go('todolist');
                    });
                }
            });

	};


	$scope.login = function() {
		User.login($scope.newUser).then(function(res){
		        if(JSON.stringify(res.data).length < 3){
                    alert('Username and password do not match')
                }else{
				    current_user.user_id = JSON.parse(JSON.stringify(res)).data[0].id;
				    $state.go('todolist');
			    }
			});;
	};


	$scope.newTodo = {};
	$scope.addTodo = function() {
	    if(!$scope.newTodo.title){
	       alert("Title cannot be empty.")
	    }else{
	        if(!$scope.newTodo.description){
	            alert("Description cannot be empty.")
	        }else{
	            if(!$scope.newTodo.date_html){
	                alert("Date cannot be empty.")
	            }else{
	               Todos.addOne($scope.newTodo, current_user.user_id)
			            .then(function(res){
				            $state.go('todolist');
			            });
	            }
	        }
	    }

	};

	$scope.toggleCompleted = function(todo) {
		Todos.update(todo, current_user.user_id);
	};

	$scope.deleteTodo = function(id){
		Todos.delete(id);
		$scope.todos = $scope.todos.filter(function(todo){
			return todo.id !== id;
		})
	};

	Todos.all(current_user.user_id).then(function(res){
		$scope.todos = res.data;
	});
});

app.service('Todos', function($http, TODO_URL){
	var Todos = {};

	Todos.all = function(id){
		return $http.get(TODO_URL, {params: {user_id: id}});
	};

	Todos.update = function(updatedTodo, id){
	    //format put data
	    updatedTodo.user = id;
		return $http.put(TODO_URL + updatedTodo.id, updatedTodo);
	};

	Todos.delete = function(id){
		return $http.delete(TODO_URL + id + '/');
	};

	Todos.addOne = function(newTodo, id){
	    //format post data
	    newTodo.user_id = id
	    var date = new Date(newTodo.date_html);
        var day = date.getDate();
        var monthIndex = date.getMonth() + 1;
        var year = date.getFullYear();
	    newTodo.date = year+"-"+monthIndex+"-"+day;
	    newTodo.user = id;
        return $http.post(TODO_URL, newTodo)
    };

	return Todos;
});

app.service('User', function($http, USER_URL){
	var User = {};

	User.login = function(newUser){
		return $http.get(USER_URL, {params: {username: newUser.username, password: newUser.password}});
	};

    User.checkUsername = function(newUser){
        return $http.get(USER_URL, {params: {username: newUser.username}});
    };

    User.signup = function(newUser){
        return $http.post(USER_URL, newUser);
    };

	return User;
});




