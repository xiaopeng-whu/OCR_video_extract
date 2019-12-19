%图片相关系数法：定义两幅图像的相关系数来衡量相邻图像帧的相似性。
 
%图像数量
NOF=8457;

mkdir([cd,'/keyframes_images']);%建立目录

directory1=[cd,'\images\']; % 输入图像文件夹
directory2=[cd,'\keyframes_images\']; % 输出图像文件夹
 
img_path_list = dir(strcat(directory1,'*.jpg'));%获取该文件夹中所有jpg格式的图像
 
for i=1:NOF-1
    image_name_i = strcat(num2str(i),'.jpg'); %图像名
    img_i = imread(strcat(file_path,image_name_i)); %读取该图像
    img_i_cut = imcrop(img_i,[800 550 500 150]); %截取图像
    image_name_i_plus = strcat(num2str(i+1),'.jpg');% 后一张图像名
    img_i_plus = imread(strcat(file_path,image_name_i_plus)); %读取后一张图像
    img_i_plus_cut = imcrop(img_i_plus,[800 550 500 150]); %截取图像
    img_sim(i)=corr2(img_i_cut(:,:,1),img_i_plus_cut(:,:,1))+corr2(img_i_cut(:,:,2),img_i_plus_cut(:,:,2))+corr2(img_i_cut(:,:,3),img_i_plus_cut(:,:,3)); %计算前后两张图像的相似度
    img_sim(i)=img_sim(i)/3;
end

disp(['img_sim end']);

Threshold=0.98; %相似度阈值
 
disp(['print begin']);
for i=1:length(img_sim)
    if img_sim(i)<Threshold
        disp(i);
        Img_I=imread([directory1,[num2str(i) '.jpg'];]);
        imwrite(Img_I,[directory2,[num2str(i) '.jpg'];]); %将关键帧图片存在一个文件夹中
    end
end
disp(['print end']);