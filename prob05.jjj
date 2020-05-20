const fs = require('fs')
function detect(num) {
    if (num < 0 ) return
    for (let i = 2; i < num; i++){
      	if(num % i == 0) return false
    }
    return num > 1
}
function init(){
	let details = fs.readFileSync(`${__dirname}/input.txt`,'utf8')
	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)
	let result = detect(parseInt(lines[0]))
	if(result) console.log(`${lines[0]} is PRIME`)
	else console.log(`${lines[0]} is NOT Prime`)
}
init()
