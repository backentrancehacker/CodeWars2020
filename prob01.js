const fs = require('fs')
function init(){
	let details = fs.readFileSync(`${__dirname}/input.txt`,'utf8')
	console.log(`Welcome to CodeWars, ${details}!`)
}

init()