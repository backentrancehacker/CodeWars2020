const fs = require('fs')

const operators = {
	MULTIPLY: '*',
	DIVIDE: '/',
	ADD: '+',
	SUBTRACT: '-',
	POWER: '^'
}
function num(_float, _digits){
	let rounded = Math.pow(10, _digits);
	return (Math.round(parseFloat(_float) * rounded) / rounded).toFixed(_digits);
}
function init(){
	let details = fs.readFileSync(`${__dirname}/input.txt`,'utf8')

	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)

	for(let line of lines){
		let tokens = line.split(' ').map(inp => inp.trim()).filter(inp => inp.length)

		let num1 = num(tokens[0], 1),
			num2 = num(tokens[1], 1),
			operator = operators[tokens[2]] || tokens[2]
			expected = num(tokens[3], 1),
			toEval = operator == '^' ? `Math.pow(${num1}, ${num2})` : `${num1}${operator}${num2}`

		let result = num(eval(toEval), 1)

		console.log(result == expected ? `${result} is correct for ${num1} ${operator} ${num2}` : `${num1} ${operator} ${num2} = ${result}, not ${expected}`)
	}
}
init()