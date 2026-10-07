"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps 
and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:
TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. 
    If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

Example 1:
Input:
["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]
Output:
[null, null, "happy", "happy", null, "sad"]

Explanation:
TimeMap timeMap = new TimeMap();
timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
timeMap.get("alice", 1);           // return "happy"
timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
timeMap.get("alice", 3);           // return "sad"

Constraints:
1 <= key.length, value.length <= 100
key and value only include lowercase English letters and digits.
0 <= timestamp <= 10^7
All the timestamps of set are strictly increasing.
At most 2 * 10^5 calls will be made to set and get.
"""

class TimeMap:

    def __init__(self):
        self.store = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]

        left = 0
        right = len(values) - 1
        result = ""

        while left <= right:
            middle = (left + right) // 2

            if values[middle][0] <= timestamp:
                result = values[middle][1]
                left = middle + 1

            else:
                right = middle - 1

        return result

"""
We create self.store as a dictionary where each key stores a list of [timestamp, value] pairs. 
In set(), if the key does not exist yet, we create an empty list, then append the new timestamp and value. 
Because the problem guarantees timestamps are added in increasing order, each key's list is automatically sorted by timestamp. 
In get(), we first return "" if the key does not exist. Otherwise, we use Binary Search on that key's timestamp list. 
If the middle timestamp is less than or equal to the requested timestamp, that value is valid, so we save it in result 
and continue searching to the right because there might be an even later valid timestamp. 
If the middle timestamp is too large, we search the left half. 
At the end, result contains the value with the largest timestamp that is still <= the requested timestamp.
"""

"""
For example, after set("alice", "happy", 1) and set("alice", "sad", 3), the dictionary contains {"alice": [[1, "happy"], [3, "sad"]]}. 
If we call get("alice", 2), Binary Search first checks one of these timestamps; timestamp 1 is valid because 1 <= 2, 
so result = "happy" and we search farther right. Timestamp 3 is too large because 3 > 2, so we move left and stop. 
The final result is "happy". If we call get("alice", 3), timestamp 3 is valid, so the result becomes "sad".
"""

"""
Time Complexity: set() is O(1) because we append to the list. get() is O(log n) because we use Binary Search over the stored timestamps for that key.
Space Complexity: O(n) overall because we store every key/value/timestamp entry.
"""

def main():
    time_map = TimeMap()

    time_map.set("alice", "happy", 1)

    print(time_map.get("alice", 1))
    print(time_map.get("alice", 2))

    time_map.set("alice", "sad", 3)

    print(time_map.get("alice", 3))
    print(time_map.get("alice", 4))

    print("\nStored Data:")
    print(time_map.store)


if __name__ == "__main__":
    main()