from modules.data_loader import DataLoader
from modules.camera_pose_estimation import CameraPoseEstimation
from modules.initial_alignment import InitialAlignment
from modules.icp_alignment import ICPAlignment
from modules.automation import Automation
from modules.logging_report import LoggingReport

def main():
    # 初始化模組
    data_loader = DataLoader()
    camera_pose_estimation = CameraPoseEstimation()
    initial_alignment = InitialAlignment()
    icp_alignment = ICPAlignment()
    automation = Automation()
    logging_report = LoggingReport()

    # 數據加載和處理流程
    images, point_clouds = data_loader.load_data()
    camera_poses = camera_pose_estimation.estimate_poses(images)
    aligned_point_clouds = initial_alignment.align(point_clouds, camera_poses)
    final_aligned_point_clouds = icp_alignment.refine_alignment(aligned_point_clouds)
    automation.process(final_aligned_point_clouds)
    logging_report.generate_report()

if __name__ == "__main__":
    main()
