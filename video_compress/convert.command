ffmpeg -threads 4 -i 00780.MTS -r 29.97 -vcodec libx264 -s 480x272 -flags +loop -cmp +chroma -deblockalpha 0 -deblockbeta 0 -crf 24 -bt 256k -refs 1 -coder 0 -me_method umh -me_range 16 -subq 5 -partitions +parti4x4+parti8x8+partp8x8 -g 250 -keyint_min 25 -level 30 -qmin 10 -qmax 51 -trellis 2 -sc_threshold 40 -i_qfactor 0.71 -acodec aac -strict experimental -ab 128k -ar 48000 -ac 2 00780_convert.avi



-ar freq : audio sampling frequency 音频采样率  48000 HZ  模拟信号转为数字信号的采样频率，周期为 freq
-ab bitrate : audio bitrate in bit/s 比特率 每秒音频数据存储需要的空间大小

-acodec aac -strict experimental 使用 aac 编码解码

-qmax q  : maximum video quantizer scale (VBR) 　VBR（Variable Bitrate） 视频动态比特率的最大值

-s 480x272 : set frame size 设置画面高度宽度

-threads 4 : 4线程处理
