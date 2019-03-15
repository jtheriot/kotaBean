import numpy
import pandas

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
                        colList.append(colName)

        else:
            for val in df[col].unique():
                colName = '.'.join([str(col), str(val)])

                if colName in colList:
                    continue

                else:
                    colList.append(colName)

    return colList

def create_binary_matrix(df):
    binaryMatrix = numpy.
