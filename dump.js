const fs = require('fs').promises
const Operators = {
	'Pepperoni': 32,
	'Red Peppers': 16,
	'Pineapple': 84,
	'Olive': 20,
	'Sardines': 12,
	'Onion': 28,
	'Sausage': 40,
	'Ham': 36,
	'Cheese': 0,
}
class Token{
	constructor(type, val){
		this.type = type,
		this.val = val
	}
}
const determine = inp => {
	if(!inp) return 'eof'
	if(parseInt(inp) == inp || inp == '/') return 'number'
	if(inp.includes(' ')) return 'whitespace'
	if(isNaN(inp) && inp != '&') return 'string'
}
const process = tokens => {
	let index = 0
	let ast = []
	
	const progress = () => (index++)
	loop:
	while(index < tokens.length){
		let current = tokens[index]
		let mode = determine(current)
		let result
		switch(mode){
			case 'string': 
				result = ''
				while(determine(tokens[index]) == 'string'){
					result += tokens[index]
					progress()
				}
				ast.push(new Token('string', result))
				break
			case 'number':
				result = ''
				while(determine(tokens[index]) == 'number'){
					result += tokens[index]
					progress()
				}
				ast.push(new Token('number', result))
				break
			case 'eof':
				break loop
		}
		progress()
	}
	return ast
}

async function init(){
	let details = await fs.readFile(`${__dirname}/input.txt`,'utf8')

	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)
	for(let line of lines){
		let ast = process(line)
		let mult = ast[0].val

		ast.shift()

		let values = {}
		for(let i = 0; i < ast.length; i++){
			let token, val, cache

			if(i % 2 == 0){
				token = ast[i]
				val = token.val
				cache = ''

				let altered = val.split('/')
				cache += `(${altered[0] / altered[1]}) `
				
				token = ast[i + 1]
				cache += `* ${Operators[token.val]}`

				values[token.val] = (eval(cache) * mult) + (values[token.val] || 0)
			}
		}
		
		console.log(values)
		// console.log(mult)
	}
	
}
init()


const fs = require('fs').promises

const TOPPINGS = {
	'Pepperoni': 32,
	'Red_Peppers': 16,
	'Pineapple': 84,
	'Olive': 20,
	'Sardines': 12,
	'Onion': 28,
	'Sausage': 40,
	'Ham': 36
}
const SPECIAL = {
	'Cheese': '',
	'Hawaiian': '1/2 Pineapple 1/2 Ham',
	'Fishaster': '1/2 Sardines 1/2 Onion',
	'Meat-Lovers': '1/3 Pepperoni 1/3 Sausage 1/3 Ham',
	'Combo': '1/4 Red_Peppers 1/4 Olive 1/4 Onion 1/4 Sausage'
}

class Token{
	constructor(type, val){
		this.type = type
		this.val = val
	}
}
class Interpreter{
	constructor(code){
		this.index = 0
		this.format(code)
		this.results = {}
		this.current = this.code[this.index]
	}
	format(code){
		let cache = code
		for(let key in SPECIAL){
			cache = cache.replace(key, `${SPECIAL[key]}`)
		}
		cache = cache.split(' ').map(inp => inp.trim()).filter(inp => inp.length)
		this.mult = cache[0]
		this.code = cache
	}
	consume(){
		this.index++
		this.current = this.code[this.index]
	}
	next(){
		if(this.code[this.index + 1]) return this.code[this.index + 1]
		else return ''
	}
	express(){
		while(this.index < this.code.length){
			let current = this.current,
				next = this.next(),
				cache = this.mult
			/*
			if(current.includes('(')){
				while(this.next() != ')'){
					let _current = this.current,
						_next = this.next()
					
					if(TOPPINGS.hasOwnProperty(_next)){
						let _cache = eval(`(${_current}) * ${TOPPINGS[_next]}`) * current
						this.results[_next] = (this.results[_next] || 0) + _cache
					}
					this.consume()
				}
			}
			*/
			if(current.includes('/')) cache = eval(current) * cache
			if(TOPPINGS.hasOwnProperty(next)){
				this.results[next] = eval(`${cache} * ${TOPPINGS[next]}`) 
			}
			// else if(TOPPINGS.hasOwnProperty(current) && !next){
			// 	this.results[current] = (cache * TOPPINGS[current])
			// }

			this.consume()
		}
		return this.results
	}
}
async function init(){
	let details = await fs.readFile(`${__dirname}/input.txt`,'utf8')

	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)
	let results = []
	for(let line of lines){
		let interpreter = new Interpreter(line)
		results.push(interpreter.express())
	}
	let master = {}
	for(let result of results){
		for(let key in result){
			master[key] = (master[key] || 0) + result[key]
		}
	}
	console.log(master)
	
}
init()