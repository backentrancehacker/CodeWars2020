const fs = require('fs').promises

const TOPPINGS = {
	'Pepperoni': 32,
	'Red_Peppers': 16,
	'Pineapple': 84,
	'Olive': 20,
	'Sardines': 12,
	'Onion': 28,
	'Sausage': 40,
	'Ham': 36,
	'eof': 0
}
const SPECIAL = {
	'Cheese': '',
	'Hawaiian': '1/2 Pineapple 1/2 Ham',
	'Fishaster': '1/2 Sardines 1/2 Onion',
	'Meat-Lovers': '1/3 Pepperoni 1/3 Sausage 1/3 Ham',
	'Combo': '1/4 Red_Peppers 1/4 Olive 1/4 Onion 1/4 Sausage'
}
class Pizza{
	constructor(info, special){
		this.results = {}
		// if(toppings){
		this.toppings(info)	
		// }
	}
	toppings(normal){
		if(!normal) return
		let altered = normal.replace('Red Peppers', 'Red_Peppers').split(' ').map(inp => inp.trim()).filter(inp => inp.length)
		for(let i = 0; i < altered.length; i ++){
			let current = altered[i]
			let next = altered[i] || 'eof'
			console.log(next)
			if(TOPPINGS.hasOwnProperty(next)){
				if(!this.mult) this.mult = parseInt(current)
				this.results[next] = this.mult * TOPPINGS[next]
			}
		}
		console.log(this.results)
	}
	getResults(){
		return this.results
	}
}

async function init(){
	let details = await fs.readFile(`${__dirname}/input.txt`,'utf8')

	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)
	console.log((new Pizza('2 Pepperoni')))
	// let results = []
	// for(let line of lines){
	// 	let interpreter = new Interpreter(line)
	// 	results.push(interpreter.express())
	// }
}
init()