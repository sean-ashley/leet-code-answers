class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        #set up two pointers
        pointera = 0
        pointerb = len(numbers) - 1
        
        while pointera < pointerb:
            
            if (numbers[pointera] + numbers[pointerb]) == target:
                return [pointera + 1 , pointerb + 1]
            
            elif (numbers[pointera] + numbers[pointerb]) > target:
                pointerb -= 1
            
            else:
                pointera += 1
