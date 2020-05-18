const fs = require('fs')
function soda(a, b){
	a = Math.abs(a)
	b = Math.abs(b)
	while(b){
		let factor = b
		b = a % b
		a = factor
	}
	return a
}
function init(){
	let details = fs.readFileSync(`${__dirname}/input.txt`,'utf8')
	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)
	console.log(soda.apply(null, lines))

}
init()
