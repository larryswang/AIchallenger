# EECS 595 Project

## project folder structure

aichallenger

    data

        sentiment_analysis_trainingset.csv

        sentiment_analysis_validationset.csv

    predict

    model

    scripts

        *all the scripts
        
    README.md

## to run
### create virtualenv environment
install virtualenv environment:
`python3 -m pip install --user virtualenv`

create venv folder:
`python3 -m virtualenv venv`

### activate virtualenv environment
`source venv/bin/activate`

### install all dependencies
`pip install numpy`

`pip install pandas`

`pip install jieba`

`pip install sklearn`

### run the scripts 
preprocessing (under scripts folder): 
`python data_preprocess.py`, this will create a pkl file in model/ folder

training (under scripts folder): 
`python main_train.py`