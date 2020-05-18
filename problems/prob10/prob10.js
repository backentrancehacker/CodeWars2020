const fs = require('fs')
const tree = {
	NOUNS: [],
	ADVERBS: [],
	VERBS: [],
	ADJECTIVES: []
}

const map = {
	'[AJ]': 'ADJECTIVES',
	'[N]' : 'NOUNS',
	'[AV]': 'ADVERBS',
	'[V]' : 'VERBS'
}
const len = (json) => {
	for(let key in json){
		if(json[key].length) return true
	}
	return false
}
function init(){
	let details = fs.readFileSync(`${__dirname}/input.txt`,'utf8')
	let tokens = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)

	let base = tokens[0]
	tokens.shift()

	let index = 0,
		mode

	while(index < tokens.length - 1){
		let token = tokens[index]
		mode = token.match(/NOUNS|ADVERBS|VERBS|ADJECTIVES/) ? token : mode
		if(token != mode)
			tree[mode].push(token)
		index++
	}

	let phrases = []
	main: 
	while(len(tree)){
		let altered = base.split(' ')
		for(let i = 0; i < altered.length; i++){
			let loc = altered[i]
			if(map.hasOwnProperty(loc)){
				let trans = map[loc]
				let arr = tree[trans]
				if(!arr[0]) break main
				altered[i] = arr[0]
				tree[trans].shift()
			}
		}
		phrases.push(altered.join(' '))	
	}
	console.log(phrases.join('\n'))

}

init()