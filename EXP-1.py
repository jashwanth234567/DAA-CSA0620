
def fun(words):
    result=[]
    for word in words:
        if word == word[::-1]:
            result.append(word) 
    return result
            
words = ["abc","car","ada","racecar","cool"]
print("data of elements in array stored ",words)
print("palindrome words in the give the array  ",fun(words))
