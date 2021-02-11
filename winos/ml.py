
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from imblearn.under_sampling import RandomUnderSampler
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt


def clean_for_ml(df, u_input):
    df = df.drop(['Unnamed: 0','designation','description','region_1','region_2','taster_name','taster_twitter_handle','title', 'iso3'],axis=1)
    df = df.dropna(how = 'any')
    freq = df.country.value_counts()
    freq = freq[freq >= 1000]

    df = df[df["country"].isin(freq.index.values)]
    df['country']=df['country'].astype('category').cat.codes+1
    df['province']=df['province'].astype('category').cat.codes+1
    df['winery']=df['winery'].astype('category').cat.codes+1
    df['variety']=df['variety'].astype('category').cat.codes+1

    rus = RandomUnderSampler()
    data_rus, target_rus = rus.fit_resample(df.drop(['country'],axis=1),df['country'])
    datanew = pd.DataFrame(data_rus)
    targetnew = pd.DataFrame(target_rus)
    datanew.columns = ['points', 'price', 'province', 'variety', 'winery']
    targetnew.columns = ['country']
    df = pd.merge(datanew,targetnew, right_index=True, left_index=True)
    # print(df)
    # print(df.country.value_counts())

    X = df.drop('country', 1)
    y = df['country']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    Xp_train, Xp_test, yp_train, yp_test=pca(X_train, X_test, y_train, y_test)
    
    if (u_input=='knn'):
        knn(X_train, X_test, y_train, y_test, Xp_train, Xp_test, yp_train, yp_test)
    elif(u_input=='correlation'):
        correlation(df)
    elif(u_input=='tree'):
        tree(X_train, X_test, y_train, y_test,Xp_train, Xp_test, yp_train, yp_test)

def pca(X_train, X_test, y_train, y_test):
    # X = df.drop('country', 1)
    # y = df['country']
    # # print (X,'then  y \n' ,y)
    # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    pca= PCA(n_components='mle')
    X_train=pca.fit_transform(X_train)
    X_test=pca.transform(X_test)
    return (X_train,X_test,y_train,y_test)

def knn(X_train, X_test, y_train, y_test, Xp_train, Xp_test, yp_train, yp_test):
    # print(y_train)
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    knn.fit(Xp_train, yp_train)
    yp_pred = knn.predict(Xp_test)
    print("Accuracy without PCA: ",metrics.accuracy_score(y_test, y_pred))
    print("Accuracy with PCA: ",metrics.accuracy_score(yp_test, yp_pred))

def correlation(df):
    correlation_mat = df.astype('float').corr()
    sns.heatmap(correlation_mat, annot = True)
    plt.show()
    print(df.corr())

def tree(X_train, X_test, y_train, y_test, Xp_train, Xp_test, yp_train, yp_test):
    clf = DecisionTreeClassifier(criterion="entropy", max_depth=15)
    clf= clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print("Accuracy without PCA :",metrics.accuracy_score(y_test, y_pred))

    clf = DecisionTreeClassifier(criterion="entropy", max_depth=15)
    clf= clf.fit(Xp_train, yp_train)
    yp_pred = clf.predict(Xp_test)
    print("Accuracywith PCA :",metrics.accuracy_score(yp_test, yp_pred))
