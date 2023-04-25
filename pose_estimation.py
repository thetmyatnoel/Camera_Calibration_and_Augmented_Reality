import numpy as np
import cv2 as cv

input_file = 'chessboard.MOV'
K = np.array([[1.65450289e+03, 0.00000000e+00, 9.64907984e+02],
 [0.00000000e+00, 1.65798710e+03, 5.36056186e+02],
 [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]])
dist_coeff = np.array ([ 3.37401908e-01, -2.22725768e+00,  1.79713514e-03, -7.08231523e-04,
  4.80412419e+00])
board_pattern = (10, 7)
board_cellsize = 0.025
board_criteria = cv.CALIB_CB_ADAPTIVE_THRESH + cv.CALIB_CB_NORMALIZE_IMAGE + cv.CALIB_CB_FAST_CHECK

video = cv.VideoCapture(input_file)
assert video.isOpened(), 'Cannot read the given input, ' + input_file

pyramid_base = board_cellsize * np.array([[4, 2, 0], [5, 2, 0], [5, 4, 0], [4, 4, 0]])
pyramid_top = board_cellsize * np.array([[4.5, 3, -1]])

obj_points = board_cellsize * np.array([[c, r, 0] for r in range(board_pattern[1]) for c in range(board_pattern[0])])

while True:
    valid, img = video.read()
    if not valid:
        break

    complete, img_points = cv.findChessboardCorners(img, board_pattern, board_criteria)
    if complete:
        img_points = np.asarray(img_points, dtype=np.float32)
        ret, rvec, tvec = cv.solvePnP(obj_points, img_points, K, dist_coeff)

        line_base, _ = cv.projectPoints(pyramid_base, rvec, tvec, K, dist_coeff)
        line_top, _ = cv.projectPoints(pyramid_top, rvec, tvec, K, dist_coeff)
        cv.polylines(img, [np.int32(line_base)], True, (255, 0, 0), 2)
        for b, t in zip(line_base, [line_top] * 4):
            cv.line(img, tuple(np.int32(b.flatten())), tuple(np.int32(t.flatten())), (0, 255, 0), 2)

        R, _ = cv.Rodrigues(rvec)
        p = (-R.T @ tvec).flatten()
        info = f'XYZ: [{p[0]:.3f} {p[1]:.3f} {p[2]:.3f}]'
        cv.putText(img, info, (10, 25), cv.FONT_HERSHEY_DUPLEX, 0.6, (0, 255, 0))

    cv.imshow('Pose Estimation (Chessboard)', img)
    key = cv.waitKey(10)
    if key == ord(' '):
        key = cv.waitKey()
    if key == 27:
        break

video.release()
cv.destroyAllWindows()
