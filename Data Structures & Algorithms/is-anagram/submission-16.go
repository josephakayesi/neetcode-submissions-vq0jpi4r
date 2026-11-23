func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	sCount := [26]int{}
	tCount := [26]int{}

	for _, v := range s {
		sCount[int(v) - int('a')] += 1
	}

	for _, v := range t {
		tCount[int(v) - int('a')] += 1
	}

	for i := 0; i < 26; i++ {
		if sCount[i] != tCount[i] {
			return false
		}
	}

	return true
}
