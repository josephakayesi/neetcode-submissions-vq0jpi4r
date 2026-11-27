type Solution struct{}

// Note that ASCII characters includes `a-zA-Z0-9*_()` and perhaps others I have not considered. 
// To use a separator to encode the string maybe inefficient as genuine text could be misinterpreted
// To make this efficient and make it work I iterate through each string and calculate its length
// For each length I will encode the metadata of the string using the formula `{len(string)}#{string}`
// To decode: I will iterate the encoded string. I will keep iterating till I find the next `#` which tells me that the len(string) has reached
// Now for the next set of characters i will iterate the length of string to get the word it forms and store it in my result

func (s *Solution) Encode(strs []string) string {
	var encoded strings.Builder

	for _, str := range strs {
		encoded.WriteString(strconv.Itoa(len(str)))
		encoded.WriteByte('#')
		encoded.WriteString(str)
	}

	return encoded.String()
}


func (s *Solution) Decode(encoded string) []string {
	result := []string{}
	i := 0
	current := 0

	for i < len(encoded) {
		if encoded[i] == '#' {
			start, end := i + 1, current + i + 1
			result = append(result, encoded[start:end])
			i = i + current + 1
			current = 0
			continue
		}
		
		current = current*10 + int(encoded[i]-'0')
		i++
	}

	return result	
}
