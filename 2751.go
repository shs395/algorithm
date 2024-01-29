package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer  = bufio.NewWriter(os.Stdout)
)

func main() {
	defer writer.Flush()
	scanner.Scan()
	N, _ := strconv.Atoi(scanner.Text())

	arr := make([]int, N)

	for i := 0; i < N; i++ {
		scanner.Scan()
		x, _ := strconv.Atoi(scanner.Text())
		arr[i] = x
	}

	sort.Ints(arr)

	for i := 0; i < N; i++ {
		writer.WriteString(strconv.Itoa(arr[i]) + "\n")
	}

}
