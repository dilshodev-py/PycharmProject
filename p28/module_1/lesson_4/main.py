"""Functions in Python"""

"""
type function_name (type params) {
    logic
    return
}
"""

"""
def function_name(params: type) -> type:
    logic
    return 
    
    
function = lambda params : logic
"""


# (lambda num1 , num2 : str(num1) + str(num2))()
# add = lambda num1 , num2 : str(num1) + str(num2)   # nomsiz function
# max = lambda num1 , num2 : num1 if num1 > num2 else num2
# print(max(90 , 65))


def make_fullname(first_name: str, last_name: str = "") -> str:
    return first_name + ' ' + last_name


def toq_son(start: int, end: int) -> None:
    for i in range(start, end):
        if i % 2 == 1:
            print(i)


# print(toq_son(50, 100))

# f = make_fullname("Qodir")
# print(f)

# str_slice(text , start , end , step)
#
# str_slice("Hello" , 0, 3) -> 'Hel'

# open budjet -> bot


# def str_slice(text: str , start: int , end:int , step:int = 1) -> str:
#     result = ''
#     while start < end:
#         result += text[start]
#         start += step
#     return result
#
#
# print(str_slice("Hello", 0, 3))


# def pow(value: int | float , daraja : int | float) -> int | float:
#     return value ** daraja
#
# print(pow(27, 1/3))


# def reverse_word(word: str) -> str:
#     return word[::-1]

# def reverse_word(word: str) -> str:
#     result = ""
#     i = len(word) - 1
#     while i >= 0:
#         result += word[i]
#         i -= 1
#     return result
#
# print(reverse_word("text"))





