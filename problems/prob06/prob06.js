const fs = require('fs')

let map={1:"B",2:"BB",3:"BBB",4:"BW",5:"W",6:"WB",7:"WBB",8:"WBBB",9:"BK",10:"Z",20:"ZZ",30:"ZZZ",40:"ZP",50:"P",60:"PZ",70:"PZZ",80:"PZZZ",90:"ZB",100:"B",200:"BB",300:"BBB",400:"BG",500:"G",600:"GB",700:"GBB",800:"GBBB",900:"BR",1000:"R"}

function translate(num){
	let split = num.split('').reverse()
	let results = []
	for(let i = 0; i < split.length; i++){
		let part = split[i]
		part = part.padEnd(i + 1, '0')
		results.push(parseInt(part))
	}
	results = results.reverse()
	let translated = ''
	for(let result of results){
		translated += map[result] || ''
	}
	return translated
}
function init(){
	let details = fs.readFileSync(`${__dirname}/input.txt`,'utf8')
	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)
	
	for(let line of lines){
		console.log(translate(line))
	}
}
init()
