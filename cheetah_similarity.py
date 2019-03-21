import argparse
import numpy
import pandas

from scipy import spatial

from cheetah_similarity_functions import *

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputPath')
    parser.add_argument('--outputPath')
    args = parser.parse_args()

    data = pandas.read_csv(args.inputPath)
    colList = create_column_list(data)
    binaryMatrix = create_binary_matrix(data, colList)
    similarityData = measure_similarity(binaryMatrix, data)
    similarityData.to_csv(args.outputPath)

    print(similarityData)


if __name__== "__main__":
  main()


