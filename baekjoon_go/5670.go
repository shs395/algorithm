package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
)

type Trie struct {
	children  map[rune]*Trie
	endOfWord bool
}

func (t *Trie) Insert(word string) {
	current := t
	for _, c := range word {
		if current.children[c] == nil {
			current.children[c] = &Trie{
				children: make(map[rune]*Trie),
			}
		}
		current = current.children[c]
	}
	current.endOfWord = true
}

func (t *Trie) Search(word string) bool {
	current := t
	for _, c := range word {
		if current.children[c] == nil {
			return false
		}
		current = current.children[c]
	}
	return current.endOfWord
}

func dfs(t *Trie, num int, p *int) {
	current := t
	tmpSum := num

	if current.endOfWord == true {
		*p += tmpSum
	}
	for key := range current.children {
		if len(current.children) >= 2 {
			dfs(current.children[key], tmpSum+1, p)
		} else if len(current.children) == 1 {
			if current.endOfWord == true {
				dfs(current.children[key], tmpSum+1, p)

			} else {
				dfs(current.children[key], tmpSum, p)

			}
		}
	}
}

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer  = bufio.NewWriter(os.Stdout)
)

func main() {
	for scanner.Scan() {
		N, _ := strconv.Atoi(scanner.Text())
		if N == 0 {
			break
		}
		trie := &Trie{children: make(map[rune]*Trie)}

		for i := 0; i < N; i++ {
			scanner.Scan()
			word := scanner.Text()
			trie.Insert(word)
		}

		result := 0
		p := &result

		for key := range trie.children {
			dfs(trie.children[key], 1, p)
		}

		fmt.Printf("%.2f\n", math.Round((float64(result)/float64(N)*100))/100)

	}

}
