package main

import "fmt"

func main() {
	var T int
	fmt.Scan(&T)

	for i := 0; i < T; i++ {
		var tmp string
		fmt.Scan(&tmp)
		fmt.Println(string(tmp[0]) + string(tmp[len(tmp)-1]))
	}

}
