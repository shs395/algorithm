package main

import (
	"bufio"
	"os"
	"sort"
	"strconv"
)

type Trie struct {
	children  map[rune]*Trie
	endOfWord bool
}

func (t *Trie) Insert(word string) {
	current := t
	for _, w := range word {
		if current.children[w] == nil {
			current.children[w] = &Trie{
				children: make(map[rune]*Trie),
			}
		}
		current = current.children[w]
	}
	current.endOfWord = true
}

func (t *Trie) Search(word string) bool {
	current := t
	for _, w := range word {
		if current.children[w] == nil {
			return false
		}
		current = current.children[w]
	}
	return current.endOfWord
}

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer  = bufio.NewWriter(os.Stdout)
)

func main() {
	defer writer.Flush()

	scanner.Scan()
	t, _ := strconv.Atoi(scanner.Text())

	for i := 0; i < t; i++ {
		trie := &Trie{children: make(map[rune]*Trie)}
		flag := true
		scanner.Scan()
		n, _ := strconv.Atoi(scanner.Text())
		arr := make([]string, n)

		for j := 0; j < n; j++ {
			scanner.Scan()
			arr[j] = scanner.Text()
		}

		sort.Strings(arr)

		for j := 0; j < n; j++ {
			for k := 0; k < len(arr[j]); k++ {
				if trie.Search(arr[j][:k+1]) == true {
					flag = false
					break
				}
			}
			if flag == false {
				break
			}
			trie.Insert(arr[j])
		}

		if flag == false {
			writer.WriteString("NO\n")
		} else {
			writer.WriteString("YES\n")
		}
	}

}
