func groupAnagrams(strs []string) [][]string {
	words := map[string][]string{}

	for _, word := range strs {
		key := keystring(word)
		words[key] = append(words[key], word)
	}

	var result [][]string 

	for _, v := range words {
		result = append(result, v)
	}

	return result
}

func keystring(w string) string {
	count := [26]int{}

	for _, c := range w {
		count[c-'a']++
	}

	var key string 

	for _, v := range count {
		key = key + strconv.Itoa(v) + "#"
	}

	return key
}
