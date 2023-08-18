prediction=[{'boxes': tensor([[ 463.2278,  492.0945,  524.2745,  543.1918],
        [ 719.0969,  733.7517,  776.8850,  781.1722],
        [ 650.6390,   72.7556,  708.9260,  137.0632],
        [ 922.5723,  270.0039,  995.7748,  335.2264],
        [ 689.7517,   14.0318, 1884.4875, 1057.5914],
        [1335.9111,  542.1382, 1917.5630, 1072.4794],
        [ 144.6495,    0.0000, 1465.6884, 1076.8715],
        [ 608.3247,  989.2097,  665.8813, 1036.1261],
        [ 757.1891,  595.7855, 1897.0961, 1078.2555],
        [ 475.5089,  150.6285,  536.3021,  213.0928],
        [1759.2998,  264.0535, 1821.2380,  318.6915],
        [1326.4570,   29.6509, 1884.1067,  652.1895],
        [1344.4120,  147.3298, 1405.1614,  203.0952],
        [ 682.3860,  717.9130,  779.2701,  787.2537],
        [1696.4534,  782.5741, 1767.8085,  832.4656],
        [ 322.3041,  798.3397,  370.9144,  835.2972],
        [ 322.2950,  797.1754,  370.5246,  837.2778],
        [ 278.2716,  151.6615,  959.9333, 1054.4834],
        [ 920.0955,  268.9501,  998.0834,  335.8763],
        [ 801.7682,  695.7858, 1546.1615, 1060.2850],
        [ 459.4806,  313.3503,  676.4756,  466.9601],
        [ 536.4110,  663.9547,  606.0880,  748.5099],
        [ 341.1513,  451.2970, 1694.1349, 1077.0492],
        [ 655.5180,  114.0751,  693.5930,  153.2521]], device='cuda:0'), 'labels': tensor([53, 53, 53, 53, 64, 64, 64, 53, 64, 53, 53, 64, 53, 53, 53, 37, 53, 64,
        37, 64, 56, 56, 64, 53], device='cuda:0'), 'scores': tensor([0.9012, 0.7610, 0.7213, 0.5960, 0.4480, 0.4346, 0.3053, 0.2294, 0.2237,
        0.1887, 0.1793, 0.1735, 0.1702, 0.1526, 0.1222, 0.0989, 0.0967, 0.0938,
        0.0897, 0.0773, 0.0659, 0.0625, 0.0530, 0.0503], device='cuda:0')}]

pred_boxes=[[(463, 492), (524, 543)], [(719, 733), (776, 781)], [(650, 72), (708, 137)], [(922, 270), (995, 335)], [(689, 14), (1884, 1057)], [(1335, 542), (1917, 1072)], [(144, 0), (1465, 1076)], [(608, 989), (665, 1036)], [(757, 595), (1897, 1078)], [(475, 150), (536, 213)], [(1759, 264), (1821, 318)], [(1326, 29), (1884, 652)], [(1344, 147), (1405, 203)], [(682, 717), (779, 787)], [(1696, 782), (1767, 832)], [(322, 798), (370, 835)], [(322, 797), (370, 837)], [(278, 151), (959, 1054)], [(920, 268), (998, 335)], [(801, 695), (1546, 1060)], [(459, 313), (676, 466)], [(536, 663), (606, 748)], [(341, 451), (1694, 1077)], [(655, 114), (693, 153)]]
pred_labels=[53, 53, 53, 53, 64, 64, 64, 53, 64, 53, 53, 64, 53, 53, 53, 37, 53, 64, 37, 64, 56, 56, 64, 53]
pred_score=[0.9012221, 0.7610265, 0.7213229, 0.5959654, 0.4480301, 0.43456036, 0.30529016, 0.22936694, 0.22374584, 0.18869679, 0.1792607, 0.1734604, 0.1702141, 0.15261094, 0.12221192, 0.098899454, 0.096669525, 0.09384448, 0.08965103, 0.07730669, 0.06590453, 0.06252259, 0.05298276, 0.050304584]

try:
    if pred_score[0] > score_threshold:
        # threshold selection, this could be improved with GPU operations
        new_boxes = [i for i, j in zip(pred_boxes, pred_score) if j > score_threshold]
        new_scores = [i for i in pred_score if i > score_threshold]
        new_labels = [i for i, j in zip(pred_labels, pred_score) if j > score_threshold]

        image_drawed = draw_bounding_boxes_frame(a_frame_image, new_boxes, new_scores, new_labels,
                                                 self.COCO_INSTANCE_CATEGORY_NAMES)
    else:
        image_drawed = a_frame_image
except(IndexError):
    print('IndexError')




    COCO_INSTANCE_CATEGORY_NAMES = [
        '__background__', 'person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus',
        'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'N/A', 'stop sign',
        'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
        'elephant', 'bear', 'zebra', 'giraffe', 'N/A', 'backpack', 'umbrella', 'N/A', 'N/A',
        'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball',
        'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket',
        'bottle', 'N/A', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl',
        'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza',
        'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'N/A', 'dining table',
        'N/A', 'N/A', 'toilet', 'N/A', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
        'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'N/A', 'book',
        'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush'
    ]