var currentTime = new Date()
var month = currentTime.getMonth() + 1
    if((String(month)).length==1)
    month='0'+month;
var day = currentTime.getDate()
    if((String(day)).length==1)
    day='0'+day;
var year = currentTime.getFullYear()

    
    var chart = c3.generate({
        data: {
            x: 'DatumUhrzeit',
            url: '/temperature-monitoring/temperatureEvaluation/aktuell.csv',
            type: 'spline',
            xFormat: '%Y-%m-%d %H:%M',
        },
        axis: {
            x: {
                label: {
                    text: 'Zeitpunkt',
                    position: 'outer-right'
                },
                type: 'timeseries',
                tick: {
                    format: '%Y-%m-%d %H:%M',
                    multiline: false,
                    culling: {
                        max: 12
                    },
                },
            },
            y: {
                label: {
                    text: 'Temperatur in °C',
                    position: 'outer-top'
                },
            },
        },
        grid: {
            x: {
                show: true
            },
            y: {
                show: true
            }
        },
        point: {
            show: false
        },
        zoom: {
            enabled: true
        }
    });
