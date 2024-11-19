def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]
    
    for str in strs[1:]:
        while not str.startswith(prefix):
            prefix = prefix[:-1]
            
    if not prefix:
        return ""
    
    return prefix

strs = ["flower", "flow", "flight"]

print(longest_common_prefix(strs))
    
    
    
    