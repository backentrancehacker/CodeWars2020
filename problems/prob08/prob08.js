const fs = require('fs')

function insert(input, _split, res) {
    if (input.length <= _split) {
        res.push(input)
        return res
    }
    let line = input.substring(0, _split),
		i = line.search(/\s(?!.*\s)/),
		next = _split
    if (i > 0) {
        line = line.substring(0, i)
        next = i
    }
    res.push(line)
    return insert(input.substring(next), _split, res)
}

// function foldRgx(s, n) {
//     var rgx = new RegExp('.{0,' + n + '}', 'g');
//     return s.match(rgx);
// }

    
function init(){
	let details = fs.readFileSync(`${__dirname}/input.txt`,'utf8')
	let line = details.trim(),
		altered = new Array

	insert(line, 80, altered)
	console.log(altered.map(inp => inp.trim()).filter(inp => inp.length).join('\n'))
}
init()
