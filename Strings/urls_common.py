from urllib.parse import urlparse

def urls_common(firstr, second):
    p1 = urlparse(firstr)
    p2 = urlparse(second)
    common = p1.scheme + '://'
    if p1.netloc == p2.netloc:
        common += p1.netloc
        # Find common path
        path1 = p1.path.split('/')
        path2 = p2.path.split('/')
        common_path = []
        for a, b in zip(path1, path2):
            if a == b:
                common_path.append(a)
            else:
                break
        common += '/'.join(common_path)
        if common_path and not common.endswith('/'):
            common += '/'
    return common

url1 = "https://www.example.com/path/to/resource"
url2 = "https://www.exampfsdfle.com/path/to/another"
common_url = urls_common(url1, url2)
print(common_url)