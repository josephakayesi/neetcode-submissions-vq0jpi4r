class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let sMap = {}
        let tMap = {}

        if(s.length !== t.length) return false 

        for(let i = 0; i < s.length; i++){
            sMap[s[i]] = sMap[s[i]] ? sMap[s[i]] + 1 : 1
            tMap[t[i]] = tMap[t[i]] ? tMap[t[i]] + 1 : 1
        }

        for(let key of Object.keys(sMap)){
            if(sMap[key] !== tMap[key]) return false
        }

        return true
    }
}
