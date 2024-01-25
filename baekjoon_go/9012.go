package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer  = bufio.NewWriter(os.Stdout)
)

func main() {
	defer writer.Flush()
	var T int
	scanner.Scan()
	T, _ = strconv.Atoi(scanner.Text())

	for i := 0; i < T; i++ {
		var stack []byte
		scanner.Scan()
		str := scanner.Text()

		for j := 0; j < len(str); j++ {
			if str[j] == 40 {
				stack = append(stack, str[j])
			} else if str[j] == 41 {
				if len(stack) == 0 {
					stack = append(stack, str[j])
					break
				} else if stack[len(stack)-1] == 40 {
					stack = stack[:len(stack)-1]
				} else {
					stack = append(stack, str[j])
					break
				}
			}
		}

		if len(stack) > 0 {
			fmt.Fprintln(writer, "NO")
		} else {
			fmt.Fprintln(writer, "YES")
		}

	}
}
