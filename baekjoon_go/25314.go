package main

import "fmt"

func main() {
	var N int
	fmt.Scan(&N)

	for i := 0; i < N/4; i++ {
		fmt.Printf("long ")
	}
	fmt.Printf("int")

}
