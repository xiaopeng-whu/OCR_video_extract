obj = VideoReader('Most_Popular_Programming_Languages_1965_-_2019.mp4');%输入视频位置
NOF=obj.NumberOfFrames;% 帧的总数
mkdir([cd,'/images']);%建立目录
directory=[cd,'/images/'];
 
for i=1:NOF
    Img_I=read(obj,i); %读取视频
    imwrite(Img_I,[directory,[num2str(i) '.jpg'];]); %每一帧输出一张jpg
end;

% 因为大致38帧一季度，每19帧取一帧，加快运行时间
% 但我不能保证这样取出来的某季度的图片数据会不会出现重叠，所以规范的做法还是索性全部提取出来再交给下一步作处理
% i = 1;
% while i<NOF
%     Img_I=read(obj,i); 
%     imwrite(Img_I,[directory,[num2str(i) '.jpg'];]);
%     i = i+19; %大致是半秒取一帧
% end