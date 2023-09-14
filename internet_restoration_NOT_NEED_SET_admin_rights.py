import subprocess
import ctypes

def run_as_admin(cmd):
    ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", f"/K {cmd}", None, 1)

def main():
    try:
        power_shell_commands = [
            "Get-NetRoute -NextHop '10.18*' | Where-Object { ($_.DestinationPrefix) -notlike '10.*' } | Remove-NetRoute -Confirm:$false -ErrorAction 'SilentlyContinue';",
            "Add-Content -Path $env:windir\\System32\\drivers\\etc\\hosts -Value \"`n45.84.154.220`tdion.vc\" -Force",
            "Add-Content -Path $env:windir\\System32\\drivers\\etc\\hosts -Value \"`n45.84.154.220`tgw.dion.vc\" -Force",
            "Add-Content -Path $env:windir\\System32\\drivers\\etc\\hosts -Value \"`n45.84.154.220`tapi-clients.dion.vc\" -Force",
            "Add-Content -Path $env:windir\\System32\\drivers\\etc\\hosts -Value \"`n45.84.154.220`tsockets-pool.dion.vc\" -Force"
        ]

        cmd = " ".join(power_shell_commands)
        run_as_admin(f'powershell -NoProfile -ExecutionPolicy Bypass -Command "{cmd}"')

        print("PowerShell commands executed successfully.")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
