package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	reader = bufio.NewReader(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
	K, sum int
	stack  []int
)

func main() {
	defer writer.Flush()

	fmt.Fscan(reader, &K)

	for i := 0; i < K; i++ {
		var tmp int
		fmt.Fscan(reader, &tmp)

		if tmp == 0 {
			stack = stack[:len(stack)-1]
		} else {
			stack = append(stack, tmp)
		}
	}

	for _, x := range stack {
		sum += x
	}

	fmt.Fprint(writer, sum)

}
