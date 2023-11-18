class TestDataEmptyArray(object):
    @staticmethod
    def get_array():
        # Returns an empty array
        return []

class TestDataUniqueValues(object):
    @staticmethod
    def get_array():
        # Returns an array of at least two unique elements
        return [5, 2, 8, 3, 4]

    @staticmethod
    def get_expected_result():
        # Returns the expected minimum value index for this array
        return 1  # Index of the smallest element 2

class TestDataExactlyTwoDifferentMinimums(object):
    @staticmethod
    def get_array():
        # Returns an array where the minimum value occurs at exactly 2 indices
        return [1, 3, 1, 2]

    @staticmethod
    def get_expected_result():
        # Returns the expected index of the first occurrence of the minimum value
        return 0  # Index of the first occurrence of value 1

def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False

def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2
    assert len(list(set(seq))) == len(seq)
    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

def TestWithExactlyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])
    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

# Run the tests
TestWithEmptyArray()
TestWithUniqueValues()
TestWithExactlyTwoDifferentMinimums()
print("OK")
