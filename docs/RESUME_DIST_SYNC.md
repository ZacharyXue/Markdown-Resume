# dist 双机同步机制（本地 ⇄ 阿里云）

> **重要边界：`dist/` 包含真实简历数据，绝不推送到 GitHub 公开仓库。**
> 同步仅发生在两台机器之间：本机 WSL ⇄ 阿里云 ECS，通过 ECS 上的私有 git bare 仓库中转。
> 公开仓库 `.gitignore` 已排除 `dist/`，任何 push 到 GitHub 的操作都不会携带 dist 内容。

## 架构

```
本机 /home/xzh/Markdown-Resume/dist       阿里云 ECS
┌──────────────────────────┐   SSH    ┌────────────────────────────────┐
│ 工作副本（独立私有 git）    │◄────────►│ /root/resume-dist-bare.git      │
│ remote: aliyun            │ push/pull │ 裸仓库中枢（纯中转，无工作区）   │
└──────────────────────────┘           └───────────────┬────────────────┘
                                                       │ git pull/push
                                                       ▼
                                           ┌──────────────────────────────┐
                                           │ /root/Markdown-Resume/dist    │
                                           │ 远程工作副本                    │
                                           └──────────────────────────────┘
```

- **裸仓库中枢**：`/root/resume-dist-bare.git`（ECS 上，仅存储 commit，不维护工作区）
- **远程工作副本**：`/root/Markdown-Resume/dist`（ECS 上，用于在该机器上查看/编辑简历）
- **本机 remote 名**：`aliyun`（指向裸仓库，SSH 免密）

## 日常用法（一个命令搞定）

在**本机** `dist/` 下运行（脚本已随 dist 仓库提交，两边都有）：

```bash
cd dist

./sync.sh push      # 本地改了简历 → 提交 + 推中枢 + 远程工作副本自动同步
./sync.sh pull      # 远程改了简历 → 远程提交 + 推中枢 + 本地自动同步
./sync.sh status    # 查看两侧工作状态和最近提交（确认是否分叉）
```

## 手动命令（等价操作，供排查）

```bash
# 本地 → 远程
git add -A && git commit -m "update: xxx" && git push aliyun master
ssh root@<ECS> "cd /root/Markdown-Resume/dist && git pull origin master"

# 远程 → 本地
ssh root@<ECS> "cd /root/Markdown-Resume/dist && git add -A && git commit -m 'update: xxx' && git push origin master"
git pull aliyun master
```

## 规则与注意事项

1. **dist 内容永不进 GitHub**：公开仓库 push 前检查 `git status` 无 dist 相关变更；`.gitignore` 已兜底。
2. **所有同步操作从本机发起**：远程无需反向 SSH 回本机，简化权限面。
3. **分叉与冲突**：如果两台机器都改过且互相同步，git 会要求 merge/解决冲突——本地执行 `git pull aliyun master` 时处理即可。内网单人场景极少发生。
4. **服务器地址**：脚本 `sync.sh` 内含真实 SSH 地址与路径，因其随 dist 私有仓库分发，不泄露到公开仓库；本文档对外仅用占位符描述。
5. **日常编辑源**：本机 `dist/` 仍是主工作区，远程副本主要用于在 ECS 上应急查看/编辑（code-server 场景）。

## 相关文件

- `dist/sync.sh` — 双向同步脚本（dist 私有仓库内，含真实服务器地址）
- `../docs/BRIDGE.md` — PDF 导出工作流