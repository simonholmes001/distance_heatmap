import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import figure

# import argparse
#
# parser = argparse.ArgumentParser(description='Input a source for the distance map')
# parser.add_argument('-s', '--source_file', help='An input source file must be named', required=True)
#
# args = parser.parse_args()
#
# source = args.source_file

class Heatmap:

    def __init__(self, source):
        self.source = source


    def loader(self):
        """
        Takes as input a pickle object of a square pytorch tensor (distance map)
        :return: distance map as a pytorch tensor
        """

        with open(self.source, 'rb') as labels_file:
            self.distance_map = pd.read_pickle(labels_file)

        return self.distance_map


    def make_distance_map(self):

        plt.figure(figsize = (15,7.5))
        ax = sns.heatmap(self.distance_map)
        plt.savefig("plot.png")
        plt.show()

def main(source):
    heat = Heatmap(source)
    heat.loader()
    heat.make_distance_map()

if __name__ == '__main__':
    main(source)