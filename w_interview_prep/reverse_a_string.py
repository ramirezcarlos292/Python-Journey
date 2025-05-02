class Solution:
    def reverse_string(my_string):
        store = []
        for letter in range(len(my_string)-1, -1, -1):
            store.append(my_string[letter])
        print("".join(store))
    


Solution.reverse_string("abcdefg")
Solution.reverse_string("")
Solution.reverse_string(" ")
Solution.reverse_string(" __")
Solution.reverse_string("gfedcba")
Solution.reverse_string("carlos ivan ramirez martinez")
Solution.reverse_string("alejandra margarita rivas simental")