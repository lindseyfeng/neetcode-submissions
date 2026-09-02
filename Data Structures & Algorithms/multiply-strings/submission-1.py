class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic1 = {
        "0":0, 
        "1":1,
        "2":2,
        "3":3,
        "4":4,
        "5":5,
        "6":6,
        "7":7,
        "8":8,
        "9":9
        }
        dic2 = {
        0:"0", 
        1:'1',
        2:"2",
        3:"3",
        4:"4",
        5:"5",
        6:"6",
        7:"7",
        8:'8',
        9:"9"
        }
        int_num1 = 0
        int_num2 = 0

        for i in num1:
            int_num1 = int_num1*10+dic1[i]
        for i in num2:
            int_num2 = int_num2*10+dic1[i]
        
        res = int_num1*int_num2
        ans = ""
        while res >= 10:
            digit = res%10
            ans = dic2[digit] + ans
            res = res //10
        return dic2[res] + ans
