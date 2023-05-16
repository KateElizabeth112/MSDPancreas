# Convert the names of the training and test images to have the nnUNet format
import os

#ROOT_DIR = '/Users/katecevora/Documents/PhD/data/AMOS_3D/'
ROOT_DIR = '/vol/biomedic3/kc2322/data/MSDPanccreas'
TRAIN_DIR = os.path.join(ROOT_DIR, "nnUNet_raw/Dataset100_MSDPancreas/imagesTr")


def main():
    # list files in training directory
    names = os.listdir(TRAIN_DIR)

    # count of training cases
    count = 0

    for n in names:
        if n.endswith(".nii.gz"):
            count += 1
            try:
                n.split("_")[2][0]
            except:
                root = n.split(".")[0]
                n_new = root + "_0000.nii.gz"

                os.rename(os.path.join(TRAIN_DIR, n), os.path.join(TRAIN_DIR, n_new))

    print("Number of training cases: {}".format(count))

if __name__ == "__main__":
    main()