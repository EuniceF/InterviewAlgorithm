class Solution:
    def permutation(self, st):
        if st == '':
            return []
        res = []
        self.helper(st, res, '')
        return sorted(set(res))
    
    def helper(self, st, res, path):
        if st == '':
            res.append(path)
        else:
            for i in range(len(st)):
                self.helper(st[:i] + st[i+1:], res, path + st[i])

# test
test = Solution()
print(test.permutation('abb'))
print(test.permutation('abc'))