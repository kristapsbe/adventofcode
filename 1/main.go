// https://adventofcode.com/2023/day/1
package main

import (
	"io/ioutil"
	"path/filepath"
	"strings"
)

func main() {
	// https://adventofcode.com/2023/day/1/input
	abs, err := filepath.Abs("./1/input.txt") // this feels really funky
	// open input file
	content, err := ioutil.ReadFile(abs) // https://www.scaler.com/topics/golang/golang-read-file/
	if err != nil {
		panic(err)
	}
	// convert the files content into a string
	str := string(content)
	// https://stackoverflow.com/questions/25080862/how-to-strings-split-on-newline
	lines := strings.Split(str, "\n")
	// https://www.geeksforgeeks.org/how-to-iterate-over-an-array-using-for-loop-in-golang/
	for i := 0; i < len(lines); i++ {
		tmp := lines[i]
		// https://www.educative.io/answers/what-is-the-unicodeisnumber-function-in-golang
		for j := 0; j < len(tmp); j++ {
			//if unicode.IsDigit(tmp[j]) {

			//}
		}
	}
}
