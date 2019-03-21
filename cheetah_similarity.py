import numpy
import pandas

from scipy import spatial

df = pandas.read_csv('/home/justin/kotaBean/data/animal_features.csv')

def create_column_list(df):
    colList = []
    for col in df:
        if col == 'Animal':
            continue

        elif col == 'Habitat':
            for val in df[col].unique():
                try:
                    for h in val.split(','):
                        colName = '.'.join([col, h])

                        if colName in colList:
                            continue

                        else:
                            colList.append(colName)

                except:
                    colName = '.'.join([str(col), str(val)])

                    if colName in colList:
                        continue

                    else:
                        collList.append(colName)

        elif col == 'Location':
            for val in df[col].unique():
                try:
                    for h in val.split(','):
                        colName = '.'.join([col, h])

                        if colName in colList:
                            continue

                        else:
                            colList.append(colName)

                except:
                    colName = '.'.join([str(col), str(val)])

                    if colName in colList:
                        continue

                    else:
                        colList.append(colName)

        else:
            for val in df[col].unique():
                colName = '.'.join([str(col), str(val)])

                if colName in colList:
                    continue

                else:
                    colList.append(colName)

    return colList

def create_binary_matrix(df, colList):
    binaryMatrix = numpy.zeros(shape = (len(df), len(colList)))

    for index, row in df.iterrows():
        j = 0
        for item in colList:
            col = colList[j].split('.')[0]
            val = colList[j].split('.')[1]

            dfVal = df.iloc[index][col]

            try:
                for listVal in dfVal.split(','):
                    if listVal == val:
                        binaryMatrix[index, j] = int(1)

                    else:
                        continue

            except:
                if dfVal == val:
                    binaryMatrix[index, j] = int(1)

                else:
                    continue

            j += 1

    return binaryMatrix


def measure_similarity(binaryMatrix, df):
    df['Similarity_Score'] = ''
    cheetah = binaryMatrix[0]
    for i in range(len(binaryMatrix)):
        result = spatial.distance.cosine(cheetah, binaryMatrix[i])
        print(result)
        df.at[i, 'Similarity_Score'] = result


    return df


