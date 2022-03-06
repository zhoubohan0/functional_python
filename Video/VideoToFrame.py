import cv2
import os
import time
def output(frame, show=None, tofile=None):
    if tofile is not None:
        cv2.imwrite(tofile, frame)
    if show:
        cv2.imshow('', frame)
        cv2.waitKey()
def vtf(srcpath, destpath):
    if not os.path.exists(destpath):
        os.mkdir(destpath)
    start = time.time()
    videoCapture = cv2.VideoCapture()
    videoCapture.open(srcpath)
    fps = videoCapture.get(cv2.CAP_PROP_FPS)
    frames = videoCapture.get(cv2.CAP_PROP_FRAME_COUNT)
    print("fps=", int(fps), "frames=", int(frames))
    for i in range(int(frames)):
        _, frame = videoCapture.read()
        destfile = os.path.join(destpath, r"%d.jpg" % (i))
        output(frame, tofile=destfile)
    end = time.time()
    print('Successfully!')
    print(f'total:{round(end-start,2)}s')

if __name__ == '__main__':
    srcpath = r"./video.mp4"
    destpath=r'./images'
    vtf(srcpath,destpath)

