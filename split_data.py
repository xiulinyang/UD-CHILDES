from pathlib import Path
from glob import glob
from tqdm import tqdm
from conllu import parse_incr
with open('UD-CHILDES_gold/Violet_Providence_eud_gold.conllu', 'w') as final:
    data_file = open("UD-CHILDES-gold/Violet_Providence_eud_gold.conllu", "r", encoding="utf-8")
    for tokenlist in parse_incr(data_file):
        for tok in tokenlist:
            tok['feats']='_'


        sent=tokenlist.serialize()
        final.write(sent)

# with open('UD-CHILDES_gold/Abe_kuczaj_eud_gold_r.conllu', 'w') as final:
#     data_file = Path("UD-CHILDES_gold/Abe_kuczaj_eud_gold.conllu").read_text().strip().split('\n')
#     for line in tqdm(data_file):
#         if len(line.split('\t'))==10:
#             if '-' in line.split('\t')[0] and line[-1]=='_':
#                 line = line[:-1]+'SpaceAfter=No'
#         final.write(line)
#         final.write('\n')

# all_files = glob('UD_corpora/*.conllu')
# for file in all_files:
#     name = Path(file).stem
#     with open(f'UD-CHILDES-gold/{name}_gold.conllu', 'w') as gold, open(f'UD-CHILDES_silver/{name}_silver.conllu', 'w') as silver:
#         conllu_file = Path(file).read_text().strip().split('\n\n')
#         for sent in tqdm(conllu_file):
#             if '# gold_annotation = True' in sent:
#                 gold.write(sent)
#                 gold.write('\n\n')
#             else:
#                 silver.write(sent)
#                 silver.write('\n\n')


