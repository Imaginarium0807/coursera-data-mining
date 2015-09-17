#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.cluster import KMeans
from collections import defaultdict

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

def cluster_cuisines(cuis_labels, sim_matrix_list):

    cluster_dict = defaultdict(list)

    K_clusters = 5

    km = KMeans(n_clusters=K_clusters, init='k-means++', max_iter=100, n_init=1,
                verbose=True)

    km.fit(sim_matrix_list)
    
    order_centroids = km.cluster_centers_.argsort()[:, ::-1]
    
    for idx, label in enumerate(km.labels_):
        cluster_dict[label].append((idx, cuis_labels[idx])) 

    return cluster_dict

def plot_heatmap(cuis_labels, sim_matrix_list, cluster_dict):

    cmap_list = ['Blues', 'Greens', 'Reds', 'Purples', 'Oranges',
                'Greys', 'RdPu','YlGn', 'YlOrBr', 'BuPu']

    cluster_cuis_labels = []
    tot_idx = 0

    for key in range(len(cluster_dict.keys())):
        x_idx = []
        y_idx = []
        col = []  
        for cuis in cluster_dict[key]:
            cluster_cuis_labels.append(cuis[1])
            sim_temp = sim_matrix_list[cuis[0]][cuis[0]-tot_idx:] + sim_matrix_list[cuis[0]][:cuis[0]-tot_idx]
            for i in range(len(sim_matrix_list[cuis[0]])):
                x_idx.append(tot_idx)
                y_idx.append(i)
                col.append(float(sim_temp[i]))
            tot_idx+=1
            
        plt.scatter(x_idx, y_idx, cmap=cmap_list[key], c=col, marker='o', s=50, edgecolor='none')

    plt.xticks(range(len(cluster_cuis_labels)), cluster_cuis_labels, rotation=90)
    plt.yticks(range(len(cluster_cuis_labels)), cluster_cuis_labels)

    plt.xlim((-1,len(cluster_cuis_labels)))
    plt.ylim((-1,len(cluster_cuis_labels)))

    plt.gcf().subplots_adjust(bottom=0.3)

    plt.show()

def main():

    cuis_labels_file = 'cuisine_indices.txt'
    cuis_sim_file = 'cuisine_sim_matrix.csv'

    cuis_labels = read_cuis_labels(cuis_labels_file)
    sim_matrix_list = read_sim_matrix(cuis_sim_file)
    cluster_dict = cluster_cuisines(cuis_labels, sim_matrix_list)
    plot_heatmap(cuis_labels, sim_matrix_list, cluster_dict)

if __name__=="__main__":
    main()






