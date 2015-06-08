var weather;
var cols = 30;
var rows = 30;
// var img;
var mo = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"];

function preload() {
    weather = loadJSON('/getData');
    // img = loadImage("assets/pic3.jpg"); 
}

function setup() {
    createCanvas(1200, 600);
    // image(img, 0, 0);

    rW = width / sqrt(900);
    rH = height / sqrt(900);
    
    // noLoop();

}

function draw() {
    background(200);
    // image(img, 0, 0);
    noStroke();
    //	stroke(255);
    var rainMin = weather.rainmin;
    var rainMax = weather.rainmax;
    var tMaxMin = weather.tmaxmin;
    var tMaxMax = weather.tmaxmax;
    var tMinMin = weather.tminmin;
    var tMinMax = weather.tminmax;
    var counter = 0;
    // console.log(float(tMaxMax));
	    for (var x = 0; x < cols; x++) {
	        for (var y = 0; y < rows; y++) {
	            //console.log(counter%12);
	            year = Math.floor(counter / 12);
	            // console.log(year);
				var rain, Tmax, Tmin;

	            if (weather.stats[year].months[counter % 12][mo[counter % 12]].rain != "---" && 
	            	weather.stats[year].months[counter % 12][mo[counter % 12]].tmax != "---" && 
	            	weather.stats[year].months[counter % 12][mo[counter % 12]].tmin != "---")
	            {
	                rain = float(weather.stats[year].months[counter % 12][mo[counter % 12]].rain);
	                Tmax = float(weather.stats[year].months[counter % 12][mo[counter % 12]].tmax);
	                Tmin = float(weather.stats[year].months[counter % 12][mo[counter % 12]].tmin);
	                //console.log(float(tMaxMin));
	                var r = map(rain, rainMin, rainMax, 0, 255);
	                var b = map(Tmax, tMaxMin, tMaxMax, 0, 255);
	                var g = map(Tmin, tMinMin, tMinMax, 0, 255);
	                fill(r, g, b);

	            } else {
	                fill(255, 0, 255);
	            }

	            rect(x * rW, y * rH, rW, rH);
	        	displayData(rain, Tmax, Tmin);


		        //console.log(g);
		        //console.log(b);
		        counter++;

		        
	    	}
	}	
}

function displayData(rain, Tmax, Tmin)
{
				var By = Math.floor(mouseY / rH);
		        var Bx = Math.floor(mouseX / rW);
		        var totalmonths = (Bx * 30 + By) + 1;
		        var years = Math.floor(totalmonths / 12);
		        var months = totalmonths % 12;
		        fill(0);
		        textSize(20);


		        var data = float(weather.stats[years].months[months][mo[months]].tmax);
		        //text(years + " / " + months + " / " + data, mouseX + 20, mouseY + 20);
		        text("Year: " + years + "Month: " + months + "rain: " + rain + "tmax" + Tmax + "tmin: " + Tmin , mouseX+ 20, mouseY+20);
		        // if (x == Bx && y == By) {
		        //     console.log(years + " / " + months + " / " + r + " / " + g + " / " + b);
	        	// }
}