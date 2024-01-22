package main

import "fmt"

func main() {
	var N, v int
	fmt.Scan(&N)

	var a = make([]int, N)

	for i := 0; i < N; i++ {
		fmt.Scan(&a[i])
	}

	fmt.Scan(&v)

	cnt := 0

	for i := 0; i < N; i++ {
		if a[i] == v {
			cnt++
		}
	}

	fmt.Println(cnt)

}
