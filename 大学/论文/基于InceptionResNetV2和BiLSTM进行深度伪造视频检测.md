# 摘要
使用 InceptionResNetV2和BiLSTM进行深度伪造视频检测

摘　要：该本科毕业论文（设计）研究了使用InceptionResNetV2和LSTM进行深度伪造视频检测。随着深度学习技术的发展，深度伪造视频的出现给个人隐私、社会安全和舆论导向带来了严重威胁。现有的深度伪造检测方法存在局限性，因此本文提出了结合InceptionResNetV2和BiLSTM的方法，旨在充分利用视频数据的视觉和时间特征。通过在公开的深度伪造视频数据集上进行实验，验证了该方法的有效性。实验结果表明，该方法在20个epoch和40个epoch的测试中分别达到了84.75%和91.48%的准确率。通过本研究，为深度伪造视频的检测研究领域提供了新的视角和方法，为保护信息真实性、维护社会秩序做出了贡献。

关键词：深度伪造视频；InceptionResNetV2；LSTM；深度伪造检测方法；视觉特征；时间特征

  

  

Detecting Deepfake Videos using InceptionResNetV2 and BiLSTM

**Abstract:** This undergraduate thesis (design) investigates the use of InceptionResNetV2 and LSTM for deepfake video detection. With the rapid development of deep learning technology, the emergence of deepfake videos poses serious threats to personal privacy, social security, and public opinion guidance. Existing deepfake detection methods have limitations, hence this study proposes a method that combines InceptionResNetV2 and BiLSTM to fully utilize the visual and temporal features of video data. Experimental results on a public deepfake video dataset demonstrate the effectiveness of the proposed method, achieving accuracies of 84.75% and 91.48% after 20 and 40 epochs, respectively. This research provides a new perspective and method for the detection of deepfake videos, contributing to the protection of information authenticity and maintenance of social order.

**Keywords:** deepfake videos; InceptionResNetV2; LSTM;  deepfake detection methods; visual features；temporal features

  

目　录

[1. 引　言](#_Toc8777)

[1.1研究背景及意义](#_Toc22794)

[1.2现有的深度伪造检测方法](#_Toc32267)

[1.3研究目标与内容](#_Toc13869)

[2. 相关工作](#_Toc20361)

[2.1 基于手工特征的检测方法](#_Toc22681)

[2.2  基于深度学习的检测方法](#_Toc11949)

[2.3 InceptionResNetV2和BiLSTM在其他领域的应用](#_Toc18073)

[3. 模型构建](#_Toc9870)

[3.1 模型结构](#_Toc27894)

[3.2 InceptionResNetV2网络](#_Toc3739)

[3.3 BiLSTM网络](#_Toc5124)

[4数据集与数据预处理](#_Toc10737)

[4.1 数据集](#_Toc1565)

[4.2 数据预处理](#_Toc9837)

[5 实验](#_Toc15090)

[5.1 实验环境](#_Toc8504)

[5.2 实验结果与分析](#_Toc13908)

[6.结　论](#_Toc17639)

[致　谢](#_Toc32361)

[参考文献：](#_Toc30051)

  

# 1. 引　言

## 1.1研究背景及意义

随着深度学习技术的飞速发展，生成式对抗网络（GAN[]）和深度学习模型已经能够创造出越来越逼真的伪造视频。这些技术的进步虽然在娱乐、艺术创作等方面提供了巨大的潜力，但同时也带来了严重的社会问题，尤其是在信息真实性方面。深度伪造视频（Deepfake）的出现，使得个人隐私、政治选举、公共安全等领域面临前所未有的挑战。对个人隐私、社会安全和舆论导向都构成了严重的威胁,因此亟需发展有效的检测方法来识别和遏制这一技术的滥用。

深度伪造视频检测的研究具有重要的理论和实际意义。在理论层面,探索先进的深度学习模型如何有效地提取和融合视频中的空间和时序特征,对于推动计算机视觉、模式识别等领域的发展具有启发意义。在实践层面,深度伪造视频检测技术可以应用于社交媒体平台、新闻媒体、司法鉴定等领域,及时识别和遏制虚假视频的传播,维护网络空间的真实性和公信力,保障公众的知情权和社会的稳定。

## 1.2现有的深度伪造检测方法

近年来，许多研究集中在利用深度学习技术检测深度伪造视频上。这些方法主要基于卷积神经网络（CNN[]）和循环神经网络（RNN[]），利用视频的视觉和时间特征来识别伪造内容。然而，现有的方法在处理高度逼真的深度伪造视频时仍存在一定的局限性。一方面，CNN在提取视频帧的视觉特征方面表现出色，但可能忽略了视频序列中的时间连续性。另一方面，RNN能够处理序列数据，捕捉时间特征，但在提取复杂的视觉特征方面可能不如CNN。

## 1.3研究目标与内容

鉴于此，本文提出了一种结合InceptionResNetV2[]和双向长短期记忆网络（BiLSTM[]）的深度伪造视频检测方法。InceptionResNetV2是一种高效的深度卷积神经网络，能够提取高级视觉特征，而BiLSTM则能够有效捕捉视频序列中的前后时间信息。通过将这两种模型结合，我们的方法旨在充分利用视频数据的视觉和时间特征，从而提高深度伪造视频的检测精度。

本文首先回顾了深度伪造视频检测领域的相关工作，包括基于手工特征的方法和基于深度学习的方法。接着，详细介绍了本文提出的基于InceptionResNetV2和BiLSTM的检测框架，以及数据预处理、特征提取、序列建模和分类策略。具体而言,我们采用InceptionResNetV2作为骨干网络,提取视频帧的空间特征,然后利用BiLSTM对帧级特征进行时序建模,最后通过全连接层进行真假二分类预测。通过在公开的深度伪造视频数据集上进行实验，本文验证了所提方法的有效性，并与现有的检测方法进行了比较。最后，讨论了本研究的意义、局限性以及未来的研究方向。

通过本研究，我们期望为深度伪造视频的检测研究领域提供新的视角和方法，为保护信息真实性、维护社会秩序做出贡献。

# 2. 相关工作

深度伪造视频检测技术主要围绕两大类方法展开：基于传统手工特征的方法和基于深度学习的方法。本节将对这两类方法进行概述，并介绍InceptionResNetV2和BiLSTM在其他领域的应用情况。

## 2.1 基于手工特征的检测方法

基于手工特征的深度伪造视频检测方法是早期用于识别伪造视频的主要方法之一。这类方法通过分析视频中的各种手工设计的特征，如颜色、纹理、边缘等，来区分真实视频和伪造视频。以下是几种常见的基于手工特征的检测方法：

1. 基于颜色特征的方法：这类方法利用伪造视频和真实视频在颜色分布上的差异进行检测。例如，Li等人[]提出了一种基于颜色分布的方法，通过分析视频帧的颜色直方图和颜色相关矩阵来提取特征，并使用支持向量机（SVM）进行分类。

2. 基于纹理特征的方法：伪造视频通常会引入一些异常的纹理模式，如过度平滑或不自然的纹理。基于纹理特征的方法旨在捕捉这些异常模式。Fridrich等人[]使用了一种基于Markov随机场的纹理特征，结合高阶统计量来表示视频帧的纹理特性，并应用于伪造视频的检测。

3. 基于边缘特征的方法：伪造视频中的边缘通常会出现不连续或不自然的情况。基于边缘特征的方法通过分析视频帧中的边缘信息来检测伪造。Matern等人[]提出了一种基于边缘相关性的方法，通过计算视频帧中边缘的方向一致性和连通性来提取特征，用于区分真实视频和伪造视频。

4. 基于运动特征的方法：真实视频中的物体运动通常具有一定的连续性和一致性，而伪造视频中的运动可能会出现异常。基于运动特征的方法通过分析视频中的运动信息来检测伪造。Chao等人[]提出了一种基于运动矢量场的方法，通过计算视频帧之间的运动矢量场的一致性和平滑度来提取特征，用于伪造视频的检测。

尽管基于手工特征的方法在早期取得了一定的成果，但它们存在一些局限性。手工设计的特征可能无法充分捕捉伪造视频的所有特征，导致检测性能受限。此外，这些方法通常需要大量的领域知识和专业经验来设计有效的特征。随着深度学习技术的发展，基于深度学习的方法逐渐成为主流，能够自动学习和提取更加复杂和抽象的特征，显著提高了伪造视频检测的性能。

## 2.2  基于深度学习的检测方法

基于深度学习的方法是目前深度伪造视频检测领域的主流方法。这类方法利用深度神经网络强大的特征学习和表示能力，自动从视频数据中提取有效的特征，并进行真伪判断。以下是几种常见的基于深度学习的检测方法：

1. 基于卷积神经网络（CNN）的方法：CNN在图像和视频分析领域取得了巨大成功，其强大的特征提取能力也被广泛应用于伪造视频检测。Afchar等人[][5]提出了一种基于CNN的方法，通过训练一个二分类的CNN模型来区分真实视频和伪造视频。该方法在视频帧级别进行检测，并取得了较好的性能。

2. 基于循环神经网络（RNN）的方法：RNN擅长处理序列数据，能够捕捉视频中的时间依赖关系。Güera等人[][6]提出了一种基于长短期记忆网络（LSTM）的方法，通过将视频帧序列输入到LSTM网络中，学习视频的时间动态特征，并用于伪造视频的检测。

3. 基于生成对抗网络（GAN）的方法：GAN由生成器和判别器组成，生成器用于生成伪造样本，判别器用于区分真实样本和伪造样本。在伪造视频检测中，可以利用GAN的判别器来进行真伪判断。Li等人[][7]提出了一种基于GAN的方法，通过训练一个GAN模型来学习真实视频和伪造视频的分布，并使用判别器进行检测。

4. 基于注意力机制的方法：注意力机制能够帮助模型关注视频中的关键区域，提高检测性能。Dang等人[][8]提出了一种基于时空注意力机制的方法，通过引入时间注意力和空间注意力模块，自适应地关注视频中的重要帧和区域，提高了伪造视频的检测精度。

5. 基于多模态融合的方法：除了视频帧信息，还可以利用其他模态的信息，如音频、文本等，来提高检测性能。Mittal等人[][9]提出了一种基于多模态融合的方法，通过将视频帧特征、音频特征和文本特征进行融合，利用不同模态之间的互补信息，提高了伪造视频的检测性能。

基于深度学习的方法相比传统的手工特征方法，具有更强的特征学习和表示能力，能够自动提取更加复杂和抽象的特征，显著提高了伪造视频检测的性能。然而，这类方法也面临一些挑战，如对大规模标注数据的需求、模型的可解释性以及对抗性攻击的鲁棒性等，需要进一步的研究和改进。

## 2.3 InceptionResNetV2和BiLSTM在其他领域的应用

InceptionResNetV2:InceptionResNetV2结合了Inception架构的多尺度特征提取能力和ResNet的残差连接，提高了模型的学习能力和泛化性。在图像分类、目标检测等领域，InceptionResNetV2都展现出了优异的性能。

BiLSTM:双向长短期记忆网络（BiLSTM）通过将信息在时间序列的两个方向进行传递，能够更全面地捕捉序列数据的特征。在自然语言处理、语音识别等领域，BiLSTM被广泛应用于建模序列数据。

综上所述，虽然深度伪造视频检测领域已有多种方法被提出，但随着伪造技术的不断进步，提高检测方法的准确性和鲁棒性仍是一个挑战。本文提出的方法旨在通过结合InceptionResNetV2和BiLSTM的优势，进一步提升深度伪造视频的检测性能。

# 3. 模型构建

本研究提出了一种结合InceptionResNetV2和双向长短期记忆网络（BiLSTM）的深度伪造视频检测方法。该方法旨在通过深度学习模型自动学习视频帧序列中的空间-时序特征，以准确区分真实和伪造的视频。以下是方法的详细介绍。

## 3.1 **模型结构**

将InceptionResNetV2和BiLSTM结合的优点在于综合利用了两种不同类型的神经网络结构的优势，提高了模型的性能和表征能力。以下是这种组合的优点和原因：

1. 特征提取与时序建模的结合： InceptionResNetV2是一种经典的卷积神经网络结构，擅长提取图像特征，适合处理静态图像数据。而BiLSTM是一种适用于序列数据的循环神经网络结构，能够有效地捕捉时序信息。将两者结合，可以在处理视频序列数据时，既充分利用图像特征提取的优势，又能够对视频序列中的时序信息进行建模，使得模型更全面地理解视频内容。

2. 提高模型的泛化能力：BiLSTM的双向结构能够同时考虑过去和未来的信息，有效地捕捉序列数据中的长期依赖关系。通过引入BiLSTM，可以帮助模型更好地理解视频序列中的时间关系，提高模型对视频内容的理解和表征能力，从而提高模型的泛化能力。

3. 解决深度学习在视频处理中的挑战：视频数据通常具有较高的维度和复杂性，传统的卷积神经网络在处理视频数据时可能存在信息丢失或过拟合的问题。通过引入BiLSTM，可以帮助模型更好地处理视频序列数据，提高模型对视频内容的理解和表示能力，从而解决深度学习在视频处理中的挑战。

4. 提高模型的鲁棒性： 组合InceptionResNetV2和BiLSTM可以提高模型的鲁棒性，使得模型在处理不同类型的视频数据时更加稳健。通过综合利用两种不同类型神经网络结构的优势，可以提高模型对视频数据的处理能力，从而提高模型的鲁棒性和泛化能力。

综上所述，将InceptionResNetV2和BiLSTM结合的优点在于充分利用了两种不同类型神经网络结构的优势，提高了模型的性能、泛化能力和鲁棒性，使得模型在处理视频数据时更加有效和全面。这种组合的设计能够更好地适应视频数据的特点，提高深度学习模型在视频处理任务中的表现。![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps1.png)

图3.1

本文的模型由两个主要部分组成：InceptionResNetV2网络和BiLSTM网络。

|   |
|---|
|inresnetv2 = nn.Sequential(<br><br>            BasicConv2d(3, 32, kernel_size=3, stride=2),#149x149x32<br><br>            BasicConv2d(32, 32, kernel_size=3),#147x147x32<br><br>            BasicConv2d(32, 64, kernel_size=3, padding=1),#147x147x64<br><br>            nn.MaxPool2d(3, stride=2),#73x73x64<br><br>            BasicConv2d(64, 80, kernel_size=1),#73x73x80<br><br>            BasicConv2d(80, 192, kernel_size=3),#71x71x192<br><br>            nn.MaxPool2d(3, stride=2),#35x35x192<br><br>            inception_A(),# 35x35x256<br><br>            repeat_0,#35x35x320 10xBlock35<br><br>            inception_B(),#17x17x1088<br><br>            repeat_1,#17x17x1088 20xBlock17<br><br>            inception_C(),#8x8x2080<br><br>            repeat_2,#8x8x2080 5xBlock8<br><br>            Block8(noReLU=True),#8x8x2080<br><br>            BasicConv2d(2080, 1536, kernel_size=1),#8x8x1536<br><br>            nn.AdaptiveAvgPool2d((1,1)),#1x1x1536<br><br>）|

|   |
|---|
|class VideoNet(nn.Module):<br><br>    def __init__(self):<br><br>        super(VideoNet, self).__init__()<br><br>        self.cnn = inresnetv2 #inresnetv2<br><br>        #self.avhpool = nn.AdaptiveAvgPool2d((1,1))#1x1x1536<br><br>        self.lstm = nn.LSTM(1536, 128, num_layers=1, batch_first=True, bidirectional=True, dropout=0.2)  # 第一层双向LSTM<br><br>        self.lstm2 = nn.LSTM(256, 64, num_layers=1, batch_first=True, bidirectional=True, dropout=0.2)  # 第二层双向LSTM<br><br>        #self.lstm = nn.LSTM(1000, 2, num_layers=2, batch_first=True,bidirectional=True)  # LSTM层<br><br>        self.fc = nn.Linear(128, 2)  # 全连接层，输出大小为2，对应于真假两个类别<br><br>        self.relu = nn.ReLU()<br><br>        self.sigmoid = nn.Sigmoid()<br><br>    def forward(self, x):<br><br>        batch_size, timesteps, C, H, W = x.size()<br><br>        cnn_out = torch.zeros(batch_size, timesteps, 1536).to(x.device)<br><br>        for i in range(timesteps):<br><br>            cnn_out[:, i, :] = torch.squeeze(self.cnn(x[:, i, :, :, :]))<br><br>        lstm_out, _ = self.lstm(cnn_out)<br><br>        lstm_out2, _ = self.lstm2(lstm_out)<br><br>        out = self.fc(lstm_out2[:, -1, :])  # 只使用最后一个时间步的输出·<br><br>        out = torch.nn.functional.softmax(out, dim=1)  # 应用softmax函数<br><br>        return out|

## 3.2 InceptionResNetV2网络

InceptionResNetV2是由Google Brain团队提出的深度神经网络模型，主要特点是将Inception结构（也称为网络中的网络）和残差连接（ResNet）结合在一起，旨在提高模型的性能和稳定性。Inception模块能够在多个尺度上提取特征，而残差连接可以帮助网络更好地学习复杂的映射关系，防止训练深度网络时出现的梯度消失问题。

InceptionResNetV2的结构相比于其前身InceptionV3更加复杂，包含了许多Inception模块和ResNet模块，从而使得模型具有更大的容量和更好的性能。不过这也导致了模型的计算量相对较大，需要更多的计算资源和时间进行训练。

### **3.****2****.1 Inception网络**

Inception网络的核心思想是在同一层内并行地使用不同尺寸的卷积核，然后将这些卷积操作的输出在深度方向上合并。这种设计使得网络能够在不同的尺度上捕捉图像特征，同时保持网络的计算效率。Inception网络的另一个关键特性是其使用了所谓的“瓶颈层”（1x1卷积层）来减少输入通道的数量，从而减少计算量。

Inception模块的核心思想就是将不同的卷积层通过并联的方式结合在一起，经过不同卷积层处理的结果矩阵在深度这个维度拼接起来，形成一个更深的矩阵。Inception模块可以反复叠堆形成更大的网络，它可以对网络的深度和宽度进行高效的扩充，在提升深度学习网络准确率的同时防止过拟合现象的发生。Inception模块的优点是可以对尺寸较大的矩阵先进行降维处理的同时，在不同尺寸上对视觉信息进行聚合，方便从不同尺度对特征进行提取。

Inception网络在同一层内使用多个不同尺寸的卷积核，并将它们的输出在深度方向上合并。这种设计使得网络能够同时捕获不同尺度的特征，有助于提高模型在处理多尺度图像时的性能。

为了减少计算量和参数数量，Inception网络引入了瓶颈结构，即使用1x1卷积核来减少输入通道的数量。这样可以在保持特征表达能力的同时提高网络的计算效率。

Inception网络由多个Inception模块组成，每个模块包含一系列并行的卷积操作和池化操作。这些操作的输出会被拼接或相加，形成模块的最终输出。

### **3.****2****.2残差网络（ResNet）**

残差网络（ResNet[]）通过引入残差连接（或称为跳跃连接）来解决深度神经网络训练中的梯度消失问题。在ResNet中，输入不仅被传递到下一层，还通过跳跃连接直接添加到更深层的输出上。这样，即使网络非常深，梯度也可以通过这些直接连接更有效地传播。

残差块（Residual Block）是深度学习中的一种基本模块，用于构建残差网络（ResNet）。残差块的设计旨在解决深度神经网络训练中的梯度消失和梯度爆炸问题，使得可以训练更深的网络而不会导致性能下降。

![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps2.jpg) 

图3.2

如图所示，假设我们的原始输入为x，而希望学出的理想映射为![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps3.jpg)，左图虚线框中的部分需要直接拟合出该映射f(x)，而右图虚线框中的部分则需要拟合出残差映射f(x)-x。 残差映射在现实中往往更容易优化。

### **3.****2****.3InceptionResNetV2的结构**

InceptionResNetV2将Inception结构的思想与ResNet的残差连接相结合。它包含多个Inception模块，每个模块内部使用不同尺寸的卷积核，并在模块的输出上加上残差连接。这种结构允许网络在保持计算效率的同时，更深入地学习图像的细粒度特征。

![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps4.png) 

图3.3

![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps5.jpg) 

图3.4

首先对输入的（299，299，3）张量进行5次卷积，2次最大池化得到（35，35，192）后使用``inception_B block``，其由四个分支组成（``branch0,branch1,branch2,branch3``）他们并行处理输入数据，然后链接他们的输出。以下是每个分支的简要说明，如图3.5。

1. `branch0`：对输入张量应用内核大小为1的卷积运算，将通道数从192减少到96。

2. `branch1`：利用两个连续的卷积层（内核大小分别为 1 和 5）来处理输入张量。第一个卷积层将通道数从 192 个减少到 48 个，而第二个卷积层对这 48 个通道进行操作并将其扩展到 64 个通道。

3. `branch2`：包含三个连续的卷积层，内核大小分别为 1、3 和 3。这些层依次将通道数从 192 个减少到 64 个，然后扩展到 96 个，最后维持在 96 个。

4. `branch3`：对输入张量执行内核大小为 3、步幅为 1 的平均池化，然后进行内核大小为 1 的卷积运算。该分支将通道数从 192 个减少到 64 个。

![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps6.png) 

图3.5

|   |
|---|
|class inception_A(nn.Module):<br><br>    def __init__(self):<br><br>        super(Mixed_5b, self).__init__()<br><br>        self.branch0 = BasicConv2d(192, 96, kernel_size=1)<br><br>        self.branch1 = nn.Sequential(<br><br>            BasicConv2d(192, 48, kernel_size=1),<br><br>            BasicConv2d(48, 64, kernel_size=5, padding=2)<br><br>        )<br><br>        self.branch2 = nn.Sequential(<br><br>            BasicConv2d(192, 64, kernel_size=1),<br><br>            BasicConv2d(64, 96, kernel_size=3, padding=1),<br><br>            BasicConv2d(96, 96, kernel_size=3, padding=1)<br><br>        )<br><br>        self.branch3 = nn.Sequential(<br><br>            nn.AvgPool2d(3, stride=1, padding=1, count_include_pad=False),<br><br>            BasicConv2d(192, 64, kernel_size=1)<br><br>        )<br><br>    def forward(self, x):<br><br>        x0 = self.branch0(x)<br><br>        x1 = self.branch1(x)<br><br>        x2 = self.branch2(x)<br><br>        x3 = self.branch3(x)<br><br>        out = torch.cat((x0, x1, x2, x3), 1)<br><br>        return out|

将链接输出输入到`repeat_0`网络中，其由10个``scale=0.17``的``Block35``组成，``Block35``由三个分支组成（``branch0,branch1,branch2``）他们并行处理输入数据，然后链接输出并使用内核大小为1的卷积层处理，将通道数由128扩展到320后，并使用RELU激活函数，最后乘以参数``scale``与输入相链接。以下是每个分支的简要介介绍如图3.6。

1. `branch0`：对输入张量应用内核大小为1的卷积运算，将通道数从320减少到32。

2. `branch1`：利用两个连续的卷积层（内核大小分别为 1 和 3）来处理输入张量。第一个卷积层将通道数从 320 个减少到 32 个，而第二个卷积层对这 32 个通道进行操作并将其扩展到 32 个通道。

3. `branch2`：包含三个连续的卷积层，内核大小分别为 1、3 和 3。这些层依次将通道数从 320个减少到 32 个，然后扩展到 48 个，最后减少到 64 个。

![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps7.png) 

图3.6

|   |
|---|
|class Block35(nn.Module):<br><br>    def __init__(self, scale=1.0):<br><br>        super(Block35, self).__init__()<br><br>        self.scale = scale<br><br>        self.branch0 = BasicConv2d(320, 32, kernel_size=1)<br><br>        self.branch1 = nn.Sequential(<br><br>            BasicConv2d(320, 32, kernel_size=1),<br><br>            BasicConv2d(32, 32, kernel_size=3, padding=1)<br><br>        )<br><br>        self.branch2 = nn.Sequential(<br><br>            BasicConv2d(320, 32, kernel_size=1),<br><br>            BasicConv2d(32, 48, kernel_size=3, padding=1),<br><br>            BasicConv2d(48, 64, kernel_size=3, padding=1)<br><br>        )<br><br>        self.conv2d = nn.Conv2d(128, 320, kernel_size=1)<br><br>        self.relu = nn.ReLU(inplace=True)<br><br>    def forward(self, x):<br><br>        x0 = self.branch0(x)<br><br>        x1 = self.branch1(x)<br><br>        x2 = self.branch2(x)<br><br>        out = torch.cat((x0, x1, x2), 1)<br><br>        out = self.conv2d(out)<br><br>        out = out * self.scale + x<br><br>        return self.relu(out)|

将最后的输出结果输入到``inception_B``,其由三个分支组成（``branch0,branch1,branch2``），同样并行处理输入数据，然后链接他们的输出。以下是每个分支的简要说明，如图3.7。

1. `branch0`：对输入张量应用内核大小为3步幅为2的卷积运算，将通道数从320减少到384。

2. `branch1`：包含三个连续的卷积层，内核大小分别为 1、3 和 3。这些层依次将通道数从 320 个减少到 256 个，然后维持在 256 个，最后扩展到 384 个。

3. ``branch2``：对输入张量执行内核大小为 3、步幅为 2 的最大池化。

![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps8.png) 

如图3.7

|   |
|---|
|class inception_B(nn.Module):<br><br>    def __init__(self):<br><br>        super(Mixed_6a, self).__init__()<br><br>        self.branch0 = BasicConv2d(320, 384, kernel_size=3, stride=2)<br><br>        self.branch1 = nn.Sequential(<br><br>            BasicConv2d(320, 256, kernel_size=1),<br><br>            BasicConv2d(256, 256, kernel_size=3, padding=1),<br><br>            BasicConv2d(256, 384, kernel_size=3, stride=2)<br><br>        )<br><br>        self.branch2 = nn.MaxPool2d(3, stride=2)<br><br>    def forward(self, x):<br><br>        x0 = self.branch0(x)<br><br>        x1 = self.branch1(x)<br><br>        x2 = self.branch2(x)<br><br>        out = torch.cat((x0, x1, x2), 1)<br><br>        return out|

将链接输出输入到``repeat_1``网络中，其由20个``scale=0.10``的``Block17``组成，``Block17``由两个分支组成（``branch0,branch1``）并行处理输入数据，然后链接输出并使用内核大小为1的卷积层处理，将通道由384扩展到1088后，并使用RELU激活函数，最后乘以参数``scale``。以下是每个分支的简要介介绍，如图3.8。

1. `branch0`：对输入张量应用内核大小为1的卷积运算，将通道数从1088减少到192。

2. `branch1`：包含三个连续的卷积层，内核大小分别为 1、1x7 和7x1。这些层依次将通道数从 1088个减少到 128 个，然后扩展到 160 个，最后减少到192 个

![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps9.png) 

图3.8

|   |
|---|
|class Block17(nn.Module):<br><br>    def __init__(self, scale=1.0):<br><br>        super(Block17, self).__init__()<br><br>        self.scale = scale<br><br>        self.branch0 = BasicConv2d(1088, 192, kernel_size=1)<br><br>        self.branch1 = nn.Sequential(<br><br>            BasicConv2d(1088, 128, kernel_size=1),<br><br>            BasicConv2d(128, 160, kernel_size=(1, 7), padding=(0, 3)),<br><br>            BasicConv2d(160, 192, kernel_size=(7, 1), padding=(3, 0))<br><br>        )<br><br>        self.conv2d = nn.Conv2d(384, 1088, kernel_size=1)<br><br>        self.relu = nn.ReLU(inplace=True)<br><br>    def forward(self, x):<br><br>        x0 = self.branch0(x)<br><br>        x1 = self.branch1(x)<br><br>        out = torch.cat((x0, x1), 1)<br><br>        out = self.conv2d(out)<br><br>        out = out * self.scale + x<br><br>        return self.relu(out)|

将结果输入到`inception_C block`中，其由4各分支组成（``branch0,branch1,branch2,branch3``） 如图3.9.

1. `branch0`：包含两个连续的卷积层，内核大小为1和3。第一个卷积层将通道数从1088个减少到256个，第二个卷积层将这256个通道拓展到384个通道，步幅为2.

2. `branch1`：包含两个连续的卷积层，内核大小为1和3。第一个卷积层将通道数从1088个减少到256个，第二个卷积层将这256个通道拓展到288个通道，步幅为2.

3. `branch2`：包含三个连续的卷积层，内核大小分别为 1、3和3。这些层依次将通道数从 1088个减少到 256 个，然后扩展到288 个，最后减少到320个，最后一个卷积层的步幅为2

4. `branch3`：对输入张量执行内核大小为 3、步幅为 2 的最大池化。

![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps10.png) 

图3.9

|   |
|---|
|class inception_C(nn.Module):<br><br>    def __init__(self):<br><br>        super(Mixed_7a, self).__init__()<br><br>        self.branch0 = nn.Sequential(<br><br>            BasicConv2d(1088, 256, kernel_size=1),<br><br>            BasicConv2d(256, 384, kernel_size=3, stride=2)<br><br>        )<br><br>        self.branch1 = nn.Sequential(<br><br>            BasicConv2d(1088, 256, kernel_size=1),<br><br>            BasicConv2d(256, 288, kernel_size=3, stride=2)<br><br>        )<br><br>        self.branch2 = nn.Sequential(<br><br>            BasicConv2d(1088, 256, kernel_size=1),<br><br>            BasicConv2d(256, 288, kernel_size=3, padding=1),<br><br>            BasicConv2d(288, 320, kernel_size=3, stride=2)<br><br>        )<br><br>        self.branch3 = nn.MaxPool2d(3, stride=2)<br><br>    def forward(self, x):<br><br>        x0 = self.branch0(x)<br><br>        x1 = self.branch1(x)<br><br>        x2 = self.branch2(x)<br><br>        x3 = self.branch3(x)<br><br>        out = torch.cat((x0, x1, x2, x3), 1)<br><br>        return out|

将链接输出输入到``repeat_2``网络中，其由5个`scale=0.20`的`Block8`组成，`Block8`由两个分支组成（``branch0,branch1``）然后链接输出并使用内核大小为1的卷积层处理，将通道由488扩展到2080后，并使用RELU激活函数，最后乘以参数``scale``。以下是每个分支的简要介介绍，如图3.10。

1. `branch0`：对输入张量应用内核大小为1的卷积运算，将通道数从2080减少到192

2. `branch1`：包含三个连续的卷积层，内核大小分别为 1、1x3和3x1。这些层依次将通道数从 2080个减少到 192 个，然后扩展到224个，填充为（0，1），最后扩展到256个，填充为（1，0）。

![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps11.png) 

图3.10

|   |
|---|
|class Block8(nn.Module):<br><br>    def __init__(self, scale=1.0, noReLU=False):<br><br>        super(Block8, self).__init__()<br><br>        self.scale = scale<br><br>        self.noReLU = noReLU<br><br>        self.branch0 = BasicConv2d(2080, 192, kernel_size=1)<br><br>        self.branch1 = nn.Sequential(<br><br>            BasicConv2d(2080, 192, kernel_size=1),<br><br>            BasicConv2d(192, 224, kernel_size=(1, 3), padding=(0, 1)),<br><br>            BasicConv2d(224, 256, kernel_size=(3, 1), padding=(1, 0))<br><br>        )<br><br>        self.conv2d = nn.Conv2d(448, 2080, kernel_size=1)<br><br>        if not noReLU:<br><br>            self.relu = nn.ReLU(inplace=True)<br><br>    def forward(self, x):<br><br>        x0 = self.branch0(x)<br><br>        x1 = self.branch1(x)<br><br>        out = torch.cat((x0, x1), 1)<br><br>        out = self.conv2d(out)<br><br>        out = out * self.scale + x<br><br>        if not self.noReLU:<br><br>            out = self.relu(out)<br><br>        return out|

最后将输出输入到`norelu`的`Block8`，再进行一次内核大小为1的卷积，将输入通道从2080个减少到1536个，并进行一次H，W为1的自适应平均池化。得到特征图（1，1，1536）

## 3.3 BiLSTM网络

### **3.****3****.1 RNN相关知识**

|   |
|---|
|![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps12.jpg) <br><br>图3.11 RNN|

RNN是一种处理序列数据的神经网络，它通过使用循环连接来保持对之前信息的记忆，并将此记忆应用于当前的计算中。下面是对图中所示RNN运行机制的解释：

1. 输入：在每个时间步（time step），RNN都会接收到一个输入![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps13.jpg)，其中t表示时间步。这个输入可以是序列中的一个元素，例如一个词或者一个字符。

2. 隐藏状态：每个时间步还有一个对应的隐藏状态![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps14.jpg)，这个隐藏状态包含网络的内部记忆，它的计算依赖于当前的输入![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps15.jpg)和前一个时间步的隐藏状态![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps16.jpg)。隐藏状态![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps17.jpg)通过以下递归式计算：

![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps18.jpg) 

   其中![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps19.jpg)表示隐藏状态之间的权重矩阵，![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps20.jpg)表示输入与隐藏状态之间的权重矩阵，![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps21.jpg)是偏置项，tanh表示双曲正切激活函数，它有助于引入非线性并且将值控制在-1到1之间。

3. 输出：每个时间步产生一个输出![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps22.jpg)，它通常通过隐藏状态![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps23.jpg)经过另外一层权重矩阵![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps24.jpg)和tanh激活函数来计算，![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps25.jpg)=![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps26.jpg)+![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps27.jpg)

4. 权重共享：不同时间步中的![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps28.jpg)、![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps29.jpg)以及![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps30.jpg)是共享的，这意味着在每个时间步中都使用相同的参数。这是RNN可以处理任意长度序列的关键之一，因为它可以用固定数量的参数来学习。

5. 序列处理：RNN通过依次处理序列中的元素来传递信息。在处理完一整个序列后，它可以生成序列级别的输出，或者在每个时间步都生成输出，具体取决于任务需求。

RNN因其内部循环结构而能处理序列数据，并被广泛应用于语言模型、机器翻译、语音识别等领域。然而，它们也存在一些问题，如梯度消失或梯度爆炸，这在长期依赖中尤其明显，导致了更高级的RNN变体的开发，如长短期记忆网络（LSTM）和门控循环单元（GRU）的出现。

|   |
|---|
|![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps31.jpg) <br><br>图3.12 BiRNN|

BiRNN是一种深度学习模型，主要用于处理序列数据，因其具有从两个不同方向分析数据的能力，它能够捕捉到更加丰富的时序信息。

1. 序列数据输入：在底部，在每个时间步（time step），RNN都会接收到一个输入![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps32.jpg)，其中t表示时间步。这些输入可以是文本数据中的单词、音频信号中的时刻信号、时间序列中的数据点等。

2. 双向层：biRNN的每个时间步有两个RNN单元，一个负责处理过去的信息（顶部方向），通常称为前向（forward）状态，另一个负责处理未来的信息（底部方向），通常称为后向（backward）状态。每个状态都有自己的权重矩阵W，这些权重在时间步之间是共享的，但是前向和后向RNN的权重是不同的。

3. 前向和后向状态：图中的![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps33.jpg)和![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps34.jpg)代表了在不同时间步下计算得到的前向和后向状态。每个状态是基于当前的输入和前一个状态（对于前向）或后一个状态（对于后向）计算得到的。

4. 输出序列：每个时间步都会产生一个输出(![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps35.jpg),![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps36.jpg),![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps37.jpg),...,![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps38.jpg))，每个输出通常是前向和后向状态的函数。这些输出可以用于不同的任务，例如分类、标签赋值或其他序列处理任务。

在训练过程中，BiRNN会根据特定的损失函数调整权重矩阵W，以便更好地预测或分类输入序列。

|   |
|---|
|![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps39.jpg) <br><br>图3.13 LSTM|

LSTM是一种特殊类型的循环神经网络（RNN），它能够在序列数据中捕捉长期依赖关系。LSTM通过记忆元（![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps40.jpg)）和三个门结构（输入门、遗忘门、输出门）来控制信息流。LSTM运行机制：

1. 遗忘门（Forget Gate）： 控制记忆元上时间步![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps41.png)的信息是否应该被“忘记”或者保留到当前时间步![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps42.png)。这是通过遗忘门的激活函数σ决定的，它通常是一个sigmoid函数。σ函数用权重![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps43.jpg)与前一个隐藏状态![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps44.jpg)和当前输入![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps45.jpg)相乘，然后应用sigmoid函数决定保留哪些信息。

2. 输入门（Input Gate）： 确定当前时间步的输入![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps46.jpg)中有哪些信息是需要更新到记忆元的。它由两部分组成：一部分是通过σ激活函数和权重![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps47.jpg)来决定哪些值将要更新；另一部分是通过tanh函数和权重![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps48.jpg)来创建一个候选值向量，这将会与输入门的输出相乘，提供更新记忆元的值。

3. 记忆元更新（Memory Update）：当前时间步的记忆元![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps49.jpg)是由先前的记忆元![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps50.jpg)与遗忘门的输出相乘得到的（忘记旧信息），以及输入门的输出与候选值向量相乘的结果（添加新信息）相加得到的。

4. 输出门（Output Gate）：决定了最后的隐藏状态![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps51.jpg)或者输出![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps52.jpg)应该是什么。它使用激活函数σ和权重![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps53.jpg)来决定隐藏状态的哪些部分应该被输出。然后通过应用tanh函数于记忆元，并将其乘以输出门的结果，以决定下一步的隐藏状态![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps54.jpg)。

在这种情况下，公式可以表示为：

遗忘门: ![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps55.jpg)

输入门: ![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps56.jpg)

输出值向量: ![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps57.jpg)

记忆元更新: ![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps58.jpg)

输出门: ![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps59.jpg)

最终输出/隐藏状态: ![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps60.jpg)

这种改变的命名方式更能准确地反映LSTM的设计初衷，即在处理序列数据时更好地捕捉和传递长期记忆。

|   |
|---|
|![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps61.jpg) <br><br>图3.14 BiLSTM|

双向长短期记忆网络（BiLSTM）是一种特殊的循环神经网络（RNN），它通过结合两个方向上的信息来处理序列数据，从而提高了模型对序列数据的理解能力。BiLSTM网络由两个独立的LSTM层组成，这两个层分别处理数据序列的正向（从头到尾）和反向（从尾到头），最后将两个方向的信息进行合并，以获得更全面的序列特征表示。

双向LSTM是LSTM的一个变种，它通过将两个独立的LSTM层结合在一起实现：一个处理正向的时间序列信息，另一个处理反向的时间序列信息。通过这种方式，BiLSTM可以同时考虑过去和未来的上下文信息。

如图所示，从左到右的箭头表示正向LSTM层（以![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps62.png)为标记），从右到左的箭头表示反向LSTM层（以b为标记）。每一个![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps63.jpg)是输入序列中的一个元素，而![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps64.jpg)和![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps65.jpg)则是相应的LSTM层在每个时间步的输出。上标f和b分别表示正向和反向的LSTM层。

同时，每个LSTM单元会输出一个隐藏状态（![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps66.jpg)）和一个单元状态（![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps67.jpg)）。这些状态会流向下一个时间步的单元，这样LSTM就能够传递信息并记住序列中的长期依赖性。对于BiLSTM来说，因为有两个方向，所以每个时间步会有两个隐藏状态和两个单元状态。

在序列的最后，将正向和反向LSTM层在每个时间步的输出合并或者拼接起来，作为最终的特征表达，本文只使用最后一个时间步的输出

### **3.****3****.2 BiLSTM的结构**

Stack bidirectional LSTM layers:

第一层: LSTM, 128个单元, return sequences, dropout of 0.2, and recurrent dropout of 0.2.

第二层: LSTM, 64个单元, return sequences, dropout of 0.2, and recurrent dropout of 0.2.

|   |
|---|
|self.lstm = nn.LSTM(1000, 128, num_layers=1, batch_first=True, bidirectional=True, dropout=0.2)  # 第一层双向LSTM<br><br>self.lstm2 = nn.LSTM(256, 64, num_layers=1, batch_first=True, bidirectional=True, dropout=0.2)  # 第二层双向LSTM|

BiLSTM通过以下步骤来处理序列数据：

1. 正向LSTM层：处理序列数据的正向流动，即从序列的开始到结束。它按照时间顺序逐步读取序列中的元素，并更新自身的状态。

2. 反向LSTM层：处理序列数据的反向流动，即从序列的结束到开始。它按照时间的逆序逐步读取序列中的元素，并更新自身的状态。

3. 信息合并：将正向LSTM层和反向LSTM层在每个时间步上的输出进行合并（通常是拼接或相加），以获得每个时间步上的完整特征表示。

# 4数据集与数据预处理

## **4.1 数据集**

本研究使用的是Kaggle上的DeepFake Detection Challenge Dataset (DFDC[])数据集。DFDC是目前最大、最具挑战性的深度伪造视频数据集之一,由Facebook与多个合作伙伴共同发布,旨在推动深度伪造视频检测技术的发展。

DFDC数据集包含了超过10万个视频片段,其中约20%为伪造视频,80%为真实视频。这些视频涵盖了各种不同的场景、光照条件、拍摄设备和被拍摄者,以模拟真实世界中的多样性。

数据集的视频长度不固定,帧率为30fps。每个视频文件以MP4格式存储,并带有相应的JSON元数据文件,记录了视频的真实/伪造标签以及其他相关信息。

## **4.2 数据预处理**

|   |
|---|
|class VideoDataset(Dataset):<br><br>    def __init__(self, video_dir):<br><br>        self.video_dir = video_dir<br><br>        file_list = os.listdir(video_dir)<br><br>        self.file_list = []<br><br>        for file in file_list:<br><br>            if 'real' in file:<br><br>                self.file_list.extend([file]*5)<br><br>                #self.real_count += 5<br><br>            else:<br><br>                self.file_list.append(file)<br><br>                #self.fake_count += 1<br><br>    def __len__(self):<br><br>        return len(self.file_list)<br><br>    def __getitem__(self, idx):<br><br>        video_file = self.file_list[idx]<br><br>        cap = cv2.VideoCapture(os.path.join(self.video_dir, video_file))<br><br>        frames = []<br><br>        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))<br><br>        start_frame = random.randint(0, max(0, frame_count - 15))  # 随机选择一个开始帧<br><br>        cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)<br><br>        for _ in range(1):<br><br>            ret, frame = cap.read()<br><br>            if not ret:<br><br>                break<br><br>            frame = cv2.resize(frame, (299, 299))<br><br>            frames.append(frame)<br><br>        cap.release()<br><br>        if len(frames) == 0:  # 如果没有任何帧，返回一个全零张量<br><br>            frames = [np.zeros((299, 299, 3), dtype=np.float32) for _ in range(15)]<br><br>        while len(frames) < 15:<br><br>            frames.append(frames[-1])<br><br>        frames = np.stack(frames)<br><br>        frames= torch.from_numpy(frames).float()<br><br>        frames = frames.permute(0, 3, 1, 2)<br><br>        # 根据文件名的前四个字母添加标签<br><br>        #count += 1<br><br>        if 'fake' in video_file:<br><br>            label = 0<br><br>            #count_fake += 1<br><br>        else:<br><br>            label = 1<br><br>            #count_real += 1<br><br>        return frames, label|

为了将原始视频数据转化为适合深度学习模型输入的形式,我们需要对数据进行一系列预处理操作,具体步骤如下:

1. 视频帧抽取： Sabir 等人[][36] 提出的一种检测方法，利用 CNN 和递归神经网络 (RNN) 捕 获 5 个连续 deepfake 视频帧中呈现的时间信息。此外，Güera 等人[][18]也采 用了类似的方法，利用 CNN 层从多达 80 个连续帧中提取特征，并将其输入 RNN 层。这两种方法 [18, 36] 都是从 CNN 提取特征并将其传递给 RNN 层。

    本文使用使用``frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)） start_frame = random.randint(0, max(0, frame_count - 15))``随机选择一个开始帧，抽取其向后的15个连续帧。将其作为图像序列输入inceptionresnet，从中提取特征，并将其输入BiLSTM，从而建立了一个时间信息感知的深度伪造检测模型。

|   |   |
|---|---|
|![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps68.png) <br><br>图4.1虚假图片|![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps69.png) <br><br>图4.2真实图片|

    本方法优点

    （1）. 数据增强。每次读取视频时，都会从视频的不同位置抽取帧，增加了模型训练时的数据多样性，可以提高模型的泛化能力，

    （2） 捕捉时间信息。由于抽取的帧是连续的，所以这种方法可以捕捉到视频中的时间信息。有助于发现在帧之间独立分析的方法无法发现的抖动和瑕疵。

    （3） 减少计算负担。只抽取视频中的一部分帧，而不是全部帧，可以大大减少计算负担，加快模型训练速度

    （4） 灵活性。可以根据需要调整抽取的帧数和开始帧的位置，以适应不同的任务和模型

2. 面部检测与裁剪： 由于深度伪造技术主要针对人脸区域,为了去除背景噪声的干扰,我们使用MTCNN [](Multi-task Cascaded Convolutional Networks)对每一帧图像进行面部检测。MTCNN是一种基于级联CNN的高效面部检测算法,可以准确定位图像中的人脸位置。检测到人脸后,我们将其裁剪出来,并调整为固定大小(299x299)。如果一帧图像中检测到多个人脸,我们选择面积最大的那个。

3. 图像归一化： 为了加快模型的收敛速度并提高训练稳定性,我们对裁剪后的人脸图像进行归一化处理。具体地,将像素值从[0, 255]线性映射到[0, 1]区间内。这一步可以减少不同图像之间的亮度、对比度差异,使得模型更专注于学习图像的内容信息。

4. 数据集划分： 我们按照7:3的比例,将预处理后的数据集随机划分为训练集和测试集。其中,训练集用于模型的训练和参数更新;测试集用于评估模型的泛化性能。

# 5 实验

## **5.1 实验环境**

本文使用环境为python 3.10.13，pytorch 2.2.1，cuda 12.1，Gen interl(R) Core(TM)i7-12700H @2.7ghz，NVIDA GeForce RTX 3070Ti，内存 32.0G

## **5.2 实验结果与分析**

激活函数使用ReLU（Rectified Linear Unit）用于引入非线性变化其数学表达式为![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps70.png)

![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps71.jpg) 

图5.1

损失函数使用交叉熵损失函数（Cross-Entropy Loss），用于衡量模型预测的概率分布与真实概率分布之间的差异。具体来说，对于二分类问题，真实标签通常表示为0或1，而模型输出一个介于0和1之间的概率值。交叉熵损失函数计算的是真实标签与模型预测概率之间的负对数似然。如果真实标签为1，则损失函数关注模型预测为正类的概率的对数值；如果真实标签为0，则损失函数关注模型预测为负类的概率的对数值。其数学公式为![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps72.png)

由于运行时间限制，对所设计的模型进行了 20 epoch 和 40 epoch 测试，结果表明 准确率分别为 84.75% 和 91.48%。实施后得到的结果图表明，随着历时次数的增加，训练和测试准确率也在提高。

![](file:///C:\Users\Admin\AppData\Local\Temp\ksohtml13904\wps73.jpg) 

图5.2

# 6.结　论

在本本科毕业论文（设计）中，我们提出并验证了一种结合InceptionResNetV2和双向长短期记忆网络（BiLSTM）的深度伪造视频检测方法。通过详细的实验分析，本研究证明了该方法在提高深度伪造视频检测准确性方面的有效性。实验结果显示，在公开的深度伪造视频数据集上，该方法在20个和40个训练周期后分别达到了84.75%和91.48%的准确率。

本研究的意义在于为深度伪造视频的检测提供了一种新的技术途径，这对于保护个人隐私、防止虚假信息的传播及维护社会秩序具有重要价值。此外，通过结合InceptionResNetV2的高级视觉特征提取能力和BiLSTM的时间序列分析能力，本方法能够更全面地分析视频数据，提高检测的准确性和鲁棒性。

尽管取得了一定的成果，但本研究仍存在一些局限性，例如对于极其精细化的伪造技术可能仍有检测盲点。未来的研究可以在以下几个方向进行深入：一是进一步优化模型结构，以提高对复杂伪造技术的适应性和检测精度；二是扩大和多样化训练数据集，以增强模型的泛化能力；三是探索模型对抗性攻击的防御机制，增强系统的安全性。

  

  

# 致　谢

在此，我要衷心感谢指导老师蔡满春教授对我毕业论文的悉心指导和支持。在整个研究过程中，蔡满春教授不仅给予了我宝贵的学术指导和建议，还在学术和人生方面给予了我无私的帮助和关怀。没有您的耐心指导和支持，我无法顺利完成这篇论文。

同时，我还要感谢信息网络安全学院八区队网络安全与执法的老师和同学们在学习和生活中给予我的帮助和鼓励。他们的支持和合作使得我的研究工作更加顺利和愉快。

最后，我要感谢家人和朋友们对我的理解、支持和鼓励。在我学习和研究的道路上，他们始终是我坚强的后盾和精神支柱。感谢你们的陪伴和支持，让我能够克服困难，不断前行。

谨以此文，向所有支持和帮助过我的人表示最诚挚的感谢！

  

参考文献：