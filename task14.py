def find_pattern(items: list, pattern: str, match_type: str) -> list:
    if match_type == "starts":
        return list(filter(lambda x: x.lower().startswith(pattern.lower()), items))
    
    elif match_type == "ends":
        return list(filter(lambda x: x.lower().endswith(pattern.lower()), items))
    
    elif match_type == "contains":
        return list(filter(lambda x: pattern.lower() in x.lower(), items))
    else:
        return []
print(find_pattern(["apple", "banana", "apricot", "grape"], "ap", "starts"))
# ["apple", "apricot"]