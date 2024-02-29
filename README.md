# **Azure OpenAI Service 工作坊手册**

![cover](./imgs/cover.webp)

各位大家好，如果您希望学习 Azure OpenAI Service ，本动手工作坊是最佳选择，我们会涵盖基础知识，以及 RAG 入门（包括如何通过 Python 使用 Azure OpenAI Service SDK ，利用 Semantic Kernel 构建工程级应用，以及通过 Prompt flow 来结合工作流来完成企业级提示词的融入和评估，还有和企业大数据的整合 Microsoft Fabric）当然也基于多模态模型的内容给到初学者更多动手的案例。如果你感兴趣，可以通过该练习去进行学习。

## **课前准备**

1. 申请 Azure 试用 https://azure.microsoft.com/en-us/free

2. 申请 Azure OpenAI Service  https://aka.ms/oai/access

3. 具备 Python 基础 https://learn.microsoft.com/en-us/training/paths/beginner-python/

*注意：* 如果您希望获取本次工作坊的 ppt 可以下载相关 pdf 

1. Chat With Your Data  [点击访问](./pdf/ChatWithYourData.pdf)

2. 多模态应用的应用与实践 [点击访问](./pdf/MultiModalApplication.pdf)


## **工作坊目录**

### **一.  Chat With Your Data**

**1. 基础接口**

如果您希望学习如何使用 Python 结合 Azure OpenAI Service SDK 访问不同模型，以及如何使用 Embeddings 通过向量方式和您的数据交互。

[访问链接](./ChatWithYourData/Start/)

**2. Semantic Kernel**

Semantic Kernel 是一个轻量级的开源框架，通过 Semantic Kernel 您可以快速使用不同编程语言(C#/Python/Java)结合 LLMs(OpenAI、Azure OpenAI、Hugging Face 等模型) 构建智能应用。在我们进入生成式人工智能后，人机对话的方式有了很大的改变，我们用自然语言就可以完成与机器的对话，门槛降低了非常多。结合提示工程和大型语言模型，我们可以用更低的成本完成不同的业务。但如何把提示工程以及大模型引入到工程上？我们就需要一个像 Semantic Kernel 的框架作为开启智能大门的基础。在 2023 年 5 月，微软 CTO Kevin Scott 就提出了 Copilot Stack 的概念，人工智能编排就是核心。 Semantic Kernel 具备和 LLMs 以及各种提示工程/软件组成的插件组合的能力，因此也被看作 Copilot Stack 的最佳实践。通过 Semantic Kernel，你可以非常方便地构建基于 Copilot Stack 的解决方案，而且对于传统工程，也可以无缝对接。


[访问链接](./ChatWithYourData/SemanticKernel/)


附加 ： [获取 Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook)



**3. Prompt flow**

Prompt flow 是一套开发工具，旨在简化基于 LLM 的人工智能应用程序的端到端开发周期，从构思、原型设计、测试、评估到生产部署和监控。 它使即时工程变得更加容易，并使您能够构建具有生产质量的 LLM 应用程序。

通过快速流程，您将能够：

创建将 LLMs、提示、Python 代码和其他工具链接到可执行工作流程中的流程。

轻松调试和迭代您的流程，尤其是与 LLMs 的交互。

评估您的流程，使用更大的数据集计算质量和性能指标。

将测试和评估集成到您的 CI/CD 系统中，以确保流程的质量。

将您的流程部署到您选择的服务平台或轻松集成到应用程序的代码库中。

（可选但强烈推荐）利用 Azure AI 中的云版本提示流与您的团队协作。

[[访问链接](./ChatWithYourData/Promptflow/)


**4. Fabric**

Microsoft Fabric 是面向企业的一体化分析解决方案，涵盖从数据移动到数据科学、实时分析和商业智能的所有内容。 它提供一套全面的服务，包括数据湖、数据工程和数据集成，全部放在一个位置。

使用 Fabric 时，无需将来自多个供应商的不同服务拼凑在一起。 相反，你可以享受高度集成、端到端且易于使用的产品，旨在简化分析需求。

该平台构建在服务型软件 (SaaS) 的基础之上，将简单性和集成性提升到一个全新的水平。



*Workshop 1* 访问您的非结构化数据 ，构建 RAG 应用

*Workshop 2* 访问您的结构化数据，构建自然语言到 SQL 的引擎


### **二.  多模态模型的应用与实践**

**1. 基础学习**

*GPT-4V*

GPT-4V 全称是GPT-4 with Vision，它可以理解图片，为用户解析图片并回答图片相关的问题。 GPT-4V可以准确理解图像的内容，识别图像中物体、计算物体的数量、提供图片相关的洞察和信息、提取文本等。可以说 , GPT -4V 是大型语言模型的皇者，也让大型模型更好地理解世界。GPT-4V 的视觉主要能力和应用方向

物体检测：GPT-4V 能够识别并检测图像中的各种常见物体，例如汽车、动物和家居用品等。其识别能力已在标准图像数据集上进行了评估。

文本识别：此模型具备光学字符识别（OCR）技术，可在图像中发现打印或手写文字，并将其转换为机器可读的文本。这项功能在文档、标志和标题等图像中得到了验证。

人脸识别：GPT-4V 能够找出并识别图像中的人脸。它还具有一定程度的能力，可以通过面部特征来判断性别、年龄和种族属性。该模型的面部分析能力已在 FairFace 和 LFW 等数据集上进行了测试。

验证码解决方案：GPT-4V 在解决基于文本和图像的验证码时展示了视觉推理能力。这表明模型具有高级的解谜技巧。

地理定位：GPT-4V 能够识别风景图片中所呈现的城市或地理位置。这说明模型掌握了关于现实世界的知识，但也意味着存在泄露隐私的风险。

复杂图像：处理复杂的科学图表、医学扫描或具有多个重叠文本组件的图像时，该模型表现较差。它无法把握上下文细节。


*Whisper*

Whisper 是由OpenAI开发的一种先进的自动语音识别（ASR）模型。这个模型专注于转录语音为文本，且在多种语言和不同的环境中都表现出了卓越的性能。以下是关于Whisper模型的一些关键特点：

特点 多语言支持：Whisper模型能够处理多种不同的语言和方言，使其在全球范围内具有广泛的适用性。

高精度识别：它能准确地识别和转录语音，即使在背景噪音较多的环境中也能保持较高的准确率。

自适应不同语境：Whisper不仅能识别标准的语音输入，还能适应各种口语化和非正式的对话风格。

易于集成和使用：作为一个机器学习模型，Whisper可以集成到各种应用和服务中，提供语音识别功能。


[访问链接](./LearningMultiModal/Basic/)


**2. 进阶学习**


[访问链接](./LearningMultiModal/Workshop/)

*Workshop 1* 用 Azure OpenAI Service 和 Azure Speech Service 结合，完成一个完整的语音聊天机器人 

*Workshop 2* 你有做过机器学习做物体识别吗？通过多模态模型 gpt-4-turbo-vision 可以简化物体识别流程，结合 gpt-4 强大的代码生成能力，我们完成一个物体识别的工作。


## **学习资料**

1. 学习 Azure OpenAI Service 的相关知识  https://learn.microsoft.com/zh-cn/credentials/applied-skills/develop-generative-ai-solutions-with-azure-openai-service/

2. 了解 Semantic Kernel https://github.com/microsoft/semantic-kernel

3. 了解 PromptFlow  https://microsoft.github.io/promptflow/

4. 了解 Microsoft Fabric https://learn.microsoft.com/en-us/fabric/get-started/microsoft-fabric-overview 














