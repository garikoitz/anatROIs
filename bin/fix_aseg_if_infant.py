#!/usr/bin/env python2.7
# Create the two hemispheres

if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('-mriDir', type=str,  help='Path to fs mri dir')
    args = ap.parse_args()

    import numpy as np
    import nibabel as nib
    import os 
    from scipy import ndimage

    # Backup the old aseg
    os.rename(os.path.join(mriDir,'aseg.mgz'),os.path.join(mriDir,'aseg_old.mgz'))

    # Read the old one
    img = nib.load(os.path.join(args.mriDir,'aseg_old.mgz'))

    # Extract the data
    data = img.get_fdata()
   
    # Fix thalamus
    data[data==9]=10
    data[data==48]=49

    # Fix medulla
    data[np.logical_and(data>=173, data<=175)]=16
    
    # fix vermis  
    CL=data==8
    CR=data==47  
    DL=ndimage.morphology.distance_transform_edt(CL==0)
    DR=ndimage.morphology.distance_transform_edt(CR==0)
    data[np.logical_and(data==172, DL<DR)]=8
    data[data==172]=47 

    # save the file
    newimg = nib.Nifti1Image(data, img.affine, img.header)
    nib.save(newimg, os.path.join(mriDir,'aseg.mgz'))

