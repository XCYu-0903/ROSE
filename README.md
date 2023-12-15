# ROSE: A Recognition-Oriented Speech Enhancement Framework in Air Traffic Control Using Multi-Objective Learning

**Xincheng Yu, Dongyue Guo, Jianwei Zhang, Yi Ling**

**Abstract:**Radio speech echo is a specific phenomenon in the air traffic control (ATC) domain, which degrades speech quality and further impacts automatic speech recognition (ASR) accuracy. In this work, a recognition-oriented speech enhancement (ROSE) framework is proposed to improve speech intelligibility and also advance ASR accuracy, which serves as a plug-and-play tool in ATC scenarios and does not require additional retraining of the ASR model. Specifically, an encoder-decoder-based U-Net framework is proposed to eliminate the radio speech echo based on the real-world collected corpus. By incorporating the SE-oriented and ASR-oriented loss, ROSE is implemented in a multi-objective manner by learning shared representations across the two optimization objectives. An attention-based skip-fusion (ABSF) mechanism is applied to skip connections to refine the features. A channel and sequence attention (CSAtt) block is innovatively designed to guide the model to focus on informative representations and suppress disturbing features. The experimental results show that the ROSE significantly outperforms other state-of-the-art methods for both the SE and ASR tasks. In addition, the proposed approach can contribute to the desired performance improvements on public datasets.

Some audio examples can be found [here](https://xcyu-0903.github.io/ROSE-demo/)

## ROSE Architecture

<p><img align="center" src="https://raw.githubusercontent.com/XCYu-0903/ROSE/main/model_pic/model.png" style="  display: block ;
                        margin-left: auto;
                        margin-right: auto;
                        width: 100%;"></p>

## SE results on Voice Bank + DEMAND dataset

<p><img align="center" src="https://raw.githubusercontent.com/XCYu-0903/ROSE/main/model_pic/comparison_SE.png" style="  display: block ;
                        margin-left: auto;
                        margin-right: auto;
                        width: 100%;"></p>

