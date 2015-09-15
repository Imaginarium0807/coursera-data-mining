#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt

def read_cuis_labels(cuis_labels_file):

    cuis_labels = []

    labels_file = open(cuis_labels_file, 'r')

    for label in labels_file:
        cuis_labels.append(label.strip())

    labels_file.close()

    return cuis_labels

def read_sim_matrix(cuis_sim_file):

    sim_matrix_list = []

    matrix_file = open(cuis_sim_file, 'r')

    for line in matrix_file:
        sim_matrix_list.append(line.strip().split(','))

    matrix_file.close()

    return sim_matrix_list

def plot_heatmap(cuis_labels, sim_matrix_list):
    
    for i in range(len(sim_matrix_list)):
        for j in range(len(sim_matrix_list[i])):
            plt.scatter(i, j, color=str(1.0-float(sim_matrix_list[i][j])))

    plt.xticks(range(len(cuis_labels)), cuis_labels, rotation=90)
    plt.yticks(range(len(cuis_labels)), cuis_labels)

    plt.xlim((-1,len(cuis_labels)))
    plt.ylim((-1,len(cuis_labels)))

    plt.gcf().subplots_adjust(bottom=0.3)

    plt.show()

def main():

    cuis_labels_file = 'cuisine_indices.txt'
    cuis_sim_file = 'cuisine_sim_matrix.csv'

    cuis_labels = read_cuis_labels(cuis_labels_file)
    sim_matrix_list = read_sim_matrix(cuis_sim_file)
    plot_heatmap(cuis_labels, sim_matrix_list)

if __name__=="__main__":
    main()






