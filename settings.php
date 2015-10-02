<?php
require "/var/www/vendor/autoload.php";
$app = new \Slim\Slim(array(
    'debug' => true
));


// Der Querystring wird ignoriert
$app->environment['PATH_INFO'] = rtrim(strtok($_SERVER['REQUEST_URI'], '?'), '/');





$app->GET("/settings/status", function () use ($app) {
    $val = trim(@shell_exec("/usr/local/bin/gpio -g read 26"));
    if($val == 1){
    echo "true";
    } else {
    echo "false";
    }
});





$app->GET("/settings/downloads", function () use ($app) {
    $verz = opendir ( '/var/www/temperature-monitoring/temperatureEvaluation/readings/' );
    echo "[\n";
    while ( $file = readdir ( $verz ) )
    {
        if ( $file != '.' && $file != '..')
        {
            echo '{"name":"';
            echo "$file";
            echo '"},';
            echo "\n";
        }
    }
    closedir ( $verz );
    echo '{"ignore":"thisLine"}]';
});







$app->GET("/settings/stop", function () use ($app) {
    exec('python /var/www/temperature-monitoring/temperatureEvaluation/stopButton.py');
    shell_exec("/usr/local/bin/gpio -g write 26 0");
});






$app->PUT("/settings/sensornames", function () use ($app) {
    $body = $app->request->getBody();
    $jsonFile = fopen('/var/www/temperature-monitoring/temperatureEvaluation/sensornames.json',"wa+");
    fwrite($jsonFile, $body);
    fclose($jsonFile);
});

$app->PUT("/settings/projectname", function () use ($app) {
    $body = $app->request->getBody();
    $jsonFile = fopen('/var/www/temperature-monitoring/temperatureEvaluation/projectname.json',"wa+");
    fwrite($jsonFile, $body);
    fclose($jsonFile);
    exec('python /var/www/temperature-monitoring/temperatureEvaluation/startButton.py');
    shell_exec("/usr/local/bin/gpio -g write 26 1");
});

$app->run();
