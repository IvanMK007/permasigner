import requests
import subprocess
import os
from shutil import copy
from shutil import rmtree


class DpkgDeb:
    def download_linux_64(args):
        if args.debug:
            print(f"[DEBUG] Downloading dpkg-deb on Linux x86_64.")

        res = requests.get(
            "http://ftp.us.debian.org/debian/pool/main/d/dpkg/dpkg_1.21.9_amd64.deb", stream=True)
        try:
            if res.status_code == 200:
                with open(f"dpkg.deb", "wb") as f:
                    f.write(res.content)
                    if args.debug:
                        print(f"[DEBUG] Wrote file.")
            else:
                print(
                    f"[-] dpkg download URL is not reachable. Status code: {res.status_code}")
                exit(1)
        except requests.exceptions.RequestException as err:
            print(f"[-] dpkg download URL is not reachable. Error: {err}")
            exit(1)

        subprocess.run(f"ar x dpkg.deb".split(), stdout=subprocess.DEVNULL)
        if args.debug:
            print(f"[DEBUG] Extracted with ar.")
        subprocess.run(f"tar -xf data.tar.xz".split(),
                       stdout=subprocess.DEVNULL)
        if args.debug:
            print(f"[DEBUG] Extracted with tar.")
        copy("usr/bin/dpkg-deb", "dpkg-deb")
        if args.debug:
            print(f"[DEBUG] Copied.")
        subprocess.run(f"chmod +x dpkg-deb".split(), stdout=subprocess.DEVNULL)
        os.remove("data.tar.xz")
        os.remove("control.tar.xz")
        os.remove("debian-binary")
        os.remove("dpkg.deb")
        rmtree("etc")
        rmtree("sbin")
        rmtree("usr")
        rmtree("var")
        if args.debug:
            print(f"[DEBUG] Cleaned up.")

    def download_linux_arm64(args):
        if args.debug:
            print(f"[DEBUG] Downloading dpkg-deb on Linux aarch64.")

        res = requests.get(
            "http://ftp.us.debian.org/debian/pool/main/d/dpkg/dpkg_1.21.9_arm64.deb", stream=True)
        try:
            if res.status_code == 200:
                with open(f"dpkg.deb", "wb") as f:
                    f.write(res.content)
                    if args.debug:
                        print(f"[DEBUG] Wrote file.")
            else:
                print(
                    f"[-] dpkg download URL is not reachable. Status code: {res.status_code}")
                exit(1)
        except requests.exceptions.RequestException as err:
            print(f"[-] dpkg download URL is not reachable. Error: {err}")
            exit(1)

        subprocess.run(f"ar x dpkg.deb".split(), stdout=subprocess.DEVNULL)
        if args.debug:
            print(f"[DEBUG] Extracted with ar.")
        subprocess.run(f"tar -xf data.tar.xz".split(),
                       stdout=subprocess.DEVNULL)
        if args.debug:
            print(f"[DEBUG] Extracted with tar.")
        copy("usr/bin/dpkg-deb", "dpkg-deb")
        if args.debug:
            print(f"[DEBUG] Copied.")
        subprocess.run(f"chmod +x dpkg-deb".split(), stdout=subprocess.DEVNULL)
        os.remove("data.tar.xz")
        os.remove("control.tar.xz")
        os.remove("debian-binary")
        os.remove("dpkg.deb")
        rmtree("etc")
        rmtree("sbin")
        rmtree("usr")
        rmtree("var")
        if args.debug:
            print(f"[DEBUG] Cleaned up.")


class Ldid:
    linux_64_url = "https://github.com/ProcursusTeam/ldid/releases/latest/download/ldid_linux_x86_64"
    linux_arm64_url = "https://github.com/ProcursusTeam/ldid/releases/latest/download/ldid_linux_aarch64"
    macos_64_url = "https://github.com/ProcursusTeam/ldid/releases/latest/download/ldid_macos_x86_64"
    macos_arm64_url = "https://github.com/ProcursusTeam/ldid/releases/latest/download/ldid_macos_arm64"

    def download_linux_64(args):
        if args.debug:
            print(f"[DEBUG] Downloading ldid on Linux x86_64.")

        res = requests.get(Ldid.linux_64_url, stream=True)
        try:
            if res.status_code == 200:
                with open(f"ldid", "wb") as f:
                    f.write(res.content)
                    if args.debug:
                        print(f"[DEBUG] Wrote file.")
            else:
                print(
                    f"[-] ldid download URL is not reachable. Status code: {res.status_code}")
                exit(1)
        except requests.exceptions.RequestException as err:
            print(f"[-] ldid download URL is not reachable. Error: {err}")
            exit(1)

        subprocess.run(f"chmod +x ldid".split(), stdout=subprocess.DEVNULL)

    def download_linux_arm64(args):
        if args.debug:
            print(f"[DEBUG] Downloading ldid on Linux aarch64.")

        res = requests.get(Ldid.linux_arm64_url, stream=True)
        try:
            if res.status_code == 200:
                with open(f"ldid", "wb") as f:
                    f.write(res.content)
                    if args.debug:
                        print(f"[DEBUG] Wrote file.")
            else:
                print(
                    f"[-] ldid download URL is not reachable. Status code: {res.status_code}")
                exit(1)
        except requests.exceptions.RequestException as err:
            print(f"[-] ldid download URL is not reachable. Error: {err}")
            exit(1)

        subprocess.run(f"chmod +x ldid".split(), stdout=subprocess.DEVNULL)

    def download_macos_64(args):
        if args.debug:
            print(f"[DEBUG] Downloading ldid on macOS x86_64.")

        res = requests.get(Ldid.macos_64_url, stream=True)
        try:
            if res.status_code == 200:
                with open(f"ldid", "wb") as f:
                    f.write(res.content)
                    if args.debug:
                        print(f"[DEBUG] Wrote file.")
            else:
                print(
                    f"[-] ldid download URL is not reachable. Status code: {res.status_code}")
                exit(1)
        except requests.exceptions.RequestException as err:
            print(f"[-] ldid download URL is not reachable. Error: {err}")
            exit(1)

        subprocess.run(f"chmod +x ldid".split(), stdout=subprocess.DEVNULL)

    def download_macos_arm64(args):
        if args.debug:
            print(f"[DEBUG] Downloading ldid on macOS arm64.")

        res = requests.get(Ldid.macos_arm64_url, stream=True)
        try:
            if res.status_code == 200:
                with open(f"ldid", "wb") as f:
                    f.write(res.content)
                    if args.debug:
                        print(f"[DEBUG] Wrote file.")
            else:
                print(
                    f"[-] ldid download URL is not reachable. Status code: {res.status_code}")
                exit(1)
        except requests.exceptions.RequestException as err:
            print(f"[-] ldid download URL is not reachable. Error: {err}")
            exit(1)

        subprocess.run(f"chmod +x ldid".split(), stdout=subprocess.DEVNULL)
