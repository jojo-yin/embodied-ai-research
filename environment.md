# environment.md

## 前置条件

Windows 10/11 x64，需 NVIDIA 显卡（开发机为 RTX 5070，驱动 592.01）。

## 复现

```powershell
git clone https://github.com/jojo-yin/embodied-ai-research.git
cd embodied-ai-research
winget install --id astral-sh.uv -e
uv sync
```

`uv sync` 会按 `uv.lock` 装齐所有包，缺 Python 3.11 时自动下载。

## 验证

```bash
uv run python verify.py
```

末行打印 `PASS` 即成功。

## 版本

| | |
|---|---|
| Python | 3.11.17 |
| torch | 2.11.0+cu128 |
| torchvision | 0.26.0+cu128 |
| numpy | 2.4.6 |
| matplotlib | 3.11.2 |

完整依赖（22 个包）见 `uv.lock`。

## 注意

`uv.lock` 是自动生成的锁文件，**不要手改**。
`pyproject.toml` 与 `uv.lock` 改动后需一起提交。
