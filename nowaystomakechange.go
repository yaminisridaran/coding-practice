package main

import "fmt"

func noofwaystomakechange(n int, denoms []int) int {
	ways := make([]int, n+1)
	ways[0] = 1
	for _, denom := range denoms {
		for amount := 1; amount < n+1; amount++ {
			if denom <= amount {
				ways[amount] += ways[amount-denom]
			}
		}
	}
	return ways[n]
}

func main() {
	denoms := []int{1, 2, 3}
	target := 4
	fmt.Println(noofwaystomakechange(target, denoms))
}
