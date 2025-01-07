# UD-CHILDES
This repository contains the Universal Dependencies (UD) treebanks derived from CHILDES corpora. The data is available in the ```UD_corpora``` folder.  
Some conllu files are larger than 100M, so if you want to contribute to this dataset, please make sure you have installed [git-lfs](https://git-lfs.com/).
## Sources  
This repository aggregates annotated CHILDES UD treebanks from the following sources:

- [x] Paper: [Cross-linguistically Consistent Semantic and Syntactic Annotation of Child-directed Speech](https://arxiv.org/abs/2109.10952) by Ida Szubert, Omri Abend, Nathan Schneider, Samuel Gibbon, Louis Mahon, Sharon Goldwater, and Mark Steedman 
   - Data Source: [CHILDES_UD2LF_2](https://github.com/Lou1sM/CHILDES_UD2LF_2)  
   - CHILDES corpus: Adam Corpus (from the Brown Corpus) 

- [x] Paper: [Dependency Parsing Evaluation for Low-resource Spontaneous Speech](https://aclanthology.org/2021.adaptnlp-1.16/) by Zoey Liu and Emily Prud’hommeaux.
   - Data Source: [Parsing_Speech](https://github.com/zoeyliu18/Parsing_Speech/tree/main)  
   - CHILDES corpus: Eve Corpus (from the Brown corpus)

- [x] Paper: [Data-driven Parsing Evaluation for Child-Parent Interactions](https://aclanthology.org/2023.tacl-1.97.pdf) by Zoey Liu and Emily Prud’hommeaux
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

- [ ] Paper: [High-accuracy Annotation and Parsing of CHILDES Trans](https://aclanthology.org/W07-0604.pdf)
  - Data Source: not found
- [ ] Paper: [Testing the Universal Grammar Hypothesis (NSF)](https://sites.socsci.uci.edu/~lpearl/CoLaLab/TestingUG/index.html)
  - Data Source: [CHILDES Constituency Treebaank](https://sites.socsci.uci.edu/~lpearl/CoLaLab/CHILDESTreebank/childestreebank.html)
  - CHILDES corpora cover:
    - *Adam_Brown* (*Includes trace-annotation, 3to4 and 4up subsections include additional animacy and thematic role annotation*)
    - *Eve_Brown* (*Includes trace-annotation, animacy, and thematic role annotation*)
    - *Sarah_Brown*
    - *HSLLD*: HV1-ER and HV1-MT subsections (*Includes trace-annotation*)
    - *Soderstrom*
    - *Suppes*
    - *Valian* (*Includes trace-annotation, animacy, and thematic role annotation*)
    - The following only contains child-directed speech utterances containing wh-words
      - *Bates*
      - *Bernstein*
      - *VanHouten/Threes*
      - *VanHouten/Twos*
      - *VanKleeck*

‼️ Note: Part of the corpora were automatically parsed and did not pass the validation test provided by the [UD tools](https://github.com/UniversalDependencies/tools/blob/master/validate.py). You can get the validator errors by running the following command:

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
  - Employed STANZA for generating FEATS information.  

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
  For all `.conllu` files except `adam_eud.conllu`, the data originates from previous work and is not entirely manually annotated. Sentences lacking human annotations were annotated using Stanza, indicated in the metadata by `annotate_gold=True/False`.
- **Tokenization Notes:**  
  In all current corpora, `# childes_toks` refers to the original tokenized text from the source data, while `# text` represents the tokenization as it appears in the dependency tree.
- **Additional Metadata:**  
  All other metadata originates from the source data we collected.


#Citations
If you find the dataset helpful, please cite the following papers: 
```bibtex
@misc{szubert2024crosslinguisticallyconsistentsemanticsyntactic,
      title={Cross-linguistically Consistent Semantic and Syntactic Annotation of Child-directed Speech}, 
      author={Ida Szubert and Omri Abend and Nathan Schneider and Samuel Gibbon and Louis Mahon and Sharon Goldwater and Mark Steedman},
      year={2024},
      eprint={2109.10952},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2109.10952}, 
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