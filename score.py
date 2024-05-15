import sys

modelname = sys.argv[1] # 7b, 8b or breeze
type_of_all_errors = "txts/wrongtype.txt"

with open(f'eval-{modelname}.txt', 'r') as f:
    error_texts = f.readlines()
with open(type_of_all_errors, 'r') as f:
    labels = f.readlines()

# errorcode: noun 1, relation 2, sentence 3 -> factual errors
#           imagined 4, comment 5, unknown 6 -> unverifiable errors

result = [[], [], [], [], [], []]
cnt = 0
for line in error_texts:
    if "Yes" in line or "No" in line:
        errorcode = int(labels[cnt])
        if "Yes" in line: #error found
            result[errorcode-1].append(1)
        else: # error missed
            result[errorcode-1].append(0)
        cnt += 1
    else: continue

fact = result[0]+result[1]+result[2]
unve = result[3]+result[4]+result[5]
print(f"---Result of model {modelname}---")
print("Total acc:", sum(fact+unve), '/', len(fact+unve), ';', sum(fact+unve)/len(fact+unve))
print("Fact. err:", sum(fact), '/', len(fact), ';', sum(fact)/len(fact))
print("Unvr. err:", sum(unve), '/', len(unve), ';', sum(unve)/len(unve))

print("---Error subtype accuracies---")
print("1- noun acc:", sum(result[0]), '/', len(result[0]), ';', sum(result[0])/len(result[0]))
print("2- rela acc:", sum(result[1]), '/', len(result[1]), ';', sum(result[1])/len(result[1]))
print("3- sent acc:", sum(result[2]), '/', len(result[2]), ';', sum(result[2])/len(result[2]))
print("4- imag acc:", sum(result[3]), '/', len(result[3]), ';', sum(result[3])/len(result[3]))
print("5- comm acc:", sum(result[4]), '/', len(result[4]), ';', sum(result[4])/len(result[4]))
print("6- unkn acc:", sum(result[5]), '/', len(result[5]), ';', sum(result[5])/len(result[5]))

