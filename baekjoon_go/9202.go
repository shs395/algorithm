package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

type Trie struct {
	children  map[rune]*Trie
	endOfWord bool
}

func (t *Trie) Insert(s string) {
	current := t
	for _, c := range s {
		if current.children[c] == nil {
			current.children[c] = &Trie{
				children: make(map[rune]*Trie),
			}
		}
		current = current.children[c]
	}
	current.endOfWord = true
}

func (t *Trie) Search(s string) bool {
	current := t
	for _, c := range s {
		if current.children[c] == nil {
			return false
		}
		current = current.children[c]
	}
	return current.endOfWord
}

func makeSliceUnique(s []string) []string {
	keys := make(map[string]struct{})
	res := make([]string, 0)
	for _, val := range s {
		if _, ok := keys[val]; ok {
			continue
		} else {
			keys[val] = struct{}{}
			res = append(res, val)
		}
	}
	return res
}

func dfs(
	x int, y int,
	boggleWords *[]string,
	boggle [4]string,
	visited [4][4]bool,
	word string,
	trie *Trie,
	found map[string]bool,
) {
	for i := 0; i < 8; i++ {
		nx := x + dx[i]
		ny := y + dy[i]

		if (nx >= 0 && nx <= 3) &&
			(ny >= 0 && ny <= 3) &&
			visited[nx][ny] == false {
			if trie.children[rune(boggle[nx][ny])] != nil {
				newWord := word + string(boggle[nx][ny])
				visited[nx][ny] = true
				if trie.children[rune(boggle[nx][ny])].endOfWord == true {
					// if found[]
					*boggleWords = append(*boggleWords, newWord)
				}
				dfs(nx, ny, boggleWords, boggle, visited, newWord, trie.children[rune(boggle[nx][ny])], found)
				visited[nx][ny] = false
			}
		}
	}
}

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer  = bufio.NewWriter(os.Stdout)
	dx      = [8]int{-1, -1, -1, 0, 0, 1, 1, 1}
	dy      = [8]int{1, 0, -1, 1, -1, 1, 0, -1}
)

func main() {
	defer writer.Flush()

	scanner.Scan()
	w, _ := strconv.Atoi(scanner.Text())
	trie := &Trie{children: make(map[rune]*Trie)}

	for i := 0; i < w; i++ {
		scanner.Scan()
		trie.Insert(scanner.Text())
	}

	scanner.Scan()
	scanner.Scan()
	b, _ := strconv.Atoi(scanner.Text())

	for i := 0; i < b; i++ {
		var boggle [4]string
		var boggleWords []string

		for j := 0; j < 4; j++ {
			scanner.Scan()
			boggle[j] = scanner.Text()
		}

		// dfs
		for j := 0; j < 4; j++ {
			for k := 0; k < 4; k++ {
				if trie.children[rune(boggle[j][k])] != nil {
					var visited [4][4]bool
					var found map[string]bool
					visited[j][k] = true
					dfs(j, k, &boggleWords, boggle, visited, string(boggle[j][k]), trie.children[rune(boggle[j][k])], found)
					visited[j][k] = false
				}
			}
		}

		boggleWords = makeSliceUnique(boggleWords)

		sort.Slice(boggleWords, func(i, j int) bool {
			if len(boggleWords[i]) == len(boggleWords[j]) {
				return boggleWords[i] < boggleWords[j]
			}
			return len(boggleWords[i]) > len(boggleWords[j])
		})

		sum := 0
		score := map[int]int{
			1: 0,
			2: 0,
			3: 1,
			4: 1,
			5: 2,
			6: 3,
			7: 5,
			8: 11,
		}

		// fmt.Println(boggleWords)

		for _, x := range boggleWords {
			sum += score[len(x)]
		}

		fmt.Fprintln(writer, sum, boggleWords[0], len(boggleWords))

		if i != b-1 {
			scanner.Scan()
		}
	}
}
