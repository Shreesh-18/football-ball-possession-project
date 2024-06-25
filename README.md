Football Ball Possession Project
This project aims to analyze football match footage using computer vision techniques to track players, the ball, and the referee. The project leverages YOLO (You Only Look Once) for real-time object detection, OpenCV for image and video processing, and KMeans clustering for pixel segmentation.

Key Features:
Object Detection: Utilizes YOLOv4 for identifying players, the ball, and the referee in football match videos.
Pixel Segmentation: Applies KMeans clustering to segment pixels and distinguish between different elements in the footage.
Ball Possession Calculation: Uses pandas for data manipulation and interpolation to compute ball possession statistics for both teams based on detected ball movements.
Output: Generates visual outputs and statistics to analyze ball possession dynamics throughout the match.
