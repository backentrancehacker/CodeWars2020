const fs = require('fs')
function init(){
	let details = fs.readFileSync(`${__dirname}/input.txt`,'utf8')
	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)
	for(let line of lines){
		console.log(parseInt(line.split('').reverse().join('')))
	}
}

init()