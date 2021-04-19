import photos, shortcuts

for asset in photos.get_albums():
    if not asset.assets:
        asset.delete()
        
shortcuts.open_shortcuts_app()
