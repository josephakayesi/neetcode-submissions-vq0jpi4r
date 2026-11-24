import (
	"slices"
)

func topKFrequent(nums []int, k int) []int {
	// Use bucket sorting for this problem
	// Keep a map with each element and its count. 
	// Keep a bucket (array of arrays) where the index is the frequency of the elements
	// Append the element to the array corresponding to its frequency
	// Iterate in reverse order and for each non-empty array, append the element to the resulting array

	// Explore the priority queue solution for this

	frequency := map[int]int{}

	for _, num := range nums {
		frequency[num]++
	}

	buckets := make([][]int, len(nums) + 1)

	for num, count := range frequency {
		buckets[count] = append(buckets[count], num)
	}

	result := []int{}

	for _, bucket := range slices.Backward(buckets) {
		for _, num := range bucket {

			result = append(result, num)

			if len(result) == k {
				return result
			}
		}
	}

	return []int{}
}
