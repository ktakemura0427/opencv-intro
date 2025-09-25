import cv2
import cv2.aruco as aruco
import numpy as np
import math

# 立方体の座標
cube = np.float32(
    [
        [0.025, 0.025, 0],
        [-0.025, 0.025, 0],
        [-0.025, -0.025, 0],
        [0.025, -0.025, 0],
        [0.025, 0.025, 0.05],
        [-0.025, 0.025, 0.05],
        [-0.025, -0.025, 0.05],
        [0.025, -0.025, 0.05]
    ])

def rotate_cube(cube, angle):
    axis = [0,0,1]
    axis = axis / np.linalg.norm(axis)
    x, y, z = axis + [0.025, 0.025, 0]
    kn=np.array([
        [0,-z,y],
        [z,0,-x],
        [-y,x,0],
        ])
    rot_matrix = np.eye(3) + math.sin(angle)*kn + (1-math.cos(angle))*kn@kn
    return np.dot(cube, rot_matrix.T)

def draw_lines(img,outpts):
    #底面,上面の描画
    for i in range(0,3):
        cv2.line(img,outpts[i],outpts[i+1],(255,0,0),2)
    for i in range(4,7):
        cv2.line(img,outpts[i],outpts[i+1],(0,255,0),2)
    cv2.line(img,outpts[3],outpts[0],(255,0,0),2)
    cv2.line(img,outpts[7],outpts[4],(0,255,0),2)
    #支柱の描画
    for i in range(4):
        cv2.line(img,outpts[i],outpts[i+4],(0,0,250),2)

def draw_points(img,outpts):
    for i in range(8):
        cv2.circle(img, outpts[i], 10, (200, 200, 200), thickness=-1, lineType=cv2.LINE_AA)
        cv2.putText(img, str(i), outpts[i], cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0), thickness=2)



def main():
    global cube
    cap = cv2.VideoCapture(0)
    ret, img = cap.read()
    
#    scale_percent = 100 # percent of original size
    width = int(img.shape[1])
    height = int(img.shape[0])

    # Set AR Marker
    aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)
    parameters = aruco.DetectorParameters()
    center = (width, height)
    focal_length = center[0] / np.tan(60/2 * np.pi / 180)
    camera_matrix = np.array(
        [[focal_length, 0, center[0]],
        [0, focal_length, center[1]],
        [0, 0, 1]], dtype = "double"
        )
    dist_coeffs = np.zeros((4,1)) # レンズ歪みなしと仮定

    rotation_angle=0
    while cap.isOpened():
        ret, img = cap.read()
        corners, ids, _ = aruco.detectMarkers(img, aruco_dict, parameters=parameters)

        rotation_angle +=1
        rotated_cube=rotate_cube(cube,rotation_angle)

        if len(corners) > 0:
            for i, corner in enumerate(corners):
                #ARマーカのカメラに対する姿勢を算出
                rvecs, tvecs, _objPoints = aruco.estimatePoseSingleMarkers(corner, 0.05, camera_matrix, dist_coeffs)
                tvec = np.squeeze(tvecs)
                rvec = np.squeeze(rvecs)
                rvec_matrix = cv2.Rodrigues(rvec) # 回転ベクトルからrodoriguesへ変換
                rvec_matrix = rvec_matrix[0]      # rodoriguesから抜き出し

                # cubeの座標をARマーカに合わせる
                imgpts, jac = cv2.projectPoints(rotated_cube.T, rvecs, tvecs, camera_matrix, dist_coeffs)
                outpts = []

                for lp in imgpts:
                    lp_int = lp.astype(np.int64)#int64に変換
                    outpts.append( tuple(lp_int.ravel()) )#1次元のリストに変換して，append
                    
                # ARマーカに合わせたcubeを描画
                draw_lines(img,outpts)
                draw_points(img,outpts)

        cv2.imshow('frame', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
