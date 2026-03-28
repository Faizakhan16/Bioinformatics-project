filename = input("Enter FASTA file name: ")

with open(filename, "r") as file:
    data = file.read()

lines = data.split("\n")
dna = lines[1]

print("Length:", len(dna))
print("A:", dna.count("A"))
print("T:", dna.count("T"))
print("G:", dna.count("G"))
print("C:", dna.count("C"))

gc = dna.count("G") + dna.count("C")
gc_content = (gc / len(dna)) * 100

print("GC Content:", gc_content)

codon_table = {
    "ATG": "M", "TTT": "F", "TTC": "F",
    "TAA": "*", "TAG": "*", "TGA": "*"
}

protein = ""

for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    if len(codon) == 3:
        protein += codon_table.get(codon, "?")

print("Protein:", protein)