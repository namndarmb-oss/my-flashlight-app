name: Build Luxury Torch APK

on:
  push:
    branches: [ main, master ]
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v5
      with:
        python-version: '3.10'
    
    - name: Cache pip packages
      uses: actions/cache@v4
      with:
        path: ~/.cache/pip
        key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
        restore-keys: |
          ${{ runner.os }}-pip-
    
    - name: Cache Buildozer
      uses: actions/cache@v4
      with:
        path: .buildozer
        key: ${{ runner.os }}-buildozer-${{ hashFiles('buildozer.spec') }}
        restore-keys: |
          ${{ runner.os }}-buildozer-
    
    - name: Install system dependencies
      run: |
        sudo apt-get update
        sudo apt-get install -y \
          python3-pip \
          build-essential \
          git \
          python3-dev \
          ffmpeg \
          libsdl2-dev \
          libsdl2-image-dev \
          libsdl2-mixer-dev \
          libsdl2-ttf-dev \
          libportmidi-dev \
          libswscale-dev \
          libavformat-dev \
          libavcodec-dev \
          zlib1g-dev \
          libgstreamer1.0-0 \
          gstreamer1.0-plugins-base \
          gstreamer1.0-plugins-good \
          libjpeg-dev \
          libpng-dev \
          libtiff-dev \
          libfreetype6-dev \
          libncurses5-dev \
          libncursesw5-dev \
          autoconf \
          automake \
          libtool \
          pkg-config
    
    - name: Install Buildozer
      run: |
        pip install --upgrade pip
        pip install buildozer cython
    
    - name: Install project dependencies
      run: |
        pip install kivy kivymd plyer
    
    - name: Build APK
      run: |
        buildozer android debug
    
    - name: Upload APK
      uses: actions/upload-artifact@v4
      with:
        name: luxury-torch-apk
        path: bin/*.apk
        retention-days: 30
    
    - name: Create Release
      if: github.event_name == 'push' && github.ref == 'refs/heads/main'
      uses: softprops/action-gh-release@v2
      with:
        files: bin/*.apk
        tag_name: v${{ github.run_number }}
        name: Luxury Torch v${{ github.run_number }}
        draft: false
        prerelease: false
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
