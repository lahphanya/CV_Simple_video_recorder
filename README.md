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

스크린샷

* **S**

  * 현재 프레임 스크린샷 저장
  * 저장 후 파일명(`time_stamp`)을 화면에 표시

밝기, 대비

* **[ / ]**

  * 밝기(Brightness) 감소 / 증가 (실시간 적용)

* **, / .**

  * 대비(Contrast) 감소 / 증가 (실시간 적용)

* **R**

  * 밝기 / 대비 초기화
  * (Brightness: 0, Contrast: 1.0)

종료

* **ESC**

  * 프로그램 종료


