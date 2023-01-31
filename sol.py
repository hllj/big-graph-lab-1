class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        next_word = {}
        wordList.append(beginWord)
        for word in wordList:
            n = len(word)
            for i in range(n):
                change = word[:i] + "*" + word[i + 1:]
                if change not in next_word:
                    next_word[change] = [word]
                else:
                    next_word[change].append(word)
        # print(next_word)
        q = []
        q.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)
        while len(q) > 0:
            word, cnt = q.pop(0)
            n = len(word)
            for i in range(n):
                change = word[:i] + "*" + word[i + 1:]
                for nxt in next_word[change]:
                    if nxt not in visited:
                        q.append((nxt, cnt + 1))
                        visited.add(nxt)
                        if nxt == endWord:
                            return cnt + 1
        return 0