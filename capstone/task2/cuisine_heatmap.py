#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

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

    x_idx = []
    y_idx = []
    col = []

    for i in range(len(sim_matrix_list)):
        for j in range(len(sim_matrix_list[i])):
            x_idx.append(str(i))
            y_idx.append(str(j))
            col.append(float(sim_matrix_list[i][j]))
            
    plt.scatter(x_idx, y_idx, cmap='Greys', c=col, marker='o', s=50, edgecolor='none')

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






