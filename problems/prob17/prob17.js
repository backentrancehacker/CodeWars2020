const fs = require('fs').promises
class City{
	constructor(name){
		this.name = name
		this.connections = []
	}
	add(city){
		this.connections.push(city.name)
		this.duplication()
	}
	has(connection){
		if(connection == this.name) return false
		for(let i of this.connections){
			if(i == connection) return true
		}
	}
	duplication(){
		this.connections = [...new Set(this.connections)].filter(con => con != this.name)
	}
	sort(cities){
		let altered = new Array
		for(let key in cities){
			if(this.has(key)) altered.push(key)
		}
		this.connections = altered
	}
	print(){
		if(this.connections.length > 0)
			console.log(`${this.name} is neighbor to ${this.connections.join(', ')}`)
		else console.log(`City ${this.name} is remote and has no neighbours!`)
	}
}
async function init(){
	let details = await fs.readFile(`${__dirname}/input.txt`,'utf8')

	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)

	let count = parseInt(lines[0])
	lines.shift()

	let cities = {}
	
	for(let i = 0; i < count; i++){
		cities[lines[i]] = (new City(lines[i]))
	}

	lines.splice(0, count)

	for(let line of lines){
		let tokens = line.split(' ').map(inp => inp.trim()).filter(inp => (cities[inp] || inp.match(/train|air|road/)))
		if(tokens[2] != 'air'){
			cities[tokens[0]].add(cities[tokens[1]])
			cities[tokens[1]].add(cities[tokens[0]])	
		}
	}
	for(let key in cities){
		let city = cities[key]
		for(let connection of city.connections){
			if(cities[connection].has(key)){
				for(let subConnection of cities[connection].connections){
					city.add(cities[subConnection])
				}
			}
		}
		city.sort(cities)
		city.print()
	}	
}
init()