package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	S      string
	i      int
	reader = bufio.NewReader(os.Stdin)
	writer = bufio.NewWriter(os.Stdout)
)

func main() {
	defer writer.Flush()
	fmt.Fscan(reader, &S, &i)
	fmt.Fprint(writer, string(S[i-1]))
}
