from collections import Counter
import matplotlib.pyplot as plt

r = Counter("AMAN")
print(r)
plt.bar(r.keys(), r.values())
plt.show()
