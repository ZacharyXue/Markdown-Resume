<center>
    <h1>薛子皓</h1>
    <div>
        <span>
            <img src="assets/phone-solid.svg" width="18px">
            18335830614
        </span>
        ·
        <span>
            <img src="assets/envelope-solid.svg" width="18px">
            xuezihao2016@outlook.com
        </span>
    </div>
</center>

## <img src="assets/info-circle-solid.svg" width="30px"> 个人信息

- 求职意向：测试开发工程师
- 工作经验：3 年

## <img src="assets/info-circle-solid.svg" width="30px"> 个人总结

3 年测试开发经验，专注测试平台搭建与 CI/CD 流水线建设。具备从 AI 模型部署到自动化测试框架、再到测试集群运维的全链路能力。学习能力强，善于在新技术领域快速上手并推动落地，胜任跨团队协作与工具链建设。

## <img src="assets/graduation-cap-solid.svg" width="30px"> 教育经历

- 硕士，早稻田大学，Information, Production and System，2021.4~2023.4
  - 主要课程：数据结构与算法、机器学习、深度学习
- 学士，哈尔滨工业大学，机械电子工程，2015.9~2019.7

## <img src="assets/briefcase-solid.svg" width="30px"> 工作经历

- **字节跳动，2024.11~至今**

  - 作为 AI 工具链 GitLab Owner，负责 100+ 节点、15000 CPU 测试集群部署与运维，独立开发 GitLab 仓库权限管理、强合、飞书消息通知、全量日志等二次开发工具，支撑团队 CI/CD 流水线高效运转
  - 深度参与自研 AI 芯片审核业务测试体系建设：覆盖 30+ 审核模型，性能测试从 0 到 1 搭建，引入 Diff 测试弥补多框架测试缺口；部署流程由 30 分钟优化至 5 分钟，推动审核业务 2k+ 卡、ViT 5k+ 卡大规模上量部署

- **华为技术有限公司，2023.5~2024.10**

  - 作为子特性版本负责人，带领 5 人团队（2OD+3 外包）负责存储服务器特性交付，设计测试方案与用例，规划测试组网与节奏，基于内部自研框架组织编写自动化测试脚本，自动化覆盖率达 80%，累计交付新需求 70+
  - 参与 openEuler 补丁回合及 BIOS Core 调频开发

- **美的集团股份有限公司，项目实习生，2021.9~2021.12**

  - 参与基于 TI IWR6843 毫米波芯片的睡眠检测功能开发，包括呼吸率、心率检测及在床/离床检测

## <img src="assets/project-diagram-solid.svg" width="30px"> 项目经历

- **GitLab CI Job 报错信息采集定位 Agent（2026.5~至今）**

    *Go, GitLab CI*

    在 GitLab Runner 中添加 Agent，在 CI Job 执行失败时自动采集 Pod 状态、日志、进程等上下文信息，调用豆包模型进行分析，初步定位报错原因。整体准确率约 70%，其中 Job 环境类问题判断准确率达 90%+。

- **GitLab CI 集群 WebShell 开发（2026.1~2026.3）**

    *Python, Go, GitLab CI, Kubernetes*

    为 GitLab Runner 在 Kubernetes 集群下开发 WebShell 功能，支撑 200+ 用户在线调试，替代此前本地复现的定位方式，显著提升开发定位效率。主要工作包括：
    - 创建测试 Pod 时将信息上报至集群内 Proxy 服务
    - Proxy 服务绑定 CLB 对外暴露接口，将请求的 Session 反向代理到指定 Runner 控制节点。

- **GitLab CI/CD 基础搭建（2025.9~2026.1）**

    *GitLab CI, Kubernetes*

    负责从 BD 系统迁移 5 条测试流水线至 GitLab CI，解决环境耦合问题。主要包括：
    - 使用 Redis 替代 BD 侧跨 Job 环境变量、火山云 TOS 替换 BD TOS，完成测试流程适配与镜像环境迁移
    - 基于 FTP 实现代码在 BD 与 GitLab 环境的定时同步与手动同步
    - 搭建并维护 GitLab CI CPU 集群与自研芯片测试集群。

- **自研芯片审核业务上量（2024.11~2025.6）**

    *Python, C++, Linux*

    - 维护并增强模型精度测试工具，开发多框架下模型端到端性能测试工具，支撑 30+ 审核模型测试
    - 开发自动部署工具，将单次部署流程从 30 分钟缩短至 5 分钟
    - 负责模型在 Merlin 平台的部署与问题定位，适配自研芯片至内部传统机器学习框架 Quicksilver

- **XX 项目集成验证测试（2023.9~2024.2）**

    *Python, Linux, RDMA*

    - 负责所在特性测试执行策略设计、新特性测试设计、测试用例设计
    - 带领 4 人团队开展迭代期间手工测试与自动化脚本编写；组织大规模仿真验证、性能测试、兼容性测试、长稳测试。

## <img src="assets/tools-solid.svg" width="30px"> 技能清单

- 语言：Python、Go、C++
- 工具/平台：GitLab CI/CD、Kubernetes、Linux、Docker、Git
- 其他：接口测试（HTTP/gRPC）、MySQL、Redis、Prometheus、Grafana
