const fs = require('fs')
const angle = (hrs, min) => {
	let result = Math.abs((hrs * 30 + min * 0.5) - (min * 6))
	return Math.min(360 - result, result)
}
const num = (_float, _digits) => {
	let rounded = Math.pow(10, _digits);
	return (Math.round(parseFloat(_float) * rounded) / rounded).toFixed(_digits);
}

function init(){
	let details = fs.readFileSync(`${__dirname}/input.txt`,'utf8')

	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)
	for(let time of lines){
		let result = angle.apply(null, time.split(':'))
		result = num(result, 2)
		console.log(`The angle between the Hour hand and Minute hand is ${result} degrees`)
	}
}
init()