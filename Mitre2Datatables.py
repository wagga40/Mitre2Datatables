from pyattck import Attck
import json

print("-= Mitre2Datatables =-\n")

print(" [+] Init pyattck")
attack = Attck()

MitreDictJSON = {}
MitreDictJSONFinal = {}
MitreDictJSONTmp = {}

MitreTaticsOrdered = {}
MitreTaticsOrdered["Reconnaissance"] = 1
MitreTaticsOrdered["Resource Development"] = 2
MitreTaticsOrdered["Initial Access"] = 3
MitreTaticsOrdered["Execution"] = 4
MitreTaticsOrdered["Persistence"] = 5
MitreTaticsOrdered["Privilege Escalation"] = 6
MitreTaticsOrdered["Defense Evasion"] = 7
MitreTaticsOrdered["Credential Access"] = 8 
MitreTaticsOrdered["Discovery"] = 9
MitreTaticsOrdered["Lateral Movement"] = 10
MitreTaticsOrdered["Collection"] = 11
MitreTaticsOrdered["Command and Control"] =  12
MitreTaticsOrdered["Exfiltration"] =  13
MitreTaticsOrdered["Impact"] = 14

output = "Mitre2Datatables.json"

print(" [+] Building reference array")
maxTechniques = 0
for tactic in attack.enterprise.tactics:
    MitreDictJSON[tactic.name] = {}
    techniquesCounter = 0
    for technique in tactic.techniques:
        MitreDictJSON[tactic.name][technique.technique_id] = technique.name
        techniquesCounter += 1
    if techniquesCounter > maxTechniques: maxTechniques=techniquesCounter

print(" [+] Sorting...")
# Sort keys
for tactic, techniques in MitreDictJSON.items():
    MitreDictJSONFinal[tactic] = []
    for technique_id, technique_name in sorted(techniques.items()): # Not very efficient, but good enough for now...
        MitreDictJSONFinal[tactic].append(f'{technique_id}-{technique_name}')

matrix = []
emptyTacticCounter = 0

print(" [+] Building output...")
# Build the datatable JSON
while emptyTacticCounter < len(MitreTaticsOrdered):
    emptyTacticCounter = 0
    matrix_line = ["", "", "", "", "", "", "", "", "", "", "", "", "", ""]
    for tactic, tactic_index in MitreTaticsOrdered.items():
        if len(MitreDictJSONFinal[tactic]) > 0:
            matrix_line[tactic_index-1] = MitreDictJSONFinal[tactic].pop(0)
        else:
            emptyTacticCounter += 1
    matrix.append(matrix_line)

# Removing last empty element from matrix
matrix.pop(len(matrix)-1)

print(f' [+] File saved to : {output}')
with open(output, "w", encoding="utf-8") as f:
    json.dump(matrix, f, indent = 4, ensure_ascii=False)    

