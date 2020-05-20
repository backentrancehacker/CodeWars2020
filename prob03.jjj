const fs = require('fs')
function factor(a, b){
	a = Math.abs(a)
	b = Math.abs(b)
	while(b){
		let _factor = b
		b = a % b
		a = _factor
	}
	return a
}
function init(){
	let details = fs.readFileSync(`${__dirname}/input.txt`,'utf8')
	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)
	console.log(factor.apply(null, lines))

}
init()
