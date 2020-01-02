
function renderResults(val){
    // render with https://www.zingchart.com/
    const charConfig = {
        type: "bar3d",
        plot: {
            aspect: "cylinder",
            tooltip:{ 
                "text":"%kl gets <br>%v %t.",
                "placement":"node:top",
                "padding":"10%",
                "border-radius":"5px",
                "background-color":"#ff9999",
              }
        },
        "title": {
            "text": "Vote results",
            "font-color": "#7E7E7E",
            "backgroundColor": "none",
            "font-size": "22px",
            "alpha": 1,
            "adjust-layout":true,
        },
        "scaleX":{
            "values": val['scaleX'],
            "placement":"default",
            "tick":{
                "size":20,
                "placement":"cross"
            },
            "itemsOverlap":true,
            "item":{
                "offsetY":-20
            }
        },
        "series": [
            {
                "values": val['series'],
                "alpha": 0.95,
                "background-color": "#66ccff",
                "text": "votes",
            },
        ]
    };

    zingchart.render({ 
        id : 'polls_chart', 
        data : charConfig, 
        height: '100%', 
        width: '100%' 
    });
    
}

function render_am_chartjs(val){

    
    am4core.ready(function() {

        myDict = []

        val['scaleX'].forEach((v,i) =>{

            let d = {
                'answer':v,
                'votes':val['series'][i]
            }
            myDict.push(d)
        });
        

        // Themes begin
        am4core.useTheme(am4themes_animated);
        // Themes end

        // Create chart instance
        var chart = am4core.create("chartdiv", am4charts.XYChart);

        // Add data
        chart.data = myDict;

        // Create axes

        var categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
        categoryAxis.dataFields.category = "answer";
        categoryAxis.renderer.grid.template.location = 0;
        categoryAxis.renderer.minGridDistance = 20;

        categoryAxis.renderer.labels.template.adapter.add("dy", function(dy, target) {
        if (target.dataItem && target.dataItem.index & 2 == 2) {
            return dy + 25;
        }
        return dy;
        });

        var valueAxis = chart.yAxes.push(new am4charts.ValueAxis());

        // Create series
        var series = chart.series.push(new am4charts.ColumnSeries());
        series.dataFields.valueY = "votes";
        series.dataFields.categoryX = "answer";
        series.name = "Votes";
        series.columns.template.tooltipText = "{categoryX}: [bold]{valueY}[/]";
        series.columns.template.fillOpacity = .8;

        var columnTemplate = series.columns.template;
        columnTemplate.strokeWidth = 1;
        columnTemplate.strokeOpacity = 1;

    }); // end am4core.ready()

}

function render_chart_js(val){

    let datasets = [];
    
    const backgroundColors = ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"];

    var randomColorGenerator = function () { 
        return '#' + (Math.random().toString(16) + '0000000').slice(2, 8); 
    };

    val['scaleX'].forEach((v,i) =>{
        let j = i;
        if (i > (backgroundColors.length -1)){
            j = 0;
        }
        let ds = {
            label: v,
            backgroundColor: randomColorGenerator(), //backgroundColors[j],
            borderColor: 'gray',
            borderWidth: 1,
            data: [val['series'][i]]
        }
        datasets.push(ds)

    });

    var barChartData = {
        // labels: val['scaleX'],
        datasets: datasets
    };
    
    var ctx = document.getElementById('myChart').getContext('2d');
    myBar = new Chart(ctx, {
        type: 'bar',
        data: barChartData,
        options: {
            responsive: true,
            tooltips: {
                callbacks: {
                  title: function(tooltipItem, data) {
                    let index = tooltipItem[0]['datasetIndex'];
                    let val = data['datasets'][index];
                    return val['label'];
                  },
                  label: function(tooltipItem, data) {
                    let index = tooltipItem['datasetIndex'];
                    return "Votes: "+data['datasets'][index]['data']
                  },
                  afterLabel: function(tooltipItem, data) {
                    let dataset = data['datasets'][tooltipItem['datasetIndex']];
                    let total = 0;
                    data['datasets'].forEach(d=>{
                        total += d['data'][0]
                    })
                    let percent = Math.round((dataset['data'] / total) * 100)
                    return '(' + percent + '%)';
                  }
                },
            },
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Votes results'
            },
            scales: {
                yAxes: [{
                    display: true,
                    ticks: {
                        suggestedMin: 0,
                    }
                }],
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Answers'
                    },
                    ticks: {
                        major: {
                            fontStyle: 'bold',
                            fontColor: '#FF0000'
                        }
                    }
                }]
            }
        }
    });

}

