// JavaScript Document
function Meterconvert(value);
{
	var variable = document.getElementById("input").value;
if(value === "Meters")
{
	var output = variable / 0.3048;
}
	
document.getElementById("ouput").value = output;
}