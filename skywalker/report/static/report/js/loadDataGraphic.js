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

// PAGE RELATED SCRIPTS
$(document).ready(function() {
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
});