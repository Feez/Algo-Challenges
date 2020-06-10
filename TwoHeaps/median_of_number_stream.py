import heapq

class MedianOfAStream:
    def __init__(self):
        self.lower_half_arr = []
        self.upper_half_arr = []
    
    def insert_num(self, num):
        if len(self.lower_half_arr) == 0 or num > self.lower_half_arr[0]:
            heapq.heappush(self.upper_half_arr, num)
        else:
            heapq.heappush(self.lower_half_arr, -num)

        self.balance()

    def balance(self):
        lower_half_extra_nums = len(self.lower_half_arr) - len(self.upper_half_arr)

        if lower_half_extra_nums > 1:
            heapq.heappush(self.upper_half_arr, -heapq.heappop(self.lower_half_arr))
        elif lower_half_extra_nums < -1:
            heapq.heappush(self.lower_half_arr, -heapq.heappop(self.upper_half_arr))

    def find_median(self):
        if len(self.lower_half_arr) == 0:
            if len(self.upper_half_arr) == 0:
                return 0.0
            return self.upper_half_arr[0]
        
        all_num_count = len(self.lower_half_arr) + len(self.upper_half_arr)

        if all_num_count % 2 == 0:
            lower = -self.lower_half_arr[0]
            upper = self.upper_half_arr[0]

            return (lower + upper) / 2
        else:
            return self.upper_half_arr[0]


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
