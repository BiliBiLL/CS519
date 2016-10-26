import sys

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums == [] or len(nums) == 1:
            print "haha"
            return None
        else:
            
            first = 0
            last = len(nums)-1
            while first < last:
                print first,last
                #print nums[first],nums[last]
                if nums[first] + nums[last] == target:
                    return [first,last]
                if nums[first] + nums[last] < target:
                    print "first++"
                    first += 1
                if nums[first] + nums[last] > target:
                    print "last--"
                    last -= 1
            
        
            
if __name__ == "__main__":
    nums = [3,2,4]
    print twoSum(nums,6)
