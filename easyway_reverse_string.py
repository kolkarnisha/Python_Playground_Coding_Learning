def reverse(str):
    return "".join(reversed(str))
reverse("nisha")

def reverse(s):
    empty=""
    for i in s:
        empty=i+empty
    return empty
reverse("nisha")
