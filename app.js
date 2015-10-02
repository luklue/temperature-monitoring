'use strict';


angular.module('myApp', []).controller('SensornamesCtrl', function($scope, $http, $sce){
    $http.get('/temperature-monitoring/temperatureEvaluation/sensornames.json').then(function(sensornamesResponse) {
        $scope.sensornames = sensornamesResponse.data;
    });
    

    
    $http.get('/settings/status').then(function(data) {
        if (data.data == "true") {
            $scope.status = true;
        } else if (data.data == "false") {
            $scope.status = false;
        }
    });

    $http.get('/settings/downloads').then(function(downloads) {
        $scope.downloads = downloads.data;
    });
   
   
    $scope.sensornames = [{}];

    $scope.putData = function() {
        $http.put('/settings/sensornames', $scope.sensornames).then(function() {
        });
        $http.put('/settings/projectname', $scope.projectname).then(function() {
        });
        location.reload();
    };


    $http.get('/temperature-monitoring/temperatureEvaluation/projectname.json').then(function(projectnameResponse) {
        $scope.projectname = projectnameResponse.data;
    });
    
    $scope.projectname = {};
    
    $scope.reload = function() {
        $http.get('/settings/stop').then(function() {
        });
        location.reload();
    };
    
    


});