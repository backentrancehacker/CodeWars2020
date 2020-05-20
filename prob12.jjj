const fs = require('fs')

const convertY = yards => (parseInt(yards) * 3 * 0.3048 * 100)
const convertF = feet => (parseInt(feet) * 0.3048 * 100)
const convertI = inches => (parseInt(inches) * 2.54)

function init(){
	let details = fs.readFileSync(`${__dirname}/input.txt`,'utf8')

	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)

	for(let line of lines){
		let parts = line.split(' ')
		let result = convertY(parts[0] || 0) + convertF(parts[1] || 0) + convertI(parts[2] || 0)

		console.log(result.toFixed(2))
		
	}

}

init()