from codon_table import codon_table

#analyze DNA sequence
def analyze_dna_sequence(dna_sequence):
    if not all(nucleotide in "ATCG" for nucleotide in dna_sequence):
        raise ValueError("Invalid DNA sequence: only A, T, C, and G are allowed.")
    nucleotide_counts = {
        "A": dna_sequence.count("A"),
        "T": dna_sequence.count("T"),
        "C": dna_sequence.count("C"),
        "G": dna_sequence.count("G")
    }
    return nucleotide_counts

#count nucleotides in a DNA sequence and return the length of the sequence
def count_nucleotides(dna_sequence):
    return len(dna_sequence)

#calculate the GC content of a DNA sequence
def gc_content(dna_sequence):
    if not dna_sequence:
        return 0
    gc_count = dna_sequence.count("G") + dna_sequence.count("C")
    return (gc_count / len(dna_sequence)) * 100

#calculate the AT content of a DNA sequence
def at_content(dna_sequence):
    if not dna_sequence:
        return 0
    at_count = dna_sequence.count("A") + dna_sequence.count("T")
    return (at_count / len(dna_sequence)) * 100

#get the complementary strand of a DNA sequence
def complement(dna_sequence):
    complement = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    return ''.join(complement[nucleotide] for nucleotide in reversed(dna_sequence))

#transcribe a DNA sequence to mRNA
def transcribe(dna_sequence):
    transcription = {
        "A": "A",
        "T": "U",
        "C": "C",
        "G": "G"
    }
    return ''.join(transcription[nucleotide] for nucleotide in dna_sequence)

#actual translation of mRNA to protein sequence code
def translate(mrna_sequence):
    start = mrna_sequence.find("AUG")
    if start ==-1:
        return "start codon not found"
    
    protein_sequence = []
    for i in range(start, len(mrna_sequence) - 2 , 3):
        codon = mrna_sequence[i:i+3]
        if codon in ["UAA", "UAG", "UGA"]:
            break
        amino_acid = codon_table.get(codon, "Unknown")
        protein_sequence.append(amino_acid)
    if not protein_sequence:
         return "No protein coded"
    
    return "-".join(protein_sequence)
     
     
