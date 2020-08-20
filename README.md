App dịch màn hình realtime
*đặt vấn đề:
-khi sử dụng điện thoại có nhiều nội dung cần dịch: ảnh trong app, text trong manga, đọc hentai không cần bật tab google dịch
====> ứng dụng dịch realtime ngay trên màn hình

*chương trình:
-root needed? : có thể có hoặc không, ưu tiên non-root
-dựa trên tính năng của android: filter screen
-dạng: filter-screen hoặc dạng pop-up
-cách hoạt động: + quét toàn bộ content tại thời điểm sử dụng (realtime) ===> dịch ===> hiển thị đè đè nội dung đã dịch lên màn hình (có thể cần root), lặp lại quá trình trên khi có sự thay đổi nội dung
				 + quét toàn bộ content tại thời điểm mở pop-up ===> dịch ===> hiển thị đè nội dung đã dịch lên màn hình
-yêu cầu: -transparent 100%
		  -ngoại trừ pop-up và nội dung text, không được làm mất, che phủ, thay đổi content trên màn hình tại thời điểm dịch
		  
*những thuật toán cần sử dụng:
-text-detector
-text-recognize (OCR)

*mở rộng:
-cho phép chọn 1 vùng cố định để dịch realtime


*reference:
-text-detector: https://www.pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/
-text-recognize: https://www.pyimagesearch.com/2018/09/17/opencv-ocr-and-text-recognition-with-tesseract/
