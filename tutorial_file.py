## Passing Lists as Arguments to a Function

names = ["Bruce", "Billy Bob", "Billy Bob Jr.", "Bobby", "Bobby Jr."]

def add_prefix_to_names(strings):
    for i in range(len(strings)):
        strings[i] = "Mr. " + strings[i]

add_prefix_to_names(names[:])
print(names)