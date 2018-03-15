def compose_image(images, masks, background):
    """
    description:
    this function takes images and corresponding masks and one background to
    generate augmented traning dataset image.

    rotate, translate, resize
    
    input:
    images: a list of image arrays
    masks: a list of mask arrays
    background: a image array of background

    output:
    image: a composed image
    masks: a list of newly transformed masks
    """
    pass

def generate_composed_images(root_dir, max_cnt=200):
    """
    description:
    this function takes the root directory and read dataset and generated
    augmented dataset.

    input:
    root_dir: the root directory of the dataset

    outputs:

    """
