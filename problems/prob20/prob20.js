const fs = require('fs')

function init(){
	let details = fs.readFileSync(`${__dirname}/input.txt`,'utf8')

	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)
	console.log((new Pizza('2 Pepperoni')))
	// let results = []
	// for(let line of lines){
	// 	let interpreter = new Interpreter(line)
	// 	results.push(interpreter.express())
	// }
}
init()