# UD-CHILDES (silver)
This repository contains the Universal Dependencies (UD) **silver** treebanks derived from CHILDES corpora. The data is available in the ```silver_data``` folder. As using ```lfs``` to download the treebank might not work due to the quota issue, we upload the zip file to the folder. 

You can get the gold UD CHILDES treebank from [UD_English-CHILDES](https://github.com/UniversalDependencies/UD_English-CHILDES).

## Stats
| Child  | Corpus      | Child age range     |  Silver sents | Silver toks |
|--------|-------------|---------------------|------------|-------------|
| Laura  | Braunwald  | 1;3–7;0 (1;3–7;0)    | 41,862       | 205,427     |
| Adam   | Brown         | 1;6–5;2 (1;6–5;2)     | 93,315       | 452,348     |
| Eve    | Brown                     | 1;6–5;1 (1;6–5;2)   | 108,044      | 532,319     |
| Abe    | Kuczaj     | 2;4–5;0 (2;4–5;0)   | 38,630       | 230,489     |
| Sarah  | Brown                     | 1;6–5;2 (1;6–5;2)    | 104,926      | 517,654     |
| Lily   | Providence   | 0;11–4;0 (0;11–4;0)   | 79,573       | 422,245     |
| Naima  | Providence                | 1;3–3;11 (0;11–4;0)    | 236,350      | 1,422,543   |
| Violet | Providence                | 0;11–4;0 (0;11–4;0) | 32,801       | 164,975     |
| Thomas | Thomas     | 2;0–4;11 (2;0–4;11) | 313,550      | 2,039,132   |
| Emma   | Weist      | 2;2–4;10 (2;1–5;0)   | 74,825       | 474,460     |
| Roman  | Weist                     | 2;2–4;9 (2;1–5;0)    | 73,595       | 467,633     |
| Overall| NA| NA| 1,197,471|6,892,314|


‼️ Note: The treebank is silver so it does not pass the validation test provided by the [UD tools](https://github.com/UniversalDependencies/tools/blob/master/validate.py). You can get the validator errors by running the following command:

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
The creation of this unified resource is detailed in:

Xiulin Yang, Zhuoxuan Ju, Lanni Bu, Zoey Liu, Nathan Schneider (2025). [UD-English-CHILDES: A Collected Resource of Gold and Silver Universal Dependencies Trees for Child Language Interactions](https://arxiv.org/abs/2504.20304). arXiv preprint.

```
@misc{yang2025udenglishchildescollectedresourcegold,
      title={UD-English-CHILDES: A Collected Resource of Gold and Silver Universal Dependencies Trees for Child Language Interactions},
      author={Xiulin Yang and Zhuoxuan Ju and Lanni Bu and Zoey Liu and Nathan Schneider},
      year={2025},
      eprint={2504.20304},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2504.20304},
}
```
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

# Acknowledgments

We acknowledge Ida Szubert, Omri Abend, Samuel Gibbon, Louis Mahon, Sharon Goldwater, Mark Steedman, and Emily Prud’hommeaux for their contributions to the original UD treebanking efforts. We also thank Brian MacWhinney for helpful discussions.

