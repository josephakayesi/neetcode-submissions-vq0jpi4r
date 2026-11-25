func groupAnagrams(strs []string) [][]string {
	groups := map[[26]int][]string{}

	for _, word := range strs {
		key := key(word)
		groups[key] = append(groups[key], word)
	}

	var result [][]string 

	for _, g := range groups {
		result = append(result, g)
	}

	return result
}

func key(w string) [26]int {
	count := [26]int{}

	for _, c := range w {
		count[c-'a']++
	}
	return count
}
