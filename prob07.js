const fs = require('fs')
let colors = ['RED', 'PURPLE', 'BLUE', 'GREEN', 'YELLOW', 'ORANGE']

Array.prototype.index = function(target) {
	for(let i = 0; i < this.length; i++){
		if(target == this[i]) return i
	}
	return
}

function mix(c1, c2){
	if(!colors.includes(c1)) return c1 == 'WHITE' ? `LIGHT ${c2}` : `DARK ${c2}`
	
	else if(!colors.includes(c2)) return c2 == 'WHITE' ? `LIGHT ${c1}` : `DARK ${c1}`
	else{
		let _i1 = colors.index(c1),
			_i2 = colors.index(c2)

		let i1 = Math.max(_i1, _i2),
			i2 = Math.min(_i1, _i2)

		return (i1 - i2 < (i2 + colors.length) - i1) ?  colors[Math.floor((i1+i2)/2)] : colors[Math.floor((i1 + i2 + colors.length)/2) % colors.length]
	}
}

function init(){
	let details = fs.readFileSync(`${__dirname}/input.txt`,'utf8')
	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)
	
	for(let line of lines){
		console.log(mix.apply(null, line.split(' ').map(inp => inp.trim())))
	}
}
init()
