package main

import (
	"bufio"
	"fmt"
	"os"
)

var reader = bufio.NewReader(os.Stdin)
var writer = bufio.NewWriter(os.Stdout)

func main() {
	defer writer.Flush()

	var N int
	min := 1000001
	max := -1000001

	fmt.Fscan(reader, &N)

	for i := 0; i < N; i++ {
		var tmp int
		fmt.Fscan(reader, &tmp)
		if tmp > max {
			max = tmp
		}

		if tmp < min {
			min = tmp
		}
	}
	fmt.Fprintf(writer, "%d ", min)
	fmt.Fprintf(writer, "%d ", max)
}
