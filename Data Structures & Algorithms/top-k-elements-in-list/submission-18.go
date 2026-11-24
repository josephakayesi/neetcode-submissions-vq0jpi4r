import "slices"

func topKFrequent(nums []int, k int) []int {
	// Use bucket sorting for this problem
	// Keep a map with each element and its count. 
	// Keep a bucket (array of arrays) where the index is the frequency of the elements
	// Append the element to the array corresponding to its frequency
	// Iterate in reverse order and for each non-empty array, append the element to the resulting array

	// Explore the priority queue solution for this

	frequency := map[int]int{}

	for _, num := range nums {
		if _, ok := frequency[num]; ok {
			frequency[num]++
		} else {
			frequency[num] = 1
		}
	}

	buckets := make([][]int, len(nums) + 1)

	for k, v := range frequency {
		buckets[v] = append(buckets[v], k)
	}

	result := []int{}

	for _, b := range slices.Backward(buckets) {
		for _, v := range b {
			result = append(result, v)

			if len(result) == k {
				return result
			}
		}
	}

	return result
}
