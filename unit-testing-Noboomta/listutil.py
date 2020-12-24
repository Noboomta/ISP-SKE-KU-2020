def unique(list):
    """Return a list containing only the first occurence of each distinct
       element in list, in the same order as the first occurences in the
       list parameter.

    Arguments:
        list: a list of elements (not modified)
    Returns:
        a new list containing only distinct elements from list,
        in the same order as they first appear in list

    Examples:
    >>> unique([5])
    [5]
    >>> unique(["b","a","a","b","b","b","a","a"])
    ['b', 'a']
    >>> unique([])
    []
    """
    ans = []
    for ele in list:
        if(ele not in ans):
            ans.append(ele)
    return ans

if __name__ == "__main__":
    """Run the doctests in all methods."""
    import doctest
    doctest.testmod(verbose=True)
