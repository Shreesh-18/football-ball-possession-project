import cv2

def read_video(video_path):
    cap=cv2.VideoCapture(video_path) #capturing video frames 
    frames=[]
    while(True):
        ret,frame=cap.read()   #.read() returns a value and frame if value is true
        if not ret:            #breaking if val==false
            break
        frames.append(frame)   #video gets read as frames
    return frames
def save_video(output_video_frames,output_video_path):
    fourcc=cv2.VideoWriter_fourcc(*'XVID') #output format 'XVID'
    res=cv2.VideoWriter(output_video_path,fourcc,24.0,(output_video_frames[0].shape[1],output_video_frames[0].shape[0])) #video writer takes in the output video path, its type,fps,size of frame
    for f in output_video_frames: #iterating over frames and writing it to video writer 
        res.write(f)
    res.release()    



