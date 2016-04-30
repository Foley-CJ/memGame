function renderShape(shape){

	var svg = d3.select("#inner_box").append("svg")
		.attr("width", 180)
		.attr("height", 104)


	if (shape.design =='square'){
		svg.append("rect")
			.attr("width", 100)
			.attr("height", 100)
			.attr("x", 40)
			.attr("class", "shape")
			.attr("stroke", "black")
			.style("fill", shape.color)
			;}

	else if (shape.design == 'circle'){
		svg.append("circle")
			.attr("cx", 90)
			.attr("cy", 51)
			.attr("r", 50)
			.attr("class", "shape")
			.attr("stroke", "black")
			.style("fill", shape.color);}
	
	else if (shape.design == 'triangle'){
		svg.append("path")
			.attr("d", "M40 100 L140 100 L90 0 Z")
			.attr("stroke", 'Black')
			.attr("class", "shape")
			.style("fill", shape.color)
	}

	else{
		console.log('error')
	}
}
