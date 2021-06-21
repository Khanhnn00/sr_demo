# A Demonstration of Single Image Super-Resolution


### Setup
0. **Minimum requirements.** This project was originally developed with Python 3.6, PyTorch 1.7 and CUDA 9.0. The training requires at least a Titan X GPUs (12Gb memory each).
1. **Setup your Python environment.** Please, clone the repository and install the dependencies. We recommend using Anaconda 3 distribution:
    ```
    conda create -n <environment_name> --file requirements.txt
    ```

3. **Download pre-trained models.** Download the pretrained weights of some model and put it to yout `<project>/models/weights/` folder.

    | Backbone | Initial Weights | Comment |
    |:---:|:---:|:---:|
    | EDSR | [EDSR.pth (512M)](https://drive.google.com/file/d/1Y67gODB1Krq4LEXzDk1ChKzWFbGvn2ni/view?usp=sharing)|
    | SRFBN | [EDSR.pth (49M)](https://drive.google.com/file/d/1KLz5TGhyebk9uUL09Vc0IlT_n7Z99w07/view?usp=sharing) |
    | D_DBPN | [D_DBPN.pth](https://drive.google.com/file/d/1B52cQ_kvM6ThJu96ZxjEUmlxFarPHyBt/view?usp=sharing) |
    | RCAN | [RCAN.pth](https://drive.google.com/file/d/16Zv9A8njlNOJia1PIKjiXysejFugLmBG/view?usp=sharing) |


### How to Run

Currently we only support SRFBN and EDSR model.

First you can change the config in options/test/<your_chosen_model>.json file

Next, run the following command:
    ```
    python app.py
    ```

Go to the url host in the terminal log and try your demo.
You can change the port and the url domain by setting in the line: ```app.run()``` in ```app.py```

The input image will be stored in ```static/downloads```, while the super-resolved image will be available in ```static/uploads```

## Acknowledgements
We thankZhen Li for releasing his [code](https://github.com/Paper99/SRFBN_CVPR19) that helped in the early stages of this project.

