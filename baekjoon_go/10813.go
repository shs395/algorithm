package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	reader := bufio.NewReaderSize(os.Stdin, 2048)
	writer := bufio.NewWriterSize(os.Stdout, 2048)
	defer writer.Flush()

	var N, M int
	fmt.Fscan(reader, &N, &M)

	arr := make([]int, N)

	for i := range arr {
		arr[i] = i + 1
	}

	for i := 0; i < M; i++ {
		var t1, t2 int
		fmt.Fscan(reader, &t1, &t2)

		tmp := arr[t1-1]
		arr[t1-1] = arr[t2-1]
		arr[t2-1] = tmp
	}
	for i := 0; i < N; i++ {
		fmt.Fprintf(writer, "%d ", arr[i])
	}

}
