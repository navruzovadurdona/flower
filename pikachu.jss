<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>Пикачу из CSS</title>
  <style>
    body {
      background: #87ceeb;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }

    .pikachu {
      position: relative;
      width: 200px;
      height: 180px;
    }

    .ear {
      position: absolute;
      width: 30px;
      height: 80px;
      background: yellow;
      border-radius: 50% 50% 0 0;
      top: -60px;
    }

    .ear.left {
      left: 10px;
      transform: rotate(-20deg);
    }

    .ear.right {
      right: 10px;
      transform: rotate(20deg);
    }

    .ear::after {
      content: "";
      position: absolute;
      width: 100%;
      height: 30px;
      background: black;
      bottom: 0;
      border-radius: 0 0 50% 50%;
    }

    .face {
      width: 100%;
      height: 100%;
      background: yellow;
      border-radius: 50% / 40%;
      position: relative;
      z-index: 1;
      box-shadow: 0 0 0 4px #333;
    }

    .eye {
      width: 20px;
      height: 20px;
      background: black;
      border-radius: 50%;
      position: absolute;
      top: 50px;
    }

    .eye.left {
      left: 40px;
    }

    .eye.right {
      right: 40px;
    }

    .cheek {
      width: 24px;
      height: 24px;
      background: red;
      border-radius: 50%;
      position: absolute;
      bottom: 30px;
    }

    .cheek.left {
      left: 20px;
    }

    .cheek.right {
      right: 20px;
    }

    .mouth {
      width: 40px;
      height: 20px;
      background: #d6336c;
      border-radius: 0 0 50% 50%;
      position: absolute;
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%);
    }
  </style>
</head>
<body>
  <div class="pikachu">
    <div class="ear left"></div>
    <div class="ear right"></div>
    <div class="face">
      <div class="eye left"></div>
      <div class="eye right"></div>
      <div class="cheek left"></div>
      <div class="cheek right"></div>
      <div class="mouth"></div>
    </div>
  </div>
</body>
</html>
