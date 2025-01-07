# UD-CHILDES
This repository contains the Universal Dependencies (UD) treebanks derived from CHILDES corpora. The data is available in the provided zip file.

## Sources  
This repository aggregates annotated CHILDES UD treebanks from the following sources:

1. **Adam Corpus**  
   - Source: [CHILDES_UD2LF_2](https://github.com/Lou1sM/CHILDES_UD2LF_2)  

2. **Brown_Eve Corpus**  
   - Source: [Parsing_Speech](https://github.com/zoeyliu18/Parsing_Speech/tree/main)  

3. **Other Corpora**  
   - Includes:  
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
   - Source: [Spoken_Parsing](https://github.com/ufcompling/spoken_parsing)  

‼️ Note: Part of the corpora were automatically parsed and did not pass the validation test provided by the [UD tools](https://github.com/UniversalDependencies/tools/blob/master/validate.py). You can get the validator errors by running the following command:

```commandline
git clone https://github.com/UniversalDependencies/tools.git
cat amdam_eud.conllu | python validate.py --lang en --max-err=0
```

## Processing  
The processing steps are carried out by the script ```adam_data_process.py``` and ```other_data_process.py```. The dependencies can be found in ```requirements.txt```.

```commandline
# to process the Adam Corpus
python adam_data_process.py

# to process other corpora
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

‼️ **Note for All Other Corpora:** The data is sourced from previous work and is not fully manually annotated. To ensure a more coherent dataset, sentences without human annotations were annotated using Stanza. This is indicated in the metadata with `annotate_gold=True/False`.  
‼️ **Note for Eve Corpus:** We filtered out 22 annotation errors where sentences lacked a root node.  

## Contributors  
- Adam Corpus: [Lou1sM](https://github.com/Lou1sM)  
- Eve Corpus: [zoeyliu18](https://github.com/zoeyliu18)  
- Other Corpora: [ufcompling](https://github.com/ufcompling)  