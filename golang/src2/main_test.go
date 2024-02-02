package main

import "testing"

func TestSum(t *testing.T) {
	result := sum(2, 3)
	expected := 5
	if result != expected {
		t.Errorf("sum(2, 3) returned %d, expected %d", result, expected)
	}
}

func TestFibonacci(t *testing.T) {
	tests := []struct {
		n        int
		expected int
	}{
		{0, 0},
		{1, 1},
		{2, 1},
		{3, 2},
		{4, 3},
		{5, 5},
		// Add more test cases as needed
	}

	for _, test := range tests {
		result := fibonacci(test.n)
		if result != test.expected {
			t.Errorf("fibonacci(%d) returned %d, expected %d", test.n, result, test.expected)
		}
	}
}

func TestReadData(t *testing.T) {
	filename := "testdata/data.txt"
	expected := []int{1, 2, 3, 4, 5}

	result := readData(filename)

	if len(result) != len(expected) {
		t.Errorf("readData(%s) returned %v, expected %v", filename, result, expected)
		return
	}

	for i := 0; i < len(result); i++ {
		if result[i] != expected[i] {
			t.Errorf("readData(%s) returned %v, expected %v", filename, result, expected)
			return
		}
	}
}
