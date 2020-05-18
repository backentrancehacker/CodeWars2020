const stdin = process.stdin
const input = question => {
	console.log(question)

	stdin.resume()

	stdin.setEncoding('utf8')
	return new Promise((resolve, reject) => {
		stdin.on('data', (data) => {
			resolve(data)
			stdin.pause()
		})
	})
}

module.exports.input = input