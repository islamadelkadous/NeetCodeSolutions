class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return '##_##'
        return '.'.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == '##_##':
            return []
        return s.split('.')
