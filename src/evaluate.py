from sklearn.metrics import f1_score , precision_score , recall_score

def get_score(model , X_test , y_test) :

    y_pred = model.predict(X_test)

    f1 = f1_score(
        y_test ,
        y_pred ,
        average = "weighted"
    )

    p = precision_score(
        y_test ,
        y_pred ,
        average = "weighted"
    )

    r = recall_score(
        y_test ,
        y_pred ,
        average = "weighted"
    )

    return f1 , p , r