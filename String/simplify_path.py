class Solution:
    def simplifyPath(self, path: str) -> str:
        path_ary = path.split("/")
        res = []
        for i, dir in enumerate(path_ary):
            if dir == '.' or not dir:
                continue
            elif dir == '..':
                if res:
                    res.pop()
                else:
                    continue
            else:
                res.append(dir)
        
        return "/" + "/".join(res)