package main

import "fmt"

func main() {
	var A, B, C int
	var h, m int

	fmt.Scanln(&A, &B)
	fmt.Scanln(&C)

	h = ((A*60 + B + C) / 60) % 24

	m = (A*60 + B + C) % 60

	fmt.Println(h, m)

}
