# Complete the function below.
def _max_florists(occupied_paths, florist_intervals, low, high, count, end_index):
    if low < high:
        print(occupied_paths)
        print(low)
        current_florist = florist_intervals[low]
        exceed = False
        if current_florist[0] > end_index:
            return _max_florists(occupied_paths, florist_intervals, low + 1, high, count, end_index)

        for i in range(current_florist[0], current_florist[1]):
            key = str(i) + '-' + str(i + 1)
            # print('key is: ', key)
            if key not in occupied_paths:
                break;
            if occupied_paths[key] >= 3:
                exceed = True
                break;
        if not exceed:
            original_dict = occupied_paths.copy()
            for i in range(current_florist[0], current_florist[1]):
                key = str(i) + '-' + str(i + 1)
                if key in occupied_paths:
                    occupied_paths[key] += 1
            count = max(_max_florists(original_dict, florist_intervals, low + 1, high, count, end_index),
                        _max_florists(occupied_paths, florist_intervals, low + 1, high, count + 1, end_index))
    return count


def max_florists(path_length, florist_intervals):
    print(path_length)
    print(florist_intervals)

    occupied_paths = {}

    for i in range(0, path_length):
        key = str(i) + '-' + str(i + 1)
        occupied_paths[key] = 0
    print(occupied_paths)

    return _max_florists(occupied_paths, florist_intervals, 0, len(florist_intervals), 0, path_length)


if __name__ == "__main__":
    #res = max_florists(9, [[1,10],[1,6], [2,8], [3,5]])

    #res = max_florists(16, [[1, 10], [1, 6], [1, 7],[10, 16], [10, 14]])
    #res = max_florists(5, [[1, 5], [1, 2], [2, 3], [3, 4], [4, 5]])
    res = max_florists(0, [[1,2]])
    #res = max_florists(16, [[1, 10], [19, 20], [1, 6], [1, 7], [10, 16], [10, 14], [10, 19]]) # failed
    print(res)