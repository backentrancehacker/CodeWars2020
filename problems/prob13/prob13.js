const fs = require('fs').promises

async function init(){
	let details = await fs.readFile(`${__dirname}/input.txt`,'utf8')

	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)
	let money = parseInt(lines[0].split(' ')[0])
	lines.shift()

	let result,
		spent = {},
		total = 0

	for(let line of lines){
		let parts = line.split(' ')
		spent[parts[0]] = parseInt(parts[1])
	}
	for(let key in spent){
		let cost = spent[key]
		total += cost
		if(money - total > 0){
			console.log(`I can afford ${key}`)
		}
		else{
			total -= cost
			console.log(`I can't afford ${key}`)
		}
	}
	console.log(money - total)
	
}
init()