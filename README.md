# UD-CHILDES
This repository contains the Universal Dependencies (UD) **silver** treebanks derived from CHILDES corpora. The data is available in the ```silver_data``` folder. As using ```lfs``` to download the treebank might not work due to the quota issue, we upload the zip file to the folder. 

## Stats
| corpus | children     | gold annotation                                                       | speakers | UPOS   | feats         | utterances              | tokens                   |
| ------ | ------------ | --------------------------------------------------------------------- | -------- | ------ | ------------- | ----------------------- | ------------------------ |
| S+24   | Adam (Brown) | Dependency trees, UPOS; features are from the original CHILDES corpus | adults   | gold   | converted[^1] | 17,233 (all gold trees) | 91,114 (all gold trees)  |
| LP21   | Eve (Brown)  | Dependency trees; others (feats, XPOS, UPOS) are unspecified          | all      | silver | silver        | 110,251 (2,207 gold)    | 540,816 (8,497 gold)     |
| LP23   | 10 Children  | Dependency trees; others (feats, XPOS, UPOS) are unspecified          | all      | silver | silver        | 1,135,591 (34,530 gold) | 6,629,368 (168,284 gold) |
[^1]: from CHILDES morphology layer

## LP23  Stats

| CORPUS NAME       | # gold utterances | # gold toks | # silver utterances | # silver toks |
| ----------------- | ---------------- | ----------- | ------------------ | ------------ |
| Adam              | 17233            | 91114       | 0                  | 0            |
| Brown_Eve         | 2207             | 8497        | 108044             | 532319       |
| Adam_Brown        | 5324             | 24361       | 104949             | 516526       |
| Sarah_Brown       | 5347             | 23233       | 104926             | 517654       |
| Abe_kuczaj        | 4167             | 22437       | 38630              | 230489       |
| Naima_Providence  | 2534             | 14360       | 236350             | 1422543      |
| Emma_Weist        | 2423             | 13730       | 74825              | 474460       |
| Violet_Providence | 721              | 1857        | 32801              | 164975       |
| Thomas_Thomas     | 4240             | 20333       | 313550             | 2039132      |
| Roman_Weist       | 3653             | 20557       | 73595              | 467633       |
| Laura_Braunwald   | 4622             | 21079       | 41862              | 205427       |
| Lily_Providence   | 1499             | 6337        | 79573              | 422245       |
| LP23 Overall      | 34530            | 168284      | 1101061            | 6461084      |


## Sources  
This repository aggregates annotated CHILDES UD treebanks from the following sources:

- [S+24] Paper: [Cross-linguistically Consistent Semantic and Syntactic Annotation of Child-directed Speech](https://link.springer.com/article/10.1007/s10579-024-09734-y) by Ida Szubert, Omri Abend, Nathan Schneider, Samuel Gibbon, Louis Mahon, Sharon Goldwater, and Mark Steedman 
   - Data Source: [CHILDES_UD2LF_2](https://github.com/Lou1sM/CHILDES_UD2LF_2)  
   - CHILDES corpus: Adam Corpus (from the Brown Corpus)
   - The dataset is built based on the preannotation of [High-accuracy Annotation and Parsing of CHILDES Transcripts](https://aclanthology.org/W07-0604.pdf)

- [LP21] Paper: [Dependency Parsing Evaluation for Low-resource Spontaneous Speech](https://aclanthology.org/2021.adaptnlp-1.16/) by Zoey Liu and Emily Prud’hommeaux.
   - Data Source: [Parsing_Speech](https://github.com/zoeyliu18/Parsing_Speech/tree/main)  
   - CHILDES corpus: Eve Corpus (from the Brown corpus)

- [LP23] Paper: [Data-driven Parsing Evaluation for Child-Parent Interactions](https://aclanthology.org/2023.tacl-1.97.pdf) by Zoey Liu and Emily Prud’hommeaux
  - Source: [Spoken_Parsing](https://github.com/ufcompling/spoken_parsing)  
  - CHILDES corpora:  
     - *Abe_Kuczaj*  
     - *Adam_Brown*  
     - *Emma_Weist*  
     - *Laura_Braunwald*  
     - *Lily_Providence*  
     - *Naima_Providence*  
     - *Roman_Weist*  
     - *Sarah_Brown*  
     - *Thomas_Thomas*  
     - *Violet_Providence*


‼️ Note: Parts of the corpora are automatically parsed and do not pass the validation test provided by the [UD tools](https://github.com/UniversalDependencies/tools/blob/master/validate.py). You can get the validator errors by running the following command:

```commandline
git clone https://github.com/UniversalDependencies/tools.git
cat CONLLU_FILE_PATH | python validate.py --lang en --max-err=0
```

## Processing  

### Scripts
The processing steps are carried out by the script ```adam_data_process.py``` and ```other_data_process.py```. The dependencies can be found in ```requirements.txt```.

```commandline
# to process the Adam Corpus from CHILDES_UD2LF_2
python adam_data_process.py

# to process other corpora from Parsing_Speech and Spoken_Parsing
python other_data_process.py PATH_OF_ANNOTATED_CHILDES_CORPUS NAME_OF_THE_CSV_FILE
```

The annotated data should be downloaded from the two sources mentioned above; the csv file should be downloaded from the ```childesr``` package in R.
```R
library(childesr)
library(dplyr)
d_eng_na <- get_utterances(corpus = 'Brown') # corpus name
write.csv(d_eng_na, "Brown.csv", row.names = FALSE) # the file name of csv
```

### Adam Corpus  
- **Conversion**:  
  - Utilized the official [UD version conversion tool](https://github.com/UniversalDependencies/tools/tree/master) to transform annotations to UD V2 format. Command: ```python convert.py PATH_TO_CONLLU_FILE > OUTPUT_PATH``` 

- Enhancements:  
  - Added multiword item annotation.  
  - Included MISC annotation fields.  
  - Standardized text formatting:  
    - Capitalized the first letter of each sentence.  

### Eve and Other Corpora  
- Feature Extraction:  
  - Employed STANZA for generating FEATS information. (code see ```other_data_process.py```) 

- Additional Processing Steps:  
  - Integrated non-annotated sentences from the same corpus.  
  - Added multiword item annotations and MISC annotations.
  - Applied the [GUM tool](https://github.com/amir-zeldes/gum/blob/master/_build/utils/depedit.py) to enrich UD relations using the command ```python depedit.py PATH_TO_CONLLU_WITHOUT_EUD -c eng_enhance.ini > OUTPUT_PATH```
  - Standardized text formatting:  
    - Capitalized the first letter of each sentence.  
    - Added punctuation where necessary.  
‼️ **Note for Eve Corpus:** We filtered out 22 annotation errors where sentences lacked a root node. 


## Metadata Explanation

Some metadata fields are self-explanatory, but the following require clarification:
- **Annotation Source:**  
  For all `.conllu` files except `adam_eud.conllu`, the data originates from previous work and is not entirely manually annotated. Sentences lacking human annotations were annotated using Stanza (code see ```other_data_process.py```), indicated in the metadata by `annotate_gold=True/False`.
- **Tokenization Notes:**  
  In all current corpora, `# childes_toks` refers to the original tokenized text from the source data, while `# text` represents the tokenization as it appears in the dependency tree.
- **Additional Metadata:**  
  All other metadata originates from the source data we collected.


# Citations
If you find the dataset helpful, please cite the following papers: 
```bibtex
@article{szubert-24,
	title = {Cross-linguistically consistent semantic and syntactic annotation of child-directed speech},
	url = {https://doi.org/10.1007/s10579-024-09734-y},
	journal = {Language Resources and Evaluation},
	author = {Szubert, Ida and Abend, Omri and Schneider, Nathan and Gibbon, Samuel and Mahon, Louis and Goldwater, Sharon and Steedman, Mark},
	month = may,
	year = {2024}
}
```
```bibtex
@inproceedings{liu-prudhommeaux-2021-dependency,
    title = "Dependency Parsing Evaluation for Low-resource Spontaneous Speech",
    author = "Liu, Zoey  and
      Prud{'}hommeaux, Emily",
    editor = "Ben-David, Eyal  and
      Cohen, Shay  and
      McDonald, Ryan  and
      Plank, Barbara  and
      Reichart, Roi  and
      Rotman, Guy  and
      Ziser, Yftah",
    booktitle = "Proceedings of the Second Workshop on Domain Adaptation for NLP",
    month = apr,
    year = "2021",
    address = "Kyiv, Ukraine",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.adaptnlp-1.16/",
    pages = "156--165",
    abstract = "How well can a state-of-the-art parsing system, developed for the written domain, perform when applied to spontaneous speech data involving different interlocutors? This study addresses this question in a low-resource setting using child-parent conversations from the CHILDES databse. Specifically, we focus on dependency parsing evaluation for utterances of one specific child (18 - 27 months) and her parents. We first present a semi-automatic adaption of the dependency annotation scheme in CHILDES to that of the Universal Dependencies project, an annotation style that is more commonly applied in dependency parsing. Our evaluation demonstrates that an outof-domain biaffine parser trained only on written texts performs well with parent speech. There is, however, much room for improvement on child utterances, particularly at 18 and 21 months, due to cases of omission and repetition that are prevalent in child speech. By contrast, parsers trained or fine-tuned with in-domain spoken data on a much smaller scale can achieve comparable results for parent speech and improve the weak parsing performance for child speech at these earlier ages"
}
```
```bibtex
@article{liu-prudhommeaux-2023-data,
    title = "Data-driven Parsing Evaluation for Child-Parent Interactions",
    author = "Liu, Zoey  and
      Prud{'}hommeaux, Emily",
    journal = "Transactions of the Association for Computational Linguistics",
    volume = "11",
    year = "2023",
    address = "Cambridge, MA",
    publisher = "MIT Press",
    url = "https://aclanthology.org/2023.tacl-1.97/",
    doi = "10.1162/tacl_a_00624",
    pages = "1734--1753",
    abstract = "We present a syntactic dependency treebank for naturalistic child and child-directed spoken English. Our annotations largely follow the guidelines of the Universal Dependencies project (UD [Zeman et al., 2022]), with detailed extensions to lexical and syntactic structures unique to spontaneous spoken language, as opposed to written texts or prepared speech. Compared to existing UD-style spoken treebanks and other dependency corpora of child-parent interactions specifically, our dataset is much larger (44,744 utterances; 233,907 words) and contains data from 10 children covering a wide age range (18{--}66 months). We conduct thorough dependency parser evaluations using both graph-based and transition-based parsers, trained on three different types of out-of-domain written texts: news, tweets, and learner data. Out-of-domain parsers demonstrate reasonable performance for both child and parent data. In addition, parser performance for child data increases along children`s developmental paths, especially between 18 and 48 months, and gradually approaches the performance for parent data. These results are further validated with in-domain training."
}
```
