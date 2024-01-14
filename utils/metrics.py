import numpy as np
from scipy.spatial.distance import directed_hausdorff

N_CLASSES = 4

#Dice score
def dice_score_per_class(segmented, ground_truth, num_classes=N_CLASSES):
    dice_scores = []
    for class_label in range(num_classes):
        # if class_label != 1:
            seg_binary = (segmented == class_label)
            gt_binary = (ground_truth == class_label)
            intersection = np.sum(seg_binary & gt_binary)
            sum_ = np.sum(seg_binary) + np.sum(gt_binary)
            dice_score = (2. * intersection) / sum_ if sum_ != 0 else 1
            # dice_score = f"{dice_score:.4f}"
            dice_scores.append(dice_score)
    return dice_scores

# Hausdorff Distance (HD)
def hausdorff_distance_per_class(segmented, ground_truth, num_classes=N_CLASSES):
    hd_per_class = []
    for class_label in range(num_classes):
        # if class_label != 1:
            seg_binary = (segmented == class_label)
            gt_binary = (ground_truth == class_label)
            seg_coords = np.array(np.where(seg_binary)).T
            gt_coords = np.array(np.where(gt_binary)).T
            if seg_coords.size == 0 or gt_coords.size == 0:
                hd = 0  # or some appropriate default value
            else:
                hd1 = directed_hausdorff(seg_coords, gt_coords)[0]
                hd2 = directed_hausdorff(gt_coords, seg_coords)[0]
                hd = max(hd1, hd2)
            # hd_per_class = f"{hd_per_class:.4f}"
            hd_per_class.append(hd)
    return hd_per_class

# Relative Absolute Volume Difference (RAVD)
def ravd_per_class(segmented, ground_truth, num_classes=N_CLASSES):
    ravd_scores = []
    for class_label in range(num_classes):
        # if class_label != 1:
            seg_binary = (segmented == class_label)
            gt_binary = (ground_truth == class_label)
            ravd = abs(np.sum(seg_binary) - np.sum(gt_binary)) / np.sum(gt_binary) if np.sum(gt_binary) != 0 else 0
            # ravd_scores = f"{ravd_scores:.4f}"
            ravd_scores.append(ravd)
    return ravd_scores

