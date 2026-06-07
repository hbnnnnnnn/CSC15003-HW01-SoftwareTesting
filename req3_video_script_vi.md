# Kịch bản quay video Requirement 3

Thiết bị kiểm thử: **Mitsubishi LV16-RM**

Gợi ý chung cho mỗi video:
- Mở đầu: nói mã test case và mục tiêu kiểm thử.
- Quay rõ trạng thái ban đầu của quạt.
- Thực hiện từng bước chậm, rõ.
- Cuối video nhớ nói: **Kết quả mong đợi / Kết quả thực tế / Kết luận Pass hoặc Fail**.
- Nên quay dọc hoặc ngang nhưng giữ cố định góc máy, có đủ cả quạt và tay thao tác.

---

## Video 1 — FAN-TC001: Kiểm tra bật / tắt quạt

### Mục tiêu
Kiểm tra quạt có thể bật và tắt bình thường.

### Kịch bản đọc
> Đây là test case **FAN-TC001**, kiểm tra chức năng **bật và tắt quạt** của quạt Mitsubishi LV16-RM.  
> Trạng thái ban đầu: quạt đã được cắm điện và đang ở trạng thái tắt.  
> Bước 1: Tôi nhấn nút nguồn để bật quạt.  
> Bước 2: Quan sát cánh quạt bắt đầu quay.  
> Bước 3: Tôi nhấn nút nguồn thêm một lần nữa để tắt quạt.  
> Kết quả mong đợi: quạt bật lên bình thường khi nhấn nút nguồn, và dừng quay hoàn toàn khi nhấn tắt.  
> Kết quả thực tế: [bạn tự nói theo thực tế khi quay].  
> Kết luận: [Pass hoặc Fail].

### Mẹo quay
- Quay cận nút nguồn lúc bấm.
- Sau đó lùi nhẹ để thấy rõ cánh quạt quay rồi dừng hẳn.

---

## Video 2 — FAN-TC003: Kiểm tra 3 mức gió

### Mục tiêu
Kiểm tra quạt hỗ trợ đủ 3 mức tốc độ và lưu lượng gió tăng dần.

### Kịch bản đọc
> Đây là test case **FAN-TC003**, kiểm tra **3 mức tốc độ gió** của quạt Mitsubishi LV16-RM.  
> Trạng thái ban đầu: quạt đã bật và hoạt động bình thường.  
> Bước 1: Tôi chọn mức gió 1.  
> Bước 2: Tôi chọn mức gió 2.  
> Bước 3: Tôi chọn mức gió 3.  
> Kết quả mong đợi: quạt hoạt động được ở cả 3 mức và luồng gió tăng dần từ mức 1 đến mức 3.  
> Kết quả thực tế: [bạn tự nói theo thực tế khi quay].  
> Kết luận: [Pass hoặc Fail].

### Mẹo quay
- Có thể để một mảnh giấy hoặc khăn giấy trước quạt để thấy khác biệt luồng gió.
- Nếu âm thanh thay đổi theo tốc độ, cứ để micro thu tự nhiên.

---

## Video 3 — FAN-TC005 / FAN-TC006: Kiểm tra bật / tắt đảo gió

### Mục tiêu
Kiểm tra quạt đảo trái-phải khi bật oscillation và dừng đúng khi tắt oscillation.

### Kịch bản đọc
> Đây là test case **FAN-TC005 và FAN-TC006**, kiểm tra chức năng **đảo gió trái phải**.  
> Trạng thái ban đầu: quạt đang bật ở trạng thái bình thường.  
> Bước 1: Tôi bật chức năng đảo gió.  
> Bước 2: Quan sát đầu quạt quay qua lại theo phương ngang.  
> Bước 3: Tôi tắt chức năng đảo gió.  
> Kết quả mong đợi: khi bật, đầu quạt quay trái phải liên tục; khi tắt, đầu quạt dừng lại và giữ cố định ở một hướng.  
> Kết quả thực tế: [bạn tự nói theo thực tế khi quay].  
> Kết luận: [Pass hoặc Fail].

### Mẹo quay
- Nên quay đủ một chu kỳ đảo gió.
- Khi tắt, giữ máy thêm vài giây để chứng minh đầu quạt đứng yên.

---

## Video 4 — FAN-TC007: Kiểm tra phục hồi sau khi chặn đảo gió

### Mục tiêu
Kiểm tra hành vi của đầu quạt khi đang đảo gió bị giữ lại bằng tay rồi thả ra.

### Kịch bản đọc
> Đây là test case **FAN-TC007**, kiểm tra **hành vi phục hồi khi chặn đầu quạt trong lúc đảo gió**.  
> Trạng thái ban đầu: quạt đang bật và chức năng đảo gió đang hoạt động.  
> Bước 1: Tôi dùng tay giữ đầu quạt lại khi quạt đang đảo.  
> Bước 2: Tôi thả tay ra và quan sát hướng chuyển động tiếp theo của đầu quạt.  
> Kết quả mong đợi: sau khi thả tay, đầu quạt nên đổi hướng quay lại theo chiều ngược lại một cách mượt mà.  
> Kết quả thực tế: sau khi thả tay, đầu quạt tiếp tục đi tới biên độ đảo gió lớn nhất rồi mới đổi hướng.  
> Kết luận: **Fail**.

### Mẹo quay
- Đây là video quan trọng vì có lỗi thật.
- Quay góc rộng để thấy rõ tay giữ, lúc thả tay, và hướng đầu quạt tiếp tục di chuyển.
- Nói rõ đây là lỗi đã phát hiện trong quá trình test.

---

## Video 5 — FAN-TC015: Kiểm tra đổi mức gió khi đang đảo gió

### Mục tiêu
Kiểm tra quạt vẫn hoạt động ổn định khi thay đổi tốc độ trong lúc chức năng đảo gió đang bật.

### Kịch bản đọc
> Đây là test case **FAN-TC015**, kiểm tra **đổi mức gió khi quạt đang đảo gió**.  
> Trạng thái ban đầu: quạt đang bật và chức năng đảo gió đã được kích hoạt.  
> Bước 1: Tôi bật quạt.  
> Bước 2: Tôi bật chức năng đảo gió.  
> Bước 3: Trong khi quạt đang đảo trái phải, tôi lần lượt chuyển qua mức gió 1, mức gió 2, và mức gió 3.  
> Bước 4: Tôi quan sát xem quạt có tiếp tục đảo gió bình thường hay không, và việc đổi mức gió có làm quạt bị dừng, khựng, hay phát sinh hành vi bất thường hay không.  
> Kết quả mong đợi: quạt vẫn tiếp tục đảo gió bình thường trong suốt quá trình đổi tốc độ, không bị dừng, không bị kẹt, và không có hành vi bất thường.  
> Kết quả thực tế: [bạn tự nói theo thực tế khi quay].  
> Kết luận: [Pass hoặc Fail].

### Mẹo quay
- Quay góc đủ rộng để thấy đầu quạt đang đảo.
- Tay bấm nút hoặc xoay núm tốc độ phải nằm trong khung hình.
- Đây là case tốt hơn video tiếng ồn vì kết quả nhìn thấy rõ bằng hình ảnh.

---

## Gợi ý câu kết chung cho mọi video
Bạn có thể dùng mẫu này ở cuối mỗi video:

> Tóm lại, test case này có kết quả thực tế là [mô tả ngắn].  
> So với kết quả mong đợi, kết luận của tôi là **[Pass / Fail]**.

---

## Gợi ý đặt tên file video
- `FAN-TC001-power-on-off.mp4`
- `FAN-TC003-speed-levels.mp4`
- `FAN-TC005-006-oscillation-on-off.mp4`
- `FAN-TC007-oscillation-interruption-fail.mp4`
- `FAN-TC015-speed-change-during-oscillation.mp4`
