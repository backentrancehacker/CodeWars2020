const fs = require('fs')

const convert = input => {
	let output = []
	for(let i = 0; i < input.length; i ++){
		output.push((input.charCodeAt(i)).toString(16))
	}
	return output
}
const decrypt = input => {
	let output = convert(input.replace(/ /g, ''))
	console.log(output.join(' '))
	output = ' ' + output.join('')

	let part = ''

	
	for(let i = 1; i < output.length; i ++){
		if(i % 4 == 0) part += output.charAt(i)

	}
	
	let secret = String.fromCharCode.apply(null, part.match(/(..?)/g).map(inp => parseInt(inp, 16)))
	console.log(secret)
	// console.log(revert(part.join('.')))
}
function init(){
	let details = await fs.readFileSync(`${__dirname}/input.txt`,'utf8')

	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)
	decrypt(lines[0])
}
init()