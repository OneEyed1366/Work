#Общая идея: запускать необходимые скрипты, передавая результат их работы в PowerShell, а затем выводить этот результат в Панели уведомлений
python instPyBot.py

Add-Type -AssemblyName System.Windows.Forms
$global:balmsg = New-Object System.Windows.Forms.NotifyIcon
$path = (Get-Process -id $pid).Path
$balmsg.Icon = [System.Drawing.Icon]::ExtractAssociatedIcon($path)
$balmsg.BalloonTipIcon = [System.Windows.Forms.ToolTipIcon]::Warning
$balmsg.BalloonTipText = 'Test'
$balmsg.BalloonTipTitle = "Attentino $Env:USERNAME"
$balmsg.Visible = $true
$balmsg.ShowBalloonTip(10000)