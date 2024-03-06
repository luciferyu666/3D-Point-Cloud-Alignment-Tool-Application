import pcl
import numpy as np

def filter_point_cloud(point_cloud, std_dev_mul_thresh=1.0):
    filter = point_cloud.make_statistical_outlier_filter()
    filter.set_mean_k(50)
    filter.set_std_dev_mul_thresh(std_dev_mul_thresh)
    return filter.filter()

def downsample_point_cloud(point_cloud, leaf_size=0.01):
    vg = point_cloud.make_voxel_grid_filter()
    vg.set_leaf_size(leaf_size, leaf_size, leaf_size)
    return vg.filter()

def preprocess_point_cloud(point_cloud_path):
    point_cloud = pcl.load(point_cloud_path)
    point_cloud = filter_point_cloud(point_cloud)
    point_cloud = downsample_point_cloud(point_cloud)
    return point_cloud
