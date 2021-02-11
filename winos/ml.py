
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from imblearn.under_sampling import RandomUnderSampler
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

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

    X_train, X_test, y_train, y_test=pca(df)
    
    if (u_input=='knn'):
        knn(X_train, X_test, y_train, y_test)

def pca(df):
    X = df.drop('country', 1)
    y = df['country']
    # print (X,'then  y \n' ,y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)

    pca= PCA(n_components='mle')
    X_train=pca.fit_transform(X_train)
    X_test=pca.transform(X_test)
    return (X_train,X_test,y_train,y_test)

def knn(X_train, X_test, y_train, y_test):
    # print(y_train)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
