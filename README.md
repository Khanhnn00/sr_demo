# A Demonstration of Single Image Super-Resolution


### Setup
0. **Minimum requirements.** This project was originally developed with Python 3.6, PyTorch 1.7 and CUDA 9.0. The training requires at least a Titan X GPUs (12Gb memory each).
1. **Setup your Python environment.** Please, clone the repository and install the dependencies. We recommend using Anaconda 3 distribution:
    ```
    conda create -n <environment_name> --file requirements.txt
    ```

3. **Download pre-trained models.** Download the initial weights (pre-trained on ImageNet) for the backbones you are planning to use and place them into `<project>/models/weights/`.

    | Backbone | Initial Weights | Comment |
    |:---:|:---:|:---:|
    | WideResNet38 | [ilsvrc-cls_rna-a1_cls1000_ep-0001.pth (402M)](https://download.visinf.tu-darmstadt.de/data/2020-cvpr-araslanov-1-stage-wseg/models/ilsvrc-cls_rna-a1_cls1000_ep-0001.pth) | Converted from [mxnet](https://github.com/itijyou/ademxapp) |
    | VGG16 | [vgg16_20M.pth (79M)](https://download.visinf.tu-darmstadt.de/data/2020-cvpr-araslanov-1-stage-wseg/models/vgg16_20M.pth) | Converted from [Caffe](http://liangchiehchen.com/projects/Init%20Models.html) |
    | ResNet50 | [resnet50-19c8e357.pth](https://download.pytorch.org/models/resnet50-19c8e357.pth) | PyTorch official |
    | ResNet101 | [resnet101-5d3b4d8f.pth](https://download.pytorch.org/models/resnet101-5d3b4d8f.pth) | PyTorch official |


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
We thank PyTorch team, and Jiwoon Ahn for releasing his [code](https://github.com/jiwoon-ahn/psa) that helped in the early stages of this project.

## Citation
We hope that you find this work useful. If you would like to acknowledge us, please, use the following citation:
```
@inproceedings{Araslanov:2020:WSEG,
  title     = {Single-Stage Semantic Segmentation from Image Labels},
  author    = {Araslanov, Nikita and and Roth, Stefan},
  booktitle = {Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year = {2020}
}
```
