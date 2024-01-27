package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type Deque struct {
	DequeBack  []int
	DequeFront []int
}

func (deque *Deque) PushFront(x int) {
	deque.DequeFront = append(deque.DequeFront, x)
}

func (deque *Deque) PushBack(x int) {
	deque.DequeBack = append(deque.DequeBack, x)
}

func (deque *Deque) PopFront() (x int) {
	if len(deque.DequeBack)+len(deque.DequeFront) == 0 {
		return -1
	}

	if len(deque.DequeFront) != 0 {
		x = deque.DequeFront[len(deque.DequeFront)-1]
		deque.DequeFront = deque.DequeFront[:len(deque.DequeFront)-1]
		return
	}

	x = deque.DequeBack[0]
	deque.DequeBack = deque.DequeBack[1:]
	return
}

func (deque *Deque) PopBack() (x int) {
	if len(deque.DequeBack)+len(deque.DequeFront) == 0 {
		return -1
	}

	if len(deque.DequeBack) != 0 {
		x = deque.DequeBack[len(deque.DequeBack)-1]
		deque.DequeBack = deque.DequeBack[:len(deque.DequeBack)-1]
		return
	}

	x = deque.DequeFront[0]
	deque.DequeFront = deque.DequeFront[1:]
	return
}

func (deque *Deque) CountDeque() int {
	return len(deque.DequeBack) + len(deque.DequeFront)
}

func (deque *Deque) IsDequeEmpty() int {
	if len(deque.DequeBack) == 0 && len(deque.DequeFront) == 0 {
		return 1
	}
	return 0
}

func (deque *Deque) PrintFirst() (x int) {
	if deque.IsDequeEmpty() == 1 {
		return -1
	}

	if len(deque.DequeFront) != 0 {
		x = deque.DequeFront[len(deque.DequeFront)-1]
		return
	}

	x = deque.DequeBack[0]
	return
}

func (deque *Deque) PrintBack() (x int) {
	if deque.IsDequeEmpty() == 1 {
		return -1
	}
	if len(deque.DequeBack) != 0 {
		x = deque.DequeBack[len(deque.DequeBack)-1]
		return
	}

	x = deque.DequeFront[0]
	return
}

var (
	scanner = bufio.NewScanner(os.Stdin)
	writer  = bufio.NewWriter(os.Stdout)
)

func main() {
	scanner.Scan()
	defer writer.Flush()
	N, _ := strconv.Atoi(scanner.Text())
	deque := new(Deque)

	for i := 0; i < N; i++ {
		scanner.Scan()
		switch command := scanner.Text(); command[0] {
		case 49:
			x, _ := strconv.Atoi(command[2:])
			deque.PushFront(x)
		case 50:
			x, _ := strconv.Atoi(command[2:])
			deque.PushBack(x)
		case 51:
			fmt.Fprintln(writer, deque.PopFront())
		case 52:
			fmt.Fprintln(writer, deque.PopBack())
		case 53:
			fmt.Fprintln(writer, deque.CountDeque())
		case 54:
			fmt.Fprintln(writer, deque.IsDequeEmpty())
		case 55:
			fmt.Fprintln(writer, deque.PrintFirst())
		case 56:
			fmt.Fprintln(writer, deque.PrintBack())
		}

	}
}
