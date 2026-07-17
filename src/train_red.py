from preprocessing import get_X_y
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


def train_model(df) :

    X , y = get_X_y(df)

    X_train , X_test , y_train , y_test = train_test_split(
        X ,
        y ,
        test_size = 0.2 ,
        stratify = y , 
        random_state = 98
    )

    model = RandomForestClassifier(class_weight = "balanced_subsample")

    model.fit(
        X_train ,
        y_train
    )

    model.fit(
        X_train ,
        y_train 
    )

    return model , X_test , y_test