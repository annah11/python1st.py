# tuple comprehension & methods
h1=tuple(x**2 for x in(1,2,4,6,8))
print(h1)
h2=(*(x for x in 'pyTHOn'if x.islower()),)
print(h2)
# reaptation
# print(h1.index(3))