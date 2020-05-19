const fs = require('fs')

function init(){
	let details = fs.readFileSync(`${__dirname}/input.txt`,'utf8')

	let lines = details.split('\n').map(inp => inp.trim()).filter(inp => inp.length)
	for(let i = 0; i < lines.length - 3; i++){
		let line = lines[i]
		if(!isNaN(line.replace(/ /, ''))){
			let sentences = [
				[...new Set(lines[i + 1].split(' '))].join(' '),
				[...new Set(lines[i + 2].split(' '))].join(' ')
			]

			let statement = sentences.join(' ').split(' ').map(inp => inp.trim()).filter(inp => inp.length)

			let tree = {}

			for(let word of statement){
				if(word[0].toUpperCase() == word[0]) word = word.toLowerCase()
				if(!tree[word]) tree[word] = 1
				else tree[word] += 1
			}
			let duplicates = ''
			for(let key in tree){
				if(tree[key] > 1) duplicates += `${key} `
			}
			console.log(lines[i + 1])
			console.log(lines[i + 2])
			console.log(duplicates.split(' ').length - 1, duplicates)
		}
	}
}
init()