"""Search helpers. Complete the five function bodies, then run the doctests."""


def number_lines(lines):
    """Return (line_number, text) tuples, counting from 1.

    >>> number_lines(['Library hours', '', 'Open late'])
    [(1, 'Library hours'), (2, ''), (3, 'Open late')]
    >>> number_lines([])
    []
    """
    result = []
    for number, text in enumerate(lines, start=1):
        result.append((number, text))
    return result


def matching_lines(lines, query):
    """Return numbered lines containing query, ignoring case.

    An empty query returns no matches. Preserve the original text and numbers.

    >>> matching_lines(['Library hours', '', 'LIBRARY cafe'], 'library')
    [(1, 'Library hours'), (3, 'LIBRARY cafe')]
    >>> matching_lines(['Library hours'], '')
    []
    >>> matching_lines(['Library hours'], 'pool')
    []
    """
    if not query:
        return []
    result = []
    for number, text in enumerate(lines, start=1):
        if query.lower() in text.lower():
            result.append((number, text))
    return result


def group_matches(documents, query):
    """Return one list of matching lines per document, including empty lists.

    >>> group_matches([['Library map'], ['Pool hours'], ['LIBRARY cafe']], 'library')
    [[(1, 'Library map')], [], [(1, 'LIBRARY cafe')]]
    >>> group_matches([], 'library')
    []
    """
    result = []
    for lines in documents:
        matches = matching_lines(lines, query)
        result.append(matches)
    return result


def flatten_matches(names, groups):
    """Return (filename, line_number, text) tuples in file and line order.

    names and groups have equal lengths. Filenames are unique.

    >>> flatten_matches(['a.txt', 'b.txt'], [[(2, 'Map')], []])
    [('a.txt', 2, 'Map')]
    >>> flatten_matches([], [])
    []
    """
    result = []
    for name, group in zip(names, groups):
        for line_number, text in group:
            result.append((name, line_number, text))
    return result


def match_counts(names, groups):
    """Return a dictionary of filename: number of matching lines, including zeros.

    names and groups have equal lengths. Filenames are unique.

    >>> match_counts(['a.txt', 'b.txt'], [[(2, 'Map')], []])
    {'a.txt': 1, 'b.txt': 0}
    >>> match_counts([], [])
    {}
    """
    result = {}
    for name, group in zip(names, groups):
        result[name] = len(group)
    return result