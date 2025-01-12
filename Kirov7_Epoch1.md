# CFC Studio 共学 Epoch1 指引

---

# Kirov7

> kirov reporting

## 笔记证明

### 1.11
#### LangChain 框架

LangChain 主要提供了 6 大核心组件帮助我们更好的使用大语言模型，涵盖了 Models（模型）、Prompts（提示）、Indexes（索引）、Memory（记忆）、Chains（链）、Agents（代理），这些组件集成了数十种大语言模型、多样的知识库处理方法以及成熟的应用链、上百种可调用的工具箱，为用户提供了一个快速搭建和部署大语言模型智能应用程序的平台。
![LangChain](https://heap.crazyfay.com/uploads/1736601823.png)

#### Prompt 组件

大多数 LLM 应用程序都不会直接将用户输入传递给 LLM。通常，它们会将用户输入添加到一个更大的文本片段中，称为提示模板，该模板提供有关特定任务的附加上下文。

大多数 LLM 应用程序都不会直接将用户输入传递给 LLM。通常，它们会将用户输入添加到一个更大的文本片段中，称为提示模板，该模板提供有关特定任务的附加上下文。并且 Prompt 是所有 AI 应用交互的起点，以下是 LangChain 中一个最基础的聊天应用机器人的运行流程如下：
![LangChain](https://heap.crazyfay.com/uploads/1736601994.jpg)

为了适配不同的 LLM，LangChain 封装了 Prompt 组件，并且 Prompt 组件是高可移植性的，同一个 Prompt 可以支持各种 LLM，在切换 LLM 的时候，无需修改 Prompt。在 LangChain 中，Prompt 被分成了两大类：

- **Prompt Template**：将 Prompt 按照 template 进行一定格式化，针对 Prompt 进行变量处理以及提示词的组合。
- **Selectors**：根据不同条件去选择不同提示词，或者在不同情况下通过 Selector，选择不同示例去进一步提高 Prompt 支持能力。
    >  本质上 Selectors 只是 Prompt Template 的二次封装

对于 Prompt Template，在 LangChain 中，又涵盖了多个子组件，例如：角色提示模板、消息占位符、文本提示模板、聊天消息提示模板、提示、消息等，Prompt Template 的运行流程如下：


![Prompt](https://heap.crazyfay.com/uploads/1736601929.jpg)

不同 Prompt 组件功能的简介：

- **PromptTemplate**：用于创建文本消息提示模板，用于用于与大语言模型/文本生成模型进行交互。
- **ChatPromptTemplate**：用于创建聊天消息提示模板，一般用于与聊天模型进行交互。
- **MessagePlaceholder**：消息占位符，在聊天模型中对不确定是否需要的消息进行占位。
- **SystemMessagePromptTemplate**：用于创建系统消息提示模板，角色为系统。
- **HumanMessagePromptTemplate**：用于创建人类消息提示模板，角色为人类。
- **AIMessagePromptTemplate**：用于创建AI消息提示模板，角色为AI。
- **PipelinePromptTemplate**：用于创建管道消息，管道消息可以将提示模板作为变量进行快速复用。

Prompt 不同方法的功能简介：

- **partial**：用于格式化提示模板中的部分变量。
- **format**：传递变量数据，格式化提示模板为文本消息。
- **invoke**：传递变量数据，格式化提示模板为提示。
- **to_string**：将提示/消息提示列表转换成字符串。
- **to_messages**：用于将提示转换成消息列表。

Prompt 中重载的运算符：

- **+ 运算符**：在 Prompt 组件中，对 + 运算符使用 `__add__` 方法进行重写，所以几乎所有 Prompt 组件都可以使用 + 进行组装拼接。

#### Model 组件
Model 是 LangChain 的核心组件，但是 LangChain 本身不提供自己的 LLM，而是提供了一个标准接口，用于封装不同类型的 LLM 进行交互，其中 LangChain 为两种类型的模型提供接口和集成：

- **LLM**：使用纯文本作为输入和输出的大语言模型。
- **Chat Model**：使用聊天消息列表作为输入并返回聊天消息的聊天模型。

在 LangChain 中，无论是 LLM 亦或者 Chat Model 都可以接受 PromptValue/字符串/消息列表 作为参数，内部会根据模型的类型自动转换成字符串亦或者消息列表，屏蔽了不同模型的差异。

对于 Model 组件，LangChain 有一个模型总基类，并对基类进行了划分：
![Model](https://heap.crazyfay.com/uploads/1736602318.jpg)

调用大模型最常用的方法为：

- **invoke**：传递对应的文本提示/消息提示，大语言模型生成对应的内容。
- **batch**：invoke 的批量版本，可以一次性生成多个内容。
- **stream**：invoke 的流式输出版本，大语言模型每生成一个字符就返回一个字符。

基础聊天应用的运行流程更改成如下：
![Model](https://heap.crazyfay.com/uploads/1736602471.jpg)
