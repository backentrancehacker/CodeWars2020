const fs = require('fs')
//# 1/D TYPE-OR-TOPPING & 1/D TYPE-OR-TOPPING

let TOPPINGS = {
	'Pepperoni': 32,
	'Red_Peppers': 16,
	'Pineapple': 84,
	'Olives': 20,
	'Sardines': 12,
	'Onion': 28,
	'Sausage': 40,
	'Ham': 36,
	'None': 0
}
let SPECIAL = {
	'Hawaiian': 'Pineapple Ham',
	'Combo': 'Red_Peppers Olives Onion Sausage',
	'Fishaster': 'Sardines Onion',
	'Meat-Lovers': 'Pepperoni Sausage Ham',
	'Cheese': 'None'
}

const convert = parts => {
	let cache = []
	for(let part of parts){
		if(SPECIAL.hasOwnProperty(part)){
			let normal = SPECIAL[part].split(' ')
			for(let _push of normal){
				cache.push(_push)
			}
		}
		else{
			cache.push(part)
		}
	}
	return cache
}
const solo = parts => {
	for(let part of parts){
		if(!TOPPINGS.hasOwnProperty(part)) return false
	}
	return true
}
function init(){
	let details = fs.readFileSync(`${__dirname}/input.txt`,'utf8')

	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)

	let tree = {}

	for(let line of lines){
		let parts = convert(line.replace(/Red Peppers/gi, 'Red_Peppers').replace(/&/gi, '').split(' ').filter(inp => inp.length))

		let mult = parts[0]
		parts.shift()

		if(solo(parts)){
			for(let part of parts){
				let topping = TOPPINGS[part]
				tree[part] = (tree[part] || 0) + (topping * mult)
			}
		}
		else {
			let map = {}
			let prev
			for(let i = 1; i < parts.length; i ++){
				let current = parts[i]
					prev = parts[i - 1] || prev

				if(TOPPINGS.hasOwnProperty(current)){
					map[current] = prev
				}
			}
			
			for(let key in map){
				let current = map[key]
				if(TOPPINGS.hasOwnProperty(current)){
					map[key] = map[current]
				}
				tree[key] = (tree[key] || 0) + (TOPPINGS[key] * mult * eval(map[key]))
			}			
		}
	}
	for(let key in tree) if(key != 'None') console.log(`${key.replace('_', ' ')}: ${tree[key]}`)
	
}
init()