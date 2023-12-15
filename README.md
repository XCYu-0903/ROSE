# ROSE: A Recognition-Oriented Speech Enhancement Framework in Air Traffic Control Using Multi-Objective Learning
Xincheng Yu, Dongyue Guo, Jianwei Zhang, Yi Lin
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    .audio-container {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap; /* 允许换行 */
    }
    .example-text {
      position: relative;
      top: 50%;
      left: 0.5%; /* 左边 5% 的位置 */
      transform: translateY(-50%); /* 调整位置以垂直居中 */
    }
    .audio-item {
      width: 30%;
      margin-bottom: 10px; /* 调整每个音频条目之间的间距 */
      position: relative; /* 使图片相对于音频容器定位 */
    }
    audio {
      width: 100%; /* 音频播放器充满整个宽度 */
    }
    .audio-label {
      text-align: center;
      margin-top: 5px; /* 调整标签与进度条的间距 */
    }
    .audio-image {
      width: 90%; /* 图片充满整个宽度 */
      max-width: 100%; /* 图片最大宽度为音频容器的宽度 */
      position: relative; /*绝对定位，相对于 .audio-item 定位*/
      /*top: -40px; /* 向上偏移，使其位于进度条上方 */
      left: 50%; /* 居中 */
      transform: translateX(-50%); /* 调整位置以居中 */
    }
  </style>
</head>

<body>

<div class="audio-container">
<div class="example-text">p232_001</div>
  <div class="audio-item">
    <img src="./speech_samples/noisy/p232_001.png" alt="Image" class="audio-image">
    <audio controls id="audio1">
      <source src="./speech_samples/noisy/p232_001.wav" type="audio/wav">
      Your browser does not support the audio element.
    </audio>
    <div class="audio-label">Noisy</div>
  </div>

  <div class="audio-item">
    <img src="./speech_samples/clean/p232_001.png" alt="Image" class="audio-image">
    <audio controls id="audio2">
      <source src="./speech_samples/clean/p232_001.wav" type="audio/wav">
      Your browser does not support the audio element.
    </audio>
    <div class="audio-label">Clean</div>
  </div>

  <div class="audio-item">
    <img src="./speech_samples/ROSE/p232_001.png" alt="Image" class="audio-image">
    <audio controls id="audio3">
      <source src="./speech_samples/ROSE/p232_001.wav" type="audio/wav">
      Your browser does not support the audio element.
    </audio>
    <div class="audio-label">ROSE (Ours)</div>
  </div>
</div>


<div class="audio-container">
<div class="example-text">p232_002</div>
  <div class="audio-item">
    <img src="./speech_samples/noisy/p232_002.png" alt="Image" class="audio-image">
    <audio controls id="audio1">
      <source src="./speech_samples/noisy/p232_002.wav" type="audio/wav">
      Your browser does not support the audio element.
    </audio>
    <div class="audio-label">Noisy</div>
  </div>

  <div class="audio-item">
    <img src="./speech_samples/clean/p232_002.png" alt="Image" class="audio-image">
    <audio controls id="audio2">
      <source src="./speech_samples/clean/p232_002.wav" type="audio/wav">
      Your browser does not support the audio element.
    </audio>
    <div class="audio-label">Clean</div>
  </div>

  <div class="audio-item">
    <img src="./speech_samples/ROSE/p232_002.png" alt="Image" class="audio-image">
    <audio controls id="audio3">
      <source src="./speech_samples/ROSE/p232_002.wav" type="audio/wav">
      Your browser does not support the audio element.
    </audio>
    <div class="audio-label">ROSE (Ours)</div>
  </div>
</div>

<div class="audio-container">
<div class="example-text">p232_003</div>
  <div class="audio-item">
    <img src="./speech_samples/noisy/p232_003.png" alt="Image" class="audio-image">
    <audio controls id="audio1">
      <source src="./speech_samples/noisy/p232_003.wav" type="audio/wav">
      Your browser does not support the audio element.
    </audio>
    <div class="audio-label">Noisy</div>
  </div>

  <div class="audio-item">
    <img src="./speech_samples/clean/p232_003.png" alt="Image" class="audio-image">
    <audio controls id="audio2">
      <source src="./speech_samples/clean/p232_003.wav" type="audio/wav">
      Your browser does not support the audio element.
    </audio>
    <div class="audio-label">Clean</div>
  </div>

  <div class="audio-item">
    <img src="./speech_samples/ROSE/p232_003.png" alt="Image" class="audio-image">
    <audio controls id="audio3">
      <source src="./speech_samples/ROSE/p232_003.wav" type="audio/wav">
      Your browser does not support the audio element.
    </audio>
    <div class="audio-label">ROSE (Ours)</div>
  </div>
</div>


<script>
  // 控制音频播放和停止
  function toggleAudio(audioId) {
    var audio = document.getElementById(audioId);
    if (audio.paused) {
      audio.play();
    } else {
      audio.pause();
    }
  }
</script>

</body>
</html>
