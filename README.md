# Winos is a package which contains a way to explore Wine review data either by choosing a certain class from  [this dataset](https://www.kaggle.com/zynicide/wine-reviews). 

## Installation Intructions
To install the package run :
```bash
pip install .
```

## Few Examples 
To Look at the dataframs based off one of the Column names run:
```bash
python main.py --country  US
python main.py --price 230
python main.py  --score 88
python main.py --taster "Roger Voss"
```

To view the Dashboard  run:
```bash
python app.py
```
When you click on the link it will open a website which allows you  to look at different boxplots based off points or price. 

To view a Correlation Matrix run:
```bash
python main.py --ml correlation 

```

To see KNN or Decision tree on the data run:
```bash
python main.py --ml knn
python main.py --ml tree
```
This will show you a simple model of how KNN and Decision tree works on the Data and both will show the accuracies when perfroming PCA to the data  and when you do not. 