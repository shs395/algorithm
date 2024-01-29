package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var (
	rw = bufio.NewReadWriter(bufio.NewReader(os.Stdin), bufio.NewWriter(os.Stdout))
	N  int
)

func main() {
	defer rw.Flush()
	fmt.Fscan(rw, &N)
	var arr []int
	for i := 0; i < N; i++ {
		var x int
		fmt.Fscan(rw, &x)
		arr = append(arr, x)
	}
	sort.Ints(arr)

	for _, x := range arr {
		fmt.Fprintln(rw, x)
	}
}
