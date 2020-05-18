const fs = require('fs')
const max_minutes =  
function init(){
	let details = fs.readFileSync(`${__dirname}/input.txt`,'utf8')
	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)

	main: 
	for(let line of lines){
		let nums = line.split(' ')
		let i1 = parseInt(nums[0]),
			i2 = parseInt(nums[1])
		if(i1 == 0 && i2 == 0) break main


	}
}
init()
