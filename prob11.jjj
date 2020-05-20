const fs = require('fs')
const convert = inp => ((inp >>> 0).toString(2))
const even = inp => (inp % 2 == 0 ? true : false)
function init(){
	let details = fs.readFileSync(`${__dirname}/input.txt`,'utf8')
	let tokens = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)

	for(let number of tokens){
		let result = 'yes',
			altered = convert(parseInt(number)),
			split = altered.split('')

		if(split[Math.floor((split.length - 1) / 2)] != 0) result = 'no'

		if(split.filter(part => part == 0).length > 1) result = 'no'

		if(even(altered.length)) result = 'no'

		console.log(`${number} ${result}`)
	}
}
init()