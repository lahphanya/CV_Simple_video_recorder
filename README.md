# CV_Simple_video_recorder

OpenCV를 이용한 간단한 Video Recorder입니다.
코덱은 **XVID**를 사용하며, `.avi` 형식으로 저장됩니다.

---

주요 기능

* 실시간 화면 표시 (`display_frame`)
* 원본 프레임 (`frame`) 별도 처리 (녹화 및 스크린샷용)
* Desktop 경로에 자동 저장
* 파일명: `YYYYMMDD_HHMMSS.확장자`

---

조작 키

* **Spacebar**

  * 녹화 시작 / 종료
  * 종료 즉시 바탕화면에 자동 저장
  * 녹화 시간 표시 + 저장된 파일명을 `display_frame`에 출력
  * display_frame https://github.com/user-attachments/assets/ee83dbf5-01fb-42af-92f9-7ce84e4bedc6
  * frame https://github.com/user-attachments/assets/d0cadd4f-2eda-4c34-9762-3584a41f03e9

스크린샷

* **S**

  * 현재 프레임 스크린샷 저장
  * 저장 후 파일명(`time_stamp`)을 화면에 표시
  * dispaly_frame https://github.com/user-attachments/assets/a34a44ed-ecf6-4366-aa82-0877733b2700"
  * frame https://github.com/user-attachments/assets/3c8ccc77-af3a-4ff0-8e04-4ccdca23e165

밝기, 대비

* **[ / ]**

  * 밝기(Brightness) 감소 / 증가 (실시간 적용)
  * https://github.com/user-attachments/assets/5643b478-fdc9-4276-9bb0-9032b1ca27a6

* **, / .**

  * 대비(Contrast) 감소 / 증가 (실시간 적용)
  * https://github.com/user-attachments/assets/880b5a67-3d6b-44ca-aaa4-a144f7d7275e

* **R**

  * 밝기 / 대비 초기화
  * (Brightness: 0, Contrast: 1.0)
  * https://github.com/user-attachments/assets/ea49887c-1fef-434a-91e3-5c1bcbf805f4

종료

* **ESC**

  * 프로그램 종료


