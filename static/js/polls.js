
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

