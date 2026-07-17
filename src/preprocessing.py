def get_X_y(df) :

    # df = df.drop_duplicates() 
    # It is dropping Score 

    X = df.drop(["quality"] , axis = 1)

    y = df["quality"]

    y = y -3

    return X , y 