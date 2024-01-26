package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Queue []string

func (q *Queue) Push(x string) {
	*q = append(*q, x)
}

func (q *Queue) Pop() (x string) {
	if len(*q) == 0 {
		return "-1"
	}
	x = (*q)[0]
	*q = (*q)[1:]
	return x
}

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer  = bufio.NewWriter(os.Stdout)
)

func main() {
	defer writer.Flush()

	var N int
	scanner.Scan()
	N, _ = strconv.Atoi(scanner.Text())

	queue := new(Queue)

	for i := 0; i < N; i++ {
		scanner.Scan()
		line := scanner.Text()
		words := strings.Split(line, " ")

		switch words[0] {
		case "push":
			queue.Push(words[1])
		case "pop":
			fmt.Fprintln(writer, queue.Pop())
		case "size":
			fmt.Fprintln(writer, len(*queue))
		case "empty":
			if len(*queue) == 0 {
				fmt.Fprintln(writer, "1")
			} else {
				fmt.Fprintln(writer, "0")
			}
		case "front":
			if len(*queue) == 0 {
				fmt.Fprintln(writer, "-1")
			} else {
				fmt.Fprintln(writer, (*queue)[0])
			}
		case "back":
			if len(*queue) == 0 {
				fmt.Fprintln(writer, "-1")
			} else {
				fmt.Fprintln(writer, (*queue)[len(*queue)-1])
			}
		}
	}
}
