"""Push project files to GitHub via REST API (no local git required)."""

from __future__ import annotations

import base64
import getpass
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Iterable
import urllib.error
import urllib.request


CONFIG = {
    "owner": "BMA-Statistics-PW",
    "repo": "BMA-Accident-Analysis",
    "branch": "main",
    "message": "Update BMA Accident Analysis Dashboard",
    "exclude_dirs": {".git", ".github", "__pycache__"},
    "exclude_files": {".DS_Store", "Thumbs.db"},
}


def print_banner() -> None:
    print("\n" + "=" * 60)
    print("  GitHub Push Tool | BMA Accident Analysis")
    print("=" * 60)
    print(f"  Repo   : {CONFIG['owner']}/{CONFIG['repo']}")
    print(f"  Branch : {CONFIG['branch']}\n")


def ask_token() -> str:
    token = os.getenv("GITHUB_TOKEN", "").strip()
    if token:
        return token

    print("ไม่พบ GITHUB_TOKEN ใน Environment")
    print("กรุณาวาง GitHub Personal Access Token (scope: repo)")
    token = getpass.getpass("Token: ").strip()
    if not token:
        raise SystemExit("\nยกเลิกการทำงาน: ไม่ได้รับ token")
    return token


def make_headers(token: str) -> dict[str, str]:
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "BMA-Statistics-PW/push-script",
    }


def check_token(headers: dict[str, str]) -> bool:
    url = "https://api.github.com/user"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            user = json.loads(response.read())
        print(f"  Token OK | login: {user.get('login', '?')}")
        return True
    except urllib.error.HTTPError as err:
        print(f"  Token invalid or unauthorized (HTTP {err.code})")
        return False
    except Exception as err:  # noqa: BLE001
        print(f"  Cannot connect to GitHub: {err}")
        return False


def get_file_sha(remote_path: str, headers: dict[str, str]) -> str | None:
    url = f"https://api.github.com/repos/{CONFIG['owner']}/{CONFIG['repo']}/contents/{remote_path}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read())["sha"]
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        raise


def iter_project_files(base_dir: Path) -> Iterable[tuple[str, Path]]:
    for root, dirs, files in os.walk(base_dir):
        dirs[:] = [d for d in dirs if d not in CONFIG["exclude_dirs"]]

        root_path = Path(root)
        for name in files:
            if name in CONFIG["exclude_files"]:
                continue
            local_path = root_path / name
            rel_path = local_path.relative_to(base_dir).as_posix()
            yield rel_path, local_path


def push_file(remote_path: str, local_path: Path, headers: dict[str, str], message: str) -> bool:
    if not local_path.exists():
        print(f"  missing: {local_path}")
        return False

    content_b64 = base64.b64encode(local_path.read_bytes()).decode()
    sha = get_file_sha(remote_path, headers)
    payload: dict[str, str] = {
        "message": message,
        "content": content_b64,
        "branch": CONFIG["branch"],
    }
    if sha:
        payload["sha"] = sha

    url = f"https://api.github.com/repos/{CONFIG['owner']}/{CONFIG['repo']}/contents/{remote_path}"
    request = urllib.request.Request(
        url=url,
        data=json.dumps(payload).encode(),
        headers=headers,
        method="PUT",
    )

    try:
        with urllib.request.urlopen(request):
            pass
        status = "updated" if sha else "created"
        print(f"  {status:8} {remote_path}")
        return True
    except urllib.error.HTTPError as err:
        detail = err.read().decode(errors="ignore")
        print(f"  failed   {remote_path} (HTTP {err.code})")
        print(f"           {detail[:180]}")
        return False


def main() -> None:
    print_banner()
    script_dir = Path(__file__).resolve().parent

    token = ask_token()
    headers = make_headers(token)

    print("[1/3] Check token")
    if not check_token(headers):
        sys.exit(1)

    message = f"{CONFIG['message']} ({datetime.now().strftime('%Y-%m-%d %H:%M')})"
    files = list(iter_project_files(script_dir))
    print(f"\n[2/3] Push files ({len(files)} files)")

    success = 0
    failed = 0
    for remote_path, local_path in files:
        ok = push_file(remote_path, local_path, headers, message)
        if ok:
            success += 1
        else:
            failed += 1

    print("\n[3/3] Result")
    print("=" * 60)
    print(f"  Success : {success}")
    print(f"  Failed  : {failed}")
    print(f"  URL     : https://{CONFIG['owner'].lower()}.github.io/{CONFIG['repo']}/")
    print("=" * 60)

    if failed:
        sys.exit(2)


if __name__ == "__main__":
    main()
