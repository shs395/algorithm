package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	reader = bufio.NewReader(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
	N, M   int
)

func main() {
	defer writer.Flush()
	fmt.Fscan(reader, &N, &M)

	var arr = make([]int, N)

	for v := 0; v < M; v++ {
		var i, j, k int
		fmt.Fscan(reader, &i, &j, &k)
		for w := i; w <= j; w++ {
			arr[w-1] = k
		}
	}

	for v := 0; v < N; v++ {
		fmt.Fprintf(writer, "%d ", arr[v])
	}
}
