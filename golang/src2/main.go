package main

import (
	"fmt"
	"io/ioutil"
	"strconv"
	"strings"
)

func sum(a int, b int) int {
	return a + b
}

func fibonacci(n int) int {
	if n == 0 {
		return 0
	}
	if n == 1 {
		return 1
	}
	return fibonacci(n-1) + fibonacci(n-2)
}

func readData(filename string) []int {
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Println("Error reading file")
		return nil
	}
	lines := strings.Split(string(data), "\n")
	var numbers []int

	for _, line := range lines {
		items := strings.Split(line, " ")
		for _, item := range items {
			number, err := strconv.Atoi(item)
			if err != nil {
				fmt.Println("Error converting number", item)
				return nil
			}
			numbers = append(numbers, number)
		}
	}
	return numbers
}

func main() {
	sumResult := sum(5, 10)
	fmt.Println("Sum: ", sumResult)

	fibResult := fibonacci(10)
	fmt.Println("Fibonacci 10: ", fibResult)

	data := readData("data.txt")
	for _, d := range data {
		fmt.Println(d)
	}

}
