const fs = require('fs')
const side = 25 * 60

const toSeconds = (num) => {
	return num * 60
}
function inverse(arr){
	let cache = []
	for(let i of arr) cache.push(i * -1)
	return cache
}
function toFormat(_sec){
	let i = Math.abs(_sec),
		min = Math.floor(i / 60)

	let time = [
		min,
		i - (min * 60)
	]
	return i != _sec ? inverse(time) : time
}
function init(){
	let details = fs.readFileSync(`${__dirname}/input.txt`,'utf8')
	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)

	for(let line of lines){
		let nums = line.split(' '),	
			seconds = toSeconds(parseInt(nums[0])) + parseInt(nums[1])

		if(seconds == 0) return
		
		let message = '',
			remaining = (side * 2) - seconds

		if(remaining < 0) message = "(we're gonna need a bigger record)"
		else if(side < seconds) message = "(we'll need both sides)"

		let format = toFormat(remaining)
		console.log(`Time remaining ${format[0]} minutes ${format[1]} seconds ${message}`)
	}
}
init()
