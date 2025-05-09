codon_table = {
    # U
    'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
    'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
    'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
    # C
    'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    # A
    'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
    'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
    # G
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
    'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
    'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
}
def translate_rna_to_protein(rna_sequence):
    protein = []
    i = 0
    length = len(rna_sequence)

    # найдем старт-кодон
    start_pos = rna_sequence.find('AUG')
    if start_pos == -1:
        return ""  # нет старт-кодона

    i = start_pos

    while i + 2 < length:
        codon = rna_sequence[i:i + 3]
        amino_acid = codon_table.get(codon, '?')  # '?' для неизвестных кодонов

        if amino_acid == '*':  # стоп-кодон
            break

        protein.append(amino_acid)
        i += 3

    return ''.join(protein)


rna_seq = "AUGGCCAUGGCCCCAGAACUGAGAUCAAUAGUACCCGUAUUAAAGGGUGA"
protein_seq = translate_rna_to_protein(rna_seq)
print(protein_seq)