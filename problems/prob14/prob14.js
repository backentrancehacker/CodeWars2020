const fs = require('fs')
const determine = num => (num % 2 == 0 )

const obj = val => (
	{
		value: val,
		arr: null,
		even: 0,
		odd: 0
	}
)

function init(){
	let details = fs.readFileSync(`${__dirname}/input.txt`,'utf8')

	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)

	let holder = []
	for(let i = parseInt(lines[0]); i < parseInt(lines[1]); i++){
		holder.push(obj(i))
	}
	let results = ''
	for(let n of holder){
		n.arr = String(n.value).split('').reverse()
		for(let i = 0; i < n.arr.length; i ++){
			if(determine(i)){
				n.odd += parseInt(n.arr[i])
			}
			else{
				n.even += parseInt(n.arr[i])
			}
		}
		if(n.even == n.odd) results += `${n.value} `
	}
	console.log(results.length >= 1 ? results : 'No Numbers found with Equal Sum in the given range!')
	
}
init()