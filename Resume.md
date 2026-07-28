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

  - 作为 GitLab CI 集群 Owner，运维 100+ 节点、15000 CPU 的测试集群，独立开发仓库权限管理、消息通知、全量日志等工具
  - 推动自研芯片审核业务从 0 到 1 落地：覆盖 30+ 模型，搭建端到端性能和 Diff 测试框架，部署流程由 30 分钟优化至 5 分钟
  - 开发 CI Job 失败自动定位 Agent，采集 Pod 状态/日志/进程上下文，调用 LLM 分析根因，环境类问题准确率 90%+
  - 为 GitLab Runner 开发 K8s WebShell 功能，支撑 200+ 用户在线调试，替代本地复现方式
  - 主导 5 条测试流水线从 BD 系统迁移至 GitLab CI，解决环境耦合，自维护 CPU 和自研芯片双集群

- **华为技术有限公司 · 计算产品线 · 测试工程师**（2023.5~2024.10）

  - 作为子特性版本负责人，带领 5 人团队交付存储服务器特性，自动化覆盖率 80%，累计交付 70+ 新需求
  - 参与 openEuler 补丁回合及 BIOS Core 调频开发

- **美的集团 · 项目实习生**（2021.9~2021.12）

  - 基于 TI IWR6843 毫米波芯片开发睡眠检测功能：呼吸率、心率、在床/离床检测

## <img src="assets/project-diagram-solid.svg" width="30px"> 项目经历

- **基于 LLM 的 CI 故障定位 Agent**（2026.5~至今）

    *Go, GitLab CI, 豆包 API*

    在 GitLab Runner 中嵌入 Agent，Failed Job 触发时自动采集 Pod 状态、日志、进程等上下文，调用 LLM 分析并初步定位根因。

- **GitLab CI 集群 WebShell**（2026.1~2026.3）

    *Python, Go, Kubernetes*

    为 K8s 下的 GitLab Runner 开发 WebShell，通过 Proxy + CLB 方案将在浏览器中执行的命令反向代理到 Runner Pod，替代本地复现的定位方式。

- **XX 集成验证测试**（2023.9~2024.2）

    *Python, Linux, RDMA*

    设计测试策略与用例，带领 4 人团队开展手工+自动化测试，完成大规格仿真、性能、兼容性、长稳测试。

## <img src="assets/tools-solid.svg" width="30px"> 技能清单

- **主力语言**：Python（3 年）、Go（1.5 年）
- **辅助语言**：C++
- **平台工具**：GitLab CI/CD、Kubernetes、Docker、Linux
- **其他**：MySQL、Redis、Prometheus、Grafana、gRPC、HTTP 接口测试
