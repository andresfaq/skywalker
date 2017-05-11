/* chart colors default */
var $chrt_border_color = "#efefef";
var $chrt_grid_color = "#DDD"
var $chrt_main = "#E24913";
/* red       */
var $chrt_second = "#6595b4";
/* blue      */
var $chrt_third = "#FF9F01";
/* orange    */
var $chrt_fourth = "#7e9d3a";
/* green     */
var $chrt_fifth = "#BD362F";
/* dark red  */
var $chrt_mono = "#000";

function renderGraphic (data) {
    console.log ("render graphic :D whit data: " + data);
    // DO NOT REMOVE : GLOBAL FUNCTIONS!
    //pageSetUp();
    /* bar chart */
    if ($("#bar-chart").length) {

        var data1 = [];
        for (var i = 0; i <= 12; i += 1)
             data1.push([i, parseInt(Math.random() * 30)]);
        var data2 = [];
        for (var i = 0; i <= 12; i += 1)
            data2.push([i, parseInt(Math.random() * 30)]);
        var data3 = [];
        for (var i = 0; i <= 12; i += 1)
            data3.push([i, parseInt(Math.random() * 30)]);

        var ds = new Array();
        ds.push({
            data : data1,
            bars : {
                show : true,
                barWidth : 0.2,
                order : 1,
            }
        });
        ds.push({
            data : data2,
            bars : {
                show : true,
                barWidth : 0.2,
                order : 2
            }
        });
        ds.push({
            data : data3,
            bars : {
                show : true,
                barWidth : 0.2,
                order : 3
            }
        });

        //Display graph
        $.plot($("#bar-chart"), ds, {
            colors : [$chrt_second, $chrt_fourth, "#666", "#BBB"],
            grid : {
                show : true,
                hoverable : true,
                clickable : true,
                tickColor : $chrt_border_color,
                borderWidth : 0,
                borderColor : $chrt_border_color,
            },
            legend : true,
            tooltip : true,
            tooltipOpts : {
                content : "<b>%x</b> = <span>%y</span>",
                defaultTheme : false
            }

        });
    }
    /* end bar chart */

} 

function renderGraphicMorris (datos) {

                    // bar graph color
                if ($('#bar-graph').length) {
                    
                    Morris.Bar({
                        element : 'bar-graph',
                        data : [{
                            x : '2011 Q1',
                            y : 0
                        }, {
                            x : '2011 Q2',
                            y : 1
                        }, {
                            x : '2011 Q3',
                            y : 2
                        }, {
                            x : '2011 Q4',
                            y : 3
                        }, {
                            x : '2012 Q1',
                            y : 4
                        }, {
                            x : '2012 Q2',
                            y : 5
                        }, {
                            x : '2012 Q3',
                            y : 6
                        }, {
                            x : '2012 Q4',
                            y : 7
                        }, {
                            x : '2013 Q1',
                            y : 8
                        }],
                        xkey : 'x',
                        ykeys : ['y'],
                        labels : ['Y'],
                        barColors : function(row, series, type) {
                            if (type === 'bar') {
                                var red = Math.ceil(150 * row.y / this.ymax);
                                return 'rgb(' + red + ',0,0)';
                            } else {
                                return '#000';
                            }
                        }
                    });

                }
}

// PAGE RELATED SCRIPTS

$(document).ready(function() {

});
/** end document ready funtion*/