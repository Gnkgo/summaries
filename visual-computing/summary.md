## Frames

I, P, and B frames are fundamental components of video compression, each serving a specific role in optimizing efficiency, quality, and error resilience:

### I-Frames (Intra-frames):

Purpose: I-frames are standalone frames that don't rely on other frames for compression. They serve as reference points and contain spatial redundancies within the same frame.

Usage: I-frames are crucial for refreshing video quality, recovery from bitstream errors, and marking the end of a Group of Pictures (GOP) or a video segment.

### P-Frames (Predicted Frames):

Purpose: P-frames utilize both temporal and spatial prediction for compression. They can be temporally predicted, spatially predicted, or skipped, relying on information from previously encoded frames.

Usage: P-frames contribute to reducing video size while maintaining quality. They play a role in maintaining a continuous flow by referring to previously encoded pictures.

### B-Frames (Bi-Directional Frames):

Purpose: B-frames can reference frames both before and after them, utilizing bidirectional prediction. They offer efficiency by exploiting spatial and temporal redundancies from both past and future frames.

Usage: While efficient, B-frames are resource-intensive for both encoding and decoding. They are strategically placed in the video stream to achieve a balance between reduced file size and maintained quality.
In summary, I-frames act as independent reference points, P-frames use predictions from previous frames, and B-frames leverage bidirectional predictions for optimal video compression. Together, they form a dynamic framework for achieving efficient video encoding, streaming, and error recovery.

![Alt text](image.png)
![![Alt text](image.png)](image.png)
![Alt text](image.png)
![Alt text](image.png)
![Alt text](image.png)
![Alt text](image.png)![Alt text](image.png)
![Alt text](image.png)
![Alt text](image.png)
![Alt text](image.png)
![Alt text](image.png)
![Alt text](image.png)
![Alt text](image.png)
![Alt text](image.png)
![Alt text](image.png)
![Alt text](image.png)
![Alt text](image.png)