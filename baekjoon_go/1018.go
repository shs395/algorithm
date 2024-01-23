package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	N, M int
)

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()
	fmt.Fscan(reader, &N, &M)
	min := N * M
	arr := make([]string, N)

	for i := 0; i < N; i++ {
		fmt.Fscan(reader, &arr[i])
	}

	for i := 0; i < N-7; i++ {
		for j := 0; j < M-7; j++ {
			t := 0
			t2 := 0

			for x := i; x < i+8; x++ {
				for y := j; y < j+8; y++ {
					if (x+y)%2 == 0 && arr[x][y] == 'W' {
						t += 1
					}
					if (x+y)%2 == 1 && arr[x][y] == 'B' {
						t += 1
					}

					if (x+y)%2 == 0 && arr[x][y] == 'B' {
						t2 += 1
					}

					if (x+y)%2 == 1 && arr[x][y] == 'W' {
						t2 += 1
					}
				}
			}

			if t < min {
				min = t
			}

			if t2 < min {
				min = t2
			}

		}
	}

	fmt.Fprint(writer, min)
}
