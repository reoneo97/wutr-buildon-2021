import json
import boto3
import numpy as np
import PIL.Image as Image

import os
import platform
import shutil
import time
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

from utils.google_utils import attempt_load
from utils.datasets import LoadImages
from utils.general import (
    check_img_size, non_max_suppression, apply_classifier, scale_coords, xyxy2xywh, strip_optimizer)
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized

from models.models import *
from utils.datasets import *
from utils.general import *

def load_classes(path):
    # Loads *.names file at 'path'
    with open(path, 'r') as f:
        names = f.read().split('\n')
    return list(filter(None, names))  # filter removes empty strings (such as last line)

def detect(img):
    weights = 'weight/yolor_p6.pt'
    cfg = 'cfg/yolor_p6.cfg'
    names = 'data/coco.names'
    saveto = 'weight/model.weights'
    imgsz = 1280

    # Initialize
    device = select_device('cpu')

    # find dimension of image
    to_read = cv2.imread(img)
    height, width, _ = to_read.shape

    # Load model
    model = Darknet(cfg, imgsz)#.cuda() #if you want cuda remove the comment

    ckpt = torch.load(weights)  # load checkpoint
    try:
        ckpt['model'] = {k: v for k, v in ckpt['model'].items() if model.state_dict()[k].numel() == v.numel()}
        model.load_state_dict(ckpt['model'], strict=False)
        # save_weights(model, path=saveto, cutoff=-1)
    except KeyError as e:
        print(e)
    # model = attempt_load(weights, map_location=device)  # load FP32 model
    # imgsz = check_img_size(imgsz, s=model.stride.max())  # check img_size
    model.to(device).eval()

    # Set Dataloader
    dataset = LoadImages(img, img_size=imgsz, auto_size=64)

    # Get names, and colors for bbox
    names = load_classes(names)
    # colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(names))]

    # Run inference
    img = torch.zeros((1, 3, imgsz, imgsz), device=device)  # init img
    for path, img, im0s in dataset:
        img = torch.from_numpy(img).to(device)
        img = img.float() 
        img /= 255.0  # 0 - 255 to 0.0 - 1.0
        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        # Inference
        pred = model(img)[0]

        # Apply NMS
        pred = non_max_suppression(pred, 0.25, 0.5)

        # Process detections
        for i, det in enumerate(pred):  # detections per image
            p, s, im0 = path, '', im0s

            s += '%gx%g ' % img.shape[2:]  # print string
            gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
            if det is not None and len(det):
                # Rescale boxes from img_size to im0 size
                det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                # Print results
                for c in det[:, -1].unique():
                    n = (det[:, -1] == c).sum()  # detections per class
                    s += '%g %ss, ' % (n, names[int(c)])  # add to string

                # Write results
                results = []
                for *xyxy, conf, cls in det:
                    # Write to file
                    xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                    xywh[0] = int(xywh[0] * width)
                    xywh[1] = int(xywh[1] * height)
                    xywh[2] = int(xywh[2] * width)
                    xywh[3] = int(xywh[3] * height)
                    results.append(dict(cls = names[int(cls)], bbox = xywh))
                
                print(results)


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    fileObj = s3.get_object(Bucket=bucket_name, Key=key)
    file_content = fileObj["Body"].read()

    np_array = np.fromstring(file_content, np.uint8)
    image_np = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    cv2.imwrite("/tmp/image.jpg", image_np)

    with torch.no_grad():
        detect("/tmp/image.jpg")

    # prediction = model.predict(img[np.newaxis, ...])
    # predicted_class = imagenet_labels[np.argmax(prediction[0], axis=-1)]
    # print('ImageName: {0}, Prediction: {1}'.format(key, predicted_class))

