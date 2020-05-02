def to_rna(dna_strand):
    rna_transcription = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U'
    }

    return dna_strand.translate(dna_strand.maketrans(rna_transcription))
