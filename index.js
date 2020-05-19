while (true){
	let num = prompt('Enter a problem number ').trim().padStart(2, '0')
	let prob = require(`./problems/prob${num}/prob${num}.js`)

}
