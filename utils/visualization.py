import matplotlib.pyplot as plt

# Plot the image and corresponding label
def image_show_with_mask(_images,_mask):
    # Plot all images in a single plot
    fig, axs = plt.subplots(len(_images),2 , figsize=(5, 30))

    for i in range(len(_images)):
        slice_index = _images[i].shape[2] // 2
        axs[i][0].imshow(_images[i][:, :, slice_index], cmap='gray')
        axs[i][0].set_title(f'Image {i + 1}, Slice: {slice_index}')
        axs[i][0].axis("off")

        slice_index = _mask[i].shape[2] // 2
        axs[i][1].imshow(_mask[i][:, :, slice_index], cmap='gray')
        axs[i][1].set_title(f'Mask {i + 1}, Slice: {slice_index}')
        axs[i][1].axis("off")

    plt.show()

# Plot only the images in a single column
def image_show_only(_images):
    # Plot all images in a single column
    fig, axs = plt.subplots(len(_images), 1, figsize=(5, 5 * len(_images)))

    for i in range(len(_images)):
        slice_index = _images[i].shape[2] // 2
        axs[i].imshow(_images[i][:, :, slice_index], cmap='gray')
        axs[i].set_title(f'Image {i + 1}, Slice: {slice_index}')
        axs[i].axis("off")

    plt.show()

def boxplot(dice_data, hd_data, havd_data, tissue_headers):
    # Extracting scores for each tissue type across all images
    # Assuming the first column in your data is the background, which we are skipping
    dice_scores_csf = [row[2] for row in dice_data]  # CSF scores
    dice_scores_gm = [row[3] for row in dice_data]  # GM scores
    dice_scores_wm = [row[4] for row in dice_data]  # WM scores
    dice_scores_avg = [row[5] for row in dice_data]  # WM scores

    hd_scores_csf = [row[2] for row in hd_data]  # CSF scores
    hd_scores_gm = [row[3] for row in hd_data]  # GM scores
    hd_scores_wm = [row[4] for row in hd_data]  # WM scores
    hd_scores_avg = [row[5] for row in hd_data]  # WM scores

    havd_scores_csf = [row[2] for row in havd_data]  # CSF scores
    havd_scores_gm = [row[3] for row in havd_data]  # GM scores
    havd_scores_wm = [row[4] for row in havd_data]  # WM scores
    havd_scores_avg = [row[5] for row in havd_data]  # WM scores

    # Define colors for each boxplot group
    colors = ['lightgreen', 'skyblue', 'lightcoral','green']

    # Creating boxplots for each set of scores
    plt.figure(figsize=(18, 6))

    # Dice Coefficient Scores
    plt.subplot(1, 3, 1)
    bplot1 = plt.boxplot([dice_scores_csf, dice_scores_gm, dice_scores_wm,dice_scores_avg], labels=tissue_headers[1:], patch_artist=True)
    for patch, color in zip(bplot1['boxes'], colors):
        patch.set_facecolor(color)
    plt.title('Dice Coefficient Scores')
    plt.xlabel('Tissue Type')
    plt.ylabel('Score')

    # Hausdorff Distance Scores
    plt.subplot(1, 3, 2)
    bplot2 = plt.boxplot([hd_scores_csf, hd_scores_gm, hd_scores_wm,hd_scores_avg], labels=tissue_headers[1:], patch_artist=True)
    for patch, color in zip(bplot2['boxes'], colors):
        patch.set_facecolor(color)
    plt.title('Hausdorff Distance Scores')
    plt.xlabel('Tissue Type')
    plt.ylabel('Score')

    # Relative Absolute Volume Difference Scores
    plt.subplot(1, 3, 3)
    bplot3 = plt.boxplot([havd_scores_csf, havd_scores_gm, havd_scores_wm,havd_scores_avg], labels=tissue_headers[1:], patch_artist=True)
    for patch, color in zip(bplot3['boxes'], colors):
        patch.set_facecolor(color)
    plt.title('Relative Absolute Volume Difference Scores')
    plt.xlabel('Tissue Type')
    plt.ylabel('Score')

    plt.tight_layout()
    plt.show()
