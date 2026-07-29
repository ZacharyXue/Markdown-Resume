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

3 年测开，专注 CI/CD 基础设施与 K8s 集群运维。主导过 100+ 节点、15000 核 GitLab CI 集群建设，推动 AI 芯片审核业务 7k+ 卡大规模部署。擅长用 Python/Go 开发自动化工具提效，带过 5 人测试团队。

## <img src="assets/graduation-cap-solid.svg" width="30px"> 教育经历

- 硕士，早稻田大学，Information, Production and System，2021.4~2023.4
- 学士，哈尔滨工业大学，机械电子工程，2015.9~2019.7

## <img src="assets/briefcase-solid.svg" width="30px"> 工作经历

- **字节跳动 · AI 工具链 · 测试开发工程师**（2024.11~至今）
  - 负责 GitLab CI 集群运维、自研芯片审核业务测试、CI/CD 工具链开发

- **华为技术有限公司 · 计算产品线 · 测试工程师**（2023.5~2024.10）
  - 负责存储服务器特性测试交付，带领 5 人团队，参与 openEuler 补丁回合

## <img src="assets/project-diagram-solid.svg" width="30px"> 项目经历

- **GitLab CI/CD 平台建设**（2025.9~至今）

    *GitLab CI, Kubernetes, Go, Python*

    从 0 搭建并运维 100+ 节点、15000 CPU 的 GitLab CI 集群，服务 200+ 开发者。主要工作：
    - 主导 5 条测试流水线从 BD 系统迁移至 GitLab CI，用 Redis 替代跨 Job 环境变量、火山云 TOS 替换 BD TOS，解决历史环境耦合问题
    - 开发 GitLab 仓库权限管理、强合、飞书消息通知、全量日志等二次开发工具
    - 为 GitLab Runner 开发 K8s WebShell，通过 Proxy + CLB 将浏览器命令反向代理到 Runner Pod，替代此前本地复现的定位方式，支撑 200+ 用户在线调试
    - 开发 CI Job 失败自动定位 Agent，采集 Pod 状态/日志/进程上下文，调用 LLM 分析根因，环境类问题准确率 90%+，显著缩短故障排查时间

- **自研芯片审核业务测试**（2024.11~2025.6）

    *Python, C++, Linux, 多 AI 框架*

    从 0 到 1 搭建自研芯片审核业务测试体系。主要工作：
    - 维护并增强模型精度测试工具，搭建端到端性能测试框架，支撑 30+ 审核模型
    - 引入 Diff 测试弥补多框架（PyTorch/TensorFlow/自研框架）下的测试缺口
    - 开发自动部署工具，将单次部署流程从 30 分钟缩短至 5 分钟
    - 推动审核业务 2k+ 卡、ViT 5k+ 卡在自研芯片上大规模部署

- **存储服务器特性测试**（2023.9~2024.2）

    *Python, Linux, RDMA*

    - 设计测试策略与用例，规划测试组网与节奏，组织大规模仿真、性能、兼容性、长稳测试
    - 带领 4 人团队基于内部自研框架编写自动化脚本，自动化覆盖率达 80%，累计交付新需求 70+

## <img src="assets/tools-solid.svg" width="30px"> 技能清单

- **主力语言**：Python（3 年）、Go（1.5 年）
- **辅助语言**：C++
- **平台工具**：GitLab CI/CD、Kubernetes、Docker、Linux
- **其他**：MySQL、Redis、Prometheus、Grafana、gRPC、HTTP 接口测试
