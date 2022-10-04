

faktor = int(input())
count = int(input())
result_list = []
result_list.append(faktor)

for i in range(1, count + 1):
    if i // faktor > 0 and i > 0:
        result_list.append(i * faktor)
    if result_list.count(faktor)>1:
        result_list.remove(faktor)
result_list.sort()

print(result_list)