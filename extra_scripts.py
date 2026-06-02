Import("env")
import os

packages_dir = os.path.join(os.path.expanduser("~"), ".platformio", "packages")
tc_bin = os.path.join(packages_dir, "toolchain-xtensa-esp-elf", "xtensa-esp-elf", "bin")
if os.path.isdir(tc_bin):
    env.PrependENVPath("PATH", tc_bin)
