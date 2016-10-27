"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    sep = s.split()
    freq = [sep.count(w) for w in sep]
    freq_dict = dict(zip(sep,freq))
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    aux = [(freq_dict(key),key) for key in freq_dict]
    aux.sort()
    for 
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()

    
    https://www.youtube.com/watch?v=OQ5jsbhAv_M
