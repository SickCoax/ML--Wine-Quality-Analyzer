import os
import pandas as pd
from train_red import train_model as red
from train_white import train_model as white
from evaluate import get_score

while True :

    print()
    print("------------------------------------------")
    print("Choice   :       Task")
    print("   1     :   RED WINE MODEL")
    print("   2     :  WHITE WINE MODEL")
    print("   3     :   WANT TO EXIT ??")
    print("------------------------------------------")
    print()

    try :

        choice = int(input("Enter Your Choice : "))

    except ValueError :

        print("Invalid Option")
        
        continue

    match choice :
        
        case 1 :

            csv_path = os.path.join(
                os.path.dirname(__file__) ,
                ".." ,
                "dataset" ,
                "winequality-red.csv"
            )

            df = pd.read_csv(csv_path , sep = ";")

            model , X_test , y_test = red(df)

            y_pred = model.predict(X_test)

            f1 , p , r = get_score(model , X_test , y_test)
            
            print()
            print(f"Model Prediction : {y_pred}")
            print()

            print(f"F1 Score : {f1}")
            print(f"Precision : {p}")
            print(f"Recall Score : {r}")
            print()


        case 2 :

            csv_path = os.path.join(
                os.path.dirname(__file__) ,
                ".." ,
                "dataset" ,
                "winequality-white.csv"
            )

            df = pd.read_csv(csv_path , sep = ";")

            model , X_test , y_test = white(df)

            y_pred = model.predict(X_test)

            f1 , p , r = get_score(model , X_test , y_test)
            
            print()
            print(f"Model Prediction : {y_pred}")
            print()

            print(f"F1 Score : {f1}")
            print(f"Precision : {p}")
            print(f"Recall Score : {r}")
            print()

        case 3 :

            print("SUCESSFULLY EXITED")
            print()

            break

        case _ :

            print("Invalid Option")
            print()