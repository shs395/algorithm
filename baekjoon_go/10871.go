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

	var N, X int

	fmt.Fscan(reader, &N, &X)

	for i := 0; i < N; i++ {
		var tmp int
		fmt.Fscan(reader, &tmp)

		if tmp < X {
			fmt.Fprintf(writer, "%d ", tmp)
		}

	}

}
