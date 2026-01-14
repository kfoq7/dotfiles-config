from ignis.window_manager import WindowManager

window_manager = WindowManager.get_default()

bar = window_manager.get_window('ignis_BAR')
if bar:
    bar.set_visible(not bar.visible)
