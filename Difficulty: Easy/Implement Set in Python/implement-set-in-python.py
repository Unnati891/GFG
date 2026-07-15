st = {int(x) for x in input().split()}
i = int(input())
r = int(input())

# Insert i in set
st.add(i)

# Printing the set
for i in sorted(st):
    print(i, end=' ')
print()

# Remove r from set
st.remove(r)

# Printing the set
for i in sorted(st):
    print(i, end=' ')
print()

# Sum of set elements
sum = sum(st)

# Print sum of set
print(sum)