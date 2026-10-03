"""环境验收脚本 —— 确认 PyTorch + CUDA 真能用。

用法：
    uv run python verify.py

判据不止 torch.cuda.is_available()——那个布尔值会骗人。
关键是 sm_120（Blackwell）的预编译码必须在编译列表里，
并且 GPU 算出来的结果要和 CPU 对得上。
"""

import sys

# Windows 控制台默认 GBK，编不出中文/emoji。这里强制走 UTF-8。
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import torch  # noqa: E402


def main() -> None:
    print("Python        :", sys.version.split()[0])
    print("torch         :", torch.__version__)
    print("编译支持的架构 :", torch.cuda.get_arch_list())
    print("cuda 可用      :", torch.cuda.is_available())

    assert torch.cuda.is_available(), "CUDA 不可用——驱动或 torch 版本有问题"
    print("显卡           :", torch.cuda.get_device_name(0))
    print("算力           :", torch.cuda.get_device_capability(0))

    # 关键判据：没有 sm_120 的预编译码，就会走 PTX 现场编译的兜底路径，
    # is_available() 仍然是 True，但第一次调用要卡几十秒，之后持续慢。
    arch = torch.cuda.get_arch_list()
    assert "sm_120" in arch, f"缺 sm_120 预编译码，会走 PTX 兜底。当前：{arch}"

    print("-" * 50)

    torch.manual_seed(0)
    n = 4096
    a, b = torch.randn(n, n), torch.randn(n, n)

    cpu = a @ b
    gpu = a.cuda() @ b.cuda()
    torch.cuda.synchronize()

    diff = (gpu.cpu() - cpu).abs().max().item()
    print(f"GPU {n}x{n} 矩阵乘完成，与 CPU 最大误差 {diff:.3e}")

    # 1e-3 量级是正常的：4096 维点积累加 4096 次 fp32 舍入，相对误差约 1.7e-5。
    assert diff < 1e-2, f"数值对不上（{diff}），GPU 可能在算错"

    print("PASS")


if __name__ == "__main__":
    main()
